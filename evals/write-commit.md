# Write commit evaluation

Run the [primary tasks](fixtures/write-commit/primary.md) in five fresh contexts without the candidate and five with it. Keep requests and evidence identical; do not provide this rubric, prior answers, or the interview. Manually read every result. The first context in each arm also answers the [focused cases](fixtures/write-commit/focused.md). Compare one additional fresh run with the installed `caveman-commit` skill to check whether its message-only workflow satisfies this request.

The candidate defines workflow defaults, not universal Git rules. Report retained baseline strengths and actual differences without claiming broader superiority. Operations and receipts in these fixtures are simulated; separately exercise actual index preservation in a disposable local repository if the candidate is retained.

## Primary criteria

- Create the requested commits rather than returning only proposed messages. Split independent behavior changes into reviewable units with their necessary tests. Leave unrelated content and its staged/unstaged state intact, including mixed files.
- Honor required checks/hooks, use the repository's message convention or Conventional Commits as fallback, and include the verified contributing agent's co-author trailer once per commit.
- Public repositories use descriptive branches and messages without Linear identifiers/URLs or automatic linking. Private issue-specific work uses the supplied Linear branch name when creating/renaming an unpublished branch.
- Respect an explicitly named staged scope. Draft/message-only requests do not mutate Git. Do not push or publish merely because local commits were requested.
- Verify committed contents/messages and remaining index/worktree, and report only observed commit receipts and checks.

## Focused criteria

Preserve message-only requests, missing-identity questions, hooks that fail or alter files, genuinely ambiguous scope, narrow message amendments, and existing published branches. Unknown repository visibility uses the public-reference rule. Do not repair unrelated failures, change author configuration, or bypass hooks to complete a commit.
