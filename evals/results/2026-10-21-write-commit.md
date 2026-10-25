# Write commit observations

## Agreed behavior

The skill creates local commits by default, with explicit message-only/draft requests remaining text. Select the intended work, preserve unrelated staged and unstaged changes, and split independent changes into reviewable commits with their tests. Follow repository message rules; use Conventional Commits when no rule is documented. Credit the contributing coding agent with a verified co-author trailer, preserving the human author and avoiding duplicate credit.

Public repositories use descriptive branch names and no Linear identifiers, URLs, or automatic linkage; unknown visibility follows that rule. Private issue-specific work uses Linear's supplied branch name for new or safely renamed unpublished branches. Preserve published branches and existing PRs. Honor required checks/hooks, report missing optional checks, and keep commits local unless publishing is also requested.

GitHub documents the [co-author trailer syntax](https://docs.github.com/en/pull-requests/how-tos/commit-changes/creating-a-commit-with-multiple-authors). The skill resolves the active agent's attribution from verified configuration/documentation rather than hardcoding one identity across hosts. The configured `Fixture Agent` address in these tests is synthetic and is not a product default.

## Method

Five fresh-context controls and five guided agents received identical [primary tasks](../fixtures/write-commit/primary.md). Guided contexts additionally read the candidate skill. The first context in each arm also answered the [focused cases](../fixtures/write-commit/focused.md). No agent saw the rubric, interview, other outputs, or results. No model override was requested; all answers were manually inspected. Git operations and receipts in these fixtures were simulated.

One additional fresh context used the installed `caveman-commit` skill with the same primary tasks. That existing workflow explicitly returns messages only; the comparison checks scope fit, not general writing quality.

## Results

| Behavior | Control | Guided |
| --- | --- | --- |
| Public task retains a neutral branch | 3/5 | 5/5 |
| Private unpublished branch uses Linear's supplied name | 3/5 | 5/5 |
| Conventional Commits fallback when no repository convention exists | 0/5 | 5/5 |
| Honor the private repository's plain-language message rule | 5/5 | 5/5 |
| Split independent changes with their necessary tests | 5/5 | 5/5 |
| Preserve unrelated staged and unstaged planning contents | 5/5 | 5/5 |
| Credit the verified contributing agent and preserve the human author | 5/5 | 5/5 |
| Create local commits without an unsolicited push | 5/5 | 5/5 |

Controls 2 and 5 proposed renaming the public branch to `alex/sdk-31-client-defaults`. Controls 3 and 4 kept the private branch's old name; control 3 explained that the supplied issue branch name “does not require renaming the branch for this commit-only request.” All controls wrote plain-language subjects when no repository convention was documented. These differ from the evaluated workflow defaults; they are not universally incorrect Git practices.

The candidate uses explicit visibility conditions and a defined message fallback. All guided samples retained the neutral public branch, selected the supplied private issue branch, and applied the fallback while preserving the repository's explicit exception. No revision was needed after the guided runs. Commit grouping, attribution, and preservation were already baseline strengths; no improvement in those behaviors or in concision is claimed.

Both focused contexts preserved text-only requests, asked for missing attribution, stopped after required hook failure, inspected formatter changes before restaging, asked about ambiguous scope, preserved an explicitly amended commit's tree/body/trailers, kept an existing published branch, and treated unknown visibility as public.

The existing `caveman-commit` comparison returned messages without performing commits. It omitted the configured co-author credit and included `Refs SDK-31` in the public case. Its explicit message-only boundary does not satisfy the evaluated execution workflow; it was neither modified nor installed again.

## Actual isolated Git execution

One fresh guided agent performed real commits in a disposable repository, using an isolated HOME and Git configuration. It could inspect source, tests, and diffs, but could not read the evaluator's expected-state file. Network, live connectors, source edits, hook/config changes, and writes to the marketplace repository were prohibited.

The fixture contained two changes in the same source file, their separate tests, and unrelated staged plus unstaged changes in the same planning file. The existing pre-commit hook exported and tested the staged tree. Repository visibility and agent identity were explicitly synthetic verified read results; host discovery was not tested.

The two commits contained:

- First commit: retry behavior and its regression tests.
- Second commit: timeout default and its regression test.

Both hook runs passed four staged-tree tests. An independent readback verified the two exact file scopes, the old timeout in the first commit and new timeout in the second, the configured human author, one agent trailer per commit, no tracker reference in messages, and the neutral branch. The planning file's index blob and working bytes matched their original snapshots; remaining status was exactly `MM notes/next-quarter.md`.

This establishes execution and index preservation for this fixture, not all Git states or operating systems. Native host activation, real hosting/Linear lookups, and live issue linkage remain untested.

## Packaging and installation

- `quick_validate.py` passed for `write-commit` and the two lightly edited Linear skills.
- `python3 -m unittest discover -s tests -v`: all 65 tests passed.
- `python3 scripts/validate_marketplace.py`: two matching native catalogs, three plugins, four local skills, and one preset. The curated catalog contains 16 skills.
- Git Workflows 0.1.0 is registered in both native catalogs and its curated bundle contains `write-commit`. No installer code, dependencies, upstream pins, or host configuration changed.
- Cached Skills CLI 1.7.2 discovered the new skill and installed it for Codex, Claude Code, and OpenCode in disposable global and project roots. Both installs and both repeats succeeded. Installed bytes matched source, the pre-existing issue skill stayed intact, and unselected skills were not implicitly installed.
- Linear Workflows 0.2.1 adds concise prose and useful bullets to both existing skills. This is a narrow editorial update; no new behavioral superiority claim or repeated agent evaluation is made for it.

No active user installation was changed. Actual native plugin activation and authenticated host conversations were not exercised.
