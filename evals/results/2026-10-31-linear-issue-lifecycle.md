# Planning scope and issue lifecycle — 2026-10-31

## Decision

Linear Workflows 0.4.4 distinguishes the current session's action boundary from
the issue's intended outcome. `write-linear-issue` keeps specification work
inside a capability issue. `wrap-up-linear-issue` checks the user's accepted
scope before treating planning approval as completion. Explicit independent
research and design deliverables retain their own completion criteria.

## Method and initial result

The [protocol](../linear-issue-lifecycle.md) uses synthetic drafts and proposed
connector actions. Inputs and criteria were frozen before the corresponding
runs. Evaluators received the complete relevant skills and raw task facts, with
no criteria, expected answers, previous outputs or implementation plan. Contexts
were fresh, used the inherited model/runtime and had no model override.

Five initial contexts each answered the five
[explicit-scope requests](../fixtures/linear-issue-lifecycle/tasks.md). All passed:
capability planning remained Feature work, research stayed independent, an
agent-written planning checklist did not narrow the user's scope, an accepted
design sub-issue could close, and a title-only correction stayed narrow.
Those results and criteria were retained unchanged.

The separately frozen [design-workflow case](../fixtures/linear-issue-lifecycle/design-workflow.md)
added a workflow that requires an issue before design and stops at specification
approval, plus nearby completed specification issues. Five baseline contexts and
five candidate contexts received the identical case. The candidate changed only
the two supplied skills. All ten baseline responses were read before the skill
edits. The original five requests were then checked in one fresh candidate
context as boundaries; this is one candidate sample per boundary.

## Observed results

| Design-workflow decision | Baseline | Candidate |
| --- | --- | --- |
| Track the capability as a Feature with planning as a checkpoint | 0/5 | 5/5 |
| Leave the capability open after specification-only completion | 0/5 | 5/5 |
| Preserve constraints and the planning-only action boundary | 5/5 | 5/5 |
| Avoid real writes, implementation and automatic cancellation | 5/5 | 5/5 |

All five workflow baselines created Research issues titled around specifying the
capability. They treated the design workflow's stop as the issue's final scope,
then proposed Done after the specification and breakdown were accepted. They
correctly stated that runtime work was not complete. The failure was which
outcome the issue tracked, not a false claim that implementation existed.

All five candidates retained a prospective Feature, separated its planning
checkpoint from delivery criteria, and left it open at the later handoff. They
stopped before implementation and did not treat the Feature type as a delivery
commitment. They recorded that planning could change or reject the approach.

The candidate boundary response passed all five original requests. It preserved
the standalone Research deliverable and its inconclusive-result option. It
allowed an accepted independent design issue to close after summary verification,
left its unfinished parent unchanged, and preserved title-only edit scope.

All 16 complete responses were manually read. Raw answers, per-criterion excerpts
and fingerprints remain outside the public repository. The comparison tests the
two skills together; it does not isolate the contribution of each added paragraph.

## Sources and packaging

The baseline is published main at
`56aca9d4fdf1a53d729e9314d2f6d22ccdc899b7`, Linear Workflows 0.4.3.
Other source revisions were not evaluated.

| Skill | Baseline SHA-256 | Candidate SHA-256 |
| --- | --- | --- |
| write-linear-issue | `b495ea71b50425cba0def9f5b05dc83360c6bfae55e16a1b547055cbe9b0cffc` | `c5af3611f793f42d3858508ec81b2978ad0ab95051bf56f93791b4930f88c5a7` |
| wrap-up-linear-issue | `403ffb8b089064e08e418019223f844a1bec46fd9dbb5105099f33675c33dd0b` | `7c46511338538fb55d2304f4700cf9ae41031f9fcea828f958fa0f4e351240d2` |

- All 73 unit tests passed before and after the change.
- Marketplace validation and both skill validators passed. Existing catalogs,
  skill counts and source pins are unchanged. Both plugin manifests use 0.4.4.
- Six cached Skills CLI 1.7.2 runs installed both skills: first and repeat installs
  in disposable Codex, Claude Code and OpenCode homes. Every run copied the exact
  candidate source and preserved five unrelated files' bytes and modification times.
- The packaged change adds no runtime code, dependency or global instruction.

## Limits

These small synthetic samples do not establish general success rates or the
cause of a particular historical session. Skills were supplied explicitly;
automatic selection and authenticated Linear writes were not tested. Evaluator
file reads are reported rather than independently archived tool traces. Existing
live issues were not migrated, reopened, reclassified or closed.
