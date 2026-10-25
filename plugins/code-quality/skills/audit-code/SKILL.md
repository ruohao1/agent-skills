---
name: audit-code
description: Use when the user asks to audit a repository or a specific area for code hygiene, readability, file and folder organization, maintainability, or refactoring opportunities as the codebase grows.
---

# Audit code

Audit how easily people can understand, test, and change the code as it grows. Return a report. Refactoring, issue creation, and runtime-load analysis are separate work unless requested.

## Establish the scope

Use the requested area, or the whole repository by default. Read repository instructions, architecture decisions, entry points, dependencies, and relevant tests. Map the main flows and follow their callers and interfaces. Use existing search and analysis tools; exclude generated and vendored code unless it is the requested subject. Record what was inspected and any gaps instead of implying exhaustive coverage from a sample.

## Find useful improvements

Look for maintenance costs visible in the code: duplicated rules that must change together, changes scattered across modules, callers exposed to implementation details, mixed responsibilities, unclear names or misleading comments, dead code, unnecessary indirection, and tests that require unrelated setup.

Include file and folder organization. Consider splitting unrelated responsibilities, merging fragments that only add navigation, and renaming or moving files to make their purpose and ownership clearer. Group related code and tests when it improves navigation or keeps related changes together, following project conventions.

Trace a concrete change through the relevant code to explain its cost. A current runtime bug is not required: working code can still hide intent or make a rule difficult to change and test. Repository conventions and settled constraints inform the review; existing architecture can be challenged when the evidence supports a smaller, clearer structure.

Judge responsibilities and concepts rather than line counts. An orchestration function can contain guards and control flow. Extract distinct business rules when that makes the workflow clearer or isolates useful tests. Similar syntax alone does not establish shared knowledge. Keep useful adapters and extension points; simplify forwarding layers that add only navigation. Deleting or merging abstractions may be the best refactor.

## Verify each finding

Read the affected implementation, callers, tests, and relevant configuration before recommending a change. Before declaring code unused, check exports, registrations, dynamic references, and external consumers. Unavailable evidence leaves a question to verify, not a confirmed removal finding.

For moves and renames, trace imports, exports, registrations, configuration paths, build/test discovery, and relative resource paths. Identify the updates needed to preserve those contracts.

For each finding, connect verified source locations to a specific cost of understanding, changing, or testing the code. Distinguish current facts from possible future mistakes. Propose the smallest coherent refactor that preserves behavior and contracts; identify any required caller migration or verification. Use relevant existing checks when needed to resolve uncertainty, and distinguish reading a test from running it.

Combine observations that share one cause and would be resolved by the same refactor. Include representative occurrences and affected callers. Similar categories in independent subsystems do not establish a shared cause. Place a related testing safeguard with its refactor instead of counting it as another instance of the same problem.

## Report

Start with a short priority summary. Then number every supported finding, ordered by maintenance impact. Report all supported findings without a fixed cap; uncertain leads belong in the coverage limits.

For each finding, give concise bullets or a short paragraph covering:

- Verified file locations and the responsibility involved.
- The structural problem and its concrete maintenance consequence.
- The smallest useful refactor, including behavior or contracts to preserve.
- Relative effort, clearly marked as an estimate, with the main reason.

Use plain English, short complete sentences, and consistent terms. Preserve identifiers, commands, and references exactly. Avoid invented scores, time estimates, or line savings. End with inspected scope, checks actually run, and remaining gaps. If no worthwhile findings are supported, say so without inventing cleanup work.

## Save the report

Save to `docs/audits/YYYY-MM-DD-code.md` in the audited repository by default. Honor an explicit destination or chat-only request. When contributing to a combined audit, return findings to its coordinator without saving a separate report. Include the inspected scope and source revision when available, noting uncommitted changes. Use repository-relative source paths and line numbers inside the saved file. For a new run, add a numeric suffix if the path exists; replace a report only when an update is requested.

For a report inside a Git worktree, keep new untracked reports ignored by default. Inspect tracked state and effective ignore rules first. Reuse an effective rule; otherwise append an anchored, literal entry for that report alone to the worktree-root `.gitignore`, escaping Git pattern characters and preserving existing content and line endings. Treat already tracked reports and explicit include exceptions as tracking intent. If the user requests Git tracking, use narrow exceptions where needed and preserve other files' ignore status. Never untrack, stage, or commit files as part of the audit. Chat-only output and reports outside a Git worktree need no ignore edits.

Verify the actual report path with `git check-ignore --quiet`. Use `-v` to identify rules, not to prove exclusion: it also reports negated matches. State any tracking exception or ignore failure without claiming the report is ignored.

After saving, the final reply consists of the report link, a one-sentence priority summary, and material execution limits. The findings belong in the saved file. If saving fails, return the report with the reason and do not claim it was saved.
