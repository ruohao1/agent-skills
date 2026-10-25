# Write pull request evaluation

Run the [primary tasks](fixtures/write-pull-request/primary.md) in five fresh contexts without the candidate and five with it. Give both arms identical evidence and requests; do not show the rubric, prior answers, or interview. Manually read every answer. The first context in each arm also answers the [focused cases](fixtures/write-pull-request/focused.md).

The [original control results](results/2026-10-21-write-pull-request.md) already passed those cases. Also run the synthetic [public tracking and cleanup cases](fixtures/write-pull-request/public-tracking.md) in five fresh controls and five guided contexts. Do not expose real issue identifiers in published fixtures. Run the original primary and focused cases against the candidate as regressions, recording baseline strengths without claiming improvement where controls already pass.

The candidate defines a publication policy. A control that exposes a Linear reference fails that policy; this does not establish a universal rule against issue references. Record baseline strengths as well as differences. All records and receipts are synthetic; proposed operations do not establish authenticated execution.

## Primary criteria

- Public repository: publish from a descriptive branch without Linear identifiers; keep identifiers, URLs, and connection commentary out of public PR content. Do not attach the PR through Linear or invoke another linking workaround.
- Private repository: use the supplied issue branch name for the unpublished source branch and create a hosted draft PR when requested. Do not reinterpret a draft PR as unsaved text.
- Resolve source, target, and repository from the evidence. Push only the intended existing commits. Leave unrelated uncommitted edits intact.
- Explain the problem, resulting behavior, and actual verification concisely. Keep optional checks, merge, and deployment unclaimed. Failing relevant checks keep the PR in draft.
- Verify creation before returning the PR URL. Claim Linear association only when observed.

For the public tracking regression, omit both implementation and review identifiers from all outbound PR fields and skip linkback-producing attachments. For cleanup, remove only the authorized paragraph; preserve the retained text, closed/merged state, title, base, and source without touching Git history.

## Focused criteria

Preserve text-only drafts, narrow existing-PR edits, published branches, material branch ambiguity, unknown-visibility privacy, missing access, and reconciliation after an uncertain save. Surface Linear identifiers already embedded in public-bound history instead of silently rewriting or publishing them.

## Packaging

Keep the skill self-contained in Git Workflows, register matching native manifests/catalogs and the curated bundle, run the existing tests and validators, and check selected portable installation in disposable homes/projects. Record host activation and live connector limitations separately.
