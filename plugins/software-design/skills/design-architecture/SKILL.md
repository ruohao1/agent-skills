---
name: design-architecture
description: Use when a selected change needs system responsibilities, data ownership, runtime interactions, or deployment boundaries designed, or when an existing architecture design needs updating.
---

# Design architecture

Resolve consequential system choices for selected work. Reuse settled product requirements and decisions; keep this workflow usable without another design skill. An audit discovers and prioritizes problems. Use its evidence when relevant, and design only unresolved choices or an explicitly requested document.

Read the affected execution paths, interfaces, data stores, deployment constraints, and recorded decisions. Distinguish what exists from what is proposed. Reusing a mechanism does not establish its policies or guarantees for new work: verify the applicable contract, or state the assumption or unresolved decision. Do not infer retention, authorization, recovery, or capacity guarantees from a helper's existence.

Choose the smallest arrangement that meets the actual constraints. The existing application or process may already suffice. Explain any new process, storage, or coordination requirement. Describe who owns state and decisions, the important interactions, and the outcome each interface establishes. Cover retries, interrupted work, competing operations, and failure recovery when the selected behavior depends on them. Identify the authority that makes state transitions or publication valid.

Compare meaningful alternatives and recommend one. Ask when a choice changes scope, user behavior, significant cost, or an expensive commitment. Make routine, reversible decisions and state material assumptions. Unknown workload measurements remain unknown; initial limits are proposals. Keep unaffected decisions moving while a consequential dependency is unresolved. Leave ordinary implementation details to the builder.

## Save the handoff

Lead with the chosen approach. Add a compact responsibility/data-flow description and the contracts that make it work. Include compatibility or migration implications, meaningful alternatives, verification needs, and remaining decisions where relevant. Put each decision once and reference established context. For a small change, aim for 300–500 words; expand when consequential behavior needs more detail. A focused correction preserves the rest of the design.

Use short, complete sentences and verified source references. Distinguish source inspection from executed checks. Keep private project details out of public artifacts.

Honor an explicit destination, existing document, or text-only request. Otherwise, update the relevant design or save `docs/designs/<topic>.md` in the target repository. Read existing content first; preserve valid decisions and unrelated sections. Share one document across the relevant scopes of a coherent change. Avoid duplicate designs or overwriting unrelated files.

Read back the saved document. Return its link, a short decision summary, and material limits. If saving fails, return the unsaved design with the reason.

Keep the design available for related implementation unless instructed otherwise. Designing alone does not authorize production changes, ignore edits, staging, commits, or publication. Honor an explicit implementation request without inserting a design gate for settled decisions. Diagrams and other design skills are optional aids, not prerequisites.
