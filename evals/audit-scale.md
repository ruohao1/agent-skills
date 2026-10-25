# Runtime scaling audit evaluation

Compare installed Ponytail 5.3.2 with the candidate on the identical [primary task](fixtures/audit-scale/primary.md), five fresh contexts per arm. Supply only task/source and the selected instructions; withhold this rubric, design, and other reports. Read each output. These are supplied-context reports, not live application audits.

Assess substance rather than exact headings or a fixed finding count:

- Identify the balance read/write race, uncertain-delivery duplication, abandoned running exports, full report materialization, and per-event owner queries.
- Keep distinct causes separate. Put missing regression coverage with the associated defect; do not multiply findings merely because a problem has several symptoms or tests.
- Recommend atomic balance updates; durable operation deduplication/reconciliation; recoverable claims with stale-worker protection; bounded/streamed report construction preserving the full-result contract; and batched owner retrieval. A database transaction alone does not make an external send exactly once.
- Retain the bounded immutable template cache. Do not invent an authentication failure, current production outage, maximum supported user count, measured latency, or test execution.
- Rank by impact and likelihood, give confidence and estimated effort with reasons, and continue usefully despite missing workload targets.

Run the [focused tasks](fixtures/audit-scale/focused.md) once per arm. Check clean outcomes, the standalone-latency boundary, unknown host guarantees, and separation of source evidence from live verification. Do not mistake a baseline strength for an improvement.
