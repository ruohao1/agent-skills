---
name: design-product
description: Use when a selected product change needs its user flows, interactions, states, recovery, or visual experience designed, or when an existing product design needs updating.
---

# Design product

Resolve how the selected change behaves for its users. Reuse an adequate brief and settled decisions; a design request need not restart discovery. Work independently of architecture or code design unless a consequential dependency needs resolution. An audit discovers problems; this workflow designs selected work.

Read the relevant brief, existing experience and UI patterns, and authoritative behavior contracts. Ground decisions in that evidence. Define the user's entry, actions, meaningful states, and observable completion. For each consequential state, explain what the user sees, can do, and can safely conclude. Treat acknowledgement, completion, partial results, and an unknown outcome according to the supplied contract. Each recovery action states its safety preconditions. Preserve any identity and payload requirements; when those inputs are missing, status lookup alone does not authorize a fresh submission. A desired interaction does not establish backend support.

Compare alternatives when they change the experience meaningfully. Recommend an approach; ask when a choice changes scope, user behavior, significant cost, or an expensive commitment. Make routine, reversible choices and state material assumptions. If a missing capability blocks one interaction, identify that dependency and continue independent design. Reuse established visual patterns; a mockup or disposable prototype is useful when it resolves a choice.

## Save the handoff

Lead with the chosen approach. Put each constraint beside the flow or state it governs, then finish with focused acceptance scenarios and unresolved dependencies. Reference established context instead of restating it. Each decision appears once. For a small feature, aim for 300–500 words including a compact state table; expand when consequential behavior needs more detail. A focused correction changes the requested decision without regenerating the full design.

Use short, complete sentences and verified source references. Distinguish existing facts, proposals, and checks actually run. Keep private project details out of public artifacts.

Honor an explicit destination, existing document, or text-only request. Otherwise, update the relevant design document or save `docs/designs/<topic>.md` in the target repository. Inspect an existing file before editing; preserve valid decisions and unrelated sections. Use one document for a coherent change, sharing relevant sections with other design scopes. Do not overwrite an unrelated file or create a duplicate report.

Read back the saved document. Reply with its link, a brief decision summary, and material limits; the full design belongs in the document. If saving fails, return the unsaved design and explain the failure.

Keep the design available for the related implementation unless instructed otherwise; do not add ignore rules, stage, commit, or publish as a side effect of designing. A design request does not authorize production changes. An explicit implementation request retains its scope; do not insert another design gate for decisions already settled. Optional diagram, prototype, or brief tools are aids, not required companion skills.
