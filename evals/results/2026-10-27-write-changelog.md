# Write changelog results

Date: 2026-10-27.

## Method

Five fresh baseline agents and five fresh candidate agents completed the same
three [primary cases](../fixtures/write-changelog/cases.json) in separate local
Git repositories. Both arms received identical requests, files and handoffs.
They selected relevant skills from descriptions before loading bodies. Baselines
had the existing Git Workflows skills; candidates also had `write-changelog`.
No explicit candidate invocation or model override was used.

The first baseline gap was read before the candidate was written. All 30 primary
responses and resulting file edits were inspected manually. File comparisons
checked preservation of implementation, versions, unrelated entries and released
history. Agents performed local tests and actual edits, not hypothetical writes.

Five boundary cases used the standalone skill from a disposable installation.
A separate fresh continuation received an already completed primary workspace.
All six responses and their files were inspected. Raw transcripts and temporary
workspaces remain outside the repository.

Evaluated skill SHA-256:
`7d8636d183fe9f0e21b8895d57da85f75f78fcbbe5d6ca526a7461904d43a061`.

## Observed behavior

| Observation | Baseline | Candidate |
| --- | --- | --- |
| Update an existing changelog with an accurate unreleased entry | 5/5 | 5/5 |
| Create a missing changelog with the required migration instruction | 0/5 | 5/5 |
| Use the documented fragment process and preserve generated output | 5/5 | 5/5 |

The baselines already wrote useful existing entries and fragments. They kept
internal tracking references out of public content and preserved prior history.
For the repository without a changelog, all five ended after checking the
implementation and README. One recorded: “Did not introduce a changelog or assign
a release version or date.” The gap is against the agreed automatic-creation
preference; it does not establish that every repository needs a changelog.

The candidate was selected in all 15 primary tasks. Each missing-changelog case
created `Unreleased` with a concise compatibility entry: positive values are
required, and callers must omit `--limit` instead of using `--limit 0`. No release
date or version was invented. Existing entries and fragment formats remained
correct. The entries used short sentences and preserved technical terms; this
is not a claim of formal ASD-STE100 compliance.

The boundary cases left internal-only work, a restricted spelling correction
and an investigation without extra changelog edits. Related CSV work changed one
existing unreleased bullet. The text-only request returned one bullet without
changing files. The fresh repeat selected the skill, found the existing entry
sufficient and preserved all four workspace files, including their timestamps.

## Packaging and validation

- All 73 repository unit tests passed.
- Marketplace validation passed: two catalogs, five plugins and 14 custom
  skills. The complete curated selection contains 26 skills.
- Skill structure and whitespace checks passed. Both Git Workflows manifests
  declare 0.3.0. Existing writing skills and shared instructions are unchanged.
- Selected Skills CLI 1.7.2 installs passed in disposable Codex, Claude Code and
  OpenCode homes. Copied files matched the source. Repeated installs preserved
  timestamps and unrelated sentinel skills. No instruction files were created.
- Local documentation links resolved. A fresh independent review checked all
  responses, file edits, preserved content, packaging and installation evidence.
  It found no actionable issues and confirmed that the evaluated, packaged and
  installed skill copies match the recorded hash.

## Limits

Selection was tested with a small supplied inventory in fresh subagent contexts.
It does not establish automatic invocation across full host catalogs or every
future task. Authenticated host loading, native plugin activation and release
generation were not tested. No live installation, commit or publication was
performed. This change adds guidance, not a hook that can force invocation.

## Publication check: 2026-10-29

The original evaluation above used Git Workflows 0.3.0. Publication now packages
the identical skill as 0.5.0, preserving the subsequently added worktree skill.
The recorded SHA-256 still matches. The behavioral scenarios were not rerun.

The publication branch builds on the Linear Workflows publication branch. Its
combined catalog contains 29 skills, including 17 custom skills across five
plugins. Both Git Workflows manifests declare 0.5.0 and list the same package
metadata. The three existing Git skill files are unchanged.

All 73 unit tests, marketplace validation, skill validation and whitespace
checks passed on the combined contents. Selected first and repeated Skills CLI
1.7.2 installs passed in disposable Codex, Claude Code and OpenCode homes. Each
copy matched the evaluated source. Five unrelated files per home retained their
contents and timestamps.

These checks cover packaging and installation preservation. They do not retest
the original model comparisons or establish native host activation. No live
agent configuration was changed by the publication checks.
