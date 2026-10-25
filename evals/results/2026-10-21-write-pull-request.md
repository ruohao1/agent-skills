# Write pull request observations

## Agreed behavior

Writing a PR creates or updates it. A draft PR is hosted; an explicit text-only draft remains unsaved. Research the actual diff, related work, repository template, and matching PR, then explain the problem, resulting behavior, and actual validation concisely. Use bullets when helpful. Infer source and target from verified context and ask when ambiguous. Push intended existing commits without implicitly committing unrelated working changes.

Public repositories must expose no Linear identifiers, URLs, or connection commentary in branch names or PR content, and must skip automatic Linear linking. Unknown visibility uses the same rule. Private issue-specific work uses Linear's supplied branch name. Preserve established published branches and PRs; a safe unpublished branch can be renamed. Verify attachment before claiming it. Relevant failures or incomplete work make a PR draft; disclose missing optional checks.

Linear's [GitHub integration documentation](https://linear.app/docs/github#branch-name) describes issue-ID branch association. Its [July 2, 2026 changelog](https://linear.app/changelog/2026-07-02-initiative-properties) describes linkback comments for manually associated PRs. [Linkback settings](https://linear.app/docs/github#linkbacks), [private teams](https://linear.app/docs/private-teams), and the [attachment API](https://linear.app/developers/attachments) do not establish a generally private-only alternative. These primary sources informed the publication policy: skip automatic linking for public repositories and do not treat an internal attachment as a privacy guarantee.

## Baseline method and results

Five fresh-context agents received the identical synthetic [primary tasks](../fixtures/write-pull-request/primary.md), with no candidate skill, interview, rubric, or previous answers. The first also answered the [focused cases](../fixtures/write-pull-request/focused.md). No model override was requested. All outputs were manually read. Operations, GitHub records, and successful receipts were simulated; no Git mutation or connector call occurred.

| Behavior | Baseline |
| --- | --- |
| Public PR: publish a neutral branch and omit Linear identifiers/URLs | 5/5 |
| Skip public Linear attachment/linkback | 5/5 |
| Private PR: use the supplied issue branch name and create a hosted draft | 5/5 |
| Preserve unrelated uncommitted work | 5/5 |
| Report checks, incomplete behavior, and missing optional checks accurately | 5/5 |
| Read back the PR and confirm private issue attachment only from supplied evidence | 5/5 |

For example, control 1 proposed `HEAD:refs/heads/alex/respect-retry-after` for the public source and explained that a Linear attachment could produce a public linkback. Control 2 renamed the local branch to `respect-retry-after` before a normal push. Control 4 used an empty explicit lease to create the new remote branch; this is a different Git implementation, not an observed overwrite. All five produced concise PR bodies with concrete behavior and validation.

The focused baseline kept a text-only draft unsaved, treated unknown visibility as public, preserved a narrow existing-PR edit and its published branch, asked only for an unresolved base, reconciled an ambiguous create timeout before retrying, and paused before publishing a tracker-bearing commit message without rewrite authorization. With authentication unavailable it made no false publication claim. That fixture supplied no actual local diff text, so its draft contained placeholders rather than invented behavior.

These controls already met the evaluated behavior. They do not establish that every future task or host will do so. No improvement from custom PR guidance has been demonstrated by this sample. No candidate was evaluated in this initial comparison.

The [2026-10-23 implementation and checks](2026-10-23-write-pull-request.md) preserve these baseline observations and record the publication-policy regression cases separately.
