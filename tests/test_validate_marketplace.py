import copy
import json
from pathlib import Path
import tempfile
import unittest

from scripts import validate_marketplace as validator


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.codex = {"name":"personal", "interface":{"displayName":"Personal"}, "plugins":[]}
        self.claude = {"name":"personal", "owner":{"name":"tester"}, "plugins":[]}
        self.catalog = {"schema_version":1, "installer_version":"1.7.2",
                        "sources":{"local":{"repository":"ruohao1/agent-skills","ref":None,"local_path":"."}},
                        "skills":[], "plugins":[]}
        for name in ("product-design", "engineering"):
            skill_name = name + "-example"
            source = "./plugins/" + name
            self.codex["plugins"].append({"name":name,"source":{"source":"local","path":source},
                                           "policy":{"installation":"AVAILABLE","authentication":"ON_INSTALL"},"category":"Productivity"})
            self.claude["plugins"].append({"name":name,"source":source})
            manifest = {"name":name,"version":"1.0.0","description":"Example plugin.","author":{"name":"tester"},"skills":"./skills/"}
            self.write(f"plugins/{name}/.claude-plugin/plugin.json", manifest)
            manifest["interface"] = {"displayName":name,"shortDescription":"Example","longDescription":"An example.",
                                      "developerName":"tester","category":"Productivity","capabilities":[],"defaultPrompt":["Try it."]}
            self.write(f"plugins/{name}/.codex-plugin/plugin.json", manifest)
            path = f"plugins/{name}/skills/{skill_name}"
            self.write(path + "/SKILL.md", f"---\nname: {skill_name}\ndescription: Use when testing packaging.\n---\nInstructions.\n")
            self.catalog["skills"].append({"name":skill_name,"category":name,"ownership":"custom","source":"local","path":path,"description":"Example."})
            self.catalog["plugins"].append({"name":name,"skills":[skill_name],"native":{"marketplace":"personal","repository":"ruohao1/agent-skills"}})
        self.save_catalogs()

    def write(self, path, data):
        path = self.root / path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(data if isinstance(data, str) else json.dumps(data))

    def save_catalogs(self):
        self.write(".agents/plugins/marketplace.json", self.codex)
        self.write(".claude-plugin/marketplace.json", self.claude)
        self.write("catalog.json", self.catalog)

    def check(self):
        return validator.validate_repository(self.root)

    def test_valid_packages(self):
        self.assertEqual(self.check(), ("personal", 2, 2))

    def test_mismatched_catalogs_and_manifests(self):
        self.claude["plugins"].reverse()
        self.save_catalogs()
        with self.assertRaises(ValueError):
            self.check()
        self.claude["plugins"].reverse()
        self.save_catalogs()
        path = self.root / "plugins/product-design/.claude-plugin/plugin.json"
        data = json.loads(path.read_text())
        data["version"] = "2.0.0"
        path.write_text(json.dumps(data))
        with self.assertRaises(ValueError):
            self.check()

    def test_local_catalog_exact_membership_and_bundle(self):
        original = copy.deepcopy(self.catalog)
        for change in (lambda c:c["skills"].pop(),
                       lambda c:c["skills"][0].update(path="elsewhere/product-design-example"),
                       lambda c:c["plugins"][0].update(skills=["engineering-example"]),
                       lambda c:c["plugins"][0]["native"].update(marketplace="someone-else")):
            self.catalog = copy.deepcopy(original)
            change(self.catalog)
            self.save_catalogs()
            with self.subTest(catalog=self.catalog), self.assertRaises(ValueError):
                self.check()

    def test_duplicate_skill_names(self):
        path = "plugins/engineering/skills/product-design-example/SKILL.md"
        self.write(path, "---\nname: product-design-example\ndescription: Use when testing.\n---\nInstructions.")
        with self.assertRaises(ValueError):
            self.check()

    def test_missing_and_escaping_resources(self):
        path = self.root / "plugins/product-design/skills/product-design-example/SKILL.md"
        original = path.read_text()
        self.write("plugins/product-design/README.md", "Outside this skill.")
        for link in ("missing.md", "../../README.md"):
            path.write_text(original + f"\nRead [guide]({link}).\n")
            with self.subTest(link=link), self.assertRaises(ValueError):
                self.check()
        path.write_text(original)
        (path.parent / "resource").symlink_to(self.root / "plugins/product-design/README.md")
        with self.assertRaises(ValueError):
            self.check()

    def test_example_links_in_code_are_not_required_resources(self):
        path = self.root / "plugins/product-design/skills/product-design-example/SKILL.md"
        path.write_text(path.read_text() + '\nExample: `[output](/abs/path/output.html)`.\n\n```markdown\n[template](not-a-resource.md)\n```\n')
        self.assertEqual(self.check(), ("personal", 2, 2))

    def test_presets_require_shared_instructions_and_valid_native_agents(self):
        self.catalog["presets"] = [{"name": "personal", "description": "Personal preferences."}]
        self.save_catalogs()
        with self.assertRaises((ValueError, OSError)):
            self.check()
        self.write("configs/personal/AGENTS.md", "Keep changes focused.\n")
        for agent in ("codex", "claude-code", "opencode"):
            directory = f"configs/personal/{agent}"
            if agent == "codex":
                self.write(directory + "/agents/personal-reviewer.toml", 'name = "personal-reviewer"\ndescription = "Review."\ndeveloper_instructions = "Report findings."\n')
            else:
                self.write(directory + "/agents/personal-reviewer.md", '---\nname: personal-reviewer\ndescription: Review.\nmode: subagent\n---\nReport findings.\n')
        self.assertEqual(self.check(), ("personal", 2, 2))
        for relative, bad in (
            ("AGENTS.md", ""),
            ("AGENTS.md", "<!-- agent-skills:personal:begin -->\n"),
            ("codex/agents/personal-reviewer.toml", 'name = [broken'),
            ("codex/agents/personal-reviewer.toml", 'name = "someone-else"\ndescription = "Review."\ndeveloper_instructions = "Review."\n'),
            ("claude-code/agents/personal-reviewer.md", '---\nname: personal-reviewer\ndescription: [broken\n---\nReview.\n'),
            ("opencode/agents/personal-reviewer.md", '---\ndescription: Review.\nmode: invalid\n---\nReview.\n'),
        ):
            path = self.root / "configs/personal" / relative
            original = path.read_text()
            try:
                path.write_text(bad)
                with self.subTest(relative=relative, bad=bad), self.assertRaises((ValueError, validator.yaml.YAMLError)):
                    self.check()
            finally:
                path.write_text(original)

    def test_unregistered_preset_directory_is_rejected(self):
        (self.root / "configs/unlisted").mkdir(parents=True)
        with self.assertRaises(ValueError):
            self.check()


if __name__ == "__main__":
    unittest.main()
