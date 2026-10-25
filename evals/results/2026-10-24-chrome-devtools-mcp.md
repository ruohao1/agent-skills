# Chrome DevTools MCP setup verification

Date: 2026-10-24. These checks verify installation and browser access. They do
not measure agent task quality.

## Automated checks

- The new MCP test suite failed before implementation because selection,
  configuration writing, and MCP catalog validation were absent.
- All 73 unit tests passed after implementation. The new checks cover three
  host formats, custom roots, JSONC comments, preserved settings, private
  previews, backups, repeated installs, conflicts, and changes after preview.
- The marketplace validator passed: two catalogs, three plugins, six custom
  skills, one preset, and one MCP selection.

## Disposable installation and runtime checks

Linux checks used Chrome DevTools MCP `1.12.0`, Node `22.23.1`, npm/npx,
Chrome `155.0.8059.84`, Codex CLI `0.164.0`, Claude Code `2.1.303`, and
OpenCode `1.18.34`. The Claude binary came from a temporary package.

| Check | Observed result |
| --- | --- |
| Install all three global configurations in a disposable home | Passed |
| Repeat the install | Passed; bytes and modification times unchanged |
| Codex `mcp get chrome-devtools --json` | Read the generated entry |
| Claude `mcp get chrome-devtools` | Reported Connected |
| OpenCode `mcp list` | Reported connected |
| Claude default and custom configuration roots | CLI wrote `~/.claude.json` and `$CLAUDE_CONFIG_DIR/.claude.json`, respectively |
| Exact generated command, MCP initialize and tools/list | Server reported version `1.12.0` and 32 tools |
| Exact generated command, list_pages | Listed an isolated `about:blank` page |

The browser probe used the command from a generated configuration and an
isolated browser. It closed its server afterward.
An earlier probe inside the restricted process sandbox closed the Chrome
target. The same operation passed with normal process permissions.

## Final review

An independent final code review found no issues. The reviewer repeated all
73 unit tests and marketplace validation successfully. Project and managed
settings, and concurrent installers, remain outside the documented scope.

## Limits

Project scope is intentionally unsupported for MCP setup. macOS and Windows
were not tested. These checks do not prove availability in an already running
agent session. Managed configuration, project overrides, command-line settings,
and host trust can affect runtime access. Setup reports configuration state
separately from those checks.

## References

- [Official server and installation instructions](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- [Server options](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/configuration.md)
- [Claude MCP configuration](https://code.claude.com/docs/en/mcp)
- [OpenCode MCP configuration](https://opencode.ai/docs/mcp-servers/)
