# Report storage and incomplete coverage tasks

Use disposable copies of the [primary repository](primary.md). Supply each case's actual path and available skill inventory. Do not execute the application, contact external services, install tools, or inspect other evaluation outputs.

## Missing companion

Request a combined custom audit. Only `audit-code` and `audit-scale` are available; `audit-security` is unavailable. In the guided case, `audit-repo` is also available. Return the audit result for the available scope.

## Standalone defaults

Use three independent repository copies. Request `audit-code`, `audit-scale`, and `audit-security`, respectively, with no output-location override. Seed the matching user report in each copy: `docs/audits/2026-10-24-code.md`, `docs/audits/2026-10-24-scale.md`, or `docs/audits/2026-10-24-security.md`. Its contents must remain unchanged. The task date is 2026-10-24.

## Chat-only override

Request `audit-scale` on another copy, explicitly asking for chat-only output and no repository changes. That copy also contains an existing report. Return the result in the response.

These are separate tasks. Do not carry availability or audit results from one task into another. A response copy written outside the repository for the evaluation runner is not a saved audit report.

## Git tracking

Use disposable Git repositories and supplied completed audit results to isolate delivery behavior. Capture source, ignore-file contents, index entries, and other files' ignore status before each task. Keep the expected outcomes below out of evaluating contexts.

| Case | Expected outcome |
| --- | --- |
| Default combined report; `.gitignore` has an unrelated rule and no final newline | Add an effective literal report rule, preserve the old content, and leave other documents visible. |
| Standalone report already covered by an ignore pattern | Save the report without duplicating or changing ignore rules. |
| Update an already tracked report | Preserve tracked status and index entries; do not add an ignore rule. |
| User asks to keep a new report available for Git tracking | Leave the report unignored without staging it. |
| Existing explicit include exception matches the report | Honor tracking intent and preserve the exception. |
| Custom destination `notes/review [draft]!.md` | Ignore that literal file while leaving `notes/review d!.md` visible. |
| User requests tracking under an ignored report directory | Add narrow exceptions while keeping other report files ignored. |
| Report outside a Git worktree | Save without creating ignore configuration or initializing Git. |
| Chat-only in a Git worktree | Create no report and make no ignore or index changes. |

Verify effective exclusion with `git check-ignore --quiet`. Its verbose mode can print negated matches with exit status zero, so that alone does not prove exclusion. Verify preservation with file readback and `git ls-files --stage`.
