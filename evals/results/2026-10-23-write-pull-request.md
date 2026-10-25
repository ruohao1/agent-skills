# Pull request privacy and publication checks

## Publication policy

PR descriptions need explicit publication boundaries as well as branch names and commit messages. The evaluated policy keeps internal tracking references out of public PR content.

Git Workflows 0.2.0 adds `write-pull-request`. Its description applies to creating, drafting, updating, and editing PRs. It verifies destination visibility, excludes Linear identifiers, URLs, and connection commentary from public PR content, and skips attachments that could produce public linkbacks. Unknown visibility follows the public rule. The skill preserves narrow edits, published history, explicit text-only drafts, unrelated working changes, and honest validation. No AGENTS.md or commit-skill change is included.

## Synthetic comparison

Ran the sanitized [public creation and merged-PR cleanup fixture](../fixtures/write-pull-request/public-tracking.md) in five fresh contexts without candidate guidance, then five with the complete skill. Each agent saw only its assigned fixture and, for guided samples, the skill. Agents did not receive criteria, earlier conversation, real issue identifiers, or other outputs. No model override was used. All ten responses were read manually; parsed-operation checks also verified mutation fields and retained prose.

| Check | Controls | With skill |
| --- | --- | --- |
| Public title/body omit both implementation and review tracker IDs and URLs | 5/5 | 5/5 |
| No Linear attachment or public linkback operation | 5/5 | 5/5 |
| Correct neutral source, destination, target, and ready status | 5/5 | 5/5 |
| Accurate test results and macOS/GUI testing limits | 5/5 | 5/5 |
| Cleanup changes only the body, preserving both retained paragraphs and merged status | 5/5 | 5/5 |
| Success depends on the save receipt and matching read-back | 5/5 | 5/5 |

Controls already recognized the internal tracker context and public-linkback risk. These results provide regression coverage for an explicit publication policy; they show no measured quality gain over the controls. The [earlier passing baseline](2026-10-21-write-pull-request.md) remains valid for its samples; it did not establish reliable behavior in every future publishing session.

Guided samples could describe the completed independent review without exposing its tracker. For example, one body stated “Independent review found no remaining findings.” All cleanup mutations supplied only repository, PR number, and body; none reopened the merged PR or rewrote history. Retained text matched the fixture, allowing the final newline to vary.

## Regression and discovery checks

A fresh agent ran the two [original primary cases](../fixtures/write-pull-request/primary.md) and all seven [focused cases](../fixtures/write-pull-request/focused.md) with the skill. The public case renamed only the unpublished local branch to a neutral name, pushed the intended commits, omitted tracker references and attachments, and preserved unrelated planning edits. The private case used the exact supplied Linear branch name, created a hosted draft, disclosed the failing past-date test, and verified the existing issue association before claiming it.

The focused cases retained an explicit text-only draft, applied the public rule to unknown visibility, changed only the requested sentence in an existing PR, asked for an unresolved base, searched before retrying an uncertain create, stopped before publishing a tracker-bearing commit without rewrite authorization, and returned an unsaved draft when authentication was unavailable. The last fixture omitted actual local diff and test details; the output marked missing content rather than inventing it.

A separate fresh context first saw only the descriptions of the six packaged skills and the ordinary PR-creation request. It selected `write-pull-request`, then read that skill and produced the neutral public PR without a shared AGENTS.md trigger. This synthetic discovery result does not establish native host activation reliability.

## Packaging and installation

- Paired Git Workflows manifests declare 0.2.0 with matching name, version, description, and author. The curated catalog now has 18 skills; Git Workflows contains exactly `write-commit` and `write-pull-request`.
- `python3 -m unittest discover -s tests -v`: all 65 tests passed.
- Skill creator `quick_validate.py`: the new skill passed.
- `python3 scripts/validate_marketplace.py`: passed with 2 catalogs, 3 plugins, 6 packaged skills, and 1 preset.
- Cached Skills CLI 1.7.2 discovered all six packaged skills. Selected installs of `write-pull-request` succeeded at global and project scope for Codex, Claude Code, and OpenCode in disposable roots. Both installed copies matched the source: shared `.agents/skills` for Codex/OpenCode and `.claude/skills` for Claude Code.
- Existing `write-commit` and unrelated skill files were preserved. Unselected skills were absent. Repeating each selected install retained identical content. The existing commit skill and shared personal instructions also matched their pre-change snapshots byte for byte.

The repository fixtures and observations retain the reproducible cases. Raw responses and installer logs are not distributed.

## Limits

The synthetic comparisons made no live PR or Linear changes. Native host loading, automatic skill selection in authenticated sessions, and real retry races remain untested.
