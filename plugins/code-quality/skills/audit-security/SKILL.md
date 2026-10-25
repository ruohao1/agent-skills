---
name: audit-security
description: Use when the user asks to audit security risks in application code, dependencies, CI workflows, deployment configuration, or secret handling.
---

# Audit security

Audit how an actor could cross a trust boundary, access protected data, misuse privileges, or disrupt service. Return a report; fixes and issue creation are separate requested work.

## Establish the boundaries

Inspect the requested area, or the whole repository by default. Read repository instructions, source, callers, tests, dependency records, workflows, and deployment configuration. Establish who can supply inputs or trigger operations, what access they have, and what the system must protect. Distinguish repository configuration from verified live settings.

Research available facts before asking questions. Ask when a missing answer would change a conclusion or priority. Unknown host guarantees or deployment conditions remain explicit uncertainties.

## Trace the risks

Follow untrusted inputs and actions through authentication, authorization, interpreters, file and network operations, and privileged automation. Inspect secret storage, use, logging, and exposure. Trace relevant protections through callers and adapters before judging a local pattern.

For each finding, establish the actor, required access, reachable operation, failed protection, and consequence. A verified code path can support a finding without an exploit reproduction. If material evidence is missing, keep the claim as an unverified lead. Preserve effective controls and distinguish possible impact from observed compromise. Redact credentials and sensitive data in all evidence.

For dependencies, confirm the resolved or deployed version, current authoritative advisory, affected conditions, and actual use, including build and CI use. An affected dependency can be a finding while application exploitability remains unverified; state both conclusions separately. A matching version with unknown advisory conditions remains a lead. Scanner severity alone does not determine application risk.

Recommend the smallest fix that closes the failed boundary. Group observations resolved by the same fix; keep independent causes separate. Put related regression checks with their finding.

## Verify within scope

Use relevant existing tests and bounded reproductions in disposable environments when they resolve uncertainty. Active tests against deployed systems and sustained load tests need separately agreed targets and limits. State which checks ran, which results were supplied, and which conclusions come from inspection. Never claim exploitation, live exposure, or a clean deployment from source inspection alone.

## Report

Start with a short priority summary and the relevant actor/access assumptions. Number every supported finding, ordered by impact and likelihood under those conditions, without a fixed cap. Use a compact heading with the priority, problem, and verified locations, then four bullets of one or two short sentences each:

- **Evidence and impact:** actor/access, affected operation, failed protection, and consequence.
- **Fix and check:** smallest useful change and the check that would verify it.
- **Confidence:** what the evidence establishes and any material uncertainty, including dependency applicability versus exploitability.
- **Effort:** relative estimate and its main reason.

Use plain English and preserve technical references exactly. Report relevant findings even when runtime scaling is another consequence. When combining audits, merge a shared root cause and retain each consequence. State shared coverage and execution limits once at the end, with unverified leads. A clean or inconclusive result is valid; do not invent findings to fill the report.

## Save the report

Save to `docs/audits/YYYY-MM-DD-security.md` in the audited repository by default. Honor an explicit destination or chat-only request. When contributing to a combined audit, return findings to its coordinator without saving a separate report. Include the inspected scope and source revision when available, noting uncommitted changes. Use repository-relative source paths and line numbers inside the saved file. For a new run, add a numeric suffix if the path exists; replace a report only when an update is requested.

For a report inside a Git worktree, keep new untracked reports ignored by default. Inspect tracked state and effective ignore rules first. Reuse an effective rule; otherwise append an anchored, literal entry for that report alone to the worktree-root `.gitignore`, escaping Git pattern characters and preserving existing content and line endings. Treat already tracked reports and explicit include exceptions as tracking intent. If the user requests Git tracking, use narrow exceptions where needed and preserve other files' ignore status. Never untrack, stage, or commit files as part of the audit. Chat-only output and reports outside a Git worktree need no ignore edits.

Verify the actual report path with `git check-ignore --quiet`. Use `-v` to identify rules, not to prove exclusion: it also reports negated matches. State any tracking exception or ignore failure without claiming the report is ignored.

After saving, the final reply consists of the report link, a one-sentence priority summary, and material execution limits. The findings belong in the saved file. If saving fails, return the report with the reason and do not claim it was saved.
