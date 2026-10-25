---
name: audit-repo
description: Use when the user asks for all three custom audits or a combined maintainability, runtime scaling, and security audit of a repository or selected area.
---

# Audit repo

Produce one combined report by following the three existing audit skills. This skill coordinates their work; their instructions define how to audit each concern.

## Run the three passes

**Required companion skills:** `audit-code`, `audit-scale`, and `audit-security`.

Resolve these names through the runtime's available skills or the installed Code Quality plugin, and read their instructions. If a companion is unavailable, continue the available passes and mark the report incomplete, naming the missing coverage. Explain that the full Code Quality bundle supplies the companions; installing tools is a separate action.

Use the requested repository area, or the whole repository by default. Establish one scope and source revision for all passes. Reuse verified repository context and checks while following each companion's inspection requirements. Run each pass in turn and collect its findings without saving a child report. Apply each companion's verification limits; the audit does not authorize application fixes or issue creation.

## Combine the findings

Return one numbered list, ordered by impact and likelihood under the stated workload and access conditions. Merge findings only when the same cause and fix explain them. Keep all consequences, verified locations, the smallest useful change, relevant checks, confidence or uncertainty, and estimated effort. Keep distinct causes separate even when they share a file or category.

Resolve conflicting conclusions against source evidence. Unresolved claims remain leads; agreement between audits is not independent proof. Use concise findings with the four bullets **Evidence and impact**, **Fix and check**, **Confidence**, and **Effort**.

End with coverage for each of the three audits, checks actually run, and remaining gaps. A missing pass is incomplete coverage, not a clean result.

## Save the report

Save to `docs/audits/YYYY-MM-DD.md` in the audited repository by default. Honor an explicit destination or chat-only request. Include the inspected scope and source revision when available, noting uncommitted changes. Use repository-relative source paths and line numbers inside the saved file. For a new run, add a numeric suffix if the path exists; replace a report only when an update is requested. Save one combined report and preserve application files.

For a report inside a Git worktree, keep new untracked reports ignored by default. Inspect tracked state and effective ignore rules first. Reuse an effective rule; otherwise append an anchored, literal entry for that report alone to the worktree-root `.gitignore`, escaping Git pattern characters and preserving existing content and line endings. Treat already tracked reports and explicit include exceptions as tracking intent. If the user requests Git tracking, use narrow exceptions where needed and preserve other files' ignore status. Never untrack, stage, or commit files as part of the audit. Chat-only output and reports outside a Git worktree need no ignore edits.

Verify the actual report path with `git check-ignore --quiet`. Use `-v` to identify rules, not to prove exclusion: it also reports negated matches. State any tracking exception or ignore failure without claiming the report is ignored.

After saving, the final reply consists of the report link, a one-sentence priority summary, and material execution limits. The findings belong in the saved file. If saving fails, return the report with the reason and do not claim it was saved.
