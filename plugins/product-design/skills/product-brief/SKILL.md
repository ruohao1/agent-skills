---
name: product-brief
description: Use when a product request needs a clear user problem, bounded scope, consequential states, and observable success criteria before design or implementation.
---

# Product brief

Use ASD-STE100-inspired principles for English prose written for people. Write short, complete sentences with one main idea. Give clear instructions and put necessary conditions before their actions. Prefer active voice, simple verbs, and consistent terms. Keep related ideas connected. Preserve facts, evidence, uncertainty, and required technical detail. Reproduce code, commands, identifiers, paths, URLs, and source quotations exactly. Apply the principles for clarity; do not enforce the full STE dictionary or claim formal compliance.

Make the next product decision possible. Read supplied evidence and relevant project vocabulary. Preserve the requested output: a correction to an existing brief needs a correction, not renewed discovery. Save a document only when requested or required by the project's workflow.

Build the brief around the user's task, its trigger, the obstacle, and the observable outcome. A proposed feature is one possible solution, not evidence of a problem. Attribute observations to their source; distinguish known constraints, working assumptions, and proposed behavior. Sparse evidence should produce a testable hypothesis, not invented consensus.

Describe the entry, completion signal, and states that change what the person can safely do. For asynchronous work, separate submission, acknowledgement, and the authoritative outcome. Interrupted connectivity may leave the outcome unknown; explain recovery without assuming retry safety, permissions, or execution guarantees the supplied contract does not establish.

Give scope and a few acceptance scenarios proportional to the request. Assess whether each proposed measure captures the user outcome or merely an intermediate event. Label targets as proposals when no baseline exists.

For unresolved decisions, state the consequence of deferring each one:

- **Blocks a particular decision:** name the behavior that cannot be specified or implemented until the answer is known.
- **Can proceed in parallel:** name the assumption or learning step and when its answer becomes necessary.

For example, unknown expiry semantics can block the approval transition; an unknown usage baseline may permit that design while measurement proceeds. Do not treat every unknown as a delivery gate or invent an owner. Ask only questions whose answers change the current task; otherwise carry the uncertainty explicitly.

End with the next decision or handoff needed. A brief does not authorize implementation or external updates and does not require another skill.
