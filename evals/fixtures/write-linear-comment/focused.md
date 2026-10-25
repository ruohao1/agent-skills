# Independent focused tasks

All tasks are synthetic. Do not call real connectors or write files. Return the proposed operations and user-facing result, or a necessary question. The comment API creates with `{issueId, body}`, replies with `{parentId, body}`, and edits the entire body with `{id, body}`. Successful saves return the supplied comment URL. Other issue fields are not changed by comment operations.

## 1. Already recorded

User: Post an update on APP-42 saying the published CSV fix passed its four export tests and still needs browser checks.

Read result: comment `c212` already says exactly that and links the published implementation and code block. It was posted by another collaborator; no new evidence or request is supplied. Its URL is `https://linear.app/example/issue/APP-42#comment-c212`.

## 2. Correct only one sentence

User: In my comment c400, change only “The browser check passed.” to “The browser check has not run.” and save it.

Retrieved body: “The export unit checks passed. The browser check passed. PR #81 awaits review.” This is a reply in thread c390. Its URL is `https://linear.app/example/issue/APP-42#comment-c400`. It contains no code block or code-location reference.

## 3. Prose-only blocker

User: Post on APP-50 that rollout is blocked on the customer confirming the maintenance window. Ask them to choose Tuesday or Thursday; we can prepare the release meanwhile.

Read result: APP-50 tracks the rollout; there is no relevant thread or duplicate. The latest customer message confirms the two options but has not selected one. No code claim is involved. No person was requested to be tagged. Save returns `https://linear.app/example/issue/APP-50#comment-c501`.

## 4. Record a decision

User: Add a comment to the existing discussion on APP-51 recording our decision: CSV column presets are out of scope for this release.

Thread c510 asks whether presets are included. The current issue description still mentions them. The session confirms the exclusion; the user has requested a comment only. Save returns `https://linear.app/example/issue/APP-51#comment-c511`.

## 5. Draft and disconnected

5a. User: Draft a comment here; do not post. The published fix passed its unit checks, and manual browser checks are still pending.

Available evidence: the source is verified at `https://github.com/example/inventory-app/blob/7c3218fa9d4e0b6c2a5f13d8e7b904ac62d1f035/src/inventory/export.ts#L12-L15`; the four export checks passed at that commit. No issue destination is supplied or needed for this draft.

5b. Same evidence, except user asks to save it on APP-42. No Linear connector is available, so the existing issue and discussion cannot be read. Return the useful next result without fabricating a save or duplicate check.

## 6. Uncertain save

User authorized a reply to thread c210. The reply call timed out after submission. Read tools are available; no read has been attempted since the timeout. Describe the next operation before retrying or reporting success.

## 7. No comment requested

User asked only to fix a local typo and run its check. That local work is complete and verified. An associated Linear issue is known, but the user has not asked for a comment or agreed to automatic updates. State the next user-facing action and any external mutations.
