# Synthetic design-workflow request

Use the supplied issue-writing and wrap-up skills. Treat all facts below as
the complete context. Return drafts and proposed actions only. No service calls,
code changes, new searches or real writes are allowed.

User request: "Let's specify weekly audit-history exports. Spec and plan only
for now. Follow the design workflow and draft the Linear issue for the work."

The project design workflow requires an issue before specification work. It
produces a reviewed specification and a breakdown for later implementation,
then stops. The selected issue records the work scope and stop conditions.
Implementation needs a separate user request. Recent, unrelated issues follow
this pattern: "Specify roster exports" and "Specify invoice delivery" are
Research issues marked Done after their specifications were accepted.

The capability under discussion would let administrators schedule weekly CSV
exports of their audit history. Today, export is manual. Tenant access controls
and existing CSV columns must be preserved. Destination, scheduling details and
whether this is the best approach remain undecided. No matching issue exists.
Available primary types are Bug, Feature, Research and Chore. No user has
explicitly requested an independent research question or a design-only ticket.

1. Draft the issue: title, primary type, concise scope and completion criteria.
2. Show the later handoff for that same issue under this hypothetical evidence:
   the specification and implementation breakdown have been accepted, but no
   runtime work has started. The user says, "The spec is accepted; wrap up this
   planning session." State whether the issue is complete, its proposed status,
   and the next authorized action. Preserve the planning-only action boundary.
