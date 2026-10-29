# Changelog Skill Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans inline. Fresh agents
> perform behavioral comparisons and one final review. Track completion below.

**Goal:** Keep useful changelog entries current without a separate user request.
**Architecture:** One self-contained skill in Git Workflows, with existing
catalog and installer support. No runtime or shared instruction changes.
**Tech Stack:** Markdown, JSON, existing Python validators, Skills CLI 1.7.2.
**Spec:** [Approved design](write-changelog.md).

Publication update, 2026-10-29: the unchanged skill is packaged as Git Workflows
0.5.0 alongside worktree management. The checklist below records the original
0.3.0 implementation. Current packaging checks are recorded in the results.

## Constraints and review focus

- Shared use across Codex, Claude Code and OpenCode without a personal preset.
- Automatic selection before handoff, commit or PR; preserve text-only requests.
- Current-task user impact, clear STE-inspired prose, exact technical terms.
- Follow existing formats and generation processes; preserve released history.
- No unrelated backfill, private tracking references, invented release facts,
  commits, publication, or active installation as a side effect.
- Keep this plan with implementation. Preserve other branches and worktrees.

## Tasks

### 1. Establish observable behavior

Files: `evals/write-changelog.md`, `evals/fixtures/write-changelog/cases.json`.
Consumes the approved scope. Produces frozen synthetic inputs and observed gaps.

- [x] Run repository baseline checks.
- [x] Prepare real file-edit cases and preservation checks in disposable repos.
- [x] Run five fresh baseline contexts; read every response and resulting diff.
  Record selection, writes, reader impact, and behavior that already succeeds.

### 2. Implement and evaluate the skill

Files: `plugins/git-workflows/skills/write-changelog/SKILL.md`, evaluation report.
Consumes observed gaps. Produces a validated candidate or explicit omission.

- [x] Write concise conditional guidance with discoverable frontmatter and the
  existing STE-inspired prose rule. Do not add unused scripts or references.
- [x] Run five fresh guided contexts on identical cases. Read all file edits.
- [x] Check internal-only work, duplicate entries, explicit text-only scope,
  incomplete work, privacy, released history, and repeat preservation.
- [x] Correct only observed gaps, rerun affected cases, and record limits.

### 3. Package and verify

Files: paired Git Workflows manifests, `catalog.json`, plugin/root README,
`docs/setup.md`, `CHANGELOG.md`, and the evaluation results.
Consumes the tested skill. Produces a complete installable change.

- [x] Register the skill and update both plugin versions to 0.3.0.
- [x] Run unit, marketplace, skill, documentation-link, and whitespace checks.
- [x] Verify selected Skills CLI installs and repeat preservation in disposable
  Codex, Claude Code and OpenCode homes; compare source bytes.
- [x] Obtain one fresh whole-change review and address supported findings.
- [x] Report evidence and remaining limits. Leave commit, publication and
  active installation for a separate request.

## Progress

The skill, packaging and evaluation are complete on `feat/write-changelog`.
All 36 responses and actual file edits were inspected. Baselines already handled
existing changelogs and fragments; the candidate added the agreed automatic
creation behavior in five of five cases. Unit tests, skill validation and three
disposable install/repeat checks passed. Documentation checks passed. An
independent whole-change review inspected all responses and edits and found
no actionable issues. That initial evaluation ended before commit, publication
or live installation. The later publication check preserves the same skill and
revalidates the combined package. See the
[results](../../evals/results/2026-10-27-write-changelog.md).
