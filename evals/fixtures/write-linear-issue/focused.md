# Independent tasks

All tasks are synthetic. For each, return proposed connector operations and the final user message, or the next material question. Do not call live connectors or write files. Partial patches preserve omitted fields; label arrays replace the full set. Successful simulated saves return the supplied URL or, for new APP issues, `https://linear.app/example/issue/APP-81`. Treat each case independently.

The invoking human is Alex (`user-alex`); authenticated `me` resolves to Alex. The simulated connector accepts `assignee` as `me`, a verified user ID, or null. This identity context supports the later assignment default without changing the tasks' scope.

## 1. Small correction

User: In APP-60, replace only “Done means the API accepted the job” with “Done means a terminal succeeded event was received”, and save it.

Retrieved APP-60: title "Track job completion", description "Context: Background jobs finish asynchronously.\n\nDone means the API accepted the job.\n\nAcceptance: Display failures and allow navigation away.", label Improvement, state Started, URL `https://linear.app/example/issue/APP-60`. No other changes requested.

## 2. Capture an idea

User: Capture this idea in Linear, APP team, Inventory project: saved filter views might help when I switch between warehouses. I don't yet know whether anyone else needs this.

Search found no overlapping issue. Available labels: Feature, Improvement, Bug. Team's default state is Backlog; no mandatory template. There is no repository evidence or settled implementation. Creation returns APP-81.

## 3. Distinct follow-up

User: Create and save a linked follow-up to APP-42 for user-selectable CSV columns. The current inventory export always includes every fixed column. Let users choose columns and their order for that export; saving column presets is out of scope.

Verified `src/inventory/export.ts:14` always passes INVENTORY_COLUMNS; `src/csv/write.ts:8` accepts an ordered columns list. APP-42 is completed and covers exporting all filtered rows, including BOM; it has no column selection requirement. Search found no overlapping column selection issue. APP-42 URL is `https://linear.app/example/issue/APP-42`, team APP, project Inventory. Available labels: Feature, Improvement, Bug. No mandatory template. The relationship API supports a related-issue link. Creation returns APP-81.

## 4. Material decision

User: Write a ready-to-implement issue and save it: users should be able to cancel a queued export. Use the Inventory project in APP.

Available repository read result: `src/exports/api.ts:70` permits cancellation only in queued state. The worker can move queued to running between the UI click and server handling. Running cancellation is unsupported. Search finds no existing issue or decision about this race. Product choices for a lost cancellation race could be to report it is already running and keep the export, or to suppress its eventual delivery. These have different acceptance criteria. Labels: Feature, Bug, Improvement. No other decision is missing.

## 5. Destination ambiguity

User: Write and save an issue for "Show a useful empty state on a new inventory". The empty state should explain that there are no items and offer the existing Add item action. Do not change onboarding.

Verified repository: `src/inventory/list.tsx:30` returns an empty table for zero items; `AddItemButton` already opens the add-item form. No overlap found. Two accessible teams both have an Inventory project: APP and OPS. Session context supplies no chosen team. Both teams have Improvement, Feature and Bug labels.

## 6. Draft and disconnected cases

6a. User: Draft a concise issue here for keyboard access to the existing export button; do not save anything. Evidence: the custom button in `src/inventory/ExportButton.tsx:10` has a click handler but no keyboard activation. Keep the existing action and appearance. No overlap is known. Destination is irrelevant for this draft.

6b. Same request, except user asks to save in APP/Inventory. No Linear connector is available. Local repository evidence is available as above.

## 7. Uncertain create result

User asked to create and save a new issue in APP for the verified keyboard defect above. An initial create call timed out after submission; no success or failure receipt arrived. Search/read tools are still available, but have not yet been called. Describe the next operation before claiming success or issuing another create.
