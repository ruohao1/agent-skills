# Independent tasks

These cases are synthetic. Use only the supplied facts. Do not call real connectors or change real issues. Return the proposed mutation, or the next necessary question. Omitted update fields remain unchanged. The `assignee` field accepts a verified user ID, the authenticated current-user alias `me`, or null for unassigned.

Alex (`user-alex`) is the human invoking the skill. Except in case 5, authenticated `me` resolves to Alex. Mina (`user-mina`) is another verified team member. All new issues target APP / Inventory and have no overlap or missing scope decision. The Type group contains Bug, Feature, Research, and Chore. No mandatory template applies.

## 1. Explicit assignee

User: Create an issue to fix keyboard activation of the existing Export button and assign it to Mina. Keep its appearance and action unchanged.

Verified: `src/inventory/ExportButton.tsx:10` responds only to clicks. The caller and Mina are distinct users.

## 2. Explicitly unassigned

User: Create the same keyboard fix issue, but leave it unassigned.

The server has a default team owner for new issues; an explicit null overrides that default.

## 3. Edit an assigned issue

User: In APP-60, change only “Done when clicked” to “Done when activated by pointer or keyboard”, and save it.

APP-60: title "Activate the Export button"; description "Context: Export runs an existing action.\n\nDone when clicked." Assignee: Mina (`user-mina`). State: Started. Labels: Bug. All other fields must be preserved.

## 4. Edit an unassigned issue

Same requested sentence correction and issue as case 3, but the existing assignee is null.

## 5. Caller identity unresolved

User: Create the keyboard fix issue from case 1, with no explicit assignment instruction.

The session identifies the human as Alex, but no verified Linear account mapping exists. The connector's `me` alias resolves to an integration account, `app-automation`. Available identity lookups found two active users named Alex and cannot distinguish them. All other issue details are resolved.

## 6. Explicit reassignment

User: Assign APP-60 to me; change nothing else.

APP-60 is currently assigned to Mina. Authenticated `me` resolves to Alex.
