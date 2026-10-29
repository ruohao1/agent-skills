---
name: manage-worktrees
description: Use when starting or resuming repository edits, including code, documentation or configuration, or when finishing a task and managing its Git worktrees.
---

# Manage worktrees

Use ASD-STE100-inspired principles for English prose written for people. Write short, complete sentences with one main idea. Give clear instructions and put necessary conditions before their actions. Prefer active voice, simple verbs, and consistent terms. Keep related ideas connected. Preserve facts, evidence, uncertainty, and required technical detail. Reproduce code, commands, identifiers, paths, URLs, and source quotations exactly. Apply the principles for clarity; do not enforce the full STE dictionary or claim formal compliance.

Apply task isolation automatically, without another request. Keep the original checkout on the verified default branch, normally `main` or `master`; put task edits in separate worktrees. Read-only work creates none. Explicit user or repository workspace requirements take precedence.

## Select the task workspace

Read the task context, repository instructions, Git worktree registrations and available host/session state. Verify the original checkout, current branch and existing changes. Do not infer the original root from the current linked checkout or the parent of its Git directory. Report ambiguous repository layouts.

Reuse a worktree only when it belongs to this task and current coordination establishes that no other agent is editing it. This includes host-created worktrees outside the preferred directory. Use an available host claim/resume mechanism. Existing isolation is not proof of task identity. Git status, absent locks and directory names do not prove inactivity or ownership. If activity is uncertain, coordinate before overlapping edits or removal.

Preserve unfinished feature work already in the original checkout and report that exception. Use a separate worktree for new tasks; migration requires a separate request. Preserve other tasks, staged changes and established branches.

## Create when needed

1. Verify the remote and default branch, then fetch it. Start new independent work from that fetched ref, not the current feature branch or stale local default branch. Use an established task base for resumed work; use another feature branch only for work that explicitly depends on it. Report unavailable or ambiguous base evidence before creating from a guess.
2. Choose a distinct branch under repository naming rules. Public or unknown-visibility repositories use descriptive names without private issue identifiers. For private issue work, use the verified issue-supplied branch name when required. Check existing branches and registrations before creating one.
3. Use `<original-repo>/.worktree/<branch>`; for example, `repo/.worktree/feat/login`. Validate the branch and resolved destination, including occupied paths and symlink escapes. Use native creation only when it can honor this location; otherwise use Git.
4. Verify that the directory is untracked and effectively ignored. Preserve an existing rule. Otherwise append `/.worktree/` once to the shared local exclude file resolved by `git rev-parse --git-path info/exclude`, then verify the actual path with `git check-ignore`. Report conflicting tracked paths or include rules instead of overriding them. No tracked ignore edit or commit is needed.
5. Create a task branch with the verified base explicitly supplied, for example:
   `git -C "$original_repo" worktree add --no-track -b "$task_branch" "$task_path" "$task_base"`.
   Verify path, branch and starting commit before edits. After an uncertain result, inspect registrations and paths before retrying.

If creation or access is blocked, report it and continue useful read-only work. Do not fall back to edits in the original or another task's checkout.

Follow repository setup instructions and run relevant baseline checks in the selected workspace. Report existing failures accurately. Keep commands and edits in that workspace. Record the task, path, branch, base and creator in the session handoff so later work can resume without guessing.

## Finish and clean up

Keep the worktree while work or review is pending. Completion does not authorize committing, publishing, merging or deleting branches.

After verified merge, automatically remove only a worktree this workflow created, with current evidence that no other session uses it. Reusing a host-created workspace does not transfer cleanup ownership. A directory name or an old merged PR is insufficient.

Verify that the current tip is included in the intended base. For squash/rebase merges, use authoritative merge metadata that accounts for the exact task tip; preserve later or uncertain local commits.

Before removal, inspect tracked changes, ordinary untracked files and ignored files. Use `git status --porcelain --untracked-files=all` and `git ls-files --others --ignored --exclude-standard`. Ordinary clean status does not protect ignored `.env` files or local notes. Keep the worktree if unique data or its preservation is uncertain. Only confirmed disposable generated files may be discarded.

Recheck identity and activity immediately before removal. Run non-force `git worktree remove` from outside the target. Leave locked, refused or uncertain targets intact; do not globally prune registrations. Verify that the target directory and registration are gone and the original checkout is unchanged. Report the retained or removed path and any unresolved preservation or coordination need.
