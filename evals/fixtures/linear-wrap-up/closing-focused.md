# Independent completion cases

All material is synthetic. Do not call live tools, fetch URLs, or change files. For each case, return proposed operations and exact bodies, a draft, or the next required read. Include conditions before dependent operations. The API accepts `save_issue({id, description?, state?})`, `get_issue({id})`, and `list_comments({issueId, cursor?})`; omitted fields are unchanged. A successful save returns the issue URL and supplied fields. A later read reflects that save. Do not invent missing API results.

## 1. Equivalent summary before completion

User: "Everything is confirmed. Move APP-91 to Done."

APP-91 is In Progress, and the team's completed state is `state-done`. All acceptance is verified. Its current description is:

```markdown
## TL;DR

Corrected the workshop date to 6 November. The organizer verified the invitation; no further action is needed. [Confirmation](https://linear.app/example/issue/APP-91#comment-c910).

## Task

Correct the workshop date and obtain organizer confirmation.
```

The complete discussion confirms exactly those facts and contains no new evidence. The supplied link is verified. URL: https://linear.app/example/issue/APP-91.

## 2. Summary update failed

The user asked to close completed APP-92. The description update containing its final summary returned a definite permission-denied error. The issue is still In Progress, its description contains only the original task, and the status-change endpoint is available. The intended summary and evidence remain in memory. State the next action.

## 3. Summary update uncertain

The user asked to close completed APP-93. A description update containing its final summary timed out after submission. Status is not yet updated. `get_issue` is available and has not been tried. State the next operation and the condition for any status transition.

## 4. Acceptance incomplete

User: "Please finish APP-94 and move it to Done."

The issue requires both source research and a successful live caption comparison. Source research is complete. The authorized live experiment cannot run because test-account access is missing; no successful comparison exists. The current state is In Progress, and there is no final summary. No additional tool can resolve the missing access. State the action and response.

## 5. Explicitly limited local task

User: "Run the local checks for APP-95 and tell me the result. Leave Linear alone."

The checks have finished successfully and the local task is complete. The issue is In Progress. No other work or status change was requested. State any proposed Linear operations and the response.

## 6. Team uses a different completed state

User: "The date correction is confirmed. Resolve APP-96."

APP-96 is In Progress. The only completed state returned by its team is `state-resolved`, named Resolved. The current description is `Correct the invitation date to 6 November and obtain organizer confirmation.` The complete discussion has a verified comment at https://linear.app/example/issue/APP-96#comment-c960 confirming the correction and organizer approval. Acceptance is met. No useful follow-up exists. URL: https://linear.app/example/issue/APP-96.
