# Linear Workflows publication checks

Date: 2026-10-29. Package: Linear Workflows 0.7.0.

## Scope and method

The pre-existing context and maintenance guidance was frozen unchanged for this
publication check. The [original context results](2026-10-25-check-linear-context.md)
remain historical evidence for 0.5.0. They do not establish the later status or
maintenance behavior.

One fresh baseline context received the four 0.5.0 skills from commit
`23c5513657a57146861b20b581bc6b098dad6936`. One fresh candidate context received
the same three writing skills, the current context skill and the maintenance
skill. Both received the same eight synthetic cases and recorded selection from
descriptions before reading selected bodies. Neither received the scoring
criteria or the other response. All 16 case responses were read manually.

The [protocol](../linear-maintenance.md) and
[fixtures](../fixtures/linear-maintenance/cases.json) are reusable. These are
proposed actions against supplied facts, not executed connector operations.
There was one sample per arm, not repeated independent samples per case. This
check therefore shows specific decisions, not a reliable success-rate estimate.

Frozen skill SHA-256 values:

- `check-linear-context`:
  `b2e057839c1004c87dfe3b81935ae23c8d616d9e454f58861130199df990ed4e`
- `maintain-linear-project`:
  `c150836ab68bbd7f90fb7716a18f0f232930688e1c6bb9ebd955f01e587a541c`

## Observed decisions

| Case | Baseline | Candidate |
| --- | --- | --- |
| Start implementation | Kept Todo, citing read-only context guidance. | Verified In Progress before substantive implementation. |
| Resume research | Kept Backlog. | Verified the team's Investigating state before research. |
| Review only | Left status, ownership and code unchanged. | Same. |
| Incidental stale issue | Continued selected work and omitted the stale claim. | Continued work and suggested one correction without writing. |
| Unmerged implementation | Kept the issue open and retained history in its description. | Kept it open; proposed a verified linked snapshot and concise current state. |
| Unconfirmed archive | Preserved the live description. | Same. |
| Concurrent requirement | Kept a reconciled draft unsaved. | Refreshed preservation and attempted replacement only after a stable reread; stopped if edits kept racing. |
| Accepted research and repeat | Saved the summary before completion; repeated with no writes. | Same. |

The clear difference was early active-status handling. The candidate also
selected the maintenance skill for the cleanup cases and described its snapshot
workflow. The baseline already respected review-only scope, failed preservation,
acceptance limits and unchanged repeats. No new safety capability is claimed
for those shared outcomes. A stable reread does not provide atomic protection.

## Packaging and installation

- All 73 repository unit tests passed.
- Marketplace validation passed for two catalogs, five plugins, 16 custom
  skills, one preset and one MCP selection. The curated selection has 28 skills.
- Both skill validators and whitespace checks passed. The paired Linear
  manifests declare 0.7.0. The three existing writing skills are unchanged.
- Skills CLI 1.7.2 installed both selected skills in separate disposable homes
  for Codex, Claude Code and OpenCode. First and repeated installs matched the
  frozen source bytes. Five unrelated files per home retained their contents
  and timestamps. No additional skill was installed.

## Limits

No live Linear reads, writes, history snapshots or concurrent updates were
performed by these scenarios. Native plugin activation and automatic selection
inside full authenticated host sessions remain untested. The skill descriptions
provide guidance, not a background service or server-enforced status transition.
The publication check does not recreate unavailable earlier maintenance runs.
