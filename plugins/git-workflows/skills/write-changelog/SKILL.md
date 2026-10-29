---
name: write-changelog
description: Use when completing work that changes user-visible behavior, compatibility, configuration, performance or security, before task handoff, commits or pull requests, or when asked to write or update a repository changelog.
---

# Write changelog

Use ASD-STE100-inspired principles for English prose written for people. Write short, complete sentences with one main idea. Give clear instructions and put necessary conditions before their actions. Prefer active voice, simple verbs, and consistent terms. Keep related ideas connected. Preserve facts, evidence, uncertainty, and required technical detail. Reproduce code, commands, identifiers, paths, URLs, and source quotations exactly. Apply the principles for clarity; do not enforce the full STE dictionary or claim formal compliance.

Keep the changelog current as part of relevant work, without a separate request.
Save the entry before the task's final handoff or its requested commit or PR.
An explicit text-only request returns text; respect restrictions on file edits.
This skill does not create commits, publish releases or change versions.

## Establish the change and destination

Read the task's actual diff, relevant implementation and checks, repository
instructions, and existing changelog or release-entry process. Cover the current
task; do not backfill unrelated history. Distinguish implemented behavior from
proposals, incomplete work and verified release availability.

Follow the existing format and categories. For a generated changelog, update its
documented source entry or fragment. Preserve generated output. If no changelog
or entry process exists, create a minimal `CHANGELOG.md` with an `Unreleased`
section when there is a noteworthy change. Do not invent release dates or
versions, or move unreleased work into a release section.

## Write for project users

Record meaningful features, fixes, compatibility, configuration, performance
and security changes. Include developers who use the project's tools or APIs.
Internal refactors, tests and formatting need no entry when they do not affect
these readers. Repository-specific entry requirements take precedence.

Explain the resulting behavior and its practical effect. Include required user
actions for breaking changes, removals or changed defaults. For example:
“Reports now use JSON by default. Use `--format text` to retain plain text.”
Keep related work in one entry instead of listing commits or implementation
steps. Claims must match the available evidence; preserve material uncertainty.

Read existing unreleased entries before adding one. If the same change is
already covered, update that entry only as needed. Preserve unrelated entries,
released history and established links. Public or unknown-visibility output
must omit private Linear identifiers, URLs and tracking commentary.

## Verify the edit

Inspect the resulting entry and diff against the implemented change. Check
technical terms, migration instructions, destination format and preserved
content. Repeated completion of unchanged work should need no further edit.
Report the saved path and any material gap briefly. If no entry is warranted,
leave the changelog alone; do not create an empty file.
