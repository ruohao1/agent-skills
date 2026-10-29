# Design skills

Status: Implemented and verified. All three candidates met the criteria below; see the [evaluation results](../../evals/results/2026-10-25-design-skills.md). Keep this design with the implementation PR. Active installation remains separate follow-up work.

## Purpose and scope

Help a person and a coding agent resolve consequential design decisions before production changes. Support new projects and changes to existing systems. Keep each scope independently usable and scale the output to the requested change.

| Scope | Decisions it owns |
| --- | --- |
| Product brief | User problem, evidence, scope, constraints, and observable success criteria. Keep the existing skill. |
| Product design | User workflows, rules, interactions, error and recovery states, and relevant visual presentation. |
| Architecture design | System responsibilities, data ownership, interactions, and runtime constraints, including within one application. |
| Code design | Modules, interfaces, dependencies, and file/folder organization. |

The scopes share context. Each decision has one primary home; other scopes reference it. Reuse an adequate brief, including its consequential states and acceptance scenarios. Screens, diagrams, and prototypes support decisions when useful; they do not define separate design responsibilities.

## Agreed working rules

- Read supplied evidence and relevant project context first. For existing systems, inspect the implementation, callers, and recorded decisions. Explain why a structural change is needed and preserve valid constraints.
- Use each scope independently. Bring in another scope when a consequential dependency requires its decisions. Avoid a fixed sequence or three required documents.
- Resolve consequential behavior, contracts, responsibilities, and dependencies. Include compatibility and migration implications when relevant. Leave ordinary implementation choices open.
- Compare meaningful alternatives and recommend an approach. Ask when a choice changes scope, user behavior, significant cost, or a commitment that is expensive to reverse. Make routine, reversible decisions autonomously and state material assumptions.
- Keep observations, assumptions, proposals, and settled decisions distinct. An unresolved decision blocks only the work that depends on it.
- Allow a conclusion that the existing architecture or code structure is sufficient.

## Audit boundary

Audits discover and prioritize supported problems. Their existing recommendations can include specific refactors, preserved contracts, caller migrations, and checks.

Design resolves consequential choices for a selected improvement or a new capability. For work discovered by an audit, use a separate design step only when such choices remain or a design document is explicitly requested. Reuse the finding and evidence. A straightforward fix can proceed directly to requested implementation. A new capability can enter design without an audit.

For example, an audit can identify a duplicated rule and recommend centralizing it. Code design settles its ownership, interface, and caller migration only if those choices remain open. Focused inspection during design does not require a repository-wide audit. Existing audit behavior does not need to change.

## Output and authority

Save a concise design by default. Update a relevant existing document when possible. Use `docs/designs/<topic>.md` unless the request or applicable project instructions specify another location. Keep one document per coherent change, with only the relevant sections; separate documents when scopes evolve independently. Commit designs with the related implementation unless instructed otherwise. A design request alone does not authorize a commit, publication, or production changes.

Capture the chosen approach, meaningful alternatives, constraints, and unresolved decisions. Include verified code pointers and diagrams or prototypes when they help resolve the design. Use synthetic data in examples. Keep private project details out of public artifacts.

The default handoff stops before production changes. Implementation remains a separate requested action. Prototypes remain disposable and clearly identified; they do not become production code through the design workflow.

## Implementation proposals

These are implementation recommendations, not additional requirements supplied by the user:

- Candidate names: `design-product`, `design-architecture`, and `design-code`.
- Reuse the curated `prototype`, `archify`, `codebase-design`, and `domain-modeling` capabilities where useful. Evaluate the existing guidance before adding custom instructions. Do not vendor unchanged upstream skills.
- Keep any new skill self-contained. Optional helper skills can improve an artifact; they are not mandatory prerequisites.
- Package a justified `design-product` in the existing Product Design plugin. Package justified architecture/code skills in a `software-design` plugin. Create no empty bundle if candidates add no demonstrated value.
- Keep all existing public skills and installation routes compatible. Update catalogs, paired manifests, documentation, and the changelog only for candidates that ship.

## Approaches and tradeoffs

The agreed approach separates decision scopes. It permits a focused design request and a shared document for a change that crosses scopes. Its cost is that instructions must make ownership and handoffs explicit.

A single broad design skill would offer one entry point, but make it harder to keep a narrow request focused. Dividing skills by artifact, such as diagrams or wireframes, would duplicate capabilities already curated and would not establish who owns the underlying decision. The proposed names and packaging remain reversible choices.

## Evaluation and completion

Use anonymous synthetic cases and matched fresh baseline/candidate runs. Baselines receive the existing relevant guidance. Record skill selection separately from execution, inspect every response, and retain observed counts and limitations. Keep raw transcripts and host details outside the repository. Ship only candidates that demonstrate useful improvement.

Cover these cases:

- Product behavior with asynchronous completion, uncertain outcomes, and recovery; reuse an adequate brief.
- Architecture for a new capability where the existing application may suffice; state data ownership and runtime constraints.
- Code design for a selected audit finding with existing callers and migration constraints.
- An adequate audit recommendation that needs no further design, plus an explicit request to document an already chosen approach.
- A narrow request, a material cross-scope conflict, and an unresolved fact that affects only part of the design.
- Document updates, an alternate output location, and explicit text-only or implementation requests that override the default scope.

Successful guidance produces a bounded, usable handoff without unsupported facts, invented requirements, redundant discovery, or unauthorized production changes. The implementation must pass the repository's unit, marketplace, and skill validation checks. Check discovery and repeatable portable installation in disposable Codex, Claude Code, and OpenCode environments. Report native activation or authenticated behavior that remains untested.
