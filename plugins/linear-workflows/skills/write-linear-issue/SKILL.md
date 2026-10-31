---
name: write-linear-issue
description: Use when the user asks to write, create, capture, or improve a Linear issue for themselves or a coding agent, including issue drafts and focused edits.
---

# Write Linear issue

Use ASD-STE100-inspired principles for English prose written for people. Write short, complete sentences with one main idea. Give clear instructions and put necessary conditions before their actions. Prefer active voice, simple verbs, and consistent terms. Keep related ideas connected. Preserve facts, evidence, uncertainty, and required technical detail. Reproduce code, commands, identifiers, paths, URLs, and source quotations exactly. Apply the principles for clarity; do not enforce the full STE dictionary or claim formal compliance.

Write a concise, grounded issue that a person can scan and a coding agent can act on. A request to write an issue includes saving it to Linear. Honor explicit draft-only requests. For a narrow correction, change only the requested content; keep the existing structure and metadata.

## Establish context

Research available facts before asking questions: inspect relevant repository instructions, code/tests, supplied sources, and related Linear issues. Resolve the destination from the request and session; ask if team or project is ambiguous. Use the connected Linear tools and their actual schemas. If access is unavailable, deliver an explicitly unsaved draft and name the missing access.

Search for overlapping work before creating an issue. Read plausible matches and their relevant discussion. Existing issues are leads, not writing examples or authoritative technical evidence: verify claims against sources, and distinguish confirmed decisions from suggestions. Keep useful source links and verified code pointers; never invent paths, findings, or certainty.

Ask only questions whose answers materially change scope or acceptance criteria. Researchable facts are your work. For a ready-to-implement request, resolve those decisions before saving. An explicit “capture this idea” request can remain exploratory: record the hypothesis and open questions without inventing implementation commitments.

## Choose the issue

When the intended work matches, improve the existing issue, preserving valid requirements and discussion. For distinct work, create a separate issue and link the relevant existing work. Use a dependency only when it is established; thematic similarity supports a related link. Preserve existing discussion rather than deleting it or posting an unsolicited comment.

When the request concerns a capability, keep that outcome as the issue's scope.
Specifying or planning it is a task within the issue. A planning-only session or
design workflow limits current actions; its stop condition does not define issue
completion. Use an outcome title and track planning as a checkpoint. Keep the
problem, constraints and completion checks in the issue; link detailed designs.

Planning can lead to delivery, a revised approach, a split, deferral or cancellation.
Keep unsettled decisions open; a prospective Feature does not commit to implementation.
If delivery needs separate issues, retain a parent for the capability and link its
independently useful slices. Preserve an explicitly independent research or design
deliverable as its own issue. Nearby specification issues do not establish that scope.

## Choose the type

Choose one primary type from the issue's intended outcome, across its work phases:

- **Bug:** Restore behavior that violates an established expectation.
- **Feature:** Add or intentionally change a capability, including improvements.
- **Research:** Resolve an unknown through findings or a decision.
- **Chore:** Maintain code, documentation, or infrastructure while preserving intended behavior.

Investigation within a fix remains Bug; an investigation-only deliverable is Research. Review is a workflow status, not a purpose. Chore is not a fallback for unclear scope.

## Write the body

Use a concrete title describing the outcome. Start Context with short factual bullets: current behavior, why it matters, and essential sources. Treat the table as content prompts for each type, not mandatory separate headings:

| Type | Context | Change / scope | Acceptance criteria |
| --- | --- | --- | --- |
| Bug | Expected versus actual behavior; reproduction or evidence. A known root cause is not required. | Behavior to fix, affected cases, constraints. | Corrected behavior and relevant regression checks. |
| Feature | User need and intended outcome. | Capabilities, boundaries, settled decisions. | Observable behavior and consequential edge cases. |
| Research | Question, existing evidence, decision it informs. | Investigation boundaries and constraints. | Findings, supporting evidence, recommendation, remaining unknowns. Documented inconclusive evidence is a valid result; implementation is not required. |
| Chore | Maintenance need and why it matters. | Bounded work and behavior to preserve. | Maintenance outcome and relevant checks. |

State each requirement once. When scope and acceptance would repeat the same outcomes, combine them into one checklist. Keep each bullet focused on one point. Link verified designs or plans for implementation detail; keep the outcome, consequential constraints, and observable completion checks in the issue. If a reference is unavailable, retain known requirements in the issue and mark the reference unverified.

Include useful verified code pointers with a revision when known. Keep settled decisions; implementation suggestions remain options, and a plausible code edit is not a settled decision. Leave other implementation choices open. For explicit exploratory capture, use open questions or a useful next learning step instead of implementation acceptance.

Honor an applicable required team template while retaining this substance. Keep sections proportional, without repeated summaries or empty boilerplate. Check the rewrite against the original: keep its context and every valid requirement, including constraints, failure cases, and delivery details.

## Label and save

The default taxonomy is one workspace-wide, single-select **Type** group with Bug, Feature, Research, and Chore. Read the destination's actual taxonomy: use existing semantic equivalents when it differs, and report missing or ambiguous mappings. Reassess inaccurate labels when rewriting an issue. Respect single-select groups, never assign a group itself, and preserve unrelated valid labels. Do not invent labels or copy them blindly from nearby issues. Writing an issue does not authorize changing label definitions or creating native templates.

For a new issue with no assignment instruction, set `assignee` to the human invoking the skill. Use `me` when the connector supports it and it identifies that user; otherwise resolve their verified Linear user ID. If that identity remains ambiguous, ask before saving. An explicit other assignee or unassigned (`null`) overrides the default. On updates, preserve the current assignee unless reassignment is requested.

Save the authorized creation or update without an extra approval round. Patch only intended fields; preserve unrelated assignee, priority, status, cycle, dates, project, and relations. Account for APIs that replace full label sets. Check the save result; if it is ambiguous, read/search before retrying to avoid duplicates. Return the confirmed issue link and a brief summary, or state what remains unsaved.
