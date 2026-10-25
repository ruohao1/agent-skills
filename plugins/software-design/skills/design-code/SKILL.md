---
name: design-code
description: Use when selected work needs module responsibilities, interfaces, dependency direction, file organization, or caller migration designed, or when an existing code design needs updating.
---

# Design code

Resolve structural choices for selected work. Reuse settled product and architecture decisions. An audit discovers and prioritizes problems; use its evidence without repeating that search. Design unresolved choices or an explicitly requested document. Keep this workflow usable independently.

Read the affected implementation and its callers before choosing a structure. Check imports, exports, registrations, configuration, and test/build discovery when the proposed change affects them. Preserve valid contracts and unrelated work. Distinguish observed behavior from a proposed change.

Give each responsibility a clear owner. Describe the interface callers need, including relevant inputs, results, errors, ordering, and side effects. Show dependency direction and the knowledge the interface hides. Choose files and folders that fit those responsibilities and repository conventions. The existing structure may suffice; add a layer or abstraction only when the selected work needs it.

Compare meaningful alternatives and recommend one. Ask when a choice changes scope, user behavior, significant cost, or an expensive commitment. Make routine, reversible decisions autonomously and state material assumptions. Keep unaffected decisions moving while a consequential dependency is unresolved. Leave ordinary implementation details to the builder.

## Save the handoff

Lead with the chosen structure. Add a compact interface sketch or responsibility/file map, the contracts to preserve, and the affected callers. Describe migration and meaningful verification at the interface. Include consequential tradeoffs and remaining decisions where relevant. Put each decision once and reference established context. For a small change, aim for 300–500 words; expand when consequential behavior needs more detail. A focused correction preserves the rest of the design.

Use short, complete sentences and verified source references. Distinguish source inspection from executed checks. Keep private project details out of public artifacts.

Honor an explicit destination, existing document, or text-only request. Otherwise, update the relevant design or save `docs/designs/<topic>.md` in the target repository. Read existing content first; preserve valid decisions and unrelated sections. Share one document across the relevant scopes of a coherent change. Avoid duplicate designs or overwriting unrelated files.

Read back the saved document. Return its link, a short decision summary, and material limits. If saving fails, return the unsaved design with the reason.

Keep the design available for related implementation unless instructed otherwise. Designing alone does not authorize production changes, ignore edits, staging, commits, or publication. Honor an explicit implementation request without inserting a design gate for settled decisions. Other design skills and the upstream `codebase-design` vocabulary are optional aids, not prerequisites.
