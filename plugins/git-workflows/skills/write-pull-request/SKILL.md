---
name: write-pull-request
description: Use when the user asks to write, create, open, draft, or update a pull request or its title or description, including focused edits to an existing PR.
---

# Write pull request

Use ASD-STE100-inspired principles for English prose written for people. Write short, complete sentences with one main idea. Give clear instructions and put necessary conditions before their actions. Prefer active voice, simple verbs, and consistent terms. Keep related ideas connected. Preserve facts, evidence, uncertainty, and required technical detail. Reproduce code, commands, identifiers, paths, URLs, and source quotations exactly. Apply the principles for clarity; do not enforce the full STE dictionary or claim formal compliance.

Write and save a concise PR for a reviewer who has not seen the conversation. A draft PR is hosted; an explicit text-only draft stays unsaved. Honor narrow edits. Creating a PR includes publishing the intended existing commits when needed, but does not authorize new commits, merging, or rewriting history.

## Establish context

Read applicable repository instructions, the actual source/base diff and commits, relevant issue context, PR template, checks, and any matching PR. Verify destination repository, source, target, and visibility from repository and host evidence. Infer settled choices from the session; ask only for unresolved material ambiguity. Preserve unrelated staged and unstaged work.

## Apply repository privacy

Use authoritative destination visibility, not the source fork's visibility. If visibility remains unknown, use the public rule.

- **Public or unknown:** use a descriptive branch without Linear identifiers. Keep Linear IDs, URLs, and connection commentary out of PR titles, descriptions, and comments, including tracking footers and independent-review references. Internal issue context may inform the explanation; it is not material to copy into the public PR. Skip automatic Linear linking and attachment operations that can create public linkbacks. A private Linear issue or internal attachment does not make a public reference private.
- **Private:** for issue-specific work on a new or safely renameable unpublished branch, use Linear's actual supplied branch name (`gitBranchName` when available). Preserve established published branches and existing PRs. Resolve a missing or ambiguous issue branch name before creating one; do not invent it. Verify any requested issue association before claiming it.

Check naming conflicts before creating or renaming an unpublished branch. Before publishing, inspect the outbound branch, commit messages, changed files, and proposed PR content for Linear references. If existing history or a published branch conflicts with the public rule, surface it before publishing more; do not silently rewrite history or rename the remote branch. Keep requested cleanup edits within their stated scope.

## Write and save

Explain the concrete problem and resulting behavior, followed by actual validation and material remaining limits. Use brief prose and useful bullets; follow the repository template without copying internal tracking details. Distinguish tests, review, merge, and deployment. Keep incomplete work or failing relevant checks in draft, honoring any stricter repository publication rule. Missing optional checks are disclosed, not invented.

For an existing PR, read its current content and patch only the requested fields. Preserve other text, state, target, and metadata; a description edit does not reopen a merged PR. Avoid duplicate PRs and unsolicited discussion comments.

Use the available tools' actual schemas. Save the authorized PR without another approval round. With a CLI, pass multiline bodies through a file to preserve exact text. Read back the saved fields and visibility before reporting success. After an uncertain push or save, inspect the remote branch or matching PR before retrying. Missing access yields an explicitly unsaved draft. Return the confirmed PR URL, actual checks, and unresolved limits.
