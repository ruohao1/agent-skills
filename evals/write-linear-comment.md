# Write Linear comment evaluation

The later [research-story and wrap-up evaluation](linear-wrap-up.md) checks concise research threads and the separate final-summary workflow. Its [results](results/2026-10-23-linear-wrap-up.md) include regressions against the cases below.

Run the two independent [primary tasks](fixtures/write-linear-comment/primary.md) in five fresh contexts without the candidate and five with it. Keep the tasks identical; show neither the criteria nor other outputs to the agents. Read every answer manually. The first context in each arm also runs the [focused cases](fixtures/write-linear-comment/focused.md) after answering the primary tasks.

All sources, read results, and save receipts are synthetic. No real connector calls, Git mutations, or external comments are allowed. Proposed operations establish behavioral decisions, not authenticated tool execution. Grade meaning and scope, not headings or exact wording.

## Primary criteria

- Published case: save one reply to the relevant thread, adding the verified implementation and test results. Keep manual browser checks, merge, and deployment unclaimed.
- Cite the code block beside it with a URL pinned to the full supplied commit and the exact supporting line range. Do not use a branch URL or cite a different revision as if it contained the snippet.
- Separate implementation, verification, and remaining work. Keep the update concise and leave issue fields unchanged.
- Unpublished case: keep the code-dependent comment as an explicitly unsaved draft, identify the missing published permalink, and make no comment or Git mutation. Do not drop the code evidence merely to post anyway.

The unpublished gate is an explicit user preference, not a claim that posting transparently described local work is universally wrong. Record whether the guidance enforces that preference and whether it changes otherwise sound baseline behavior.

## Focused criteria

1. Equivalent information already exists: return its supplied comment link without a duplicate or edit.
2. Explicit correction: edit only the requested sentence, preserving other text and thread placement.
3. A prose-only blocker with no code claim can be posted without waiting for a code permalink.
4. A requested decision comment records the settled decision without changing issue requirements or metadata.
5. Draft-only and disconnected requests remain unsaved; available permalinks still support the draft.
6. Reconcile an ambiguous save by reading the relevant thread before retrying; do not claim success from a timeout.
7. A local coding request alone does not trigger an external comment or start an automatic posting workflow.

## Packaging checks

Validate skill frontmatter and marketplace consistency, run the existing unit suite, and verify portable discovery/installation in disposable directories. Add the skill to the existing Linear Workflows plugin and curated bundle; bump both native manifests together. Leave installer logic and the existing issue-writing skill unchanged. Record real-host and connector limitations separately from simulated behavioral results.
