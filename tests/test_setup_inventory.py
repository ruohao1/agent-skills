import importlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch


def skill(root, name="sample", body="original"):
    folder = root / name
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "SKILL.md").write_text(f"---\nname: {name}\ndescription: Test skill.\n---\n{body}\n")
    return folder


class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(Path("scripts/setup_inventory.py").is_file(), "inventory is not implemented")
        self.inv = importlib.import_module("scripts.setup_inventory")
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name) / "home"
        self.project = self.home / "projects/demo/sub"
        self.project.mkdir(parents=True)
        self.env = {**os.environ, "HOME": str(self.home), "CODEX_HOME": str(self.home / ".codex"),
                    "CLAUDE_CONFIG_DIR": str(self.home / ".claude"), "XDG_CONFIG_HOME": str(self.home / ".config")}

    def inspect(self, agent="opencode", scope="project"):
        return self.inv.inspect_target(self.inv.Target(agent, scope, self.project), self.env)

    def test_shared_legacy_and_parent_visibility(self):
        shared = skill(self.home / ".agents/skills")
        skill(self.project.parent / ".opencode/skills", "parent-tool")
        alias = self.home / ".config/opencode/skills/sample"
        alias.parent.mkdir(parents=True)
        alias.symlink_to(shared, target_is_directory=True)
        lock = self.home / ".agents/.skill-lock.json"
        lock.write_text(json.dumps({"version": 3, "skills": {"sample": {"source": "example/tools", "sourceType": "github"}}}))
        before = (shared / "SKILL.md").read_bytes()
        result = self.inspect()
        self.assertEqual(sorted(i.name for i in result.installations), ["parent-tool", "sample"])
        self.assertEqual(next(i.source for i in result.installations if i.name == "sample"), "example/tools")
        self.assertEqual(result.errors, [])
        self.assertEqual((shared / "SKILL.md").read_bytes(), before)

    def test_custom_roots_links_and_modified_content(self):
        self.env["XDG_CONFIG_HOME"] = str(self.home / "alternate")
        folder = skill(self.home / "alternate/opencode/skills")
        original = self.inv.fingerprint(folder)
        (folder / "SKILL.md").write_text((folder / "SKILL.md").read_text() + "edited\n")
        self.assertNotEqual(self.inv.fingerprint(folder), original)
        broken = self.home / "alternate/opencode/skills/broken"
        broken.symlink_to(self.home / "missing")
        result = self.inspect()
        self.assertIn("sample", [i.name for i in result.installations])
        self.assertTrue(any("broken" in error for error in result.errors))
        (folder / "escape").symlink_to(self.home / "outside")
        with self.assertRaises(ValueError):
            self.inv.fingerprint(folder)

    def test_codex_legacy_root_is_respected(self):
        self.env["CODEX_HOME"] = str(self.home / "custom-codex")
        skill(self.home / "custom-codex/skills", "legacy")
        result = self.inspect("codex")
        self.assertEqual([i.name for i in result.installations], ["legacy"])

    def test_native_inventory_incomplete_is_not_empty(self):
        (self.home / ".codex/plugins").mkdir(parents=True)
        completed = subprocess.CompletedProcess([], 0, '{"installed": [], "available": []}',
                                                "WARNING: proceeding, even though we could not create PATH aliases: Read-only file system\nWarning: failed to list remote marketplace plugins")
        with patch("scripts.setup_inventory.subprocess.run", return_value=completed):
            result = self.inspect("codex")
        self.assertTrue(result.errors)
        for output in ["not json", '{"unexpected": []}']:
            with patch("scripts.setup_inventory.subprocess.run", return_value=subprocess.CompletedProcess([], 0, output, "")):
                self.assertTrue(self.inspect("codex").errors)

    def test_native_plugin_skills_and_disabled_state_are_visible(self):
        package = self.home / ".codex/plugins/cache/demo/plugin/1.0.0"
        skill(package / "skills", "sample")
        (package / ".codex-plugin").mkdir()
        (package / ".codex-plugin/plugin.json").write_text(json.dumps({"name": "plugin", "skills": "./skills/"}))
        payload = {"installed": [{"pluginId": "plugin@demo", "name": "plugin", "marketplaceName": "demo",
                                  "installed": True, "enabled": False, "version": "1.0.0",
                                  "source": {"source": "local", "path": str(package)},
                                  "marketplaceSource": {"sourceType": "git", "source": "https://github.com/example/tools.git"}}],
                   "available": []}
        with patch("scripts.setup_inventory.subprocess.run", return_value=subprocess.CompletedProcess([], 0, json.dumps(payload), "")):
            result = self.inspect("codex")
        installed = next(i for i in result.installations if i.name == "sample")
        self.assertEqual(installed.source, "example/tools")
        self.assertEqual(installed.route, "native")
        self.assertFalse(installed.enabled)

    def test_codex_reads_installed_cache_not_live_checkout(self):
        package = self.home / ".codex/plugins/cache/demo/plugin/1.0.0"
        installed = skill(package / "skills", "sample", "installed revision")
        (package / ".codex-plugin").mkdir()
        (package / ".codex-plugin/plugin.json").write_text('{"skills":"./skills/"}')
        live = self.home / "checkout"
        skill(live / "skills", "sample", "new uninstalled revision")
        (live / ".codex-plugin").mkdir()
        (live / ".codex-plugin/plugin.json").write_text('{"skills":"./skills/"}')
        entry = {"pluginId":"plugin@demo","enabled":True,"version":"1.0.0",
                 "source":{"source":"local","path":str(live)},
                 "marketplaceSource":{"sourceType":"git","source":"https://github.com/example/tools.git"}}
        with patch("scripts.setup_inventory.subprocess.run", return_value=subprocess.CompletedProcess([], 0, json.dumps({"installed":[entry]}), "")):
            result = self.inspect("codex")
        record = next(i for i in result.installations if i.name == "sample")
        self.assertEqual(record.path, installed)

    def test_claude_native_source_from_marketplace_registry(self):
        package = self.home / ".claude/plugins/cache/demo/plugin/1.0.0"
        skill(package / "skills")
        (package / ".claude-plugin").mkdir()
        (package / ".claude-plugin/plugin.json").write_text('{"skills":"./skills/"}')
        registry = self.home / ".claude/plugins/known_marketplaces.json"
        registry.write_text(json.dumps({"demo":{"source":{"source":"github","repo":"example/tools"}}}))
        entry = {"id":"plugin@demo","scope":"user","enabled":True,"version":"1.0.0","installPath":str(package)}
        with patch("scripts.setup_inventory.subprocess.run", return_value=subprocess.CompletedProcess([], 0, json.dumps([entry]), "")):
            result = self.inspect("claude-code")
        self.assertEqual(next(i.source for i in result.installations if i.name == "sample"), "example/tools")

    def test_claude_plugins_from_other_projects_do_not_block_installation(self):
        package = self.home / ".claude/plugins/cache/demo/plugin/1.0.0"
        skill(package / "skills", "sample")
        (package / ".claude-plugin").mkdir()
        (package / ".claude-plugin/plugin.json").write_text('{"skills":"./skills/"}')
        entry = {"id":"plugin@demo","scope":"project","enabled":False,"version":"1.0.0",
                 "installPath":str(package),"projectPath":str(self.project.parent / "another-project"),"projectEnabled":False}
        with patch("scripts.setup_inventory.subprocess.run", return_value=subprocess.CompletedProcess([], 0, json.dumps([entry]), "")):
            result = self.inspect("claude-code", "project")
        self.assertEqual(result.installations, [])
        self.assertEqual(result.errors, [])
        entry["projectPath"] = str(self.project)
        with patch("scripts.setup_inventory.subprocess.run", return_value=subprocess.CompletedProcess([], 0, json.dumps([entry]), "")):
            result = self.inspect("claude-code", "project")
        self.assertFalse(next(i.enabled for i in result.installations if i.name == "sample"))

    def test_native_receipt_detects_local_edits(self):
        package = self.home / ".codex/plugins/cache/demo/plugin/1.0.0"
        folder = skill(package / "skills")
        (package / ".codex-plugin").mkdir()
        (package / ".codex-plugin/plugin.json").write_text('{"skills":"./skills/"}')
        receipt = self.home / ".agents/marketplace/personal/state.json"
        receipt.parent.mkdir(parents=True)
        receipt.write_text(json.dumps({"schema_version":1,"records":{"codex:sample":{
            "name":"sample","path":str(folder),"source":"example/tools","route":"native","digest":self.inv.fingerprint(folder)}}}))
        (folder / "SKILL.md").write_text((folder / "SKILL.md").read_text()+"local edit\n")
        entry = {"pluginId":"plugin@demo","enabled":True,"version":"1.0.0",
                 "marketplaceSource":{"sourceType":"git","source":"https://github.com/example/tools.git"}}
        with patch("scripts.setup_inventory.subprocess.run", return_value=subprocess.CompletedProcess([], 0, json.dumps({"installed":[entry]}), "")):
            result = self.inspect("codex")
        self.assertTrue(next(i.modified for i in result.installations if i.name == "sample"))


if __name__ == "__main__":
    unittest.main()
