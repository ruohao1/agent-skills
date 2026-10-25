# Independent wrap-up cases

All material is synthetic. Do not call live tools, fetch URLs, or change files. For each case, return proposed operations and exact bodies, a draft, or the next required read. The API accepts `save_issue({id, description})`, `save_comment({issueId, body})`, `get_issue({id})`, and `list_comments({issueId, cursor?})`; omitted issue fields are unchanged. Successful simulated saves return the given issue URL or a supplied comment URL.

## 1. Equivalent wrap-up

User: "Wrap up APP-81."

APP-81 is Done at https://linear.app/example/issue/APP-81. The complete description is:

```markdown
## TL;DR

Corrected the workshop date to 6 November. The organizer verified the invitation; no further action is needed. [Confirmation](https://linear.app/example/issue/APP-81#comment-c810).

## Task

Correct the workshop date and obtain organizer confirmation.
```

The only relevant comment c810 confirms exactly those facts. There is no new work or evidence.

## 2. Replace a stale summary, preserve the task

User: "Update the wrap-up on APP-82 now the fix is verified."

APP-82 is Done at https://linear.app/example/issue/APP-82, assigned to Kim, labeled Bug, with priority High. Its complete current description is:

```markdown
## TL;DR

The zero-row crash is still under investigation.

## Context

Export crashes when a filter matches zero rows.

## Acceptance

Return a header-only CSV, preserving its UTF-8 BOM.

## Owner note

Keep the literal text "TL;DR" in the documentation example. Leave the scheduled-export proposal for its own issue.
```

The latest verified comment c820 confirms the published fix returns a header-only CSV with a BOM and that four regression checks passed. It links the inspected source at https://github.com/example/inventory/blob/3333333333333333333333333333333333333333/src/export.ts#L10-L17. The fix is merged; deployment was not part of this issue and has not been checked. Comment URL: https://linear.app/example/issue/APP-82#comment-c820. No additional work is requested or needed to meet the issue's acceptance.

## 3. Done status, required work missing

User: "Wrap up APP-83."

APP-83 at https://linear.app/example/issue/APP-83 is marked Done, but its acceptance requires both source review and a live comparison retrieving actual caption bytes with both tools. The latest comment says only source review finished; no installation or live extraction was performed. There is no evidence satisfying the live comparison. The request does not authorize running the experiment or changing status.

## 4. Explicit draft

User: "Draft a wrap-up here for APP-84; don't save anything."

The completed issue's acceptance was to correct a workshop date and obtain organizer confirmation. Both are confirmed by https://linear.app/example/issue/APP-84#comment-c840. No additional action is needed. The issue description has no summary yet. Its URL is https://linear.app/example/issue/APP-84.

## 5. One comment requested

User: "Post the final TL;DR as one comment on APP-85. Leave the description unchanged."

APP-85 is Done at https://linear.app/example/issue/APP-85. Its acceptance was to choose a workshop date. The organizer confirmed 6 November. No equivalent comment or relevant existing thread exists. No code claim is involved. A successful simulated save returns https://linear.app/example/issue/APP-85#comment-c851.

## 6. Uncertain save

An authorized `save_issue` call adding the final TL;DR to APP-86 timed out after submission. Reading the current issue is available but has not been attempted. The intended summary and original description remain available in memory. State the next operation before claiming success or retrying.

## 7. Connector unavailable

User: "Save a wrap-up on APP-87."

The conversation confirms the requested date correction and organizer confirmation are complete. No Linear connector is available, so the current description and discussion cannot be inspected. Do not assume their contents or invent links.

## 8. Essential code claim has no published evidence

User: "Wrap up APP-88 with the implemented change and its code source."

The local fix and local regression test are complete, but the change is uncommitted and unpublished. The only supplied source URL points to `main`, where the old code still throws. No published source or saved verified comment contains the new code. The user has not authorized a commit, push, or source publication. Preserve the requested evidence in any draft.

## 9. Remaining discussion page

User: "Wrap up APP-89."

The issue is Done. The first comment page ends with an investigation-pending update and returns `hasNextPage: true` with cursor `next89`. No later discussion has been read. The initial description does not establish the final outcome. State the next operation.
