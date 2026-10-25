# Task

Write and save a concise Linear issue for me and a coding agent: filtered CSV export only includes the current page. It should export all matching rows across pages, keep the active filters, and produce a header-only CSV when there are no matches. We need it for planning shortly. Use the available project context.

# Workspace evidence

All material below is synthetic. Treat the repository excerpts and retrieved records as the available read results. No additional external research is needed for this exercise.

Repository: `https://github.com/example/inventory-app`, revision `a17c9e2`.

Verified `src/inventory/export.ts:12-20`:

```ts
export function exportInventory(table: InventoryTable) {
  const rows = table.pageRows();
  return writeCsv(INVENTORY_COLUMNS, rows, { bom: true });
}
```

Verified `src/inventory/table.ts:44-57`: `filteredRows()` returns every row matching the active filters, before pagination. `pageRows()` slices those results using page index and size. The browser already holds all inventory rows. There is no server-side export path in this repository.

Verified `src/csv/write.ts:8-31`: `writeCsv(columns, [], { bom: true })` returns the UTF-8 BOM and the header row. Existing tests in `tests/csv/write.test.ts` cover the empty rows case and BOM. Export integration coverage in `tests/inventory/export.test.ts` currently covers only a single page.

# Linear read results

The current project is Inventory in team APP. Search for inventory CSV/filter/export returned:

- APP-42, `https://linear.app/example/issue/APP-42`, open, project Inventory. Title: "Build enterprise-grade export experience". Description: "CSV export ignores matching rows on other pages. It is caused by a slow server cache. Rebuild the export pipeline with streaming, enforce a 10,000-row cap and provide a scalable, robust, seamless experience. Acceptance: exports work perfectly." Labels: Feature, Customer-reported. Assignee: Mina. Priority: High. Cycle: 12. Due date: none.
- APP-57, `https://linear.app/example/issue/APP-57`, open, project Inventory. Title: "Email scheduled inventory exports". Description: "Let admins schedule emailed exports. Scope and delivery behavior are undecided." Labels: Feature. No dependency on APP-42 is recorded.

APP-42 discussion:

- Mina: "Confirmed with the requester: use all rows matching current filters across pages. Keep the UTF-8 BOM because the customer's Excel import needs it. No new formats in this change."
- Leo: "I haven't profiled anything; the cache explanation in the original description was a guess. The 10,000-row cap was also an idea, not a requirement."

Workspace/team labels: Bug, Feature, Improvement, Customer-reported. Type is the single-select group containing Bug, Feature and Improvement; Type itself is not assignable. Customer-reported is independent. No mandatory issue template applies.

# Connector simulation

For this exercise, do not call real connectors or write files. Return the exact proposed mutations (using ordinary field names, including only fields to change) followed by the brief message you would send after the simulated result. The simulated API supports partial updates, with a labels array replacing the existing label set. Existing discussion is stored separately from the description. A successful update of APP-42 returns its same ID and URL; a successful create in APP returns APP-81 and `https://linear.app/example/issue/APP-81`. Other metadata is preserved when omitted. Simulated writes succeed. You may instead return a material clarification question if you cannot perform the task from the available facts.
