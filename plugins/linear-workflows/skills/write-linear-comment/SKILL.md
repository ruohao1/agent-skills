---
name: write-linear-comment
description: Use when the user asks to write, post, reply to, draft, or edit a comment on a Linear issue, including progress, blockers, decisions, and handoffs.
---

# Write Linear comment

Use ASD-STE100-inspired principles for English prose written for people. Write short, complete sentences with one main idea. Give clear instructions and put necessary conditions before their actions. Prefer active voice, simple verbs, and consistent terms. Keep related ideas connected. Preserve facts, evidence, uncertainty, and required technical detail. Reproduce code, commands, identifiers, paths, URLs, and source quotations exactly. Apply the principles for clarity; do not enforce the full STE dictionary or claim formal compliance.

Write concise comments for a person and a coding agent. A request to write a comment includes saving it; honor explicit draft-only requests. A coding task alone does not authorize posting, and this skill does not start automatic updates.

## Read and choose the contribution

Read the issue and relevant discussion before writing, following pagination far enough to establish the thread and whether the update already exists. Research available repository evidence and decisions first; ask only for missing information that changes the contribution or its destination. Treat earlier comments as leads, distinguishing verified facts and settled decisions from guesses.

If substantially the same information is already recorded and there is nothing new to add, return that comment's link without posting or editing. Reply in the relevant thread; use a new top-level comment for a separate update. Edit an existing comment only when explicitly requested: read its current body and preserve everything outside the requested change, including its thread placement.

## Write what changed

Lead with the useful new result, blocker, question, or decision. Add supporting evidence and a necessary next step. Match the structure to the purpose; omit repeated issue summaries and empty headings. Keep prose concise; use bullets when they make parallel points, steps, or checks easier to scan.

Separate work completed, checks actually run and their results, and unresolved work or decisions. Tie verification to the tested revision or working copy. Implementation, passing tests, merge, and deployment are different claims. Keep tentative conclusions tentative; record a decision only when it is settled.

For research reporting that permits multiple updates, use short comments to tell how the understanding developed. Each contribution is a short paragraph centered on a consequential discovery: what was learned, why it matters, and the decisive source links. Group closely related findings and continue their thread; add an update for a distinct useful takeaway, without a fixed count. Omit routine activity and repeated summaries. Present retrospective notes as a recap in the recorded order, without inventing intermediate experiments or pretending comments were posted during the work. Single-comment requests and narrow corrections keep their requested scope.

## Cite code with permanent links

Every repository code reference needs an immutable file permalink pinned to the exact commit and supporting line range. Place it beside any quoted code block. Verify from repository/remote evidence that the published revision, path, and lines contain the cited code; a branch URL or an older published implementation does not establish that. Copy verified permalinks exactly into the final body.

On GitHub, use `https://github.com/<owner>/<repo>/blob/<full-commit>/<path>#L<first>-L<last>`. For another host, use its equivalent immutable permalink. Keep excerpts small and faithful to the linked revision.

**If a code-dependent comment lacks a verified published permalink, keep it as an explicitly unsaved draft and identify the missing reference.** This includes uncommitted or unpushed changes. Preserve the requested code evidence in the draft; dropping it is not a way to bypass this rule. Preparing a comment does not authorize committing or pushing code. A prose-only blocker, question, or decision with no code claim does not need a code link.

## Save within the request

Use the connected Linear tools' actual schemas to create, reply, or edit. A comment request leaves issue descriptions and metadata unchanged. When the request also includes changing requirements, handle that separately with `write-linear-issue` if available; comment writing itself has no dependency on that skill.

Save an authorized, ready comment without an extra approval round. If access is unavailable, return an unsaved draft and identify any context you could not check. Verify the save result. After an ambiguous timeout, read the relevant discussion before retrying; if the outcome remains uncertain, report it rather than posting again blindly. Return the confirmed comment link, or a clearly labeled issue link if a comment URL is unavailable, with a brief result.
