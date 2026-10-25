import contextlib
import io
import json
import os
from pathlib import Path
import stat
import tempfile
import unittest
from unittest.mock import patch

from scripts import setup
from scripts import setup_presets
from scripts.setup_inventory import Target


class PresetTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "checkout"
        self.home = self.base / "home"
        self.project = self.base / "project with spaces; literal"
        self.root.mkdir()
        self.home.mkdir()
        self.project.mkdir()
        self.env = {"HOME": str(self.home), "CODEX_HOME": str(self.home / "codex-custom"),
                    "CLAUDE_CONFIG_DIR": str(self.home / "claude-custom"),
                    "XDG_CONFIG_HOME": str(self.home / "config-custom"), "PATH": os.environ.get("PATH", "")}
        catalog = setup.load_catalog()
        catalog["presets"] = [{"name": "personal", "description": "Personal instructions and a reviewer."}]
        (self.root / "catalog.json").write_text(json.dumps(catalog))
        self.write(self.root / "configs/personal/AGENTS.md", b"Keep changes focused.\n")
        for agent in ("codex", "claude-code", "opencode"):
            directory = self.root / "configs/personal" / agent
            (directory / "agents").mkdir(parents=True)
            if agent == "codex":
                (directory / "agents/personal-reviewer.toml").write_text('name = "personal-reviewer"\ndescription = "Review on request."\ndeveloper_instructions = "Report findings."\n')
            else:
                (directory / "agents/personal-reviewer.md").write_text('---\nname: personal-reviewer\ndescription: Review on request.\n---\nReport findings.\n')

    def run_cli(self, action="install", agent="codex", scope="global", extra=()):
        args = [action, "--preset", "personal", "--agent", *agent.split(), "--scope", scope,
                "--project", str(self.project), *extra]
        if action == "install":
            args.append("--yes")
        output = io.StringIO()
        with patch.object(setup, "ROOT", self.root), patch.dict(os.environ, self.env, clear=True), \
             contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            try:
                result = setup.main(args)
            except SystemExit as error:
                result = error.code
        return result, output.getvalue()

    def write(self, path, content):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)

    def test_fresh_all_agents_global_and_project_then_unchanged_repeat(self):
        for scope, paths in (
            ("project", [self.project / "AGENTS.md", self.project / ".codex/agents/personal-reviewer.toml",
                         self.project / "CLAUDE.md", self.project / ".claude/agents/personal-reviewer.md",
                         self.project / ".opencode/agents/personal-reviewer.md"]),
            ("global", [self.home / "codex-custom/AGENTS.md", self.home / "codex-custom/agents/personal-reviewer.toml",
                        self.home / "claude-custom/CLAUDE.md", self.home / "claude-custom/agents/personal-reviewer.md",
                        self.home / "config-custom/opencode/AGENTS.md", self.home / "config-custom/opencode/agents/personal-reviewer.md"]),
        ):
            with self.subTest(scope=scope):
                code, output = self.run_cli(scope=scope, agent="codex claude-code opencode")
                self.assertEqual(code, 0, output)
                self.assertTrue(all(path.is_file() for path in paths))
                before = {path: (path.read_bytes(), path.stat().st_mtime_ns) for path in paths}
                code, output = self.run_cli(scope=scope, agent="codex claude-code opencode")
                self.assertEqual(code, 0, output)
                self.assertEqual(before, {path: (path.read_bytes(), path.stat().st_mtime_ns) for path in paths})
                self.assertFalse(list(self.base.rglob("*.bak")))
                if scope == "project":
                    self.assertEqual((self.project / "AGENTS.md").read_text().count("Keep changes focused."), 1)

    def test_shared_instruction_edit_reaches_every_host(self):
        (self.root / "configs/personal/AGENTS.md").write_text("One shared preference.\n")
        for scope, paths in (
            ("global", [self.home / "codex-custom/AGENTS.md", self.home / "claude-custom/CLAUDE.md",
                        self.home / "config-custom/opencode/AGENTS.md"]),
            ("project", [self.project / "AGENTS.md", self.project / "CLAUDE.md"]),
        ):
            with self.subTest(scope=scope):
                code, output = self.run_cli(agent="codex claude-code opencode", scope=scope,
                                            extra=("--preset-part", "instructions"))
                self.assertEqual(code, 0, output)
                for path in paths:
                    self.assertEqual(path.read_bytes(), b"<!-- agent-skills:personal:begin -->\n"
                                     b"One shared preference.\n<!-- agent-skills:personal:end -->\n")
        self.assertFalse((self.home / "claude-custom/AGENTS.md").exists())

    def test_preview_has_no_writes_and_append_preserves_bytes_mode_and_backup(self):
        instructions = self.home / "codex-custom/AGENTS.md"
        original = b"# Private rules\r\nprivate-value-must-not-appear"
        self.write(instructions, original)
        instructions.chmod(0o640)
        settings = self.home / "codex-custom/config.toml"
        self.write(settings, b'model = "existing-choice"\n')
        code, output = self.run_cli("plan", extra=("--preset-part", "instructions"))
        self.assertEqual(code, 0, output)
        self.assertEqual(instructions.read_bytes(), original)
        self.assertFalse(list(self.base.rglob("*.bak")))
        self.assertIn("+Keep changes focused.", output)
        self.assertNotIn("private-value", output)
        code, output = self.run_cli(extra=("--preset-part", "instructions"))
        self.assertEqual(code, 0, output)
        self.assertTrue(instructions.read_bytes().startswith(original + b"\n\n"))
        backups = list(instructions.parent.glob("AGENTS.md.agent-skills-*.bak"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_bytes(), original)
        self.assertEqual(stat.S_IMODE(instructions.stat().st_mode), 0o640)
        self.assertEqual(stat.S_IMODE(backups[0].stat().st_mode), 0o640)
        self.assertEqual(settings.read_bytes(), b'model = "existing-choice"\n')
        self.assertFalse((instructions.parent / "agents").exists())

    def test_conflicting_agent_preserves_whole_target_and_can_select_instructions(self):
        role = self.home / "codex-custom/agents/personal-reviewer.toml"
        self.write(role, b'my existing agent\n')
        code, output = self.run_cli()
        self.assertEqual(code, 1, output)
        self.assertEqual(role.read_bytes(), b'my existing agent\n')
        self.assertFalse((self.home / "codex-custom/AGENTS.md").exists())
        self.assertEqual(self.run_cli(extra=("--preset-part", "instructions"))[0], 0)

    def test_modified_or_malformed_block_is_never_replaced(self):
        self.assertEqual(self.run_cli(extra=("--preset-part", "instructions"))[0], 0)
        path = self.home / "codex-custom/AGENTS.md"
        original = path.read_bytes()
        for changed in (original.replace(b"focused", b"different"), original + original,
                        original.replace(b"<!-- agent-skills:personal:end -->", b"")):
            with self.subTest(changed=changed):
                path.write_bytes(changed)
                code, output = self.run_cli()
                self.assertEqual(code, 1, output)
                self.assertEqual(path.read_bytes(), changed)
                self.assertFalse((path.parent / "agents").exists())

    def test_redirected_or_shared_destinations_do_not_write(self):
        outside = self.base / "unrelated.md"
        outside.write_bytes(b"Preserve me.\n")
        path = self.home / "codex-custom/AGENTS.md"
        path.parent.mkdir()
        for kind in ("symlink", "hardlink", "directory"):
            with self.subTest(kind=kind):
                if kind == "symlink":
                    path.symlink_to(outside)
                elif kind == "hardlink":
                    path.hardlink_to(outside)
                else:
                    path.mkdir()
                try:
                    code, output = self.run_cli()
                    self.assertEqual(code, 1, output)
                    self.assertEqual(outside.read_bytes(), b"Preserve me.\n")
                    self.assertFalse((path.parent / "agents").exists())
                finally:
                    path.rmdir() if kind == "directory" else path.unlink()
        path.parent.rmdir()
        path.parent.symlink_to(self.project, target_is_directory=True)
        self.assertEqual(self.run_cli()[0], 1)
        self.assertEqual(list(self.project.iterdir()), [])

    def test_agents_only_does_not_change_instructions(self):
        path = self.project / "CLAUDE.md"
        self.write(path, b"Existing project policy.\n")
        code, output = self.run_cli(agent="claude-code", scope="project", extra=("--preset-part", "agents"))
        self.assertEqual(code, 0, output)
        self.assertEqual(path.read_bytes(), b"Existing project policy.\n")
        self.assertTrue((self.project / ".claude/agents/personal-reviewer.md").is_file())

    def test_codex_appends_to_active_override_file(self):
        normal = self.home / "codex-custom/AGENTS.md"
        override = normal.with_name("AGENTS.override.md")
        self.write(normal, b"Normal rules.\n")
        self.write(override, b"Override rules.\n")
        code, output = self.run_cli(extra=("--preset-part", "instructions"))
        self.assertEqual(code, 0, output)
        self.assertEqual(normal.read_bytes(), b"Normal rules.\n")
        self.assertTrue(override.read_bytes().startswith(b"Override rules.\n"))
        self.assertIn(b"Keep changes focused.", override.read_bytes())

    def test_opencode_does_not_shadow_existing_claude_instructions(self):
        fallback = self.project / "CLAUDE.md"
        fallback.write_bytes(b"Project rules already used by OpenCode.\n")
        code, output = self.run_cli(agent="opencode", scope="project")
        self.assertEqual(code, 1, output)
        self.assertFalse((self.project / "AGENTS.md").exists())
        self.assertEqual(fallback.read_bytes(), b"Project rules already used by OpenCode.\n")

    def test_escaping_preset_resources_are_rejected(self):
        self.assertEqual(self.run_cli("plan")[0], 0)
        source = self.root / "configs/personal/AGENTS.md"
        source.unlink()
        source.symlink_to(self.base / "private.md")
        (self.base / "private.md").write_text("Do not copy this.")
        code, output = self.run_cli()
        self.assertEqual(code, 2, output)
        self.assertEqual(list(self.home.iterdir()), [])

    def test_invalid_preset_flags_fail_without_writes(self):
        for extra in (("--route", "native"), ("--all",), ("--preset-part", "unknown")):
            with self.subTest(extra=extra):
                code, output = self.run_cli(extra=extra)
                self.assertEqual(code, 2, output)
                self.assertEqual(list(self.home.iterdir()), [])

    def test_changes_after_preview_are_preserved_before_any_target_write(self):
        target = Target("codex", "global", self.project)
        for mutation in ("file", "source", "root"):
            with self.subTest(mutation=mutation):
                plan = setup_presets.build_plan(self.root, "personal", [target], setup_presets.PARTS, self.env)
                self.assertEqual(plan[0].status, "missing")
                path = self.home / "codex-custom/AGENTS.md"
                source = self.root / "configs/personal/AGENTS.md"
                original_source = source.read_bytes()
                env = dict(self.env)
                if mutation == "file":
                    self.write(path, b"Changed after preview.\n")
                elif mutation == "source":
                    source.write_text("A different preset now.\n")
                else:
                    env["CODEX_HOME"] = str(self.home / "moved-codex")
                try:
                    result = setup_presets.apply_plan(plan, self.root, env)
                    self.assertEqual(result[0].status, "conflict", result)
                    self.assertFalse((self.home / "codex-custom/agents").exists())
                    self.assertFalse((self.home / "moved-codex").exists())
                    if mutation == "file":
                        self.assertEqual(path.read_bytes(), b"Changed after preview.\n")
                finally:
                    source.write_bytes(original_source)
                    if path.exists():
                        path.unlink()

    def test_backup_redirect_after_preview_is_preserved(self):
        target = Target("codex", "global", self.project)
        path = self.home / "codex-custom/AGENTS.md"
        self.write(path, b"Original rules.\n")
        plan = setup_presets.build_plan(self.root, "personal", [target], setup_presets.PARTS, self.env)
        backup = next(change.backup for change in plan[0].changes if change.backup)
        unrelated = self.base / "unrelated.txt"
        unrelated.write_bytes(b"Keep these bytes.\n")
        backup.symlink_to(unrelated)
        result = setup_presets.apply_plan(plan, self.root, self.env)
        self.assertEqual(result[0].status, "conflict")
        self.assertEqual(path.read_bytes(), b"Original rules.\n")
        self.assertEqual(unrelated.read_bytes(), b"Keep these bytes.\n")
        self.assertFalse((path.parent / "agents").exists())

    def test_failed_atomic_replace_keeps_original_and_retry_uses_backup(self):
        target = Target("codex", "global", self.project)
        path = self.home / "codex-custom/AGENTS.md"
        self.write(path, b"Original rules.\n")
        plan = setup_presets.build_plan(self.root, "personal", [target], setup_presets.PARTS, self.env)
        with patch("scripts.setup_presets.os.replace", side_effect=OSError("Cannot replace this file")):
            result = setup_presets.apply_plan(plan, self.root, self.env)
        self.assertEqual(result[0].status, "failed")
        self.assertEqual(path.read_bytes(), b"Original rules.\n")
        backups = list(path.parent.glob("*.bak"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_bytes(), b"Original rules.\n")
        self.assertFalse(list(path.parent.glob(".preset-*")))
        self.assertEqual(self.run_cli()[0], 0)
        self.assertEqual(list(path.parent.glob("*.bak")), backups)

    def test_all_skills_remains_separate_from_presets(self):
        output = io.StringIO()
        args = ["plan", "--all", "--agent", "codex", "--scope", "global", "--project", str(self.project)]
        with patch.object(setup, "ROOT", self.root), patch.dict(os.environ, self.env, clear=True), contextlib.redirect_stdout(output):
            self.assertEqual(setup.main(args), 0)
        self.assertNotIn("personal-reviewer", output.getvalue())
        self.assertNotIn("Configuration preset", output.getvalue())
        self.assertEqual(list(self.home.iterdir()), [])

    def test_interactive_preset_selection_uses_the_same_preview(self):
        output = io.StringIO()
        answers = iter(("5", "personal", "instructions", "codex", "global", "n"))
        with patch.object(setup, "ROOT", self.root), patch.dict(os.environ, self.env, clear=True), \
             patch("sys.stdin.isatty", return_value=True), patch("builtins.input", side_effect=lambda prompt: next(answers)), \
             contextlib.redirect_stdout(output):
            self.assertEqual(setup.main([]), 0)
        self.assertIn("+Keep changes focused.", output.getvalue())
        self.assertEqual(list(self.home.iterdir()), [])

    def test_shared_project_write_never_shadows_claude_rules_for_another_target(self):
        fallback = self.project / "CLAUDE.md"
        fallback.write_bytes(b"Existing project policy.\n")
        code, output = self.run_cli(agent="codex claude-code opencode", scope="project", extra=("--preset-part", "instructions"))
        self.assertEqual(code, 1, output)
        self.assertFalse((self.project / "AGENTS.md").exists())
        self.assertTrue(fallback.read_bytes().startswith(b"Existing project policy.\n"))

    def test_nested_shared_instructions_do_not_hide_parent_policy(self):
        parent = self.project
        (parent / "AGENTS.md").write_bytes(b"Existing monorepo policy.\n")
        (parent / ".git").mkdir()
        self.project = parent / "packages/app"
        self.project.mkdir(parents=True)
        for agent in ("codex", "opencode"):
            code, output = self.run_cli(agent=agent, scope="project", extra=("--preset-part", "instructions"))
            self.assertEqual(code, 1, output)
            self.assertFalse((self.project / "AGENTS.md").exists())

    def test_inline_agent_definitions_and_other_filenames_are_preserved(self):
        for agent, relative, content in (
            ("opencode", "config-custom/opencode/opencode.json", b'{"agent":{"personal-reviewer":{"prompt":"Keep my reviewer"}}}'),
            ("opencode", "config-custom/opencode/opencode.jsonc", b'{// existing\n"agent": {"personal-reviewer": {"prompt": "Keep // my reviewer",},},}'),
            ("codex", "codex-custom/config.toml", b'[agents.personal-reviewer]\ndescription = "Keep my reviewer"\nconfig_file = "existing.toml"\n'),
            ("codex", "codex-custom/agents/other.toml", b'name = "personal-reviewer"\ndescription = "Keep my reviewer"\ndeveloper_instructions = "Original"\n'),
            ("claude-code", "claude-custom/agents/team/other.md", b'---\nname: personal-reviewer\ndescription: Keep my reviewer\n---\nOriginal\n'),
        ):
            with self.subTest(agent=agent, relative=relative):
                path = self.home / relative
                self.write(path, content)
                try:
                    code, output = self.run_cli(agent=agent, extra=("--preset-part", "agents"))
                    self.assertEqual(code, 1, output)
                    self.assertEqual(path.read_bytes(), content)
                    self.assertFalse(list(self.home.rglob("personal-reviewer.*")))
                finally:
                    path.unlink()

    def test_existing_parent_agent_and_custom_opencode_config_are_preserved(self):
        existing = self.project / ".opencode/agents/personal-reviewer.md"
        self.write(existing, b"---\ndescription: Existing reviewer\nmode: subagent\n---\nKeep this.\n")
        (self.project / ".git").mkdir()
        parent = self.project
        self.project = parent / "child"
        self.project.mkdir()
        code, output = self.run_cli(agent="opencode", scope="project", extra=("--preset-part", "agents"))
        self.assertEqual(code, 1, output)
        self.assertFalse((self.project / ".opencode").exists())
        custom = self.base / "custom.jsonc"
        custom.write_text('{"agent":{"personal-reviewer":{"prompt":"custom"}}}')
        self.env["OPENCODE_CONFIG"] = str(custom)
        code, output = self.run_cli(agent="opencode", extra=("--preset-part", "agents"))
        self.assertEqual(code, 1, output)
        self.assertFalse((self.home / "config-custom").exists())

    def test_unrelated_jsonc_and_agents_do_not_block_selection(self):
        settings = self.home / "config-custom/opencode/opencode.jsonc"
        content = b'{/* options */"model":"provider/model","agent":{"other":{"prompt":"quoted \\" text, } // not a comment",},},}'
        self.write(settings, content)
        code, output = self.run_cli(agent="opencode", extra=("--preset-part", "agents"))
        self.assertEqual(code, 0, output)
        self.assertEqual(settings.read_bytes(), content)

    def test_matching_global_roles_satisfy_project_selection_without_duplicates(self):
        extra = ("--preset-part", "agents")
        self.assertEqual(self.run_cli(agent="codex claude-code opencode", extra=extra)[0], 0)
        before = {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in self.home.rglob("*") if p.is_file()}
        code, output = self.run_cli(agent="codex claude-code opencode", scope="project", extra=extra)
        self.assertEqual(code, 0, output)
        self.assertEqual(list(self.project.iterdir()), [])
        self.assertEqual(before, {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in before})

    def test_opencode_custom_directory_and_inline_settings_block_collisions(self):
        custom = self.base / "custom-opencode"
        existing = custom / "agent/personal-reviewer.md"
        self.write(existing, b"Custom reviewer.\n")
        for key, value in (("OPENCODE_CONFIG_DIR", str(custom)),
                           ("OPENCODE_CONFIG_CONTENT", '{"agent":{"personal-reviewer":{"disable":true}}}')):
            with self.subTest(key=key):
                self.env[key] = value
                try:
                    code, output = self.run_cli(agent="opencode", extra=("--preset-part", "agents"))
                    self.assertEqual(code, 1, output)
                    self.assertFalse((self.home / "config-custom").exists())
                    self.assertEqual(existing.read_bytes(), b"Custom reviewer.\n")
                finally:
                    del self.env[key]

    def test_ambiguous_settings_do_not_create_agents(self):
        cases = (
            ("opencode", "config-custom/opencode/opencode.jsonc", '{"agent":{},"agent":{}}'),
            ("opencode", "config-custom/opencode/opencode.jsonc", '{"agent":{}, /* unfinished'),
            ("opencode", "config-custom/opencode/opencode.jsonc", '{"agent":{,}}'),
            ("codex", "codex-custom/config.toml", 'profiles = "invalid"'),
        )
        for agent, relative, content in cases:
            with self.subTest(content=content):
                path = self.home / relative
                self.write(path, content.encode())
                try:
                    code, output = self.run_cli(agent=agent, extra=("--preset-part", "agents"))
                    self.assertEqual(code, 1, output)
                    self.assertEqual(path.read_text(), content)
                    self.assertFalse(list(self.home.rglob("personal-reviewer.*")))
                finally:
                    path.unlink()

    def test_ambiguous_claude_name_or_unreadable_agent_directory_blocks_install(self):
        folder = self.home / "claude-custom/agents/team"
        existing = folder / "other.md"
        self.write(existing, b"---\nname: other\nname: |\n  personal-reviewer\n---\nOriginal\n")
        code, output = self.run_cli(agent="claude-code", extra=("--preset-part", "agents"))
        self.assertEqual(code, 1, output)
        existing.write_text("---\nname: personal-reviewer\n---\nOriginal\n")
        folder.chmod(0o100)
        try:
            if not os.access(folder, os.R_OK):
                code, output = self.run_cli(agent="claude-code", extra=("--preset-part", "agents"))
                self.assertEqual(code, 1, output)
                self.assertFalse((folder.parent / "personal-reviewer.md").exists())
        finally:
            folder.chmod(0o700)


if __name__ == "__main__":
    unittest.main()
