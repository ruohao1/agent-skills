# Manage Worktrees Implementation Plan

> Implement inline with independent behavioral evaluation and final review. Keep this plan with the implementation branch.

**Goal:** Isolate repository tasks without changing the original checkout or losing unfinished work.

**Architecture:** One portable instruction skill in Git Workflows. Reuse Git and existing packaging and installer helpers.

**Tech stack:** Markdown, JSON, existing Python standard-library setup tools, Git.

**Spec:** [Manage worktrees](manage-worktrees.md).

## Constraints

- Preserve all unrelated work. No automatic commit, push, merge or live installation.
- Use `repo/.worktree/<branch>` for new task worktrees; honor verified existing task workspaces.
- Use synthetic evaluation inputs. Keep raw transcripts and machine-specific paths outside the repository.
- Keep the existing shared presets, installer runtime and writing skills unchanged.

## Tasks

- [x] Verify remote default branch and create an isolated feature worktree. Preserve the existing checkout exception.
- [x] Record scenarios and criteria in `evals/fixtures/manage-worktrees/cases.json` and `evals/manage-worktrees.md`.
- [x] Run five fresh baseline contexts against three scenarios. Read a failing baseline before writing guidance, then read all results before the final assessment.
- [x] Write `plugins/git-workflows/skills/manage-worktrees/SKILL.md` to address observed gaps and the approved policy.
- [x] Repeat the same scenarios in five fresh candidate contexts. Exercise read-only, busy, blocked, dirty, host-owned and merged-work boundaries.
- [x] Run actual disposable Git operations for creation, reuse and cleanup. Verify unchanged original checkouts and preserved local data.
- [x] Update paired plugin manifests, `catalog.json`, plugin/root READMEs, `docs/setup.md` and `CHANGELOG.md`.
- [x] Run all unit tests, marketplace/skill validation and whitespace checks. Test selected installation and repeat installation for Codex, Claude Code and OpenCode in disposable homes.
- [x] Record observed results and limits in `evals/results/2026-10-28-manage-worktrees.md`; obtain independent review and address findings.

## Review focus

Confirm that worktree identity is not confused with task identity, clean status is not treated as proof of inactivity or safe ignored-file removal, cleanup ownership is supported by evidence, a squash merge does not hide later local commits, and a failed isolation step never silently permits original-checkout edits.

## Completion record

All planned checks passed. Independent review found no remaining actionable findings. Its baseline-order wording correction is reflected above and in the results report.

Review limits remain explicit: authenticated host discovery and coordination APIs were not exercised; unusual repository layouts and non-Linux execution were not verified; publication and live installation remain separate actions. The skill retains uncertain workspaces rather than claiming an atomic coordination guarantee.
