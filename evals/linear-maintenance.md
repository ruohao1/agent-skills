# Linear maintenance and status checks

This publication check uses the eight synthetic
[cases](fixtures/linear-maintenance/cases.json). It supplements the original
[context discovery evaluation](check-linear-context.md). It does not replace
that evaluation or measure a general invocation rate.

Freeze both inputs before the run. The baseline contains the four Linear
Workflows 0.5.0 skills from commit
`23c5513657a57146861b20b581bc6b098dad6936`. The candidate replaces
`check-linear-context` with the recovered 0.7.0 guidance and adds
`maintain-linear-project`. The other three skills remain identical.

Use one fresh context per arm. Present the inventory descriptions first. For
each independent case, record selected skills before reading their bodies.
Ask for ordered actions and a brief user report. Both arms receive identical
facts and requests, without scoring criteria or the other arm's responses.
Read all responses manually. Preserve raw responses outside the repository.

Check that the proposed actions:

- Start authorized implementation and research in the team's actual active
  state before substantive work, preserving unrelated fields.
- Leave review-only requests read-only and reuse fresh same-task context.
- Suggest incidental cleanup without expanding an unblocked task.
- Keep unmerged implementation open when acceptance requires merge.
- Verify complete history and equivalent access before shortening a description.
- Reconcile a concurrent requirement with both the snapshot and new description.
- Finish accepted research against its own scope, save its TL;DR before status,
  and avoid writes when an unchanged repeat needs none.

These are simulated action choices. They do not perform tracker writes,
exercise concurrency guarantees, or establish authenticated host activation.
Do not infer improvement when both arms already choose the required behavior.
Do not revise the frozen skill text during this publication check.

Run the repository unit suite, marketplace and skill validation. Check selected
and repeated Skills CLI installation in disposable homes for Codex, Claude Code
and OpenCode. Compare installed bytes and preserve unrelated file contents and
timestamps. Record the tested versions, source hashes and remaining limits.
