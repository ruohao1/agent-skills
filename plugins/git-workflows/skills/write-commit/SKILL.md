---
name: write-commit
description: Use when the user asks to commit work, write commits, or draft or edit commit messages, including a specifically requested amendment.
---

# Write commit

Use ASD-STE100-inspired principles for English prose written for people. Write short, complete sentences with one main idea. Give clear instructions and put necessary conditions before their actions. Prefer active voice, simple verbs, and consistent terms. Keep related ideas connected. Preserve facts, evidence, uncertainty, and required technical detail. Reproduce code, commands, identifiers, paths, URLs, and source quotations exactly. Apply the principles for clarity; do not enforce the full STE dictionary or claim formal compliance.

Create small, reviewable local commits by default. An explicit message-only or draft request returns text without changing Git. A coding task alone does not request a commit. Commit creation does not include pushing or opening a PR.

## Establish scope and branch

Read applicable repository instructions, the session's intended work, status, staged and unstaged diffs, and relevant checks. An explicit “commit the staged changes” defines the scope; otherwise derive it from the request and session, not everything already staged. Ask only when intended scope is genuinely ambiguous.

Verify the destination repository's visibility using authoritative host metadata. Apply this branch and message rule:

- **Public or unknown visibility:** use a descriptive branch without Linear identifiers. Omit Linear IDs, URLs, and connection commentary from commit messages and skip automatic Linear linking. If existing published branches or history conflict with this requirement, surface the conflict; do not silently rename published branches or rewrite history.
- **Private:** for issue-specific work on a new or safely renameable unpublished branch, use the actual branch name supplied by Linear (`gitBranchName` when exposed by the tool). Resolve the issue from context; ask when ambiguous or its required branch name is unavailable. Preserve established published branches and existing PRs.

Check branch-name conflicts before creating or renaming. Honor the known source/base and repository branch rules; do not guess a different base or transfer unrelated work between branches.

## Select reviewable units

Group each independent behavior change with its necessary tests and documentation. Keep a coherent change together; file count is not a reason to split it. Review each selected patch before committing.

Stage only the intended files or hunks. Preserve unrelated working contents **and their staged/unstaged state**, including mixed files. If temporarily adjusting the index, retain its original entries and restore unrelated entries on success or failure. Whole-file staging is unsuitable when only some hunks belong to the commit.

## Write the message

Follow documented repository message rules. With no documented convention, use Conventional Commits: `type(scope): imperative summary`, with scope optional. Explain the resulting change concisely. Add a body for useful motivation, breaking behavior, migration instructions, or other material context. Use bullets for parallel points when helpful.

Credit the contributing coding agent with a `Co-authored-by: Name <email>` trailer, separated from the message by a blank line. Use its verified configured or documented identity; ask for missing attribution before committing. Preserve the human Git author and existing valid trailers. Account for host-added attribution so the final message contains the agent's credit once. Do not add closing keywords merely to associate an issue.

For an explicitly requested message amendment, preserve unchanged message content, trailers, and the commit tree. A request for a new commit does not authorize amending previous commits.

## Commit and verify

Honor required checks and hooks for the selected change. Report actual results and missing optional checks. A failing required check stops the commit; do not bypass it or silently expand into unrelated repairs. If a hook changes selected files, inspect the changes and restage only the intended scope before retrying.

Create the authorized commits without an extra approval round. Verify each committed patch and message, then the remaining index and working tree. After an uncertain result, inspect HEAD/history before retrying; do not duplicate a commit. Return the confirmed hashes and subjects with concise validation and remaining limitations. Missing Git access yields an explicitly uncommitted message draft, not a claimed commit.
