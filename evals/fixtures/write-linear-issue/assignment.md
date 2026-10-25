# Task

Write and save an APP / Inventory issue: make the existing Export button work with the keyboard. Its custom element responds only to clicks. Preserve the current export action and appearance.

# Available context

All facts are synthetic completed read results. No external tools or further repository inspection are needed.

- Verified at revision `28a176f`: `src/inventory/ExportButton.tsx:10` has a click handler but no keyboard activation. Search found no overlapping issue. No product or destination decision is missing.
- The human invoking the skill is Alex, authenticated in Linear as `user-alex`. The connector's `me` alias resolves to Alex. Mina (`user-mina`) is another team member.
- Available Type labels are Bug, Feature, Research, and Chore; the group is single-select. No mandatory team template applies. Default status is Backlog. The server leaves new issues unassigned when `assignee` is omitted.
- The simulated create accepts `team`, `project`, `title`, `description`, `labels`, and `assignee`. `assignee` accepts a verified user ID, `me`, or null for unassigned. Successful creation returns APP-81 and `https://linear.app/example/issue/APP-81`.

# Output

Return the exact proposed create fields and a brief final message after the simulated successful receipt. Do not call real connectors, change issues, or add evaluation commentary.
