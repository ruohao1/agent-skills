---
name: audit-scale
description: Use when the user asks to audit runtime scaling, growing data volume, concurrent users or workers, or recovery of interrupted and retried work.
---

# Audit scale

Audit behavior as data volume or concurrent work grows, within one process or across users, workers, and jobs. Include concurrency and recovery correctness at low traffic. Return a report; fixes and issue creation are separate requested work. General performance problems unrelated to workload growth, concurrency, or recovery are outside this audit.

## Establish the workload

Inspect the requested area, or the whole repository by default. Read repository instructions and trace entry points through callers, shared stores, queues, and external operations. Establish configured process counts, data limits, adapter guarantees, and relevant tests from available evidence. Distinguish repository configuration from observed deployment state.

Research available facts before asking questions. Missing traffic targets or metrics do not prevent useful analysis: continue with demonstrated concurrency flaws and resource-growth patterns. Ask when missing information would change a conclusion or priority. State workload assumptions and triggering conditions; capacity estimates remain unverified until measured.

## Trace failure conditions

Check how reads, queries, buffered results, queued work, and resource use grow with input and concurrency. Trace competing operations and interruption windows through claims, external effects, retries, and completion. Verify what each transaction, claim, or deduplication mechanism actually protects across processes and restarts.

Read the affected implementation, callers, tests, and relevant configuration. Establish a concrete interleaving, interruption, or growth mechanism for each finding. Unknown host guarantees remain questions to verify. Distinguish a missing contract from an observed violation; preserve useful bounded caches, queues, and worker pools.

Recommend the smallest fix that addresses the cause and preserves required results and ordering. Check its effects on other workers, retries, stale completions, and external operations. Group observations resolved by the same fix; keep independent causes separate. Put related regression checks with their finding.

## Verify within scope

Use relevant existing tests and bounded reproductions in disposable environments when they resolve uncertainty. Sustained load tests and active tests against deployed systems need separately agreed targets and limits. State which checks ran, which results were supplied, and which conclusions come from inspection. Source inspection alone does not establish throughput, latency, memory thresholds, or a production outage.

## Report

Start with a short priority summary and the workload assumptions. Number every supported finding, ordered by impact and likelihood under that workload, without a fixed cap. Use a compact heading with the priority, problem, and verified locations, then four bullets of one or two short sentences each:

- **Evidence and impact:** triggering condition, failure or growth mechanism, and why it matters.
- **Fix and check:** smallest useful change and the check that would verify it.
- **Confidence:** what the evidence establishes and any material uncertainty.
- **Effort:** relative estimate and its main reason.

Use plain English and preserve technical references exactly. Report relevant findings even when security is another consequence. When combining audits, merge a shared root cause and retain each consequence. State shared coverage and execution limits once at the end, with unverified leads. A clean or inconclusive result is valid; do not invent findings to fill the report.

## Save the report

Save to `docs/audits/YYYY-MM-DD-scale.md` in the audited repository by default. Honor an explicit destination or chat-only request. When contributing to a combined audit, return findings to its coordinator without saving a separate report. Include the inspected scope and source revision when available, noting uncommitted changes. Use repository-relative source paths and line numbers inside the saved file. For a new run, add a numeric suffix if the path exists; replace a report only when an update is requested.

For a report inside a Git worktree, keep new untracked reports ignored by default. Inspect tracked state and effective ignore rules first. Reuse an effective rule; otherwise append an anchored, literal entry for that report alone to the worktree-root `.gitignore`, escaping Git pattern characters and preserving existing content and line endings. Treat already tracked reports and explicit include exceptions as tracking intent. If the user requests Git tracking, use narrow exceptions where needed and preserve other files' ignore status. Never untrack, stage, or commit files as part of the audit. Chat-only output and reports outside a Git worktree need no ignore edits.

Verify the actual report path with `git check-ignore --quiet`. Use `-v` to identify rules, not to prove exclusion: it also reports negated matches. State any tracking exception or ignore failure without claiming the report is ignored.

After saving, the final reply consists of the report link, a one-sentence priority summary, and material execution limits. The findings belong in the saved file. If saving fails, return the report with the reason and do not claim it was saved.
