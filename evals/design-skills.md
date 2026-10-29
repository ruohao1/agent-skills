# Design skill evaluation

Use anonymous synthetic cases in [primary fixtures](fixtures/design-skills/primary.json) and [focused cases](fixtures/design-skills/focused.json). Freeze fixtures before baseline runs. Keep raw responses, snapshots, host details, and tool transcripts outside the repository.

## Method

Run five fresh baseline contexts with the existing relevant skill descriptions and resources. Each performs the three independent primary cases in separate disposable projects. Record selected skills and intended actions before loading skill bodies. Complete each requested design with the supplied project files and local artifact tools. Do not force a particular skill or output path.

Evaluate each justified candidate separately with five fresh contexts on the same three-case sequence. Only add that candidate to the frozen existing-guidance bundle. Score its intended case and inspect routing and scope in the other two. Do not supply this protocol, the design specification, expected answers, earlier responses, or other candidates. Keep model selection, user preferences, task wording, word budget, and permitted tools the same. The three primary cases are independent tasks within each context, not separate model samples.

Read every response and saved artifact manually. Record failures before writing candidate guidance. Compare the following behaviors without inferring general success rates from a small sample:

- Product: reuse the approved brief; separate acceptance from authoritative completion; handle unknown and partial outcomes within the actual retry contract; specify useful interaction states without inventing server behavior.
- Architecture: choose justified responsibilities, data ownership, recovery, idempotency, account authorization, and rollout; keep alternatives proportional and avoid invented capacity measurements.
- Code: resolve module ownership and interface; preserve rounding, errors, and public caller signatures; cover all three callers and meaningful verification without a broad audit or unnecessary abstractions.
- Delivery: leave a usable, concise design artifact; distinguish persistence from the preferred `docs/designs/` convention; include verified source references; link the saved artifact without repeating it in chat.
- Authority: preserve source and unrelated files; do not implement, commit, publish, or introduce dependencies.

Run the independent focused cases with the existing bundle and with the final candidates. These are simulated selection/action checks; they do not establish actual host activation, file preservation, or failure recovery.

Also check the three primary requests against the combined final descriptions before loading bodies. Record this single selection-only check separately from the executed primary comparisons.

Add fresh filesystem checks for document updates, alternate destinations, text-only output, and standalone use without companion skills. Inspect inventories and bytes. Validate fixtures themselves, including the pricing rounding example. Report any untested cases.

The [product delivery cases](fixtures/design-skills/delivery.json) and [technical delivery cases](fixtures/design-skills/technical-delivery.json) seed an existing index, unrelated notes, and documents with protected sections. These checks use explicit invocation without an external word limit. Keep them separate from the matched discovery comparisons.

## Shipping criteria

A candidate must improve an observed gap while preserving the baseline's substantive strengths and requested scope. A delivery-only improvement is reported as such. Omit a candidate when existing guidance already meets the need. Keep synthetic examples and measured results versioned, with technical limitations and no personal context.

Run skill validation, the 73-test repository suite, marketplace validation, and portable discovery/install/repeat checks in disposable environments for Codex, Claude Code, and OpenCode. Native activation and real authenticated service behavior require separate evidence.
