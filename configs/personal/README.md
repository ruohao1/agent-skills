# Personal preset

The shared instructions apply STE-inspired principles to English prose in general agent replies: short sentences, clear actions, and consistent terms, with technical meaning preserved. They do not enforce the full ASD-STE100 dictionary or claim formal compliance. The six maintained writing skills carry the same guidance independently, so a single-skill install does not require this preset. See the [writing evaluation](../../evals/results/2026-10-24-ste-writing.md).

Reusable working preferences and one reviewer for Codex, Claude Code, and OpenCode. The instructions ask for small complete changes, concise communication, relevant verification, preservation of unrelated work, and plans delivered with implementation PRs. After any kind of task, they ask for one useful next action toward the current goal, with a brief reason, using available context. They omit suggestions without a useful follow-up and leave suggested work for the user to choose. These encode personal preferences; they are not a measured claim that reviews or generated code improve.

`personal-reviewer` reviews a requested change and its callers, reports concrete findings with evidence, and identifies verification limits. Ask your host to use it explicitly, for example: “Use personal-reviewer to review this change.” It does not select a model, provider, account, or MCP connection.

```sh
python3 scripts/setup.py plan --preset personal --agent codex claude-code opencode --scope global
python3 scripts/setup.py install --preset personal --agent codex claude-code opencode --scope global
```

Both `instructions` and `agents` are included. Add `--preset-part instructions` or `--preset-part agents` to choose one. For a project, use `--scope project --project /path/to/project`. Review the preview before adding `--yes` for unattended use. The interactive setup also offers configuration presets. Python 3.11+ is required; applying these local files requires no package download.

## Files and scope

All three hosts use the single instruction source [AGENTS.md](AGENTS.md). Setup installs its content as `AGENTS.md` for Codex and OpenCode, or `CLAUDE.md` for Claude Code. Only the native reviewer definitions live in host-specific source directories.

| Host | Global instructions | Global reviewer | Project files |
| --- | --- | --- | --- |
| Codex | `~/.codex/AGENTS.md` | `~/.codex/agents/personal-reviewer.toml` | `AGENTS.md`, `.codex/agents/personal-reviewer.toml` |
| Claude Code | `~/.claude/CLAUDE.md` | `~/.claude/agents/personal-reviewer.md` | `CLAUDE.md`, `.claude/agents/personal-reviewer.md` |
| OpenCode | `~/.config/opencode/AGENTS.md` | `~/.config/opencode/agents/personal-reviewer.md` | `AGENTS.md`, `.opencode/agents/personal-reviewer.md` |

Global paths honor `HOME`, `CODEX_HOME`, `CLAUDE_CONFIG_DIR`, and `XDG_CONFIG_HOME`. Project paths are relative to the chosen project. Codex uses an existing nonempty `AGENTS.override.md` instead of the corresponding `AGENTS.md`. The two project `AGENTS.md` entries share one file. An identical visible global or ancestor reviewer is reused.

Instructions append a marked block, preserving existing content and creating a backup. Differing reviewer definitions and instruction precedence conflicts require manual reconciliation. Main settings files are read for conflicts and remain unchanged. See [setup preservation, retry, and removal](../../docs/setup.md#configuration-presets).

An installed block from an older preset is also preserved as a conflict when its content differs from the current source. Review and reconcile that block before reinstalling; `--yes` does not replace it.

## Reviewer permissions

Claude Code allows only `Read`, `Grep`, and `Glob`. OpenCode denies other tools and allows read, glob, grep, and list; reading `.env` and `.env.*` still asks for approval, with `.env.example` allowed. These roles use supplied changes and readable files; they report missing evidence if reviewing requires an unavailable tool.

Codex custom agents inherit the parent session's permissions. Its reviewer instructions ask it not to edit, but that is not an enforced read-only sandbox. Run the parent session read-only when enforcement is required. Existing host policies and higher-precedence settings still apply. Reload sessions after installing.

## Host formats

Native formats follow [Codex custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Codex instruction files](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Claude Code subagents](https://code.claude.com/docs/en/sub-agents), [OpenCode agents](https://opencode.ai/docs/agents/), [OpenCode rules](https://opencode.ai/docs/rules/), and [OpenCode configuration](https://opencode.ai/docs/config/).

Linux checks used Codex 0.163.0, Claude Code 2.1.301, and OpenCode 1.18.34. [Verification evidence](../../evals/results/2026-10-17-personal-preset.md) distinguishes installation, native discovery, and untested model behavior. Older host versions may not support these formats.

[Shared-source and next-action checks](../../evals/results/2026-10-21-shared-preset.md) cover the current layout, installation preservation, and synthetic task responses. They do not establish native-host behavior with the updated instructions.
