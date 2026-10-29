---
name: check-linear-context
description: Use when starting or resuming work in a project that uses Linear, and before each new substantial task in that project, even within an existing session.
---

# Check Linear context

Before choosing a plan or making changes, check current Linear context without
waiting for a separate request. A handoff, saved plan, or list of affected files
does not establish that project decisions are still current.

During the same task, reuse checked context. Refresh after a pause, a scope
change, or evidence that related work changed. Honor local-only requests. Skip
trivial edits that need no project context.

## Find the project

Resolve the project from the request, supplied issue, repository instructions,
and verified repository links. If needed, search by repository or product name
and verify the match. A similar name alone is insufficient. If the mapping
remains ambiguous and affects the task, ask one focused question while
continuing independent local work. If the project does not use Linear, skip.

## Read what affects the task

Use the connected tools and their actual schemas. Start with a small set of
recent project updates and updated issues. Search related active and completed
work without a recency cutoff, then read the relevant descriptions, final
summaries, and discussion. Follow direct dependencies even when they are old.
Read enough comment pages to establish the current decision; a summary can
predate a later correction. Widen the search only to resolve a relevant gap.

Shared agent notes can help when supported, but they do not replace recent
activity. If that optional tool fails, use ordinary issue and comment reads.
If Linear access fails, state what remains unchecked and continue work that
does not depend on it. Failed or partial reads do not establish that nothing
has changed.

## Apply the findings

Check for completed or overlapping work, blockers, and changed decisions before
implementing. Distinguish proposals from settled decisions. Verify technical
claims against the repository; approval, implementation, merge, and deployment
are different states. Surface a material conflict with the request before
proceeding with the affected work. Do not silently replace the user's scope.

Briefly report only findings that change the task or its next step, with source
links and material uncertainty. Use short, factual sentences. Keep private
Linear details out of public artifacts. Once relevant context is established,
continue the task rather than producing a project-wide report.

Context discovery is read-only. It does not authorize comments, ownership
changes, saved notes or unrelated issue updates.

## Start the selected issue

When requested work on a verified issue begins, move that issue to the team's
actual active-work state before substantive implementation, research, a planning
deliverable or review fixes. This routine status update is part of starting the
authorized task; do not wait until completion or ask for separate approval.
Inspection, triage, issue-copy edits and review-only requests do not start work.

Use the team's existing workflow. In Progress and In Review can both have a
started state type; select the actual active-work state, not the first match.
An already active issue needs no write. Requested review fixes resume active
work; reviewing an implementation leaves its status alone. Do not implicitly
reopen completed or cancelled issues. If the issue or active state is ambiguous,
ask one focused question and continue independent work.

Read the current status before writing and resolve conflicting new state or
decisions. Update only this issue's status; preserve ownership, parent and sibling
states, and other fields. Verify the result. After an ambiguous timeout, reread
before retrying. If synchronization is unavailable, report the gap and continue
unblocked work without claiming that the status changed.

## Notice maintenance opportunities

If the checked context reveals stale status claims, superseded work, unclear
remaining work or descriptions crowded by progress history, suggest one
focused cleanup with a concrete example. Continue the original task when it
is unblocked. Do not repeat an unchanged proposal or widen this check into a
full backlog review. `maintain-linear-project`, when available, handles the
separate cleanup within the user's authorization; context checking works without it.
