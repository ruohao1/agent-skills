# Personal preset verification — 2026-10-17

Scope: the optional `personal` instruction and reviewer preset, selected independently of skills/plugins through `scripts/setup.py`. These are declared preferences, not a comparative evaluation of coding or review quality.

## Deterministic checks

```sh
python3 -m unittest discover -s tests -q
python3 scripts/validate_marketplace.py
```

Observed: 64 tests passed. The validator passed for two native catalogs, one local plugin, one custom skill, and one preset. Tests ran with Python 3.14.4 on Linux; CI is configured for Python 3.12. Runtime now requires Python 3.11+ for standard-library TOML parsing.

The preset suite covers both scopes and all three hosts, selection of either part, unchanged repeats, read-only previews, exact backup bytes and modes, and preservation of unrelated settings. Failure cases include changed or malformed instruction markers, same-name reviewers in native files or settings, ancestor/global roles, shared instruction precedence, JSONC comments and quoted literals, ambiguous configuration, unreadable directories, redirected/shared write paths, changes after preview, and interrupted file replacement followed by retry. The existing skill/native-plugin suite remains passing.

The independent review identified two preservation failures: a Codex write to shared project `AGENTS.md` could bypass an OpenCode fallback conflict, and an OpenCode reviewer file could override a custom reviewer stored inside `opencode.json`. Regression assertions failed before their fixes and pass afterward. Additional malformed-name and unreadable-directory regressions were also observed failing before correction.

## Actual host checks

Each probe used a disposable project and a minimal child-process environment with isolated `HOME`, `CODEX_HOME`, `CLAUDE_CONFIG_DIR`, and XDG config/cache/data/state roots. No existing user configuration or credentials were copied. Native probes are separate from CI and do not make authenticated model requests.

| Check | Global | Project |
| --- | --- | --- |
| Fresh three-host preset install | Passed | Passed |
| Repeat preserves installed bytes and modification times | Passed | Passed |
| Unrelated sentinel remains unchanged | Passed | Passed |
| Codex `debug prompt-input` includes personal instructions | Passed | Passed |
| Claude stream-JSON initialization discovers `personal-reviewer` | Passed | Passed |
| OpenCode `debug agent personal-reviewer` loads the intended role | Passed | Passed |
| OpenCode reports read/glob/grep enabled, command/write/delegation/web/skill tools disabled | Passed | Passed |
| OpenCode resolved read rules ask for `.env` and `.env.local`, allow `.env.example` and ordinary source | Passed | Passed |

The OpenCode environment-file assertion initially failed with a blanket read allowance, which overrode its default approval patterns. The preset now supplies those patterns explicitly; the final native probes passed.

In a separate existing-installation probe, OpenCode loaded a custom inline `personal-reviewer` from `opencode.json`. Preset installation returned a conflict, left the settings bytes unchanged, and created neither the reviewer file nor instructions. A second native inspection still returned the original custom prompt. OpenCode's own inspection may normalize its configuration; the preservation snapshot was taken after the initial host inspection and compared immediately after the setup command.

Observed host versions: Codex 0.163.0, Claude Code 2.1.301, OpenCode 1.18.34. Codex instruction probes used `codex debug prompt-input`. Claude discovery used `-p --input-format stream-json --output-format stream-json --verbose --strict-mcp-config` with an initialization control request and no user/model message. OpenCode probes used `opencode debug agent personal-reviewer`.

## Limits

No authenticated reviewer invocation or comparative behavior evaluation was performed. Codex reviewer TOML matches the documented native format and passes parsing checks; actual reviewer spawning was not verified. Codex custom agents inherit parent permissions, so the reviewer prompt alone does not enforce read-only behavior. Claude/OpenCode tool declarations and OpenCode's resolved restrictions were checked, not adversarial runtime enforcement.

macOS, Windows, older hosts, remote organization settings, and command-line overrides were not tested. Concurrent installers are unsupported. A multi-file failure can leave completed files and backups in place for a safe retry.

See the [preset guide](../../configs/personal/README.md) and [setup preservation rules](../../docs/setup.md#configuration-presets).
