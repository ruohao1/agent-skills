# Maintainability audit evaluation

Use the [primary task](fixtures/audit-code/primary.md) in five fresh contexts with the existing `ponytail-audit` instructions and five with the candidate. This compares the selected upstream audit with the proposed maintainability workflow; it is not a comparison against an unaided model. Supply only the task, source snapshots, and the appropriate instructions. Do not supply these criteria or prior answers. No production code, tickets, or external services may change.

Read every report. Score substance, not exact headings or a required number of findings:

- Identify the duplicated fee calculation inside orchestration and explain the maintenance/testability cost. Group its repeated sites into one root-cause finding rather than issuing a separate finding for each copy or counting test friction as another independent defect.
- Identify forwarding layers without behavior, the misleading units documentation, and the unused legacy helper when supported by the complete inventory. Naming improvements can count when their benefit is explained.
- Preserve the legitimate empty-input guard and manifest-registered exporter; do not infer dead code from the absence of direct Python calls. Similar small string operations in distinct concepts do not alone justify a shared abstraction.
- Ground findings in verified source locations and present behavior-preserving directions. A working implementation can still merit a refactor. Avoid fabricated runtime failures or traffic-growth claims.
- Rank by maintenance impact, include useful relative effort estimates, and provide all supported findings grouped by root cause. Do not reward vague risk statements, arbitrary size thresholds, numerical quality scores, or speculative line-savings estimates.
- Return a report only. Distinguish supplied test evidence from checks performed by the evaluating agent. State the inspected scope and unavailable evidence.

Run the [focused tasks](fixtures/audit-code/focused.md) once per arm. Verify that a clean orchestrator can receive no findings, unavailable external consumers prevent a definitive dead-code or safe-removal claim, and a report of independently established findings is not truncated by a fixed cap.

Before distribution, run the existing unit tests and marketplace validator, validate skill frontmatter, and check Skills CLI discovery and portable installation in disposable roots. Record baseline strengths and limitations. Do not infer authenticated host activation or real-project audit quality from these supplied-context exercises.

## File and folder organization revision

Compare the unchanged 0.1.0 skill with the revision in five fresh contexts per arm using the [file-layout tasks](fixtures/audit-code/file-layout.md). Read every answer. The first task supports a cohesive split and move into existing feature directories, with clearer file names. Check that the proposed migration accounts for internal imports, the public export, the job registration, the relative asset and its copy step, and test imports/discovery. Preserve the public subpath and repository test convention; no runtime bug or dead-code claim is supported.

The second task should remain unchanged unless evidence establishes a problem beyond file length or the separate test directory. Assess useful organization and complete migration reasoning, not a required destination filename. These examples test reports only and authorize no file moves.
