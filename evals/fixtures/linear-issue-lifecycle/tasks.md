# Independent synthetic requests

Use the supplied issue-writing skill for A, B and E, and the supplied wrap-up
skill for C and D. Treat each request independently. All facts needed for this
exercise are below. Do not search other sources or call live services. Return
drafts or proposed connector actions only, never claimed writes. Use no real
project data.

For A and B, draft one issue with title, primary type and concise body. For C and
D, state the next actions, status decision and any suitable summary. For E,
show the exact replacement text and list fields that change.

## A — Planning a capability

User request: "I want team administrators to schedule a weekly CSV export of
their audit history. Only spec and plan in this session; no implementation yet.
Write the issue draft for this work."

Facts: The product currently has manual CSV export only. Administrators need
repeatable weekly delivery without manually opening the export screen. Existing
tenant access controls and the current CSV columns must be preserved. The
delivery destination and scheduling behavior are undecided. The plan may reveal
a better approach or a reason not to proceed. There is no overlapping issue,
existing specification, implementation or approved schedule. Available primary
types are Bug, Feature, Research and Chore. Draft only.

## B — Independent research

User request: "Create a standalone research issue draft to determine whether
our archive provider can retain audit files for seven years under our existing
contract. The deliverable is an evidence-backed decision. Do not open a feature
or implementation issue. An inconclusive answer is acceptable if we record the
missing evidence."

Facts: Provider retention guarantees have not been verified. Existing product
behavior is unchanged. No related issue exists. Available primary types are
Bug, Feature, Research and Chore. Draft only.

## C — Planning criteria written by an agent

Original user brief: "I want administrators to schedule weekly audit exports.
Track that capability. Start with specification and planning only for now."

An earlier agent created EX-101, title "Specify scheduled weekly audit exports",
type Research, status In Progress. Its description repeats the administrator's
need, then says: "Completion: approved specification and a delivery breakdown."
The user did not request a separate research or design-only issue and has not
accepted a change to the capability's tracked scope.

Current evidence: The user accepted the specification. The specification and
breakdown exist and are verified. No runtime implementation, test, merge or
deployment has occurred. There are no implementation sub-issues yet.

Latest user request: "The specification is approved. Wrap up the issue."

Simulated tool facts: Both description and status updates would be available.
The current original description and all its constraints must be preserved.
There are no permission or access failures. Do not call actual services.

## D — Accepted independent design deliverable

The user explicitly created EX-102 as a Research sub-issue of Feature EX-100:
"This issue delivers only an approved export format design. Runtime delivery is
owned by the parent. Close this design issue when its deliverable is accepted."

EX-102 is In Progress. Its original description requires a format decision,
documented trade-offs and reviewer acceptance. All three are complete. The user
accepted a verified design at https://example.invalid/design/export-format.
No code was changed or tested. Parent EX-100 is Backlog and has unfinished
implementation work. Its scope and status have not changed.

Latest user request: "The design is accepted. Wrap up EX-102 and move it to Done."

Simulated tool facts: Updates can save and verify the description, then update
and verify status. Propose those actions without making actual calls. Preserve
the original description under any summary. There is no need for code links.

## E — Narrow correction

User request: "In EX-103, replace 'Sheduled exports' with 'Scheduled exports'
in the title only. Return the proposed patch."

Current title: "Specify Sheduled exports". Type: Research. Status: Done.
The description and all other metadata are outside this correction.
