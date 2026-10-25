# Issue types and skeleton observations

## Agreed design

The proposed workspace-wide Type taxonomy has four purposes, selected by the final deliverable:

| Type | Purpose | Context | Scope | Completion |
| --- | --- | --- | --- | --- |
| Bug | Restore established behavior. | Expected versus actual behavior, reproduction or evidence. | Behavior to fix, affected cases, constraints. | Corrected behavior and relevant regression checks. |
| Feature | Add or intentionally change a capability, including improvements. | User need and intended outcome. | Capabilities, boundaries, settled decisions. | Observable behavior and consequential edge cases. |
| Research | Resolve an unknown with findings or a decision. | Question, available evidence, decision it informs. | Investigation boundaries and constraints. | Findings, evidence, recommendation, remaining unknowns. |
| Chore | Maintain code, documentation, or infrastructure while preserving intended behavior. | Maintenance need and why it matters. | Bounded maintenance and behavior to preserve. | Maintenance outcome and relevant checks. |

Investigation within a fix remains Bug; investigation without implementing a fix is Research. Chore is not a fallback for unclear scope. Review belongs to workflow status, not this taxonomy. Each issue has one primary type. Existing unrelated label dimensions remain separate.

The skill supplies skeletons that honor required team templates. Keep verified pointers and settled decisions, allow unknown bug causes and inconclusive research, and retain exploratory idea capture. This defines the evaluated behavior; it does not establish that any live workspace has adopted these labels.

## Method

Ran the [four issue requests](../fixtures/write-linear-issue/types.md) in five fresh agents with the existing `write-linear-issue` skill from Linear Workflows 0.2.1, then five with the 0.3.0 revision. These are controls for a revision, not no-skill controls. One additional fresh agent per arm ran the [focused cases](../fixtures/write-linear-issue/types-focused.md). Agents received only the supplied skill and fixture, without the rubric, earlier conversation, or other outputs. No model override was used.

All outputs were read manually. Scoring concerned labels, evidence, scope, completion, and mutation boundaries, not particular heading names. The fixtures supply synthetic repository and connector read results, including an already-configured four-type workspace. Creates and updates are proposed operations followed by simulated receipts. No live connector operations occurred.

## Observations

| Check | Existing skill (0.2.1) | Explicit defaults (0.3.0) |
| --- | --- | --- |
| Exactly one appropriate Type per issue: Bug, Feature, Research, Chore | 5/5 | 5/5 |
| Bug includes verified reproduction, expected outcome, unknown cause, and preservation constraints | 5/5 | 5/5 |
| Feature distinguishes an intentional behavior change from a defect, retaining access rules and exclusions | 5/5 | 5/5 |
| Research delivers findings and a next-step recommendation; inconclusive evidence can close it | 5/5 | 5/5 |
| Chore includes the maintenance reason, affected test paths, preservation requirements, and checks | 5/5 | 5/5 |
| Verified pointers, concise scoped bodies, simulated saves, and no unrelated metadata changes | 5/5 | 5/5 |

Representative existing-skill output:

- Control 1, Bug: “The cause is unknown.” It still specifies that the verified reproduction must export all 120 matching rows.
- Control 2, Feature: “Warehouse selection currently clears search as originally specified”; completion requires retained search text and preserved access restrictions.
- Control 5, Research: “If evidence cannot distinguish the explanations, document that result and the additional evidence needed; this is a valid completed outcome.”
- Control 4, Chore: “Existing CSV tests pass with equivalent assertions and no loss of coverage.”

The focused control also met the criteria:

- Patched only the requested sentence, preserving the legacy Improvement label, Review status, and surrounding format.
- Used the required Summary and Checks headings for maintenance while retaining its context, scope, and checks.
- Saved the idea with open questions and no implementation or validation commitment. It chose Research; this case tests exploratory treatment, not a universal type for captured ideas.
- Mapped an investigation to the destination's existing Spike label without creating the proposed labels or changing its taxonomy.
- Changed only the research completion criteria to allow documented inconclusive evidence, without requiring a diagnosis, fix, or release.

The revised skill preserved all five focused behaviors. Its captured idea used Feature rather than the control's Research, while still leaving implementation and validation undecided. The fixture does not settle the idea's eventual deliverable; no classification improvement is claimed for that case. The revised skill also honored the required Summary/Checks headings and used the existing Spike label without requesting taxonomy changes.

## Decision and limits

The existing skill already met the type-specific content requirements in these samples. Successful examples did not persist the taxonomy or skeletons in the shipped instructions; the revision makes those defaults explicit.

Version 0.3.0 records the definitions and four compact skeletons in the existing skill. It preserves the required-team-template override, narrow edits, exploratory capture, existing-taxonomy mappings, and issue-saving scope. The comparative results establish no measured quality gain; the change packages explicit defaults and the new runs check for regressions. No new skill or runtime code was added.

These checks do not prove reliable source discovery or authenticated saving. The supplied workspace is a preconfigured fixture. No issue relabeling or native template creation was attempted.

## Repository checks

- `python3 -m unittest discover -s tests -v`: all 65 tests passed.
- Skill creator's `quick_validate.py`: passed.
- Direct `validate_plugin` check: Linear manifests and skill packages pass; paired manifests both declare 0.3.0.
- `python3 scripts/validate_marketplace.py`: failed with `Setup catalog must exactly match packaged custom skills`. The checked source contained `plugins/linear-workflows/skills/wrap-up-linear-issue/` without a corresponding `catalog.json` entry. This revision did not add or register it.
- Independently parsed all five original control outputs. Manually reviewed all revised outputs, which use JSON, YAML, or ordinary fields; each contains four scoped creates with the expected Type plus Inventory and correct destination.
- Source bytes match the revised candidate used by the evaluating agents.
- Installer and host activation probes were not repeated: discovery paths and installer code are unchanged.
