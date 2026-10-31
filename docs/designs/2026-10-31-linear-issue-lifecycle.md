# Preserve issue outcomes during planning

## Accepted scope

Update `write-linear-issue` and `wrap-up-linear-issue`. A planning-only session
limits present actions. A capability issue tracks its intended outcome across
planning, a decision, and any authorized delivery. Planning may lead to a revised
idea, separate delivery slices, deferral or cancellation. It does not itself
authorize implementation or establish completion.

Keep the issue as the concise source of its problem, outcome, constraints and
completion checks. A specification is work within that issue; linked documents
hold detail. Use a parent with independently useful delivery issues when needed.
Preserve explicitly scoped research or design deliverables, narrow edits and
existing authorization boundaries. Do not rewrite existing live issues.

## Implementation and verification

- Freeze synthetic planning, research, completion and narrow-edit cases.
- Run five fresh baseline contexts on the explicit-scope cases. If those already
  pass, preserve that result and test the design-workflow interaction separately.
  Compare that frozen case in five fresh contexts per arm, then recheck the
  original boundaries with the revision. Read every complete response and keep
  raw evidence outside the public repo.
- Add only guidance supported by the observed gap and the accepted scope.
- Update both Linear Workflows manifests, its README and Unreleased notes.
- Run the 73-test suite, marketplace and skill validators, and relevant portable
  installation checks in disposable homes. Record actual results and limits.

This independent work starts from main at
`56aca9d4fdf1a53d729e9314d2f6d22ccdc899b7`. Keep this plan with its implementation.
Delivery includes a reviewed local upgrade, a PR and a verified merge after the
required checks. Preserve existing local skill additions during installation.
Keep publication limited to this feature. Do not migrate live issues.
