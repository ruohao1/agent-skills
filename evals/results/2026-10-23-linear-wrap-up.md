# Linear research comments and completion wrap-up

## Shipped behavior

Linear Workflows 0.4.0 adds `wrap-up-linear-issue` and concise research-story guidance to `write-linear-comment`. The wrap-up skill's description triggers before an agent moves an issue to Done or its team's equivalent completed state. A separate wrap-up request is unnecessary: verify required work, save and verify the summary, then make and verify the authorized status transition. A failed or uncertain summary save leaves status unchanged. The final guidance omits the prototype shared-instruction trigger; the personal preset and AGENTS.md remain unchanged.

The final TL;DR sits at the top of the description and links decisive existing comments. The original task remains underneath. Research comments carry the discoveries and their implications; issue writing continues to define the work. The existing 0.3.0 issue-type guidance was preserved byte for byte. No installer runtime or native reviewer definition changed.

## Method

Followed the [evaluation criteria](../linear-wrap-up.md) with synthetic issues, source references, connector reads, and save results. Five fresh controls used the previous issue/comment skills for the [completed research](../fixtures/linear-wrap-up/completed.md) and [research story](../fixtures/linear-wrap-up/story.md) tasks. Five separate controls used the previous shared preferences and skills for [closing an issue](../fixtures/linear-wrap-up/closing.md), whose request never mentions a summary.

Five fresh guided agents performed all three tasks with the revised skills and the prototype shared-instruction trigger. These combined-guidance results do not isolate automatic skill discovery. The separate discovery check below used the unchanged final skill without that trigger. Two earlier guided samples used an earlier trigger requirement and are excluded from the comparison. Agents received only their assigned guidance and fixtures, without criteria, plans, unrelated issue history, or other outputs. No model override was used. Every output was read manually.

## Main observations

| Behavior | Existing guidance | Revised skills with prototype shared trigger |
| --- | --- | --- |
| Short final TL;DR first, linking existing research comments | 0/5 | 5/5 |
| Original research task and unrelated metadata preserved | 5/5 | 5/5 |
| Research divided into concise discovery paragraphs, in recorded order | Four long single comments; one set of three longer replies | 5/5; three or four comments |
| Summary saved and verified before an authorized Done transition, without a summary request | 0/5 | 5/5 |
| Closure leaves unrelated fields intact and avoids duplicate completion comments | 5/5 | 5/5 |

Controls wrote detailed research reports into the description: two inserted the report after Context, two appended it, and one placed it first. The last therefore met top placement, but still produced a report rather than a short navigation summary. Controls already omitted unrelated CLI/package trivia, used relevant threads, and distinguished source research from live extraction; those are preserved strengths, not new gains.

The five guided TL;DRs were 81–129 whitespace-delimited words including headings and Markdown links. They linked existing findings, retained source-only uncertainty, and proposed the separate same-video comparison. Original description suffixes also matched programmatic byte comparisons. No live experiment was presented as performed or required to finish the source-only issue.

Every closure control proposed a direct state update. For example, control 1's only mutation was `save_issue({id: "APP-90", state: "state-done"})`. Every guided closure proposed the same dependency order: description save, issue read-back, state save conditional on the verified summary, and final read-back. None requested separate permission for the wrap-up.

## Link correction and comment regressions

One initial guided research response accidentally lengthened a supplied commit hash in its runtime-source URL. The research structure was correct, but that permalink was not. Added the narrow instruction: “Copy verified permalinks exactly into the final body.” Five further fresh contexts ran the story fixture with the final comment skill alone. All five used four short comments, retained exact supplied source URLs, omitted irrelevant activity, and preserved comment-only scope. The longest comment in each sample was 84–88 whitespace-delimited words. They grouped discovery and retrieval in the original thread, then opened a comparison thread with a follow-up experiment reply.

These additional samples check the final wording; they do not establish that the added sentence alone eliminates URL transcription errors. Source inspection and final-link verification remain necessary.

The existing comment [primary](../fixtures/write-linear-comment/primary.md) and [focused](../fixtures/write-linear-comment/focused.md) regressions passed in a fresh context: a published implementation was quoted with its exact immutable source; local unpublished code remained an unsaved draft; duplicate comments were reused; a one-sentence edit preserved the rest; prose-only blockers and decisions were saved without changing issue requirements; explicit drafts and disconnected requests remained unsaved; a timed-out reply triggered a read before retry; a local coding task triggered no external mutation.

## Completion and preservation cases

Both the previous guidance and the final skill handled all nine [requested-wrap-up cases](../fixtures/linear-wrap-up/focused.md): equivalent-summary reuse, replacing only a stale summary, incomplete acceptance despite Done status, draft-only and comment-only scope, ambiguous saves, absent access, unpublished requested code evidence, and paginated discussion. No improvement is claimed for boundaries the controls already respected.

The final guidance also passed the six [completion cases](../fixtures/linear-wrap-up/closing-focused.md) with the skill available: reuse a saved summary before closing; leave status unchanged after a definite summary-save failure; read after a timeout before deciding on closure; do not close incomplete work; honor local-only scope; and use the team's Resolved state rather than assuming a state named Done.

An agent shown only the three Linear skill descriptions selected `wrap-up-linear-issue` for the ordinary closure request, then followed the summary-before-status order using that skill without the personal preset. This directly checks the final skill-only route, but one synthetic discovery case does not prove native host invocation reliability. A separate prototype preset-fallback check was also run; that fallback was removed with the redundant AGENTS.md instruction and is not part of the shipped behavior.

## Packaging and installation

- The curated catalog now contains 17 skills, including all three Linear Workflows skills. Both plugin manifests declare 0.4.0 and matching shared metadata. The two native marketplace catalogs and their plugin ordering are unchanged.
- `python3 -m unittest discover -s tests -v`: all 65 tests passed.
- Skill creator `quick_validate.py`: both changed/new skills passed.
- `python3 scripts/validate_marketplace.py`: passed with 2 catalogs, 3 plugins, 5 packaged skills, and 1 preset. Registration resolves the temporary catalog mismatch noted in the earlier issue-type work.
- Cached Skills CLI 1.7.2 discovered all five packaged skills. Direct local installs of the new wrap-up skill and revised comment skill succeeded at project and global scope for Codex, Claude Code, and OpenCode. Each selected installed file matched its source; an existing issue skill and unrelated skill were preserved; unselected skills were not installed; repeats retained identical content.
- The CLI uses shared `.agents/skills` for Codex/OpenCode and `.claude/skills` for Claude Code. An initial smoke assertion incorrectly expected an additional OpenCode-specific copy; the install log and existing inventory helper confirmed the shared destination. The corrected smoke check passed without an installer change.
- The prototype's preset-installation smoke check also preserved existing instructions and backups. That preset change was subsequently removed; no preset update is needed to use the wrap-up skill.

The fixtures, criteria, and observations above record the reproducible cases. Raw responses and installer logs are not distributed.

## Limits

No live Linear writes, installed personal-agent changes, source publication, or authenticated host conversations were performed. Native marketplace activation, real Linear concurrency, and server permissions remain untested. This is agent guidance, not a Linear server-side restriction on manual status changes. Five samples per main variant demonstrate the observed behavior, not a reliability guarantee.
