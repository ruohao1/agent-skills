import copy
import importlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from test_setup_inventory import skill


def sample_catalog():
    return {
        "schema_version": 1,
        "installer_version": "1.7.2",
        "sources": {
            "local": {"repository": "ruohao1/agent-skills", "ref": None, "local_path": "."},
            "external": {"repository": "example/tools", "ref": "a" * 40},
        },
        "skills": [
            {"name": "product-brief", "category": "product-design", "ownership": "custom",
             "source": "local", "path": "plugins/product-design/skills/product-brief", "description": "Frame a user task."},
            {"name": "diagnosing-bugs", "category": "engineering", "ownership": "upstream",
             "source": "external", "path": "skills/diagnosing-bugs", "description": "Diagnose a bug."},
        ],
        "plugins": [{"name": "product-design", "skills": ["product-brief"],
                     "native": {"marketplace": "personal", "repository": "ruohao1/agent-skills"}}],
    }


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(Path("scripts/setup.py").is_file(), "setup coordinator is not implemented")
        self.setup = importlib.import_module("scripts.setup")
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def load(self, data):
        (self.root / "catalog.json").write_text(json.dumps(data))
        return self.setup.load_catalog(self.root)

    def test_catalog_rejects_unsafe_or_ambiguous_entries(self):
        mutations = [
            lambda c: c["skills"].append(copy.deepcopy(c["skills"][0])),
            lambda c: c["skills"][0].update(source="unknown"),
            lambda c: c["skills"][0].update(category="everything"),
            lambda c: c["skills"][0].update(path="../escape"),
            lambda c: c["skills"][0].update(path="/absolute"),
            lambda c: c["skills"][0].update(name="Bad_Name"),
            lambda c: c["sources"]["external"].update(repository="example/tools; touch /tmp/pwn"),
            lambda c: c["sources"]["external"].update(ref="main"),
            lambda c: c["plugins"][0].update(skills=["absent"]),
            lambda c: c.update(schema_version=99),
        ]
        for mutate in mutations:
            data = sample_catalog()
            mutate(data)
            with self.subTest(data=data), self.assertRaises(ValueError):
                self.load(data)

    def test_selection_contains_only_curated_names(self):
        catalog = self.load(sample_catalog())
        self.assertEqual(self.setup.select_skills(catalog, "all", []), ["product-brief", "diagnosing-bugs"])
        self.assertEqual(self.setup.select_skills(catalog, "category", ["engineering"]), ["diagnosing-bugs"])
        self.assertEqual(self.setup.select_skills(catalog, "skill", ["diagnosing-bugs", "diagnosing-bugs"]), ["diagnosing-bugs"])
        self.assertEqual(self.setup.select_skills(catalog, "plugin", ["product-design"]), ["product-brief"])
        for selector, values in [("skill", ["unselected-upstream"]), ("category", ["unknown"]), ("plugin", ["unknown"])]:
            with self.subTest(selector=selector), self.assertRaises(ValueError):
                self.setup.select_skills(catalog, selector, values)

    def test_duplicate_json_keys_are_rejected(self):
        (self.root / "catalog.json").write_text('{"schema_version": 1, "schema_version": 2}')
        with self.assertRaises(ValueError):
            self.setup.load_catalog(self.root)


class SetupTests(unittest.TestCase):
    def setUp(self):
        CatalogTests.setUp(self)
        self.assertTrue(hasattr(self.setup, "build_plan"), "installation planning is not implemented")
        self.inv = importlib.import_module("scripts.setup_inventory")
        self.home = self.root / "home"
        self.project = self.root / "project with spaces; literal"
        self.project.mkdir()
        self.home.mkdir()
        self.env = {**os.environ, "HOME": str(self.home), "CODEX_HOME": str(self.home / ".codex"),
                    "CLAUDE_CONFIG_DIR": str(self.home / ".claude"), "XDG_CONFIG_HOME": str(self.home / ".config")}
        self.catalog = CatalogTests.load(self, sample_catalog())
        self.target = self.inv.Target("codex", "global", self.project)
        self.patch_root = patch.object(self.setup, "ROOT", self.root)
        self.patch_root.start()
        self.addCleanup(self.patch_root.stop)
        skill(self.root / "plugins/product-design/skills", "product-brief")
        self.calls = []

    def plan(self, names=None, target=None):
        target = target or self.target
        inventory = self.inv.inspect_target(target, self.env)
        return self.setup.build_plan(self.catalog, names or ["product-brief"], [target], "skills", {target: inventory})

    def installer(self, command, **kwargs):
        self.calls.append(tuple(command))
        self.assertIn("--copy", command)
        self.assertNotIn("--all", command)
        name = command[command.index("--skill") + 1]
        agent = command[command.index("--agent") + 1]
        self.assertIn(agent, ("codex", "claude-code", "opencode"))
        root = self.home if "--global" in command else Path(kwargs["cwd"])
        base = root / (".claude/skills" if agent == "claude-code" else ".agents/skills")
        skill(base, name)
        if name == "diagnosing-bugs":
            lock = root / ".agents/.skill-lock.json"
            lock.parent.mkdir(exist_ok=True)
            lock.write_text(json.dumps({"version": 3, "skills": {name: {"source": "example/tools", "sourceType": "github",
                                                                       "ref":"a"*40,"skillPath":"skills/diagnosing-bugs/SKILL.md"}}}))
        return subprocess.CompletedProcess(command, 0, "installed", "")

    def apply(self, plan, runner=None):
        with patch("scripts.setup.subprocess.run", side_effect=runner or self.installer):
            return self.setup.apply_plan(plan, self.catalog, self.env)

    def test_fresh_full_subset_and_additive_install(self):
        sentinel = self.home / "settings.json"
        sentinel.write_bytes(b'{"unrelated": true}\n')
        with patch.dict(os.environ, self.env, clear=True):
            plan = self.plan(["product-brief", "diagnosing-bugs"])
            self.assertEqual([p.status for p in plan], ["missing", "missing"])
            result = self.apply(plan)
            self.assertEqual([p.status for p in result], ["installed", "installed"])
            calls = len(self.calls)
            self.assertEqual([p.status for p in self.apply(self.plan(["product-brief", "diagnosing-bugs"]))], ["present", "present"])
            self.assertEqual(len(self.calls), calls)
            other = self.inv.Target("claude-code", "global", self.project)
            result = self.apply(self.plan(target=other))
            self.assertEqual(result[0].status, "installed")
            self.assertTrue((self.home / ".claude/skills/product-brief/SKILL.md").exists())
        self.assertEqual(sentinel.read_bytes(), b'{"unrelated": true}\n')

    def test_changed_destination_is_preserved(self):
        with patch.dict(os.environ, self.env, clear=True):
            plan = self.plan()
            folder = skill(self.home / ".agents/skills", "product-brief", "my local version")
            before = (folder / "SKILL.md").read_bytes()
            self.assertEqual(self.apply(plan)[0].status, "conflict")
        self.assertEqual(self.calls, [])
        self.assertEqual((folder / "SKILL.md").read_bytes(), before)

    def test_source_collision_modification_and_native_overlap_block_writes(self):
        I = self.inv.Installation
        cases = [
            I("product-brief", "someone/else", self.home / "fake", "skills", True, "digest"),
            I("product-brief", "ruohao1/agent-skills", self.home / "fake", "skills", True, "digest", modified=True),
        ]
        for installed in cases:
            result = self.setup.build_plan(self.catalog, ["product-brief"], [self.target], "skills",
                                           {self.target: self.inv.Inventory([installed], [])})
            self.assertEqual(result[0].status, "conflict")
            self.assertIsNone(result[0].command)
        native = I("product-brief", "ruohao1/agent-skills", None, "native", True, "one", plugin="product-design")
        standalone = I("product-brief", "ruohao1/agent-skills", None, "skills", True, "two")
        result = self.setup.build_plan(self.catalog, ["product-brief"], [self.target], "skills",
                                       {self.target: self.inv.Inventory([native, standalone], [])})
        self.assertEqual(result[0].status, "conflict")
        result = self.setup.build_plan(self.catalog, ["product-brief"], [self.target], "skills",
                                       {self.target: self.inv.Inventory([], ["incomplete plugin inventory"])})
        self.assertEqual(result[0].status, "needs-setup")

    def test_partial_failure_and_interrupted_receipt(self):
        def fail_second(command, **kwargs):
            if "diagnosing-bugs" in command:
                return subprocess.CompletedProcess(command, 1, "", "source unavailable")
            return self.installer(command, **kwargs)
        with patch.dict(os.environ, self.env, clear=True):
            result = self.apply(self.plan(["product-brief", "diagnosing-bugs"]), fail_second)
            self.assertEqual([p.status for p in result], ["installed", "failed"])
            self.assertEqual([p.status for p in self.plan(["product-brief", "diagnosing-bugs"])], ["present", "missing"])
            self.inv.receipt_path(self.target, self.env).unlink()
            self.assertEqual(self.plan()[0].status, "present", "identical local source can recover a lost receipt")

    def test_zero_exit_without_files_is_failed(self):
        with patch.dict(os.environ, self.env, clear=True):
            result = self.apply(self.plan(), lambda command, **kw: subprocess.CompletedProcess(command, 0, "success", ""))
        self.assertEqual(result[0].status, "failed")

    def test_noninteractive_missing_choices_has_no_effect(self):
        with patch("scripts.setup.sys.stdin.isatty", return_value=False):
            self.assertEqual(self.setup.main(["install", "--all"]), 2)
        self.assertFalse((self.home / ".agents").exists())

    def test_project_path_is_passed_literally(self):
        target = self.inv.Target("codex", "project", self.project)
        with patch.dict(os.environ, self.env, clear=True):
            result = self.apply(self.plan(target=target))
        self.assertEqual(result[0].status, "installed")
        self.assertTrue((self.project / ".agents/skills/product-brief/SKILL.md").exists())
        self.assertFalse((self.home / ".agents/skills/product-brief").exists())

    def test_installer_metadata_redirects_block_all_writes(self):
        outside = self.root / "unrelated.json"
        outside.write_text('{"version":1,"skills":{},"keep":"unrelated"}')
        target = self.inv.Target("codex", "project", self.project)
        with patch.dict(os.environ, self.env, clear=True):
            plan = self.plan(target=target)
            (self.project / "skills-lock.json").symlink_to(outside)
            result = self.apply(plan)
        self.assertEqual(result[0].status, "conflict")
        self.assertEqual(self.calls, [])
        self.assertIn('"keep":"unrelated"', outside.read_text())
        (self.project / "skills-lock.json").unlink()
        (self.project / "skills-lock.json").write_text(outside.read_text())
        with patch.dict(os.environ, self.env, clear=True):
            self.assertEqual(self.apply(self.plan(target=target))[0].status, "conflict")
        self.assertEqual(self.calls, [])

    def test_global_lock_parent_and_hardlink_are_preserved(self):
        outside = self.root / "outside-state"
        outside.mkdir()
        lock = outside / ".skill-lock.json"
        lock.write_text('{"version":3,"skills":{}}')
        self.env["XDG_STATE_HOME"] = str(self.home / "state")
        (self.home / "state").mkdir()
        (self.home / "state/skills").symlink_to(outside, target_is_directory=True)
        with patch.dict(os.environ, self.env, clear=True):
            self.assertEqual(self.apply(self.plan())[0].status, "conflict")
        self.assertEqual(self.calls, [])
        (self.home / "state/skills").unlink()
        (self.home / "state/skills").mkdir()
        os.link(lock, self.home / "state/skills/.skill-lock.json")
        with patch.dict(os.environ, self.env, clear=True):
            self.assertEqual(self.apply(self.plan())[0].status, "conflict")
        self.assertEqual(self.calls, [])

    def test_partial_upstream_remains_unresolved_until_resource_is_present(self):
        def incomplete(command, **kw):
            result = self.installer(command, **kw)
            file = self.home / ".agents/skills/diagnosing-bugs/SKILL.md"
            file.write_text(file.read_text() + '\nRead [required](required.md).\n')
            return result
        with patch.dict(os.environ, self.env, clear=True):
            self.assertEqual(self.apply(self.plan(["diagnosing-bugs"]), incomplete)[0].status, "failed")
            self.assertEqual(self.apply(self.plan(["diagnosing-bugs"]))[0].status, "needs-setup")
            (self.home / ".agents/skills/diagnosing-bugs/required.md").write_text("Required instructions.")
            self.assertEqual(self.plan(["diagnosing-bugs"])[0].status, "present")
        self.assertEqual(len(self.calls), 1)

    def test_opencode_only_global_uses_actual_shared_destination(self):
        target = self.inv.Target("opencode", "global", self.project)
        with patch.dict(os.environ, self.env, clear=True):
            plan = self.plan(target=target)
            self.assertEqual(plan[0].location, self.home / ".agents/skills/product-brief")
            self.assertEqual(self.apply(plan)[0].status, "installed")
            self.assertEqual(self.plan(target=target)[0].status, "present")

    def test_upstream_pin_and_skill_path_are_verified_before_receipt(self):
        def wrong_revision(command, **kw):
            result = self.installer(command, **kw)
            lock = self.home / ".agents/.skill-lock.json"
            data = json.loads(lock.read_text())
            data["skills"]["diagnosing-bugs"].update(ref="b"*40, skillPath="other/diagnosing-bugs/SKILL.md")
            lock.write_text(json.dumps(data))
            return result
        with patch.dict(os.environ, self.env, clear=True):
            result = self.apply(self.plan(["diagnosing-bugs"]), wrong_revision)
        self.assertEqual(result[0].status, "failed")
        self.assertFalse(self.inv.receipt_path(self.target, self.env).exists())

    def test_custom_state_root_fresh_install_and_repeat(self):
        self.env["XDG_STATE_HOME"] = str(self.home / "state")
        def install(command, **kw):
            result = self.installer(command, **kw)
            lock = self.home / ".agents/.skill-lock.json"
            target = self.home / "state/skills/.skill-lock.json"
            target.parent.mkdir(parents=True, exist_ok=True)
            lock.replace(target)
            return result
        with patch.dict(os.environ, self.env, clear=True):
            self.assertEqual(self.apply(self.plan(["diagnosing-bugs"]), install)[0].status, "installed")
            self.assertEqual(self.plan(["diagnosing-bugs"])[0].status, "present")
        self.assertEqual(len(self.calls), 1)

    def test_native_route_scope_and_overlap(self):
        for agent, scope in [("opencode", "global"), ("codex", "project")]:
            target = self.inv.Target(agent, scope, self.project)
            result = self.setup.build_plan(self.catalog, ["product-brief"], [target], "native",
                                           {target: self.inv.Inventory()}, self.env)
            self.assertEqual(result[0].status, "unsupported")
            self.assertIsNone(result[0].command)
        occupied = self.inv.Installation("product-brief", "ruohao1/agent-skills", None, "skills", True, "abc")
        result = self.setup.build_plan(self.catalog, ["product-brief"], [self.target], "native",
                                       {self.target: self.inv.Inventory([occupied])}, self.env)
        self.assertEqual(result[0].status, "conflict")
        self.catalog["plugins"][0]["skills"].append("diagnosing-bugs")
        with self.assertRaises(ValueError):
            self.setup.build_plan(self.catalog, ["product-brief"], [self.target], "native",
                                  {self.target: self.inv.Inventory()}, self.env)

    def test_native_features_require_setup(self):
        self.catalog["plugins"][0]["native"]["setup"] = {"codex": "Review hooks in /hooks."}
        installed = self.inv.Installation("product-brief", "ruohao1/agent-skills", None, "native", True,
                                          "abc", plugin="product-design", version="0.2.0")
        result = self.setup.build_plan(self.catalog, ["product-brief"], [self.target], "native",
                                       {self.target: self.inv.Inventory([installed])}, self.env)
        self.assertEqual(result[0].status, "needs-setup")
        self.assertIn("/hooks", result[0].reason)

    def test_incomplete_native_skill_is_not_present(self):
        folder = skill(self.home / "native", "product-brief", "Read [guide](missing.md).")
        installed = self.inv.Installation("product-brief", "ruohao1/agent-skills", folder, "native", True,
                                          self.inv.fingerprint(folder), plugin="product-design", version="0.2.0")
        result = self.setup.build_plan(self.catalog, ["product-brief"], [self.target], "native",
                                       {self.target:self.inv.Inventory([installed])}, self.env)
        self.assertEqual(result[0].status, "needs-setup")

    def test_native_marketplace_collision_never_registers_or_installs(self):
        with patch.dict(os.environ, self.env, clear=True):
            plan = self.setup.build_plan(self.catalog, ["product-brief"], [self.target], "native",
                                         {self.target: self.inv.Inventory()}, self.env)
            responses = []
            def native(command, **kw):
                responses.append(tuple(command))
                return subprocess.CompletedProcess(command, 0, json.dumps([{"name": "personal", "source": "https://github.com/someone/else.git"}]), "")
            result = self.apply(plan, native)
        self.assertEqual(result[0].status, "conflict")
        self.assertEqual(len(responses), 1)

    def test_native_install_is_verified_and_keeps_other_configuration(self):
        state = self.home / ".codex/unchanged.json"
        state.parent.mkdir()
        state.write_text('{"unrelated":true}')
        package = self.home / ".codex/plugins/cache/personal/product-design/0.2.0"
        calls = []
        registered = False
        warning = 'WARNING: proceeding, even though we could not create PATH aliases: Refusing to create helper binaries under temporary dir "/tmp"\n'
        def native(command, **kw):
            nonlocal registered
            calls.append(tuple(command))
            if command[1:4] == ("plugin", "marketplace", "list") or list(command[1:4]) == ["plugin", "marketplace", "list"]:
                entries = [{"name": "personal", "marketplaceSource": {"source": str(self.root)}}] if registered else []
                return subprocess.CompletedProcess(command, 0, json.dumps(entries), warning)
            if "marketplace" in command:
                registered = True
                return subprocess.CompletedProcess(command, 0, "{}", warning)
            if "add" in command:
                skill(package / "skills", "product-brief")
                (package / ".codex-plugin").mkdir()
                (package / ".codex-plugin/plugin.json").write_text('{"name":"product-design","skills":"./skills/"}')
                return subprocess.CompletedProcess(command, 0, "{}", warning)
            entry = {"pluginId":"product-design@personal", "name":"product-design", "marketplaceName":"personal",
                     "installed":True,"enabled":True,"version":"0.2.0", "source":{"source":"local","path":str(package)},
                     "marketplaceSource":{"sourceType":"git","source":"https://github.com/ruohao1/agent-skills.git"}}
            return subprocess.CompletedProcess(command, 0, json.dumps({"installed":[entry],"available":[]}), warning)
        with patch.dict(os.environ, self.env, clear=True):
            plan = self.setup.build_plan(self.catalog, ["product-brief"], [self.target], "native", {self.target:self.inv.Inventory()}, self.env)
            result = self.apply(plan, native)
        self.assertEqual(result[0].status, "installed")
        self.assertTrue(any("add" in command and "product-design@personal" in command for command in calls))
        self.assertEqual(state.read_text(), '{"unrelated":true}')

    def test_claude_existing_directory_marketplace_is_reused(self):
        target = self.inv.Target("claude-code", "global", self.project)
        folder = skill(self.home / "cache", "product-brief")
        record = self.inv.Installation("product-brief", "ruohao1/agent-skills", folder, "native", True,
                                      self.inv.fingerprint(folder), plugin="product-design", version="0.2.0")
        item = self.setup.build_plan(self.catalog, ["product-brief"], [target], "native", {target:self.inv.Inventory()}, self.env)[0]
        calls = []
        def run(command, **kw):
            calls.append(command)
            entries = [{"name":"personal", "source":"directory", "path":str(self.root)}]
            return subprocess.CompletedProcess(command, 0, json.dumps(entries), "")
        with patch("scripts.setup.subprocess.run", side_effect=run), patch("scripts.setup.inspect_target", return_value=self.inv.Inventory([record])):
            result = self.setup._apply_native(item, self.catalog, self.env)
        self.assertEqual(result.status, "installed")
        self.assertEqual(len(calls), 2, "reuse the registration and install once")

    def test_unverified_marketplace_registration_never_installs(self):
        item = self.setup.build_plan(self.catalog, ["product-brief"], [self.target], "native", {self.target:self.inv.Inventory()}, self.env)
        calls = []
        def run(command, **kw):
            calls.append(command)
            return subprocess.CompletedProcess(command, 0, "[]", "")
        result = self.apply(item, run)
        self.assertEqual(result[0].status, "failed")
        self.assertFalse(any("product-design@personal" in command for command in calls))


if __name__ == "__main__":
    unittest.main()
