# Close an issue

Synthetic exercise. Treat the supplied issue, discussion, and evidence as successful read results. Do not call live tools, fetch links, or change files. Return proposed operations in execution order, including any required read-backs, and a user-facing response. State any condition needed before a dependent operation.

User: "The organizer confirmed the corrected invitation. Finish APP-90 and move it to Done."

APP-90: "Correct the workshop invitation date"
URL: https://linear.app/example/issue/APP-90
State: In Progress (`state-active`). The team's only completed state is Done (`state-done`). Assignee: Kim. Label: Chore. Priority: Normal.

The current description is:

```markdown
## Context

The workshop invitation says 5 November, but the agreed date is 6 November.

## Acceptance

Correct the invitation to 6 November and obtain organizer confirmation.

## Owner note

Keep the existing venue and attendee list.
```

The complete discussion contains one comment, c900: "The invitation now says 6 November. The organizer checked it and confirmed the correction; venue and attendee list are unchanged."
Verified URL: https://linear.app/example/issue/APP-90#comment-c900

The invitation and organizer confirmation have both been inspected and match c900. There is no remaining required work or useful follow-up. No code is involved. No existing summary appears in the description or elsewhere.

The simulated API accepts `save_issue({id, description?, state?})`, `get_issue({id})`, and `save_comment({issueId, body})`. Description updates replace the full body; omitted fields remain unchanged. Save succeeds and returns the issue URL and supplied fields. A subsequent read reflects the last save. The comment API returns a comment URL.

Return JSON with `operations` and `response`. Do not critique or grade the instructions.
