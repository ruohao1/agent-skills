# Write Linear issue observations

## Scope and method

The evaluated format uses a concise Context → Change/scope → Acceptance criteria structure for human and agent readers. Writing includes saving. Research comes before material questions; matching work improves an existing issue, distinct work gets a linked issue, and verified code pointers must not silently become implementation decisions.

Used the synthetic [primary task and focused cases](../write-linear-issue.md). Five fresh-context control agents received the primary fixture without issue-writing guidance. Five fresh-context guided agents received the same fixture and the candidate skill. The first agent in each arm also answered the independent focused cases after its primary answer. Agents could read only the assigned material, not the rubric, other outputs, or this report. No model override was requested. All ten outputs were read manually.

The supplied excerpts and connector records stand in for successful reads. Agents proposed mutations and received a specified simulated success; they did not call a real connector. These checks measure issue-writing decisions from supplied evidence, not source discovery, tool-schema integration, authenticated saving, or statistical performance.

## Observed difference

All five controls updated APP-42 instead of creating a duplicate, removed the unsupported cache diagnosis and proposed row cap from the requirements, preserved the BOM constraint, selected Bug plus Customer-reported, and omitted unrelated metadata from their patches. They already produced usable context and acceptance checks. No improvement in those behaviors is claimed.

All five also prescribed a specific code edit that the supplied evidence made plausible but the fixture did not settle:

| Control | Verbatim instruction in the issue body |
| --- | --- |
| 1 | “switch to filteredRows()” |
| 2 | “Implementation: use `table.filteredRows()`” |
| 3 | “Use `table.filteredRows()` instead” |
| 4 | “Use `table.filteredRows()` to export every row” |
| 5 | “change `exportInventory()` to use `table.filteredRows()` instead of `table.pageRows()`” |

This is a mismatch with the confirmed preference to leave undecided implementation choices open, not evidence that the suggested edit is wrong. The candidate adds a positive structure separating current code evidence from requested behavior and settled constraints.

All five guided outputs kept `filteredRows()` as verified context and specified the required export outcome without mandating that edit. For example, guided 2 says “`filteredRows()` provides every matching row before pagination” in Context, then “Export all rows matching the active filters across pages” in Change/scope. They retained issue reuse, corrected labels, source pointers, empty-result handling, BOM preservation, and partial updates.

The narrow observed benefit is consistently separating evidence from an implementation commitment in this scenario. This does not demonstrate better reasoning in general or shorter issues. Guided 1 included an unnecessary planning sentence; guided 1 and 4 described matching active filters without separately spelling out that the filter state stays unchanged. Human review remains useful for proportionality and whether an acceptance check needs that distinction.

## Focused cases

Both the control and guided agent:

- Applied only the requested sentence correction, preserving surrounding text and metadata.
- Saved idea capture as exploratory without inventing validated demand or requiring implementation acceptance first.
- Created a distinct column-selection issue linked as related to APP-42, leaving APP-42 intact.
- Asked only the unresolved cancellation-race decision before preparing a ready-to-implement issue.
- Asked only which team should receive the ambiguous destination.
- Kept a draft-only request unsaved and identified the unavailable connector for a save request.
- Searched/read before retrying an ambiguous create timeout.

The skill preserved these already-good baseline behaviors; the comparison does not establish an improvement on them. No skill revision was needed after the guided runs. The shipped instructions are the tested candidate.

## Packaging verification

- Skill creator's `quick_validate.py`: passed.
- `python3 -m unittest discover -s tests -v`: all 64 tests passed.
- `python3 scripts/validate_marketplace.py`: passed; two matching native catalogs, two custom plugins, two custom skills, one optional preset.
- `python3 scripts/setup.py list`: includes `write-linear-issue` in Engineering; the curated selection now contains 14 skills.
- No installer logic, runtime dependencies, existing skill content, or live agent installation was changed.

## Disposable installation

Skills CLI 1.7.2 discovered both local custom skills through the repository's marketplace layout. Selected only `write-linear-issue` for Codex, Claude Code, and OpenCode, using disposable home, configuration, cache, state, and project directories. Fresh global installation, global repetition, fresh project installation, and project repetition all exited successfully. Every installed skill file matched the source bytes. An unrelated existing skill remained unchanged; the unselected `product-brief` was not installed. Shared destinations supplied Codex/OpenCode, with separate Claude copies.

The first sandboxed package fetch timed out before installation. A retry downloaded the pinned CLI and completed the disposable probes. These observations verify discovery and portable file installation, not authenticated host execution.

Native plugin installation/activation and authenticated Linear reads/writes with this skill have not been tested.
