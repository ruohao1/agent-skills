# Design skill results

Date: 2026-10-25. Synthetic projects only. Raw responses, tool transcripts, installation logs, and host paths remain outside the repository.

The three candidates met the evaluation criteria. Product Design 0.3.0 adds `design-product`; Software Design 0.1.0 adds `design-architecture` and `design-code`. Their common demonstrated benefit is a saved, scoped handoff. The architecture checks also addressed one unsupported policy assumption in the baseline.

## Method

The [protocol](../design-skills.md) uses [primary fixtures](../fixtures/design-skills/primary.json) for CSV import recovery, background report exports, and a pricing refactor. Five fresh baseline contexts received eight existing skill descriptions and their resources. Each context selected skills before reading their bodies, then completed all three cases in separate disposable projects.

Each candidate comparison adds only that candidate to the frozen bundle and repeats the same three-case sequence in five fresh contexts. Preferences, tasks, permitted tools, and the 400-word prose limit stay constant. No model override was used. The three tasks share a context; they are not independent model samples. Delivery conventions can transfer between tasks even when a later task selects a different skill.

Every completed response and saved artifact was read manually. Original fixture files were compared byte for byte. Existing pricing behavior was checked separately for per-line rounding, empty input, and discount errors. Some agents also executed baseline pricing checks; none implemented the proposed refactor.

The existing resources were frozen from installed copies. Their equivalence to the catalog-pinned upstream revisions was not verified. These small samples support observed differences, not general success rates or superiority over other models or tools.

## Existing-guidance baseline

All five contexts selected `product-brief` for product and `codebase-design` for architecture and code. The substantive designs were generally sound, but none saved a handoff.

| Behavior | Observed |
| --- | --- |
| Product scope, acceptance versus completion, partial writes, and retry contract retained | 5/5 |
| Architecture reused the existing app/worker and covered durability, idempotency, leases, authorization, and rollout | 5/5 |
| Export retention remained unknown or an explicit proposal | 4/5 |
| Code design centralized the rule, preserved rounding/errors/signatures, and covered all three callers | 5/5 |
| Saved design artifact, for each primary case | 0/5 |
| Original project files preserved | 15/15 |

One architecture response treated the existing cleanup helper as evidence of a result-retention policy. The fixture establishes a mechanism, not that policy. No substantive product or code-design deficiency was established by these primary baselines.

## Product guidance and revisions

The first `design-product` candidate was selected for product in 5/5 matched contexts. All five saved the product handoff, retained the required behavior, preserved source, and returned a concise link. They also saved later architecture and code designs. Those later saves show possible shared-context transfer; they are not independent evidence for either technical skill.

The [four filesystem delivery cases](../fixtures/design-skills/delivery.json) tested a default destination, a section-only update, a custom path, and text-only output with no companion skills. All passed. The default document was 830 whitespace-separated words and repeated recovery details. The focused update was also too expansive.

A second version gave each decision one place and added a flexible 300–500-word target for a small change. Its single matched delivery rerun passed all four cases: default/custom documents fell from 830 to 503 words, and the update from 493 to 347. Unrelated sections, the existing index, and other notes remained exact. This is one delivery comparison, not a general length benchmark.

Five fresh standalone checks of version two used explicit skill invocation and no external word cap. All saved documents and preserved source; lengths were 514, 516, 556, 497, and 528 words. One response was ambiguous about starting a new submission when the original payload was missing after a status lookup. The final version requires recovery actions to state their safety preconditions and preserve identity/payload requirements.

Five fresh standalone checks of the final version saved handoffs and explicitly required the original request ID, exact payload, and valid retention window before replay. All preserved source and handled partial writes and unknown outcomes. Lengths were 522, 559, 612, 537, and 515 words. These checks confirm the revision; they are not pooled with the earlier discovery comparison. Storage cases were not repeated after this safety-only sentence changed.

The demonstrated benefit is a saved, scoped handoff. The baseline already handled the core product contracts well. These cases do not establish visual quality or usability.

## Architecture guidance

All five matched contexts selected `design-architecture` for architecture, saved its handoff, and preserved original files. They retained the baseline's durable SQL jobs, existing worker, submission deduplication, recovery, account authorization, and compatibility. All five kept new result-retention policy unresolved or explicitly proposed; the baseline did so in 4/5. This narrow observation supports checking policies before treating an existing helper as a guarantee.

Three contexts also saved product and code artifacts, while two saved only architecture. As with the product arm, those other saves do not independently establish another skill's benefit.

The architecture half of the [technical delivery fixtures](../fixtures/design-skills/technical-delivery.json) passed all four actual filesystem cases using the skill alone. Default and custom documents were 552 words. The section-only update was 436 words including preserved sections. The existing index, source, unrelated notes, and untouched sections stayed exact. Text-only output made no file changes. Retention remained open in the saved designs.

## Code guidance

All five matched contexts selected `design-code` alongside `codebase-design` for the pricing refactor. Each saved a handoff, centralized ownership behind a concrete interface, preserved rounding and errors, covered all three public callers, and left source unchanged. This is a delivery improvement; the baseline already produced sound structural designs.

Without `design-architecture` in this isolated arm, all five also selected `design-code` for architecture. One selected it for product. Requested task scopes remained intact. All saved architecture designs, and four saved product designs. These selections and shared-context saves are reported separately from target-case success; they do not establish precise routing when companions are absent.

The code half of the technical delivery fixtures passed all four filesystem cases with no companion guidance. Default and custom documents were 446 words; the focused update was 278 words including preserved sections. Public signatures, per-line rounding, and caller migration were retained. Source, unrelated notes, and untouched sections stayed exact. Text-only output made no file changes.

## Combined selection and scope

A fresh context received all three final candidates alongside the existing bundle. Before reading skill bodies, it selected `design-product`, `design-architecture`, and `design-code` for their respective primary requests. This is one description-only selection check, not another executed primary comparison.

The same context then completed the [eight focused action cases](../fixtures/design-skills/focused.json). Like the single existing-guidance baseline, it kept audit-only work scoped, proceeded directly with an adequate implementation request, preserved a chosen architecture, honored narrow text and existing-document requests, and left unsupported retry behavior unresolved. It reused an adequate export structure and returned an explicitly unsaved design for simulated read-only storage. New designs used the intended saved-handoff convention. These were action plans, not executed file operations or actual host activation.

## Portable installation

The cached, pinned Skills CLI 1.7.2 discovered each final skill through the local marketplace. Each skill was installed alone, then installed again, in disposable global and project environments targeting Codex, Claude Code, and OpenCode. Installed bytes matched the corresponding source. No companion skills or preference files appeared; five unrelated sentinel files per run remained unchanged.

Codex and OpenCode used the canonical `.agents/skills` directory; Claude Code used its linked skill directory. The existing legacy OpenCode directory remained unchanged. An initial temporary test expected installation in that legacy path. CLI source and logs showed canonical routing, so the test expectation was corrected and the install check repeated. No repository installer code changed.

These are real local CLI discovery and file-installation checks. They do not demonstrate native plugin activation or authenticated agent use. Active user installations were not refreshed.

## Verification limits

The 73 repository unit tests passed. The marketplace validator accepted two catalogs, five custom plugins, thirteen custom skills, one preset, and one MCP selection. The full catalog contains 25 custom and upstream skills. Each new skill passed frontmatter validation. Packaged and installed files matched; publication normalized trailing blank lines in two skill files without changing their instructions.

The tests did not implement or exercise real import/export systems, concurrency, sustained load, authenticated services, or visual usability. Read-only storage failure is a simulated action case, not an injected filesystem failure. Native host activation and non-Linux runtime behavior were not checked. No installer, upstream pin, existing audit skill, or `product-brief` behavior changed.

A fresh whole-change review found no Critical, Important, or Minor issues. It checked the complete change, inspected representative raw artifacts and all final product recovery artifacts, verified manifest and source-hash consistency, and independently confirmed preservation of 340 original fixture files. It used the recorded unit and installation evidence rather than rerunning those checks; it did not independently reread every raw transcript.

## Source fingerprints

SHA-256 values below identify each evaluated `SKILL.md`, not every linked upstream resource. Existing sources were held constant across comparisons. Before publication, trailing blank lines were removed from the final product and architecture files. Instructions were unchanged. The normalized packages have separate hashes below; their isolated installation checks were repeated.

| Source | SHA-256 |
| --- | --- |
| product-brief | `c63630226d66ac3882d9600e1b0f15b04c34c2aacf0211cc6af291edff0e0cdd` |
| codebase-design | `a8d50abac5a4018f60e1d911d4b6f4e36454ca14d6c390c0695a578c7de65dad` |
| prototype | `03074862d4b6e4eaf472aa75146e1d193dd9e3bba0e4303a9b2425562d1d44cc` |
| archify | `66dfe99b35d7ceff95bcbdb00f138b8b3ec8094629acf69efba1eeda1013aaf3` |
| domain-modeling | `152e2c97239affb12a60c5f4a7e74ab546a49ae169688c81f4e2ccc42dafa579` |
| audit-code | `eff463f361ad68daa8fb0fa772137f4f3dc35420d904adbeb152631e07308bee` |
| audit-scale | `3a6d1ef86a692944a1e3a91562a511e69e634f738f2c2f664e93a5b3207e669d` |
| audit-security | `2e924771d0311c89a4c00fab2b92d730c034b3a82a699a0917afb6f60e95da03` |
| design-product v1 | `dccbfc3343756beacb821050ee4610f3001a9479048764f7aca4f8fd2f7a1d32` |
| design-product v2 | `e0873730b1303d049845d92c6e2895a323c44fb9ca5f270d8eb332c3d11dc856` |
| design-product final | `bc369822f921718d1388280a966d620cd912572f78135909a4ebb4deb7b90189` |
| design-architecture | `ad713f620d1c43db6da6fa098ce13130162e28c43f6b157b92af22f08a59b65d` |
| design-code | `4f532412d79acb6e317f9d87ee8fa9b376f993951e709f49af08ed0850e9d27b` |
| design-product packaged (EOF normalized) | `e1feca7b7309e293288355aeb80e247cb47b4e4f757a22fdbb29cef00040b206` |
| design-architecture packaged (EOF normalized) | `fdd837f7f4909880578cd70d3f764ceb4b47b155e8e3c486fca2b3d062b6d0eb` |

Primary fixture: `0d8c88b0617dc2cde8daa30ac2af49e6616dadeb58065bedc8fd6f208d8eb726`. The anonymous fixture files and this report are versioned; raw outputs remain private.
