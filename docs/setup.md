# Set up your tools

The catalog contains 28 skills, combining this repository's custom skills with selected upstream tools. Product Design and Engineering are categories; custom and upstream identify who maintains each tool. External sources stay upstream and their portable skill revisions are pinned in `catalog.json`.

Install the coding agents first. The setup command needs Python 3.11+. Installing skills also needs Node 22.20.0+, npm/npx, Git, and access to GitHub and npm. Native plugin installation needs the selected host CLI. Applying a local configuration preset needs only Python. Authentication and hook trust remain host setup steps.

## Choose what to install

From a checkout of `ruohao1/agent-skills`:

```sh
python3 scripts/setup.py
```

The terminal selector offers all skills, a category, individual skills, a plugin bundle, a configuration preset, or an MCP server. It then asks which agents and scope to use. Preview without installing:

```sh
python3 scripts/setup.py list
python3 scripts/setup.py plan --all --agent codex --scope global
```

Install the complete curated portable selection for chosen agents:

```sh
python3 scripts/setup.py install --all --agent codex claude-code opencode --scope global
```

“All skills” means the 28 named skills, not every skill in upstream repositories. Configuration presets and MCP servers are selected separately. Only list the agents you want. Shared compatibility directories may make a skill visible to another agent that reads the same directory.

Choose a category, particular skills, or a complete plugin's skills:

```sh
python3 scripts/setup.py install --category product-design --agent codex --scope global
python3 scripts/setup.py install --skill product-brief archify --agent opencode --scope project --project /path/to/project
python3 scripts/setup.py install --plugin product-design --agent claude-code --scope project
```

The default project is the current directory. Use `--project` when running the coordinator from its checkout to install into another repository. The local custom source is the checkout containing the coordinator; the target project is only the installation destination.

`install` previews the selection before confirmation. For scripts, supply every choice and add `--yes` after reviewing the corresponding `plan`. That flag does not override conflicts, trust hooks, or authenticate services.

The coordinator honors `CODEX_HOME`, `CLAUDE_CONFIG_DIR`, `XDG_CONFIG_HOME` and `XDG_STATE_HOME` when inspecting host configuration. The pinned Skills CLI writes Codex and OpenCode portable skills to the shared `~/.agents/skills` directory; inventory also checks OpenCode’s configured legacy directory. Global source metadata uses `$XDG_STATE_HOME/skills/.skill-lock.json` when set, otherwise `~/.agents/.skill-lock.json`. Scope and host configuration affect visibility as well as installation destinations.

## Existing installations

The coordinator checks visible skill directories, installer source metadata, its own content receipts, and native plugin state. It preserves matching installed content without updating it. A global or parent-project skill that already satisfies a project request is kept rather than shadowed.

Different sources using the same name, changed content recorded by this coordinator, overlapping native/standalone installations, unknown ownership, and incomplete inventory are reported before any affected write. Existing installations from other tools may have source metadata but no local content baseline; they are preserved, without a claim that local edits have been assessed. Unrelated broken or unreadable inventory can require repair before that target is safe to change.

The setup rechecks each missing destination and installer lock path immediately before invoking an installer. Redirecting lock symlinks, shared hardlinks, unsupported lock versions and project lock fields the installer would discard are preserved and reported. Required resources are checked before an existing selected skill is considered present. Do not run another installer concurrently. It does not merge edits, remove old skills, or roll back another tool's changes.

Results distinguish `installed`, `present`, `conflict`, `unsupported`, `failed`, and `needs-setup`. A source failure does not discard successful installations. Resolve the reported issue and rerun the unresolved selection; unchanged successful items are skipped. Partial files without verifiable source/content are preserved for review rather than deleted.

Receipts live at `~/.agents/marketplace/personal/state.json` for global scope, or `<project>/.agents/marketplace/personal/state.json` for project scope. They contain source/ref, paths, and content fingerprints, not credentials. Actual installed files remain authoritative. Keep receipts if you want subsequent local-edit detection.

## Configuration presets

The personal preset includes STE-inspired English writing preferences for general replies. The maintained writing skills contain that guidance themselves; installing one does not require or install the preset. Neither route enforces the full ASD-STE100 dictionary or claims formal compliance. See the [writing evaluation](../evals/results/2026-10-24-ste-writing.md).

The [personal preset](../configs/personal/README.md) supplies one shared instruction source and native reviewer definitions for all three hosts. Setup installs the shared content as `AGENTS.md` for Codex and OpenCode, or `CLAUDE.md` for Claude Code. It is independent of skill and plugin installation:

```sh
python3 scripts/setup.py list --preset personal
python3 scripts/setup.py plan --preset personal --agent codex --scope global
python3 scripts/setup.py install --preset personal --agent codex --scope global
python3 scripts/setup.py install --preset personal --preset-part agents --agent claude-code opencode --scope project --project /path/to/project
```

Both parts are selected by default; `--preset-part instructions` or `--preset-part agents` selects one. A preset cannot be combined with a skill selector or `--route native`. Preset installation writes host-native files directly and does not invoke the Skills CLI. It never rewrites `config.toml`, `settings.json`, or `opencode.json`/`opencode.jsonc`.

`plan` reads local configuration and displays proposed additions without writing or starting a host. `install` displays the same preview before confirmation; `--yes` confirms it in scripts. New files use owner-only permissions. Existing instructions retain their original bytes and permissions, with the preset appended between `<!-- agent-skills:personal:begin -->` and `<!-- agent-skills:personal:end -->`. Before changing an existing file, setup saves its original bytes and mode in an adjacent `<filename>.agent-skills-<digest>.bak`. The preview contains added lines without surrounding private instructions. Backups can contain private instructions; keep them private and out of version control.

An unchanged repeat preserves files and modification times. An edited block, incomplete markers, conflicting backup, redirected write path, unreadable configuration, or differing same-name reviewer blocks all selected files for that host and scope. An identical reviewer already visible globally or in a parent project satisfies a project selection without making another copy. Inventory checks ordinary native agent files and local settings, including OpenCode JSONC, custom configuration paths/directories, and inline environment configuration. Unusual Claude YAML name syntax requires manual reconciliation rather than guessing its identity. Remote organization settings and command-line overrides are outside this local inventory.

Project `AGENTS.md` is shared by Codex and OpenCode. Creating it can change which rules OpenCode reads, even when only Codex is selected. Setup therefore reports conflicts with differing ancestor instructions or Claude fallback rules before creating it. Apply the instructions at their existing project root or reconcile the rules manually; `--preset-part agents` remains available. Codex additions use a nonempty `AGENTS.override.md` when present. See the preset's [host format references](../configs/personal/README.md#host-formats) for precedence.

Each target is checked again immediately before applying it. Do not edit the same files or run another installer concurrently. File writes are atomic, but the whole installation is not a transaction: an I/O failure can leave earlier files installed and a backup created. Successful targets remain installed; resolve the reported issue and retry. There is no automatic settings merge, preset upgrade, or removal command.

To remove instructions, review the file and remove only the marked block. Restore a backup only if doing so will not discard subsequent edits. Remove a reviewer file only after confirming it is the preset copy you intend to remove; shared/global copies may serve other projects. To update a locally edited preset, reconcile it manually with the current source, then preview again. Reload the host session after changing configuration and complete any host trust or authentication steps yourself.

## MCP servers

Chrome DevTools MCP is an optional global configuration for all three agents:

```sh
python3 scripts/setup.py list --mcp chrome-devtools
python3 scripts/setup.py plan --mcp chrome-devtools --agent codex claude-code opencode --scope global
python3 scripts/setup.py install --mcp chrome-devtools --agent codex claude-code opencode --scope global
```

Select only the agents you use. Add `--yes` for a reviewed scripted install.
Project scope is not supported for this selection; setup reports it without
writing elsewhere. MCP selection cannot be combined with skills, presets, or
`--route native`.

New entries run `npx -y chrome-devtools-mcp@1.12.0 --headless --isolated --no-usage-statistics --no-performance-crux`.
The version is pinned in `catalog.json`. The server needs npm/npx, Chrome, and
Node `^20.19.0`, `^22.12.0`, or `>=23`. The host downloads the package on first
use, so its initial connection needs registry access and may take longer.
Setup writes configuration; it does not install Node, Chrome, or an agent CLI.

The browser starts when a browser tool is called. It uses a temporary profile
and does not attach to your ordinary Chrome session. Cookies and logins do not
persist after that browser closes. New entries disable usage statistics and
CrUX requests. Existing recognized entries keep their own version and options.
See the [upstream options](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/configuration.md)
before changing these defaults.

| Agent | Global file |
| --- | --- |
| Codex | `$CODEX_HOME/config.toml`, or `~/.codex/config.toml` |
| Claude Code | `$CLAUDE_CONFIG_DIR/.claude.json` when set, or `~/.claude.json` |
| OpenCode | `$XDG_CONFIG_HOME/opencode/opencode.json`, or `~/.config/opencode/opencode.json`; use the existing `.jsonc` file if present |

Setup adds only the missing server. It preserves other values, formatting,
comments, and existing file permissions. Changed files receive an adjacent
`.agent-skills-<digest>.bak` backup with owner-only permissions. New files also
use owner-only permissions. The preview shows the new command and paths without
printing existing settings. Backups can contain credentials; keep them private.

Disabled, ambiguous, or unrecognized Chrome entries are conflicts. Malformed
files, unsafe paths, differing backups, and edits after preview also block the
affected write. OpenCode's custom configuration environment variables and
simultaneous `.json` and `.jsonc` files require manual reconciliation. TOML
layouts that cannot accept an appended server table also require manual edits.
`--yes` does not override these checks. Successful targets remain configured if
another target fails. Do not edit the files or run another installer concurrently.

Reload the agent after installation. Use `codex mcp get chrome-devtools`,
`claude mcp get chrome-devtools`, or `opencode mcp list` to check configuration
and connection status. Then call a browser tool in a fresh session. Project,
managed, and command-line settings can override global configuration; setup does
not inspect those layers or bypass host trust. Restricted process environments
can also prevent Chrome from starting.

To update or remove the server, review its entry in the host configuration.
Setup preserves existing versions and does not provide automatic upgrades or
removal. Restore a backup only if this will not discard later changes.

See [verification results](../evals/results/2026-10-24-chrome-devtools-mcp.md)
for the tested versions and remaining runtime limits.

## Full native plugins

Portable installation supplies skill files and their resources. Full native plugins may additionally supply hooks or servers. Choose the native route explicitly for a whole plugin:

```sh
python3 scripts/setup.py install --plugin product-design --route native --agent codex --scope global
python3 scripts/setup.py install --plugin product-design --route native --agent claude-code --scope project --project /path/to/project
python3 scripts/setup.py install --plugin ponytail --route native --agent codex --scope global
```

| Route | Codex | Claude Code | OpenCode |
| --- | --- | --- | --- |
| Portable skills | Global and project | Global and project | Global and project |
| Full native plugin | Global | User/global and project | Unsupported |

Unsupported requests never fall back to a different agent or scope. A native request cannot select only one skill from a plugin. Existing standalone copies block installing an overlapping full plugin until you explicitly resolve the overlap.

Native custom plugins register this checkout; keep it available for future native marketplace operations. Native external plugins follow their upstream marketplace's version rules. Their native versions are not controlled by the portable source pins. The coordinator adds missing plugins; it does not refresh existing marketplaces or upgrade installed plugins.

Ponytail on Codex needs the host's hook-trust review in `/hooks` and a new thread. Claude may need plugin reload or a new session. The setup reports those checks as `needs-setup`; it does not assert that trust, authentication, or activation occurred. Verify functionality in the host session before relying on it.

## Direct installation and maintenance

The original shared installation command remains available:

```sh
npx skills@latest add ruohao1/agent-skills
```

It discovers this repository's local custom skills, not the remote setup catalog. It also does not apply this coordinator's preservation checks. Select the skills, agents, and scope in the Skills CLI. The coordinator uses the tested version recorded in `catalog.json`; the direct command intentionally follows `latest`.

Updating or replacing content is a separate decision. Inspect the exact installed path and source, preserve local edits you want to keep, and use the upstream installer's narrowly selected add/reinstall or native plugin update command. Avoid an unscoped update-all command when you only intend to change one tool. Re-run the setup preview afterward; changed coordinator-managed content requires review rather than automatic receipt adoption.

Retired local invocations map to upstream tools: `product-diagrams` → `archify`, `product-wireframes` → `prototype`. The setup does not automatically uninstall old copies. Remove a retired installation through the route that owns it when you choose to migrate. `product-design-review` is also retired after baseline evaluation found no useful custom guidance to add; request a design review directly. The three engineering candidates from the original rewrite were not shipped for the same reason. Engineering now includes the custom [Software Design](../plugins/software-design/README.md), [Linear Workflows](../plugins/linear-workflows/README.md), [Git Workflows](../plugins/git-workflows/README.md), and [Code Quality](../plugins/code-quality/README.md) plugins alongside selected upstream skills, including the Ponytail bundle.

## Validation evidence

Run deterministic checks from the repository root:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/validate_marketplace.py
```

Real installation checks use disposable homes and projects. A successful installer layout check does not establish that an authenticated agent session loaded and followed the skill. See the [rewrite evaluation results](../evals/results/2026-10-16-marketplace-rewrite.md) for observed versions, scenarios, and remaining host checks.

Observed on 2026-10-17: the final full portable selection installed and repeated successfully at global and project scopes for all three agents. Native product-design 0.2.0 installed and repeated on Codex global and Claude Code user/project; Ponytail 5.3.2 installed on those routes and correctly remained `needs-setup`. Codex and OpenCode discovered all thirteen portable skills through their own inspection interfaces. These Linux checks used Codex 0.163.0, Claude Code 2.1.301, OpenCode 1.18.34 and Skills CLI 1.7.2. Authenticated conversations, native hook activation and macOS/Windows runtime behavior remain untested.

Configuration preset checks and their separate limits are recorded in [personal preset verification](../evals/results/2026-10-17-personal-preset.md).

[Git Workflows](../plugins/git-workflows/README.md) adds `write-commit`, with [behavioral, isolated Git, and portable installation results](../evals/results/2026-10-21-write-commit.md). Its real hosting lookups and native host activation remain untested. Linear Workflows 0.2.1 also records the user's concise prose and useful-bullets preference.

Git Workflows 0.2.0 adds `write-pull-request`, including public-repository privacy for PR descriptions and review trackers. Its [results](../evals/results/2026-10-23-write-pull-request.md) distinguish an authorized real description cleanup from synthetic creation checks and disposable installation checks. Native host activation remains untested.

The subsequent `write-linear-issue` addition passed separate [behavioral and portable installation checks](../evals/results/2026-10-21-write-linear-issue.md) on 2026-10-21. Its native plugin activation and authenticated Linear operations remain untested; the earlier 13-skill host discovery results do not cover this addition.

Linear Workflows 0.2.0 adds `write-linear-comment`, with its own [behavioral and portable installation results](../evals/results/2026-10-21-write-linear-comment.md). Its code-dependent comments require a verified published source permalink before saving. Native activation and authenticated comment operations remain untested.

Product Design 0.3.0 adds `design-product` for flows, interactions, recovery, and visual experience. Install it independently:

```sh
python3 scripts/setup.py install --skill design-product --agent codex claude-code opencode --scope global
```

Software Design 0.1.0 adds independent `design-architecture` and `design-code` skills. Select one skill or the complete bundle:

```sh
python3 scripts/setup.py install --skill design-code --agent codex --scope global
python3 scripts/setup.py install --plugin software-design --agent codex claude-code opencode --scope global
```

All three design skills save concise handoffs under `docs/designs/` by default. An existing document, explicit destination, or text-only request takes precedence. Each works without a companion skill, audit, or mandatory implementation step. See the [design evaluation](../evals/design-skills.md) and [results](../evals/results/2026-10-25-design-skills.md) for the comparison method and validation scope.

Git Workflows 0.4.0 adds `manage-worktrees` for automatic isolation before repository edits, matching workspace resumption and verified cleanup after merge. New worktrees use `repo/.worktree/<branch>`. The skill works without the personal preset and supplies no background service or cross-host lock. See the [worktree results](../evals/results/2026-10-28-manage-worktrees.md) for observed behavior and installation limits.

Linear Workflows 0.7.0 adds `check-linear-context` and `maintain-linear-project`. Select either independently; no preset or shared instruction edit is required. Context discovery needs read access. Starting authorized work on a verified issue also needs status-update access. Project cleanup needs the relevant issue/document operations and preserves unresolved decisions. Existing writing, comments and completion rules remain in force. See the [original context evaluation](../evals/results/2026-10-25-check-linear-context.md) and [current publication checks](../evals/results/2026-10-29-linear-workflows.md) for the tested scopes and limits.
