# Linear research comments and wrap-up evaluation

Run [completed research](fixtures/linear-wrap-up/completed.md) and [research comments](fixtures/linear-wrap-up/story.md) as independent tasks in five fresh contexts with the existing issue/comment skills, then five with the revised comment skill and new wrap-up skill. The issue-writing skill remains unchanged. Give agents only the skills and task fixtures, without these criteria, prior results, or unrelated issue history. Read every output manually.

Also compare five fresh control contexts with five guided contexts on [closing an issue](fixtures/linear-wrap-up/closing.md). This request never mentions a summary. Controls use the existing issue/comment skills; guided contexts add the wrap-up skill. Keep any shared preferences identical between arms. Earlier prototype runs included a shared-instruction trigger; the results distinguish those from the separate skill-only discovery check.

These are synthetic connector decisions with simulated save results. They do not authorize live Linear writes or prove authenticated API behavior.

## Completed-issue criteria

- Put one short TL;DR first in the description, preserving the original task definition underneath.
- Summarize the actual conclusion, source-only verification limit, and supported next comparison; leave the detailed research in the existing comments.
- Link to decisive existing comments using the supplied verified URLs. Do not create duplicate completion comments, new issues, or fabricated artifacts.
- Keep status and all other metadata unchanged. Source research is complete even though a live experiment explicitly outside this issue's scope is unperformed.

## Research-comment criteria

- Use concise comments to convey the consequential discoveries and their implications in recorded order, continuing the relevant thread. Do not impose a fixed number of comments or post routine activity.
- Identify retrospective notes as a recap; do not invent intermediate experiments or imply the comments were posted during the work.
- Keep decisive source links and claim-specific uncertainty. Omit unrelated package/CLI trivia and repeated global completion statements.
- Leave issue description and metadata unchanged; this task authorizes comments only.

## Completion-trigger criteria

- On a request to finish and close an issue, save a short final TL;DR first without asking for a separate wrap-up request.
- Confirm the summary is saved before the separate status transition; use the actual team's completed state and verify that result.
- Preserve the original description and all unrelated metadata. Reuse an accurate existing summary, omit unnecessary follow-ups, and avoid duplicate comments.
- Keep status unchanged if required work is incomplete or the summary cannot be saved or verified. An unrelated local task does not authorize closing an issue.

## Focused criteria

Use [focused cases](fixtures/linear-wrap-up/focused.md) once per arm. Check equivalent wrap-ups are reused; only stale summary content is replaced; original user notes and metadata survive; required missing work prevents a false final wrap-up even when status is Done; draft, unavailable access, and comment-only requests retain their scope; ambiguous saves are read back before retrying; code evidence is not invented or published to manufacture a summary.

Use [completion cases](fixtures/linear-wrap-up/closing-focused.md) against the final guidance to check an existing summary, failed and uncertain saves, incomplete acceptance, explicit local-only scope, and a different completed-state name. Check skill discovery separately from execution: show only the installed descriptions and determine which skill applies to a closure request, then run the selected skill without a shared-instruction trigger.

Run the existing comment [published/unpublished cases](fixtures/write-linear-comment/primary.md) and [focused cases](fixtures/write-linear-comment/focused.md) against the revised comment skill to check its existing boundaries.

## Shipping checks

Validate both new/changed skills, both plugin manifests, and catalog membership. Run the full unit suite and marketplace validator. Check pinned Skills CLI discovery and disposable skill installs, recording limits separately. Do not change the ordinary issue-writing skill, personal preset, or installer runtime.
