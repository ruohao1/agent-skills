"""Add the selected Chrome DevTools MCP server to global agent configuration."""
from __future__ import annotations

from dataclasses import dataclass, replace
import json
from pathlib import Path
import re
import shlex
import sys
import tomllib
from typing import Mapping

try:
    from .setup_inventory import Target, host_roots, parse_json
    from .setup_presets import Change, _read, prepare_change, write_change
except ImportError:
    from setup_inventory import Target, host_roots, parse_json
    from setup_presets import Change, _read, prepare_change, write_change


@dataclass
class McpPlan:
    name: str
    target: Target
    status: str = 'missing'
    reason: str = 'Add the server configuration; reload the host afterward'
    change: Change | None = None


def command(server: dict) -> list[str]:
    return ['npx', '-y', 'chrome-devtools-mcp@' + server['version'], '--headless',
            '--isolated', '--no-usage-statistics', '--no-performance-crux']


def _destination(target: Target, env: Mapping[str, str]) -> Path:
    roots = host_roots(env)
    if target.agent == 'codex':
        path = roots['codex'] / 'config.toml'
    elif target.agent == 'claude-code':
        path = (roots['claude-code'] if env.get('CLAUDE_CONFIG_DIR') else roots['home']) / '.claude.json'
    else:
        for key in ('OPENCODE_CONFIG', 'OPENCODE_CONFIG_DIR', 'OPENCODE_CONFIG_CONTENT'):
            if env.get(key):
                raise ValueError(f'{key} is set; reconcile custom MCP configuration manually')
        paths = [roots['opencode'] / name for name in ('opencode.json', 'opencode.jsonc')]
        if not all(p.is_absolute() for p in paths):
            raise ValueError('Configuration roots must be absolute paths')
        existing = [p for p in paths if _read(p) is not None]
        if len(existing) > 1:
            raise ValueError('Both OpenCode config formats exist; reconcile them manually')
        path = existing[0] if existing else paths[0]
    if not path.is_absolute():
        raise ValueError('Configuration roots must be absolute paths')
    return path


def _parse(text: str, agent: str, path: Path) -> dict:
    try:
        return tomllib.loads(text) if agent == 'codex' else parse_json(text, path, comments=agent == 'opencode')
    except ValueError:
        # Parser errors can include private keys or values.
        raise ValueError(f'Cannot parse configuration; preserved: {path}') from None


def _official(entry: object, agent: str) -> bool:
    if not isinstance(entry, dict) or 'url' in entry:
        return False
    if agent == 'opencode':
        argv = entry.get('command') if entry.get('type') == 'local' else None
    else:
        args = entry.get('args', [])
        argv = [entry.get('command'), *args] if isinstance(args, list) else None
        if entry.get('type', 'stdio') != 'stdio':
            return False
    if not isinstance(argv, list) or len(argv) < 2 or not all(isinstance(a, str) for a in argv):
        return False
    if Path(argv[0]).name not in ('npx', 'npx.cmd'):
        return False
    args = argv[1:]
    while args and args[0] in ('-y', '--yes'):
        args = args[1:]
    return bool(args and re.fullmatch(r'chrome-devtools-mcp(?:@(?:latest|\d+\.\d+\.\d+))?', args[0]))


def _insert_json(text: str, data: dict, key: str, name: str, entry: dict) -> str:
    # Locate an object opening only; the shared parser validates both documents.
    tokens = [m for m in re.finditer(r'"(?:[^"\\]|\\.)*"|//[^\r\n]*|/\*[\s\S]*?\*/|[^\s]', text)
              if not m[0].startswith(('//', '/*'))]
    opening = tokens[0].end()
    addition = {key: {name: entry}}
    container = data
    if key in data:
        depth = 0
        for i, token in enumerate(tokens):
            value = token[0]
            if depth == 1 and value.startswith('"') and json.loads(value) == key and tokens[i + 1][0] == ':':
                opening = tokens[i + 2].end()
                break
            if value in ('{', '['):
                depth += 1
            elif value in ('}', ']'):
                depth -= 1
        addition, container = {name: entry}, data[key]
    inserted = json.dumps(addition, indent=2)[1:-1].rstrip() + (',' if container else '') + '\n'
    return text[:opening] + inserted + text[opening:]


def build_plan(server: dict, targets: list[Target], env: Mapping[str, str]) -> list[McpPlan]:
    items = []
    for target in targets:
        item = McpPlan(server['name'], target)
        items.append(item)
        if target.scope != 'global':
            item.status, item.reason = 'unsupported', 'MCP setup supports --scope global only; no files changed'
            continue
        try:
            path = _destination(target, env)
            before = _read(path)
            text = before.decode('utf-8') if before is not None else ('' if target.agent == 'codex' else '{}\n')
            data = _parse(text, target.agent, path)
            key = {'codex': 'mcp_servers', 'claude-code': 'mcpServers', 'opencode': 'mcp'}[target.agent]
            servers = data.get(key, {})
            if not isinstance(servers, dict):
                raise ValueError(f'MCP settings must be an object; preserved: {path}')
            matches = [entry for name, entry in servers.items() if name == item.name or _official(entry, target.agent)]
            if matches:
                if len(matches) != 1 or not _official(matches[0], target.agent) or matches[0].get('enabled', True) is not True:
                    raise ValueError('Existing server is disabled, ambiguous, or unrecognized; preserved')
                item.status, item.reason = 'present', 'Existing Chrome DevTools entry preserved, including its version and options; runtime not checked'
                continue
            argv = command(server)
            entry = ({'type': 'local', 'command': argv, 'enabled': True} if target.agent == 'opencode'
                     else {'command': argv[0], 'args': argv[1:]})
            if target.agent == 'claude-code':
                entry['type'] = 'stdio'
            if target.agent == 'codex':
                after = text + '\n[mcp_servers.chrome-devtools]\n' + '\n'.join(f'{k} = {json.dumps(v)}' for k, v in entry.items()) + '\n'
            else:
                after = _insert_json(text, data, key, item.name, entry)
            expected = {**data, key: {**servers, item.name: entry}}
            if _parse(after, target.agent, path) != expected:
                raise ValueError('Cannot add the server without changing other settings; preserved')
            item.change = prepare_change(path, before, after.encode('utf-8'))
        except UnicodeError:
            item.status, item.reason = 'conflict', 'Configuration is not UTF-8; preserved'
        except (OSError, ValueError) as error:
            item.status, item.reason = 'conflict', str(error)
    return items


def apply_plan(items: list[McpPlan], server: dict, env: Mapping[str, str]) -> list[McpPlan]:
    result = []
    for item in items:
        if item.status != 'missing':
            result.append(item)
            continue
        try:
            fresh = build_plan(server, [item.target], env)[0]
            if fresh.status != 'missing' or fresh.change != item.change:
                result.append(replace(item, status='conflict', reason='Configuration or destination changed after preview; preserved'))
                continue
            write_change(fresh.change, private_backup=True)
            if _read(fresh.change.path) != fresh.change.after:
                raise ValueError('Written configuration could not be verified')
            result.append(replace(fresh, status='installed', reason='Configuration verified; reload the host and check MCP status'))
        except (OSError, ValueError) as error:
            result.append(replace(item, status='failed', reason=str(error)))
    return result


def show(items: list[McpPlan]) -> None:
    for item in items:
        print(f'{item.status:12} {item.name} [{item.target.agent}, {item.target.scope}]: {item.reason}')
        if item.change:
            print(f'  {item.change.path}')
            if item.change.backup:
                print(f'  Backup: {item.change.backup}')


def run(server: dict, targets: list[Target], action: str, yes: bool, env: Mapping[str, str]) -> int:
    items = build_plan(server, targets, env)
    print('MCP configuration (new entries): ' + shlex.join(command(server)))
    show(items)
    if action == 'plan':
        return int(any(i.status not in ('missing', 'present') for i in items))
    if not yes and any(i.status == 'missing' for i in items):
        if not sys.stdin.isatty():
            raise ValueError('Use --yes after reviewing the MCP plan in noninteractive mode')
        if input('Add the missing MCP configurations shown above? [y/N]: ').strip().lower() not in ('y', 'yes'):
            return 0
    result = apply_plan(items, server, env)
    show(result)
    return int(any(i.status not in ('installed', 'present') for i in result))
