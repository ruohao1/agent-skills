---
name: maintain-linear-project
description: Use when reviewing or cleaning up a Linear project or backlog, or when project context reveals stale status claims, superseded issues, unclear remaining work, or descriptions crowded by progress history.
---

# Maintain Linear project

Use ASD-STE100-inspired principles for English prose written for people. Write short, complete sentences with one main idea. Prefer active voice, simple verbs, and consistent terms. Preserve facts, evidence, uncertainty, and required technical detail. Reproduce code, commands, identifiers, paths, URLs, and quotations exactly. Apply the principles for clarity; do not claim formal compliance.

## Choose the scope

When normal project work reveals drift, suggest one focused cleanup with a
concrete example, then continue the original task if it is unblocked. A context
lookup stays read-only. Starting requested work on a verified issue can use the
context skill's routine active-status transition; that does not authorize
cleanup of other issues. Use existing cleanup authorization when it covers this
project; skill availability alone does not authorize unrelated changes.

A cleanup request permits verified factual corrections, current summaries and
preserving accumulated history in a linked document. Honor inspect-only,
draft-only and narrow requests. Group unresolved decisions about cancellation,
acceptance, status, scope, priority or ownership into one proposal. Reuse settled
decisions and existing authorization without asking again.

## Establish current state

Resolve the project from verified links. Read the selected issues, relevant
discussion across pages, dependencies, related completed work and supporting
artifacts. Use actual connector schemas. For a full-project review, paginate
the issue inventory; state the limit of a partial review.

Compare recorded status with acceptance evidence. Metadata edits and inactivity
do not establish progress or completion. A completed planning parent can have
unfinished implementation children. A superseded experiment needs a disposition,
not an invented claim that its original work finished.

For implementation, completion normally requires accepted work merged into the
intended branch. Tested but unmerged work remains open, normally In Review.
Explicit issue-specific completion rules take precedence; an accepted research
or prototype deliverable can finish without a production merge. Verify merge
claims against repository or PR evidence. Cleanup does not authorize a merge,
push or deployment.

## Make the issue useful now

Keep purpose, scope, acceptance criteria and user notes in the active description.
Put a short `## Current state` section at the top of an open issue: verified
progress, remaining work or blocker, and the next action, with decisive links.
Correct outdated references without rewriting historical statements as new facts.
Keep unresolved requirements visible. Preserve unrelated fields and relations.

Current state is not the final TL;DR. Before an authorized completed-state
transition, save and verify a concise final TL;DR with outcome and verification
limits. Use `wrap-up-linear-issue` when available; keep the reconciled task and
history link beneath the summary. Verify the status change separately.

## Preserve accumulated history

When progress history crowds the description, save a dated, verbatim snapshot
of the full current body in a document linked to the same issue and project.
Keep equivalent access; do not publish private records elsewhere. Reuse an
existing complete snapshot when it matches.

Read back and compare the complete saved text and evidence links before
shortening the issue. Handle pagination or size limits without truncation.
If preservation or access cannot be verified, keep the original body intact.
After an ambiguous save, find and inspect its result before retrying.

Immediately before replacement, reread the issue. Incorporate concurrent edits
and refresh the saved snapshot when needed. Use a revision guard if available;
fresh reads alone do not make replacement atomic. If changes keep racing, leave
that issue intact and report the conflict. Verify the saved description retains
requirements, user notes, current state and its working history link.

Future consequential progress belongs in concise comment threads under existing
posting authorization. Preserve existing comments; do not replay the old log
as a stream of new comments.

## Report the result

Briefly link confirmed changes, group pending decisions, and state material
verification gaps. Reuse accurate summaries and history. An unchanged repeat
needs no writes or repeated approval request; mention an existing pending
decision only when useful. This skill runs during agent work or an explicitly
scheduled task; it does not create a background schedule.
