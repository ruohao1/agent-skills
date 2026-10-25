# Shared personal instructions and next-action observations

## Agreed behavior

Use one instruction source for the personal preset. The three existing host instruction templates were identical. `configs/personal/AGENTS.md` now supplies Codex, Claude Code, and OpenCode; setup chooses the destination filename. Native reviewer definitions remain separate because their formats differ.

After any kind of completed task, suggest one concrete next action toward the user's current goal, with a brief reason, only when useful. Use available context, finish requested work first, and leave the suggested action for the user to choose. This is a preset requirement.

## Behavioral checks

Five fresh-context control agents received the previous personal instructions. Five separate fresh-context guided agents received the shared source with the new next-action bullet. Each received the same five independent [task scenarios](../fixtures/personal-preferences.md), without the criteria, prior outputs, or results. No model override was used. Every response was read manually.

The control source contained the five existing preference bullets under `Personal coding preferences`. The candidate retains those bullets, changes the heading to `Personal preferences`, and adds the next-action bullet. To repeat the comparison, use those two instruction variants with the supplied scenarios and request each case's user-facing response and proposed operations.

| Observed behavior | Control | Guided |
| --- | --- | --- |
| Draft invitation includes a recommendation to obtain the required team-lead approval | 0/5 | 5/5 |
| Completed code fix explicitly recommends a PR for review and release | 0/5 | 5/5 |
| Research answer prioritizes Continue-button visibility as the first prototype | 5/5 | 5/5 |
| Spelling-only answer contains just the corrected sentence | 5/5 | 5/5 |
| Unfinished save remains current work, with no completion claim | 5/5 | 5/5 |
| Suggested email or Git operations are not performed | 5/5 | 5/5 |

All controls wrote the requested invitation but omitted the approval recommendation. Guided responses added one short next action; for example, guided 1 wrote: “Next: share this draft with the team lead for approval before sending.”

Three controls stopped the coding response after reporting the local fix and tests. The other two mentioned the outstanding PR/release prerequisite as status, without an explicit recommendation. Guided 1 wrote: “Next: open a pull request so the team can review the fix for release.” All guided coding responses left Git operations unperformed.

Both arms already prioritized the most common interview problem. Controls also included recommendations about the company-name field and confirmation screen within their summaries. Guided responses used three summary bullets followed by one next action, with a reason tied to the supplied evidence. This supports the requested response shape, not a claim that the underlying research judgment improved.

Both arms returned only “The meeting starts tomorrow.” for the constrained spelling request. In the unfinished case, both proposed saving the already-drafted invitation as current work and withheld a final completion response. These are retained baseline strengths.

The scenarios are synthetic, and operations are proposed rather than executed. File access was restricted to the assigned material, so this does not independently demonstrate suppression of unnecessary investigation in an unrestricted session. These results do not establish native-host compliance or reliability across arbitrary tasks.

## Installation and validation

- The shared-source regression test first failed for global and project installation because setup still requested the deleted per-host source path. It passed after changing the source lookup and destination filename mapping.
- `python3 -m unittest discover -s tests -v`: all 65 tests passed.
- `python3 scripts/validate_marketplace.py`: passed for two catalogs, two plugins, three skills, and one preset. The validator reuses the updated source loader; its tests reject empty shared instructions and source installation markers.
- Real `scripts/setup.py` subprocesses ran for all three hosts in disposable global and project environments. Fresh installations and installations over existing instructions passed, as did repeats with unchanged bytes, modification times, and modes. Existing instruction bytes and backup modes were preserved; previews wrote nothing.
- An older installed personal block produced a conflict in both scopes, including with `--yes`. All original files stayed unchanged. Source consolidation does not bypass the existing preservation rules.
- The probe used isolated home, configuration, cache, data, state, and project paths.

Native host loading and authenticated agent execution were not retested.
