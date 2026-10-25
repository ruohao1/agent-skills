# Coding Agent Marketplace

A personal catalog of custom and selected upstream skills, plugins, MCP servers, and optional working preferences for **Codex, Claude Code, and OpenCode**. Choose the tools and configuration you want. Existing matching content is preserved; conflicts are reported before replacement.

## Set up a fresh or existing installation

The six maintained writing skills include STE-inspired guidance for clear English prose, with facts and technical references preserved. Each skill works independently. The optional personal preset applies the same preference to general agent replies. This is a writing preference, not a claim of formal ASD-STE100 compliance. See the [writing evaluation](evals/results/2026-10-24-ste-writing.md).

Install your coding agents, Python 3.11+, Node 22.20.0+, npm/npx and Git first. Then:

```sh
git clone https://github.com/ruohao1/agent-skills.git
cd agent-skills
python3 scripts/setup.py
```

The selector asks what to install, which agents to target, and whether to use global or project scope. Explicit commands also work:

```sh
python3 scripts/setup.py list
python3 scripts/setup.py plan --all --agent codex --scope global
python3 scripts/setup.py install --all --agent codex --scope global
python3 scripts/setup.py install --category engineering --agent claude-code --scope global
python3 scripts/setup.py install --skill product-brief tdd --agent opencode --scope project --project /path/to/project
```

Choose any combination of `codex`, `claude-code`, and `opencode`. “All” means the 23 selected skills, not entire upstream repositories. Add `--yes` for noninteractive installation after reviewing the plan; it never overrides a conflict.

See [setup and maintenance](docs/setup.md) for preservation rules, configuration roots, native plugins, partial failures and updates.

## Personal configuration

The optional [personal preset](configs/personal/README.md) adds shared working preferences, a useful next-action suggestion after tasks, and a `personal-reviewer` agent. One instruction source serves all three hosts. It inherits your model and connections. Select it separately from skills; `--all` installs the 23 selected skills only.

```sh
python3 scripts/setup.py plan --preset personal --agent codex claude-code opencode --scope global
python3 scripts/setup.py install --preset personal --agent codex claude-code opencode --scope global
```

Use `--preset-part instructions` or `--preset-part agents` to choose one part. Existing instruction files receive a marked addition and a backup. Existing differing reviewers are preserved and reported as conflicts. Preset installation leaves main settings files unchanged.

## Chrome DevTools MCP

Configure browser inspection for any of the three agents:

```sh
python3 scripts/setup.py plan --mcp chrome-devtools --agent codex claude-code opencode --scope global
python3 scripts/setup.py install --mcp chrome-devtools --agent codex claude-code opencode --scope global
```

MCP setup is separate from `--all` skills and configuration presets. New entries
use the tested package version with an isolated, headless browser. Existing
Chrome DevTools entries keep their version and options. Setup preserves other
settings and backs up changed files. See [MCP setup](docs/setup.md#mcp-servers)
for prerequisites, paths, and activation checks.

## The selection

| Category | Skills | Maintainer |
| --- | --- | --- |
| Product Design | [product-brief](plugins/product-design/skills/product-brief/SKILL.md) | Custom, maintained here |
| Product Design | `archify` | [tt-a1i/archify](https://github.com/tt-a1i/archify) |
| Product Design | `prototype` | [mattpocock/skills](https://github.com/mattpocock/skills) |
| Engineering | [check-linear-context](plugins/linear-workflows/skills/check-linear-context/SKILL.md), [write-linear-issue](plugins/linear-workflows/skills/write-linear-issue/SKILL.md), [write-linear-comment](plugins/linear-workflows/skills/write-linear-comment/SKILL.md), [wrap-up-linear-issue](plugins/linear-workflows/skills/wrap-up-linear-issue/SKILL.md) | Custom, maintained here |
| Engineering | [write-commit](plugins/git-workflows/skills/write-commit/SKILL.md), [write-pull-request](plugins/git-workflows/skills/write-pull-request/SKILL.md) | Custom, maintained here |
| Engineering | [audit-code](plugins/code-quality/skills/audit-code/SKILL.md), [audit-scale](plugins/code-quality/skills/audit-scale/SKILL.md), [audit-security](plugins/code-quality/skills/audit-security/SKILL.md), [audit-repo](plugins/code-quality/skills/audit-repo/SKILL.md) | Custom, maintained here |
| Engineering | `codebase-design`, `domain-modeling`, `diagnosing-bugs`, `tdd` | [mattpocock/skills](https://github.com/mattpocock/skills) |
| Engineering | `ponytail`, `ponytail-review`, `ponytail-audit`, `ponytail-debt`, `ponytail-gain`, `ponytail-help` | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) |

[The catalog](catalog.json) records exact upstream commits and paths. Upstream content stays upstream. Product Design and Engineering are selection categories; ownership is independent of category. Four additional custom candidates were omitted because their [baseline evaluations](evals/results/2026-10-16-marketplace-rewrite.md) did not demonstrate a useful gap.

## Custom skills only

The shared Skills CLI route discovers the locally packaged custom skills:

```sh
npx skills@latest add ruohao1/agent-skills
```

This direct route follows `latest` and does not use the setup coordinator's conflict checks. It does not install the remote catalog. The coordinator uses the installer version pinned in `catalog.json`.

[Linear Workflows](plugins/linear-workflows/README.md) provides `check-linear-context`, `write-linear-issue`, `write-linear-comment`, and `wrap-up-linear-issue`. The context skill reads relevant project activity at session start, on resumption, and before each new substantial task. It works independently and keeps the check read-only. Research comments tell the story; the wrap-up saves a final TL;DR at the top of the description before the agent moves an issue to Done. Writing includes saving to Linear unless you request a draft; code-dependent comments stay unsaved until verified permanent code links are available. Connect Linear separately in your agent; the plugin does not bundle a connector or credentials. The [issue results](evals/results/2026-10-21-write-linear-issue.md), [comment results](evals/results/2026-10-21-write-linear-comment.md), and [wrap-up results](evals/results/2026-10-23-linear-wrap-up.md) distinguish simulated behavior from installation checks.

[Git Workflows](plugins/git-workflows/README.md) provides `write-commit` and `write-pull-request`: small local commits, verified agent attribution, concise hosted PRs, and preservation of unrelated work. Public repositories omit Linear references from commits and PR content, including implementation and review trackers; PR writing skips linking that could expose them. Private issue-specific branches use the supplied issue branch name. See the [commit results](evals/results/2026-10-21-write-commit.md) and [PR results](evals/results/2026-10-23-write-pull-request.md).

[Code Quality](plugins/code-quality/README.md) provides `audit-code` for maintainability, `audit-scale` for data growth, concurrency, and recovery, and `audit-security` for application, dependency, CI, and configuration risks. `audit-repo` runs all three and combines shared findings. Reports are saved under `docs/audits/` in the audited repository unless chat-only output is requested. New reports are ignored by Git unless tracking is requested or already established. Applying fixes and creating issues remain separate requested work. See the [coverage comparison with Ponytail](docs/audit-coverage.md) for observed benefits and remaining gaps.

## Full native plugins

Portable installation provides skill files. For full plugin features, select a complete native bundle explicitly:

```sh
python3 scripts/setup.py install --plugin product-design --route native --agent codex --scope global
python3 scripts/setup.py install --plugin ponytail --route native --agent claude-code --scope project --project /path/to/project
```

Codex supports global native installation; Claude Code supports user/global and project installation. OpenCode uses portable skills. Ponytail's native hooks need host verification/trust after installation. The coordinator reports that as `needs-setup` and never approves hooks for you. Avoid installing both native and standalone copies of the same skill.

The old `product-diagrams` and `product-wireframes` invocations are replaced by `archify` and `prototype`. `product-design-review` is no longer packaged; request a design review directly. Existing installed copies are never removed automatically.

## Develop and validate

See [adding custom or upstream tools](docs/adding-plugins.md). Keep plans with their implementation changes.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_marketplace.py
```

CI runs the deterministic checks. [Recorded evaluations](evals/results/2026-10-16-marketplace-rewrite.md) distinguish packaging, real installation, browser checks and untested agent-session behavior.
