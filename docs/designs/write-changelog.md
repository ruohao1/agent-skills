# Changelog skill design

Status: Implemented and verified. See the
[evaluation results](../../evals/results/2026-10-27-write-changelog.md).
Keep this design with the implementation on `feat/write-changelog`; do not
create a separate planning PR.

## Agreed behavior

Add a shared `write-changelog` skill for Codex, Claude Code and OpenCode.
Activate it automatically for relevant work. Update the repository changelog
before committing or opening a PR. Readers are people who use the project,
including developers who use libraries and tools.

Record meaningful features, fixes, compatibility changes, configuration changes,
performance changes and security changes. Explain the effect and any action
the reader must take. Omit refactors, tests and formatting unless they affect
users. Cover the current task. Update an existing unreleased entry for the same
change instead of adding duplicates. Leave unrelated gaps and released history
alone unless asked.

Follow the repository's existing format or changelog generation process. If
neither exists, create a minimal `CHANGELOG.md` with an `Unreleased` section for
the first noteworthy change. A changelog records changes over time. Release
notes describe a particular release; writing or publishing them is outside this
skill's initial scope.

Use the existing ASD-STE100-inspired prose guidance. Write short, complete
sentences with one main idea. Prefer active voice, simple verbs and consistent
terms. Preserve evidence, uncertainty and exact technical identifiers. Do not
enforce the full STE dictionary or claim formal compliance. Keep private Linear
references out of public or unknown-visibility output.

## Proposed implementation

Package one self-contained `write-changelog/SKILL.md` in Git Workflows. Its
description should support automatic selection without an `AGENTS.md` install.
Check the changelog before the task's final handoff even when no commit or PR is
requested. Respect explicit text-only requests and exclusions from file edits.

Read the actual task changes and repository conventions before writing. Use
the established source entry or fragment when the changelog is generated.
Preserve unrelated content. Do not invent release versions, publication dates,
verification results or availability claims. Updating a changelog does not
authorize commits, pushes, release publication or version bumps.

A standalone skill fits the agreed cross-agent use. Instructions only in a
shared configuration would miss skill-only installs. Adding the workflow only
to `write-commit` would miss tasks that finish without a commit. Keep existing
skills and installation routes compatible; add no runtime dependency.

## Evidence and completion

Before writing the candidate, compare current behavior against synthetic cases.
Then test automatic selection and actual edits with the candidate. Cover a
meaningful change, internal-only work, a repository with no changelog, an
existing generation process, a repeated update and a narrow text-only request.
Check accuracy, scope, privacy, migration instructions and preservation of
released history. Retain only guidance that shows useful improvement.

Update paired manifests, catalog membership, documentation and this repository's
changelog with the implementation. Run required repository and skill validators.
Verify discovery and repeat installations in disposable environments for all
three agents. Distinguish simulated selection and installation success from
fresh authenticated host activation. Commit, publish and active-install steps
remain separate from this design approval.
