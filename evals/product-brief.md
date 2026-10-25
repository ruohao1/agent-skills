# Product brief evaluation

Use synthetic tasks below without the candidate skill, then with it. Keep the task inputs identical. Evaluate decisions and usefulness, not prescribed headings. Report observations rather than a statistical performance claim.

## Tasks

1. **Primary — incomplete approval evidence.** We need an engineering-ready brief in the next ten minutes, without an interview. Internal operators approve scheduled maintenance requests. Requests expire after ten minutes. The API returns 202 when it accepts the approval, but execution may later fail. Two support quotes: “I clicked twice because nothing happened” and “After reconnecting I couldn't tell whether to retry.” The dashboard's proposed success metric is approvals per day, currently counted from 202 responses. Permissions, volumes, and escalation ownership are unspecified. Write a brief in at most 250 words; do not implement anything.
2. **Small correction.** A complete existing brief says “Completed means the API accepted the request.” The confirmed backend contract says only a terminal `succeeded` event establishes completion. Correct that sentence only.
3. **Weak evidence.** One colleague prefers a new activity graph; there is no user research or usage data. Draft the problem statement and a checkable next learning step without calling the preference validated demand.
4. **Consequential state.** A mobile requester loses connectivity after submitting a maintenance request. The server outcome is unknown. Specify the observable behavior and one acceptance check without promising exactly-once execution or choosing backend implementation.
5. **Scope control.** The user supplies a complete approved brief and asks only for a two-sentence engineering handoff. Produce that handoff without restarting discovery or mandating another skill.

## Criteria

- Primary: distinguishes evidence, assumptions, and unresolved decisions; keeps the actual operator task and scope clear.
- Primary: 202 is acknowledgement, not the completed user outcome; the proposed metric is assessed against that distinction.
- Primary: covers expiry, interrupted connectivity, duplicate intent, failure/recovery, and measurable acceptance without inventing permission or retry guarantees.
- Primary: identifies which unresolved decisions block implementation versus can be investigated while work proceeds.
- Other cases: obey the narrow requested output and scope; avoid unnecessary interviews, files, workflows, or implementation decisions.
