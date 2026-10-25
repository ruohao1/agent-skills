# Task

Write and save four concise Linear issues for me and coding agents in APP / Inventory from the notes below. Keep the work bounded so each issue can be closed on its own outcome.

1. An inventory export sometimes downloads a CSV containing only the visible page. The documented contract is to export every row matching the active filters. Support reproduced it with 120 matching rows and a 50-row page: the CSV contained 50 rows. We have not found the cause. Capture the fix; investigation will be part of that work. Keep the current columns and UTF-8 BOM.
2. Improve warehouse switching: choosing another warehouse should keep the current search text. Today the search is cleared, as originally specified. That behavior works as designed, but users must retype the same query for each warehouse. Preserve the existing warehouse access rules. Do not add saved searches or change the search syntax.
3. Investigate intermittent export timeouts before we decide whether to change the implementation. The existing worker retries a timed-out job once. The available log sample does not establish whether storage latency or worker contention is responsible. Compare those explanations using existing logs and a bounded local experiment. We need evidence and a recommendation about the next step; this issue does not include a production fix. It may turn out that the available evidence cannot distinguish the explanations.
4. Replace the deprecated internal CSV test helper with the already-installed supported helper. The maintainer has documented the migration; there is no product defect or unresolved design decision. Preserve the assertions, test coverage, exported bytes, and runtime dependencies. Existing CSV tests should still pass. No product behavior should change.

# Available read results

All records and code facts are synthetic. Treat them as the completed repository and connector reads for this exercise; no further tools or external sources are needed.

- Repository revision `28a176f`; `src/inventory/export.ts` coordinates export, `src/inventory/WarehousePicker.tsx` clears search on warehouse selection, and `src/jobs/export-worker.ts` retries a timeout once. The support reproduction is verified, but no faulty export code path has been isolated.
- `tests/helpers/csv.ts` wraps the deprecated helper. The supported helper is already a development dependency; the migration guide maps each assertion to an equivalent. `tests/inventory/export.test.ts` and `tests/csv/write.test.ts` use the wrapper.
- Search of APP / Inventory found no overlapping issues. None of the four notes establishes a blocking relationship between these issues.
- The workspace has one single-select label group named Type, available to every team. Its children are Bug, Feature, Research, and Chore; descriptions are empty. Type itself is not assignable. No other type labels exist. The independent label Inventory is available.
- No mandatory team template applies. Default status is Backlog; no assignee, cycle, due date, or priority was requested.
- The invoking human is Alex (`user-alex`); authenticated `me` resolves to Alex. The connector accepts that alias or a verified user ID in `assignee`.

# Connector simulation

Do not use real connectors or mutate a workspace. Return four proposed creates with ordinary fields: title, description, team, project, labels, and assignee when applicable. Simulated successful creates return APP-81 through APP-84 respectively, with URLs `https://linear.app/example/issue/APP-81` through `https://linear.app/example/issue/APP-84`. Finish with the short message you would send after those simulated receipts. Do not include evaluation commentary.
