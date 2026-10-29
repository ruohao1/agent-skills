# Manage worktrees

Status: implemented and validated. See the [evaluation results](../../evals/results/2026-10-28-manage-worktrees.md).

## Behavior

Keep independent repository tasks isolated. Apply automatically before code, documentation or configuration edits, when resuming such work, and when finishing or cleaning task worktrees. Read-only tasks create no worktree.

The original checkout stays on the verified default branch, normally main or master. New task branches start from the latest fetched default branch at `repo/.worktree/<branch>`. A task that explicitly depends on another branch uses that base. Preserve pre-existing unfinished work in the original checkout and report the exception instead of migrating it automatically.

Reuse a verified matching, inactive worktree, including a host-created worktree elsewhere. Reuse does not transfer cleanup ownership. Existing isolation alone does not identify the correct task. Use host/session evidence for activity; Git status and locks do not prove inactivity.

Use local Git exclusions, preserving existing rules. Keep the original checkout unchanged by task edits. Use native tools only when they can satisfy the selected location. If isolation is blocked, continue useful read-only work and report the limitation; do not fall back to editing the original checkout.

Follow repository setup instructions and run relevant baseline checks. Keep worktrees while implementation or review is pending. After verified merge, automatically remove only a workflow-created, inactive worktree with no unique data to lose. Check ignored files, local commits and current PR state. Preserve ambiguous, active, foreign or dirty worktrees. Do not infer merge or publication permission from cleanup.

## Packaging and evidence

Add one self-contained `manage-worktrees` skill to Git Workflows. Preserve the existing writing skills and shared presets. Update the paired plugin manifests, curated catalog, setup documentation and Unreleased changelog. No installer changes or runtime dependencies are planned.

Compare the existing guidance with the candidate using five fresh contexts per arm. Inspect all decisions. Exercise actual Git operations in disposable repositories, including ignored-file preservation and main checkout preservation. Validate packaging, run the repository tests, and check selected installation and repeat installation for all three supported agents in disposable homes.

The skill coordinates agent decisions. It does not provide an atomic cross-host lock or an automatic background cleaner. Missing activity evidence keeps the affected workspace intact. Native host activation is a separate check from package installation.
