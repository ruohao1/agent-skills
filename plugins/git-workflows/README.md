# Git Workflows

Each skill includes STE-inspired writing guidance for clear English prose. It preserves technical detail without enforcing the full ASD-STE100 dictionary or claiming formal compliance. No personal preset is required. See the [writing evaluation](../../evals/results/2026-10-24-ste-writing.md).

Version **0.4.0** supplies three independent skills:

- [manage-worktrees](skills/manage-worktrees/SKILL.md) automatically prepares or resumes an isolated workspace before repository edits. New tasks use `.worktree/<branch>` from the fetched default branch. The original checkout stays on its default branch; pre-existing unfinished work is preserved. Verified host-created task workspaces can be reused. Cleanup after merge requires confirmed ownership, inactivity and preservation of ignored local data.
- [write-commit](skills/write-commit/SKILL.md) creates small commits from the intended work, preserves unrelated staged and unstaged changes, honors checks, and credits the contributing coding agent. Message-only requests return text. Repository message conventions take priority; Conventional Commits is the fallback.
- [write-pull-request](skills/write-pull-request/SKILL.md) writes and saves a concise PR grounded in the actual diff, repository template, and checks. It publishes intended existing commits when necessary. A draft PR is hosted; an explicit text-only draft stays unsaved. Narrow edits preserve unrelated content and metadata.

Public repositories use descriptive branch names and omit Linear identifiers, URLs, and connection commentary from commit messages and PR content, including implementation and independent-review tracking. Unknown destination visibility follows the same rule. PR writing skips automatic Linear linking and attachments that can expose linkback comments. Private issue-specific work uses the branch name supplied by Linear when creating or safely renaming an unpublished branch. Published branches and history are preserved; existing privacy conflicts are reported before further publication. A missing attribution identity is resolved before committing; the commit skill does not replace the human Git author.

From this checkout:

```sh
python3 scripts/setup.py install --skill manage-worktrees write-commit write-pull-request --agent codex --scope global
```

Or use the shared route:

```sh
npx skills@latest add ruohao1/agent-skills --skill manage-worktrees write-commit write-pull-request --agent codex claude-code opencode
```

Select any skill independently by listing its name. Worktree management applies before repository edits and during task resumption or cleanup. Commit and PR skills trigger for their respective requests. No AGENTS.md addition is required. Use `--plugin git-workflows --route native` with the setup coordinator for the complete native plugin on Codex or Claude Code. OpenCode uses portable skills. Choose one route to avoid duplicate copies. The package contains instructions; Git, hosting access, and any Linear connection are supplied by your agent environment. It does not install credentials, alter agent configuration, or activate itself in existing sessions.

The [commit evaluation](../../evals/write-commit.md) and [results](../../evals/results/2026-10-21-write-commit.md), plus the [PR evaluation](../../evals/write-pull-request.md) and [results](../../evals/results/2026-10-23-write-pull-request.md), separate simulated workflow decisions from actual execution and installation checks.

The [worktree evaluation](../../evals/manage-worktrees.md) and [results](../../evals/results/2026-10-28-manage-worktrees.md) distinguish policy selection, disposable Git operations and installation checks. Worktree management provides no cross-host activity lock or background cleanup service. Uncertain activity, ownership or local data keeps a worktree intact.
