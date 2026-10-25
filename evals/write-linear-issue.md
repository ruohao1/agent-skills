# Write Linear issue evaluation

Use the synthetic [primary task](fixtures/write-linear-issue/primary.md) in five fresh contexts without the candidate, then five with it. Give each agent the task and supplied sources, not these criteria or prior results. Keep the inputs identical. Read every output; score decisions and usable content, not heading names or exact wording. Record observed differences, including baseline strengths.

These are simulated connector decisions. No real Linear issues, labels, comments, or templates may be changed. A proposed mutation and simulated receipt do not establish authenticated write behavior.

## Primary criteria

- Updates the existing issue for the same work; preserves the separate scheduled-export issue and links it only as related, not a fabricated blocker.
- Includes a concise explanation of current behavior and its consequence, bounded change, and observable acceptance for all matching rows across pages, filters, zero matches, and the existing BOM requirement.
- Uses the supplied source evidence; rejects the unsupported server-cache diagnosis and 10,000-row limit. Includes useful verified pointers without turning a proposed code edit into a mandated implementation.
- Preserves the discussion's valid constraint, unrelated metadata and labels; replaces the wrong Feature label with Bug using the supplied taxonomy. Does not assign a group as a label or invent taxonomy.
- Saves the authorized update without another approval interview; returns its link and a brief summary. Does not claim an unconfirmed save.
- Keeps the body proportional: assess redundancy and unsupported detail, not an arbitrary word count alone.

## Counterexamples

Run the [focused tasks](fixtures/write-linear-issue/focused.md) once per arm, separately from the primary answer. Evaluate:

1. A one-sentence correction only changes the requested text; it does not reformat the whole issue, relabel it, or restart discovery.
2. Explicit idea capture stays exploratory and saves without demanding implementation acceptance criteria or inventing validated demand.
3. A genuinely distinct follow-up gets its own linked issue, preserving the original issue.
4. Available facts are researched before asking a question. A missing decision that changes acceptance blocks a ready-for-implementation save; ask only that decision.
5. Ambiguous destination gets one destination question, without guessing a team or asking redundant product questions.
6. A draft-only request causes no save. An unavailable connector returns a draft with an explicit unsaved status, not a claimed issue link.
7. An ambiguous save timeout is reconciled by reading/searching before retrying, avoiding duplicate issues or an unsupported success claim.

## Shipping checks

Validate the skill frontmatter and the paired plugin/catalog entries. Run the repository's unit suite and marketplace validator. Check local Skills CLI discovery and a disposable portable installation if available. Record which real host/connector paths remain untested. Keep the skill self-contained; add no installer/runtime logic for this guidance.

## Type-specific skeleton revision

Use [four independent issue requests](fixtures/write-linear-issue/types.md) in five fresh contexts with the previous skill, then five with the candidate. This comparison isolates the added taxonomy and skeleton guidance; it does not remeasure the original skill against no skill. Preserve identical task inputs and review every answer manually.

- Classify by final deliverable: Bug, Feature, Research, Chore respectively. Investigation within a fix remains Bug; investigation without a production fix is Research. An intentional change to existing behavior is Feature. Maintenance preserves intended behavior.
- Bug records actual versus expected behavior and the supplied reproduction without inventing a cause. Its completion criteria require corrected behavior and consequential regression checks.
- Feature records the need, changed behavior, access constraints, exclusions, and observable acceptance.
- Research states the question, evidence, bounded investigation, and findings/recommendation deliverable. An inconclusive result can close the issue if its evidence limits and remaining unknowns are recorded; no fix or proven root cause is mandatory.
- Chore explains the maintenance need, bounded work, behavior to preserve, and relevant checks.
- Keep verified pointers, select exactly one available Type child, and preserve the original workflow's concise writing, save behavior, and metadata boundaries. Do not reward exact headings or repeated boilerplate.

Run [focused cases](fixtures/write-linear-issue/types-focused.md) once per arm. Check narrow updates preserve labels/status/format; required team headings win; idea capture stays exploratory; a different destination taxonomy maps by meaning without creating labels; research completion can be evidence-limited. No live label migration or native template creation is authorized by these scenarios.

If the existing skill already meets these criteria, do not claim a behavioral improvement. The four skeletons are explicitly requested defaults; checks of this revision verify their application and preservation of the existing workflow. See the [2026-10-23 observations](results/2026-10-23-write-linear-issue-types.md).

## Default assignment revision

Use the [new-issue assignment task](fixtures/write-linear-issue/assignment.md) with the previous skill and the revision. The request deliberately omits an assignee: a new issue should explicitly assign the verified invoking user through `assignee`, using `me` or that user's ID. Do not score headings or wording. Retain the concise Bug scope and authorized save.

Check the [assignment boundaries](fixtures/write-linear-issue/assignment-focused.md): explicit other assignee wins; explicit unassigned uses null; edits preserve assigned or unassigned state; an unresolved human identity requires one targeted question rather than assigning an integration account; explicit reassignment patches only assignee. These simulations authorize no live writes.

See the [assignment observations](results/2026-10-23-write-linear-issue-assignment.md) for the five-control/five-revision comparison and limits.

## Concise body revision

Use the assignment fixture's five 0.4.1 outputs as the unchanged-skill baseline, then run that identical fixture in five fresh contexts with the revision. Check short factual Context bullets, requirements stated once, and complete observable checks without a redundant scope paragraph. Word counts describe the sample; they are not a correctness threshold. Preserve default caller assignment and saving.

Run the [focused brevity cases](fixtures/write-linear-issue/concise-focused.md): retain essential requirements when plans are unavailable; link a verified design without copying its implementation detail; keep a narrow correction narrow despite the new formatting default. Review substance manually, including privacy, failure states, exclusions, and the distinction between tentative proposals and decisions.
