# Manage worktrees evaluation — 2026-10-28

## Scope and method

This evaluation checks a portable instruction skill. It does not measure a host integration or locking service.

The fixed [scenarios and criteria](../fixtures/manage-worktrees/cases.json) cover new-task setup, task resumption and merged-work cleanup. Five fresh contexts ran each arm, with all three scenarios in each context: 15 baseline responses and 15 candidate responses. Models and reasoning settings were inherited without overrides. These are proposed-action simulations, not 30 executed Git workflows.

The baseline inventory contained Superpowers 7.0.1 `using-git-worktrees` and `finishing-a-development-branch`, plus the existing `write-commit` and `write-pull-request`. The candidate added `manage-worktrees` to the same inventory. Respondents selected skills from descriptions and read selected files. They received the same task facts, without scoring criteria or earlier responses.

The first three baseline runs were read before the candidate was written. The remaining two baseline runs used the frozen baseline inputs and inventory while the candidate was developed. All 30 scenario responses were read in full. The candidate was selected in 15/15 responses. The tested skill SHA-256 is `4b27af9a37f76d5f854e258b19dbf2e7b5162b3022bf79b58fe7115c90599ffc`.

## Matched observations

| Decision | Baseline | Candidate |
| --- | --- | --- |
| New independent task proceeds without another workspace-consent question | 0/5 | 5/5 |
| New worktree uses `repo/.worktree/<branch>` when the native tool cannot choose that path | 0/5 | 5/5 |
| New task uses the fetched default branch rather than stale local main | 5/5 proposed that base or a safe correction | 5/5 proposed that base |
| Resumption selects the matching inactive host workspace and preserves the active theme task | 5/5 | 5/5 |
| Cleanup inventories ignored files and preserves uncertain local data | 5/5 | 5/5 |
| Cleanup stays targeted instead of globally pruning other registrations | 5/5 | 5/5 |

All baseline new-task responses followed the upstream consent rule and native destination preference. For example: “Before creating a worktree, ask for the consent explicitly required by Step 0 of the selected skill.” The candidate supplied the approved automatic-creation and placement policy. This demonstrates adoption of those defaults; it does not show that the baseline cannot use worktrees.

The baseline already handled task identity and ignored-file preservation correctly. No improvement is claimed for those decisions. As a secondary observation, two baseline responses also proposed deleting the merged task branch. All candidate responses kept branch deletion outside worktree cleanup.

## Boundary decisions

Nine additional candidate scenarios passed manual review:

- Read-only explanation creates no workspace or branch.
- An original checkout with staged and unstaged feature work stays intact; the agent reports the exception and isolates the new task.
- Failed creation leads to state inspection and blocked edits, without an original-checkout fallback.
- Clean status and an absent lock do not establish that another agent is inactive.
- An open PR keeps its worktree for review.
- Verified owned, inactive and empty worktree cleanup uses non-force removal and verifies the result.
- A prior squash merge does not account for later local commits.
- Reusing a host-owned worktree does not transfer cleanup ownership.
- Conflicting tracked include rules are reported rather than silently overwritten.

These decisions were simulated. Activity and host ownership were supplied facts, not observed API results.

## Disposable execution

One independent executor completed four requests in separate disposable repositories. The coordinator then read its full report, inspected the actual patches and registrations, repeated both focused test suites, and compared file hashes, branch tips, indexes and status with the starting snapshots.

| Case | Observed result |
| --- | --- |
| New task | Created `.worktree/fix/zero-count` from the newer fetched origin/main. The stale original main stayed unchanged. The existing local exclusion was preserved and `/.worktree/` was added once. |
| Resume task | Reused the matching host workspace outside the preferred directory. The active theme worktree and both task notes stayed unchanged. No replacement worktree was created. |
| Unique-data cleanup | Ordinary status was clean, but ignored `.env` and local notes were present. The worktree, registration and files were retained. |
| Safe cleanup | Non-force removal succeeded from outside the target. Its directory and registration disappeared; its branch and original checkout remained unchanged. |

Both implementation cases added a zero regression, observed `50 != 0`, then changed the fallback to apply only to `None`. Each finished with three passing tests. All original checkout files, HEADs, branches and indexes were preserved. No commits, branch deletion or global pruning occurred.

These cases exercised real Git and filesystem operations. Host activity and provenance remained trusted fixture inputs; no native coordination API was called.

A fresh context then resumed the completed new-task fixture from its handoff. It reused the existing worktree, found the fix and regression already present, and ran three passing tests. All five source/instruction files retained their bytes and modification times. HEAD and worktree registrations were unchanged; no duplicate worktree or source edit was made.

## Packaging and installation

- 73 unit tests passed.
- Marketplace validation passed: two catalogs, five plugins, 14 custom skills, one preset and one MCP selection. The curated catalog has 26 total skills.
- Skill frontmatter validation passed.
- Changed Markdown links resolved, the identifying-data scan passed, and `git diff --check` passed.
- Skills CLI 1.7.2 installed the selected skill and repeated the installation successfully for Codex, Claude Code and OpenCode in separate disposable homes.
- Each installed copy matched the tested source. Five unrelated instruction/skill files per home retained their bytes and modification times across both runs.
- Observed tool versions: Git 2.53.0, Node 22.23.1 and npm 10.9.8 on Linux.

An independent reviewer read all 39 simulated decisions, execution and repeat reports, snapshots, installation logs and changed source. It independently checked preservation and source hashes and found no remaining actionable findings.

## Limits

The new policy was exercised with inherited evaluation agents. No authenticated Codex, Claude Code or OpenCode conversation was used to measure automatic discovery. Native worktree tools, cross-host session detection, atomic claims, submodules, separate Git directories, macOS and Windows were not exercised. Successful installation does not establish runtime activation.

Git status is not evidence that another agent is inactive. The skill preserves uncertain workspaces; it cannot provide a cross-host locking guarantee. No live agent installation or publication occurred. Workflow execution made no commits or merges; fixture preparation used synthetic local history.
