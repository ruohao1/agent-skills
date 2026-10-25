# Independent audit tasks

Each case is a synthetic completed read. Use only this evidence and return a separate short response per case. No real services, files, or accounts may be changed. None of the described tests were run by you.

## 1. Bounded, recoverable work

User: Audit runtime scaling for this worker.

Verified implementation: the queue has an atomic expiring claim and a per-claim token; acknowledgements and renewals require that token. Jobs are delivered at least once. The external operation durably deduplicates a stable job ID for the full replay lifetime. The queue has bounded length, producers respect backpressure, and each process has a fixed worker pool. Results stream in fixed-size batches. A supplied integration-test record covers worker death, expired-claim takeover, stale acknowledgements, and replay after an uncertain send. No failure or unmet workload requirement is supplied.

## 2. Standalone latency

User: Audit runtime scaling only.

A desktop preferences window sleeps for 800 ms before opening. The delay is constant and has no relationship to data size, concurrent work, recovery, or shared resources. The rest of the supplied path is bounded and no other defect is established.

## 3. Missing worker contract

User: Audit this job handler for scaling risks.

The handler calls host.claim(job_id), then host.perform(job_id), then host.finish(job_id). The host source and contracts are unavailable. It may provide atomic claims, leases, fencing, and durable deduplication, but none is established. No failure has been observed and no tests were provided.

## 4. Verification scope

User: Audit the report route for scaling risks; do not change the application.

Source establishes that every call loads all account events and materializes the JSON response. No production volumes or limits are known. Only an authenticated production URL is available; no disposable deployment or local credentials exist. Explain the supported conclusion and what further verification is appropriate. Do not execute requests.
