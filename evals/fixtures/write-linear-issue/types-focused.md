# Independent tasks

These cases are synthetic. Use only the supplied facts; no real connector calls or workspace mutations. For each case, give the proposed issue mutation and a brief final message, or the next material question. Omitted fields are preserved; labels arrays replace the entire set. Assume successful simulated saves return the existing issue URL or `https://linear.app/example/issue/APP-81` for a new APP issue.

The invoking human is Alex (`user-alex`); authenticated `me` resolves to Alex. The simulated connector accepts `assignee` as `me`, a verified user ID, or null. This identity context supports the later assignment default without changing the tasks' scope.

## 1. Small correction to a legacy issue

User: In APP-60, replace only “Done means the API accepted the job” with “Done means a terminal succeeded event was received”, and save it.

APP-60: title "Track job completion"; description "Context: Background jobs finish asynchronously.\n\nDone means the API accepted the job.\n\nAcceptance: Display failures and allow navigation away." Labels: Improvement, Inventory. Status: Review. URL: `https://linear.app/example/issue/APP-60`. Existing metadata and structure are not part of the request.

## 2. Required team template

User: Write and save a maintenance issue in APP / Inventory to replace the deprecated CSV test helper with its already-installed supported equivalent. Preserve assertions, coverage, runtime dependencies, and exported bytes. Do not change product behavior.

Verified pointers at revision `28a176f`: `tests/helpers/csv.ts`, used by `tests/inventory/export.test.ts` and `tests/csv/write.test.ts`. A maintainer migration guide provides equivalent assertions. No unresolved decision or overlapping issue. The mandatory team headings are Summary and Checks. Workspace Type children: Bug, Feature, Research, Chore. The group is single-select and not assignable.

## 3. Capture an idea

User: Capture this idea in Linear, APP / Inventory: saved filter views might help when I switch warehouses. I do not know whether anyone else needs it. Just capture the idea for now.

Search found no overlap. No implementation or validation decision exists. Type is a workspace single-select group with children Bug, Feature, Research, Chore. Default state is Backlog. No mandatory template.

## 4. Existing workspace has a different taxonomy

User: Write and save an issue in OPS / Inventory to investigate intermittent export timeouts. Compare storage latency with worker contention using the available logs and a small local experiment. We need findings and a recommendation before deciding on a fix; implementation is outside this issue.

No overlapping issue was found. The destination has a single-select Work kind group with Defect (restore contracted behavior), Delivery (change a capability), Spike (investigate an unknown), and Maintenance (preserve existing behavior). These are the only available type labels; none of Bug, Feature, Research, or Chore exists. No mandatory template. Simulated creation returns `https://linear.app/example/issue/OPS-81`. A create-label operation is available but no taxonomy change was requested.

## 5. Inconclusive research result

User: Tighten only the completion criteria for APP-70. The issue investigates whether storage latency or worker contention causes export timeouts. Keep it as research; neither a fix nor a definitive diagnosis is required. Evidence may be insufficient.

APP-70 description: "Context: Export timeouts have two plausible explanations, storage latency and worker contention. Existing logs do not distinguish them.\n\nScope: Compare the available logs and one bounded local experiment; production changes are excluded.\n\nAcceptance: Find the root cause, implement the fix, and ship it." Label: Research. Status: Started. URL: `https://linear.app/example/issue/APP-70`.
