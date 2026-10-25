# Independent audit tasks

These are synthetic completed reads. Return one report per task. Do not access connectors, change source files, create issues, or inspect any real repository. Use only the supplied evidence. Checks were not run unless a case says otherwise.

## 1. Small orchestrator

User: Audit only `src/archive.py` for readability and maintainability improvements. Leave the code unchanged.

Verified source:

```python
# src/archive.py
1 def archive_orders(store, exporter):
2     orders = store.completed_orders()
3     if not orders:
4         return None
5     archive = exporter.write(orders)
6     store.mark_archived([order.id for order in orders])
7     return archive
```

Completed caller and test reads: the daily and manual entry points both use this function. Focused tests cover empty input, success, and an exporter error. An exporter error propagates before `mark_archived`; the tests assert that order. The list of IDs is the storage interface's input contract. Store and exporter are useful boundaries used by real and test implementations. No rule calculation is embedded in the function. Caller and interface reads establish no additional problem within the named scope.

## 2. Incomplete evidence

User: Audit `src/export.py` for maintainability. I suspect this helper is unused.

Verified source:

```python
# src/export.py
1 def export_records(records, writer):
2     return writer.write(records)
```

Read results: no direct call appears in the available files. README says deployed export callbacks can be selected by configuration supplied outside this checkout. That configuration and the deployed consumer code are unavailable. No repository policy guarantees this function is private, and no evidence establishes whether it is registered. The rest of the project was outside the requested scope.

## 3. Complete report

User: Produce the maintainability audit report from these completed investigation notes. Include every supported finding. Do not create tickets or modify code.

Each numbered item below is independently verified against its stated local source and callers. The affected subsystems have separate owners and no shared implementation that would fix multiple items. These are concise investigation notes, not an existing report. All recommendations preserve current externally observable behavior. No additional code is available in this fixture. Estimates and precise replacement designs have not been established.

1. `billing/fees.py:12`: invoice preview and finalization independently encode the same documented fee policy, so a policy edit must update both copies. Extract the shared calculation.
2. `mail/send.py:8`: three forwarding helpers add no behavior between the caller and the mail adapter. Keep the useful adapter boundary and remove the redundant hops.
3. `units/display.py:19`: the docstring says seconds, while the implementation and callers pass milliseconds. Correct the documented unit.
4. `archive/legacy.py:4`: a retired tar-format encoder has no callers, configuration, registrations, exports, or supported migration use. Remove it.
5. `shipping/flow.py:27`: address classification rules live inside the shipment coordinator; testing the rules requires setting up transport and storage mocks. Extract the rule calculation.
6. `search/status.py:6`: the public internal helper name `data` hides that it computes a search readiness label; six call sites require opening its body to identify that role. Rename it and its callers.
7. `reports/schema.py:33`: adding one report field requires coordinated edits to separate field-order and field-name tables that always describe the same schema. Use one schema definition.
8. `images/options.py:17`: a Boolean parameter changes both output format and cropping policy at eleven call sites, obscuring the chosen behavior. Express the independent choices explicitly.
9. `calendar/rules.py:54`: an unrelated display-theme dependency is imported at module load, so rule tests must initialize the UI. Move display work to its caller.
10. `storage/codec.py:38`: three functions rely on undocumented keys in a shared mutable scratch dictionary, making their sequencing hard to follow. Use explicit inputs and results for those phases.
11. `accounts/constants.py:9`: two separately named constants represent the same documented account-state value; both must change together. Keep one canonical name and update consumers.
12. `orders/repository.py:71`: an internal return tuple contains six adjacent strings and requires callers to remember their positions. Give the result's fields explicit names.
13. `analytics/collect.py:43`: a validation loop is copied across three ingestion entry points with the same contract. Share that validation while retaining each entry point's error presentation.
14. `payments/tests/test_rules.py:22`: pricing tests duplicate a large unrelated customer fixture; changing an unrelated profile field forces updates across all those tests. Keep a focused shared fixture with explicit relevant inputs.
15. `exports/factory.py:13`: a factory, registry, and selector exist for one fixed internal encoder, with no configuration or extension contract. Replace the chain with the existing encoder.
16. `imports/parse.py:48`: parsing, database writes, and user-message formatting are interleaved, so parser changes require storage setup and UI assertions. Separate parsing from the effectful workflow.
17. `permissions/model.py:31`: a deprecated internal alias remains alongside the current name even though all supported callers have migrated. Remove the verified-unused alias.
18. `inventory/service.py:29`: one internal convenience object exposes the entire store to a calculation that needs only stock quantities. Pass the needed data and narrow the dependency.
19. `support/format.py:16`: repeated numeric indexes into a delimiter-split record hide the meaning of each field across the formatter. Name the parsed fields once.
20. `preferences/validate.py:25`: a stale comment describes a default that was removed; code, tests, and current documentation agree on the new behavior. Update the comment.
21. `routing/resolve.py:62`: the resolver combines unrelated alias expansion and access-policy evaluation, which have independent callers and tests elsewhere. Reuse those existing functions to make the routing sequence explicit.

The notes establish 21 separate causes. Similar categories are not evidence of one shared cause. Rough effort labels may be presented as estimates, but no measured time or line savings are available. The available notes were reviewed; no tests or fresh source inspections were performed for this task.
