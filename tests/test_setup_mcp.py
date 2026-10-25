import contextlib
import copy
import io
import json
import os
from pathlib import Path
import stat
import tempfile
import tomllib
import unittest
from unittest.mock import patch

from scripts import setup
from scripts.setup_inventory import AGENTS, Target, parse_json


class McpTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.home = self.root / 'home'
        self.home.mkdir()
        self.env = {'HOME': str(self.home), 'PATH': os.environ.get('PATH', '')}
        self.server = {'name': 'chrome-devtools', 'version': '1.12.0',
                       'description': 'Inspect an isolated Chrome browser.'}
        self.catalog = setup.load_catalog()
        self.catalog['mcp_servers'] = [self.server]
        (self.root / 'catalog.json').write_text(json.dumps(self.catalog))
        self.paths = {'codex': self.home / '.codex/config.toml',
                      'claude-code': self.home / '.claude.json',
                      'opencode': self.home / '.config/opencode/opencode.json'}

    def run_cli(self, action='install', agents=AGENTS, scope='global', extra=(), yes=True):
        args = [action, '--mcp', 'chrome-devtools', '--agent', *agents, '--scope', scope,
                '--project', str(self.root), *extra]
        if action == 'install' and yes:
            args.append('--yes')
        output = io.StringIO()
        with patch.object(setup, 'ROOT', self.root), patch.dict(os.environ, self.env, clear=True), \
                patch('sys.stdin.isatty', return_value=False), \
                contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            try:
                result = setup.main(args)
            except SystemExit as error:
                result = error.code
        return result, output.getvalue()

    def write(self, path, text):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        path.chmod(0o640)

    def read(self, agent):
        path = self.paths[agent]
        return tomllib.loads(path.read_text()) if agent == 'codex' else parse_json(path.read_text(), path, comments=True)

    def test_plan_then_install_all_agents_and_unchanged_repeat(self):
        code, output = self.run_cli('plan')
        self.assertEqual(code, 0, output)
        self.assertFalse(any(self.home.iterdir()))
        self.assertIn('chrome-devtools-mcp@1.12.0', output)
        code, output = self.run_cli()
        self.assertEqual(code, 0, output)
        for agent, key in [('codex', 'mcp_servers'), ('claude-code', 'mcpServers'), ('opencode', 'mcp')]:
            entry = self.read(agent)[key]['chrome-devtools']
            command = entry['command'] if agent == 'opencode' else [entry['command'], *entry['args']]
            self.assertEqual(command, ['npx', '-y', 'chrome-devtools-mcp@1.12.0', '--headless',
                                       '--isolated', '--no-usage-statistics', '--no-performance-crux'])
            self.assertEqual(stat.S_IMODE(self.paths[agent].stat().st_mode), 0o600)
        before = {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in self.paths.values()}
        code, output = self.run_cli()
        self.assertEqual(code, 0, output)
        self.assertEqual(before, {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in before})
        self.assertFalse(list(self.home.rglob('*.bak')))

    def test_preserve_other_settings_comments_and_backups_without_printing_secrets(self):
        self.paths['opencode'] = self.paths['opencode'].with_suffix('.jsonc')
        texts = {
            'codex': '# Keep this comment\nmodel = "private-secret"\n[mcp_servers.other]\ncommand = "private-command"\n',
            'claude-code': '{"token":"private-secret","mcpServers":{"other":{"command":"private-command"}}}',
            'opencode': '// Keep this comment\n{"provider":{"mcp":{"secret":"private-secret"}},\n'
                        '"mcp":{/* keep nested */"other":{"command":["private-command"],"type":"local"},},}\n',
        }
        for agent, original in texts.items():
            self.write(self.paths[agent], original)
        code, output = self.run_cli()
        self.assertEqual(code, 0, output)
        self.assertNotIn('private-secret', output)
        self.assertNotIn('private-command', output)
        for agent, original in texts.items():
            path = self.paths[agent]
            backups = list(path.parent.glob(path.name + '.agent-skills-*.bak'))
            self.assertEqual([p.read_text() for p in backups], [original])
            self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o640)
            self.assertEqual(stat.S_IMODE(backups[0].stat().st_mode), 0o600)
            if agent == 'codex':
                self.assertTrue(path.read_text().startswith(original))
            else:
                key = 'mcpServers' if agent == 'claude-code' else 'mcp'
                current = self.read(agent)
                del current[key]['chrome-devtools']
                self.assertEqual(current, parse_json(original, path, comments=True))
            for comment in ['// Keep this comment', '/* keep nested */']:
                if comment in original:
                    self.assertIn(comment, path.read_text())

    def test_existing_official_entry_is_preserved_but_disabled_or_unknown_entries_conflict(self):
        variants = [({'command': 'npx', 'args': ['chrome-devtools-mcp@latest']}, 'present', 0),
                    ({'command': 'npx', 'args': ['chrome-devtools-mcp@latest'], 'enabled': False}, 'conflict', 1),
                    ({'command': 'private-secret', 'args': []}, 'conflict', 1),
                    ({'url': 'https://private-secret'}, 'conflict', 1)]
        path = self.paths['codex']
        for entry, status, expected in variants:
            original = '[mcp_servers.chrome-devtools]\n' + '\n'.join(f'{k} = {json.dumps(v)}' for k, v in entry.items())
            self.write(path, original)
            code, output = self.run_cli(agents=['codex'])
            self.assertEqual(code, expected, output)
            self.assertIn(status, output)
            self.assertNotIn('private-secret', output)
            self.assertEqual(path.read_text(), original)

    def test_invalid_configuration_and_unsafe_paths_are_preserved(self):
        path = self.paths['opencode']
        for original in ['{"mcp":null}', '{"mcp":{"chrome-devtools":{}}}',
                         '{"private-secret":1,"private-secret":2}', '{"token":"private-secret",bad}',
                         '{"mcp":[]}']:
            self.write(path, original)
            code, output = self.run_cli(agents=['opencode'])
            self.assertEqual(code, 1, output)
            self.assertEqual(path.read_text(), original)
            self.assertNotIn('private-secret', output)
        path.unlink()
        other = self.root / 'other.json'
        other.write_text('{}')
        path.symlink_to(other)
        code, output = self.run_cli(agents=['opencode'])
        self.assertEqual(code, 1, output)
        self.assertEqual(other.read_text(), '{}')

    def test_explicit_scope_selection_and_confirmation(self):
        for scope, extra, yes in [('project', (), True), ('global', ('--route', 'native'), True),
                                  ('global', ('--preset-part', 'instructions'), True),
                                  ('global', (), False)]:
            code, output = self.run_cli(scope=scope, extra=extra, yes=yes)
            self.assertNotEqual(code, 0, output)
            self.assertFalse(any(self.home.iterdir()))
        self.assertNotIn('chrome-devtools', setup.select_skills(self.catalog, 'all', []))

    def test_custom_roots_and_ambiguous_opencode_configuration(self):
        self.env.update(CODEX_HOME=str(self.home / 'codex-custom'),
                        CLAUDE_CONFIG_DIR=str(self.home / 'claude-custom'),
                        XDG_CONFIG_HOME=str(self.home / 'xdg-custom'))
        code, output = self.run_cli()
        self.assertEqual(code, 0, output)
        for path in ['codex-custom/config.toml', 'claude-custom/.claude.json', 'xdg-custom/opencode/opencode.json']:
            self.assertTrue((self.home / path).is_file())
        self.write(self.home / 'xdg-custom/opencode/opencode.jsonc', '{}')
        self.assertEqual(self.run_cli(agents=['opencode'])[0], 1)
        for key in ['OPENCODE_CONFIG', 'OPENCODE_CONFIG_DIR', 'OPENCODE_CONFIG_CONTENT']:
            with patch.dict(self.env, {key: 'private-secret'}):
                code, output = self.run_cli(agents=['opencode'])
                self.assertEqual(code, 1, output)
                self.assertNotIn('private-secret', output)

    def test_configuration_changed_after_preview_is_preserved(self):
        from scripts import setup_mcp
        target = Target('codex', 'global', self.root)
        plan = setup_mcp.build_plan(self.server, [target], self.env)
        self.write(self.paths['codex'], 'model = "changed"\n')
        result = setup_mcp.apply_plan(plan, self.server, self.env)
        self.assertEqual(result[0].status, 'conflict')
        self.assertEqual(self.paths['codex'].read_text(), 'model = "changed"\n')
        self.assertFalse(list(self.home.rglob('*.bak')))

    def test_catalog_rejects_unpinned_or_unknown_servers(self):
        for mutation in [dict(version='latest'), dict(version='1.12.0; command'), dict(name='unknown'), dict(description='')]:
            data = copy.deepcopy(self.catalog)
            data['mcp_servers'][0].update(mutation)
            (self.root / 'catalog.json').write_text(json.dumps(data))
            with self.assertRaises(ValueError):
                setup.load_catalog(self.root)


if __name__ == '__main__':
    unittest.main()
