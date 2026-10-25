# Linear Workflows

Each skill includes STE-inspired writing guidance for clear English prose. It preserves technical detail without enforcing the full ASD-STE100 dictionary or claiming formal compliance. No personal preset is required. See the [writing evaluation](../../evals/results/2026-10-24-ste-writing.md).

Version **0.4.3** contains three skills for a person and a coding agent:

- [write-linear-issue](skills/write-linear-issue/SKILL.md) writes concise context, scope, and observable acceptance criteria using Bug, Feature, Research, and Chore skeletons. It selects one primary purpose, researches available facts, improves matching issues, links distinct work, and maps to the destination's existing labels.
- [write-linear-comment](skills/write-linear-comment/SKILL.md) writes requested progress, blocker/question, decision, and completion/handoff comments. Research updates tell the story through short, consequential discoveries in the relevant thread. Code references use verified commit permalinks and exact line ranges; code-dependent comments remain drafts until those links exist.
- [wrap-up-linear-issue](skills/wrap-up-linear-issue/SKILL.md) runs before an agent moves an issue to Done or its team's equivalent completed state. It saves and verifies a short TL;DR at the top of the description, linking decisive comments and preserving the original task, then makes the authorized status change. No separate wrap-up request is needed. It also handles requested summaries of already-completed work without changing status.

Writing includes saving to Linear. Issue context uses short factual bullets; each requirement appears once, combining scope and acceptance when they overlap. Verified plans hold implementation detail; essential constraints stay in the issue. Explicit draft-only requests and narrow corrections keep their requested scope; idea capture can remain exploratory. Issue pointers describe verified facts, while implementation choices remain open unless already decided. Comments distinguish completed work, actual verification, and unresolved decisions. Posting comments requires a comment request. Requested requirement changes belong to issue writing; the final outcome belongs to wrap-up.

The wrap-up skill's description supplies the completion trigger; no personal preset or AGENTS.md change is needed. Incomplete required work or an unconfirmed summary save leaves status unchanged. An existing accurate summary is reused. This is skill guidance, not a server-side Linear status restriction; it does not intercept manual status changes or start updates when unrelated local tasks finish.

The issue skill defaults to one workspace-wide, single-select Type group with those four types. New issues are assigned to the invoking user unless another assignee or unassigned is requested; edits preserve existing ownership unless reassignment is requested. Required team templates take precedence. Research can close with documented inconclusive findings; bugs do not require a known cause before capture. Writing issues does not migrate labels or create native Linear templates.

Connect Linear in your agent with the access needed for the selected skill: read issues and discussion, create/reply/edit comments, or read teams/projects/labels, create/update issues, and link related work. This package supplies instructions, not a connector, credentials, or a team/project selection. Without a connection, the skills return unsaved drafts. Triage, roadmap planning, and backlog cleanup are outside this plugin.

From this checkout:

```sh
python3 scripts/setup.py install --skill write-linear-issue write-linear-comment wrap-up-linear-issue --agent codex --scope global
```

The shared repository route is:

```sh
npx skills@latest add ruohao1/agent-skills --skill write-linear-issue write-linear-comment wrap-up-linear-issue --agent codex claude-code opencode
```

Choose any skill independently by listing only its name. Examples: “Write an issue for this change,” “Post the verified research findings,” or “Finish this issue and move it to Done.” For the complete native bundle on Codex or Claude Code, select `--plugin linear-workflows --route native`. See [setup](../../docs/setup.md) for supported scopes and existing-installation handling. Choose one installation route to avoid duplicate skill copies.

See the [issue evaluation](../../evals/write-linear-issue.md), [issue results](../../evals/results/2026-10-21-write-linear-issue.md), and [type skeleton results](../../evals/results/2026-10-23-write-linear-issue-types.md), plus the [comment evaluation](../../evals/write-linear-comment.md) and [comment results](../../evals/results/2026-10-21-write-linear-comment.md), for observed differences and verification limits. The type skeletons record the user's chosen defaults; the baseline already handled the evaluated examples correctly.

The [research and wrap-up evaluation](../../evals/linear-wrap-up.md) and [results](../../evals/results/2026-10-23-linear-wrap-up.md) cover concise research threads, summary preservation, and the automatic trigger before completion.

The [assignment results](../../evals/results/2026-10-23-write-linear-issue-assignment.md) cover the invoking-user default, explicit overrides, and preservation of existing ownership.

The [concision results](../../evals/results/2026-10-24-write-linear-issue-concision.md) cover Context bullets, removal of repeated scope, and preservation of requirements when supporting plans are unavailable.
