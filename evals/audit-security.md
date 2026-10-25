# Security audit evaluation

Use the identical [primary task](fixtures/audit-security/primary.md) in five fresh contexts with installed Ponytail 5.3.2 and five with the candidate. Give only the task/source and selected instructions, not this rubric, design, or previous reports. Read all outputs; assess substantive evidence separately from formatting.

- Identify missing object ownership checks, SQL injection, bearer-token logging, untrusted pull-request code with privileged CI credentials, and the affected archivekit dependency.
- Establish actor/access, code path, operation, impact, and actual evidence for each. A reproduction is not required for code-established findings; do not claim an exploit or tests were executed.
- Confirm affected version and advisory conditions for archivekit while leaving application exploitability unresolved. Reject the stale safeweb scanner finding. Do not infer live gateway exposure or missing session verification.
- Preserve the safe profile query. Keep each distinct root cause separate; regression tests belong with the relevant fix.
- Rank contextual impact and likelihood; show confidence and estimated effort separately with reasons. Avoid copying generic scanner severity as application risk.

Run the [focused tasks](fixtures/audit-security/focused.md) once per arm. Check the protected route, unknown advisory conditions, build dependencies, redacted evidence, bounded verification, and deduplication of a shared scaling/security cause. Distinguish baseline strengths from candidate improvements. Synthetic advisories do not establish actual registry/scanner integration.
