# Changelog

Reconstructed from repository documentation and evaluation records. Dates reflect recorded work, not verified publication dates. Plugins are versioned independently.

## Unreleased

### Added

- **Git Workflows 0.3.0:** added `write-changelog` to record meaningful user impact before task completion, commits or PRs. It follows existing changelog processes, creates a minimal changelog when none exists, and preserves released history. Entries use STE-inspired prose and include required migration steps.
- **Product Design 0.3.0:** added `design-product` for independently scoped experience designs, saved handoffs, and explicit recovery constraints.
- **Software Design 0.1.0:** added independent `design-architecture` and `design-code` skills for system contracts, module interfaces, file organization, and caller migration. Designs update existing documents or save under `docs/designs/`, with explicit paths and text-only requests preserved.
- **Code Quality 0.2.0:** added `audit-scale` for data growth, concurrency, and recovery; `audit-security` for code, dependencies, CI, configuration, and secrets; and `audit-repo` to coordinate all three custom audits. Reports include confidence, effort, and grouped checks. Added matched comparisons with Ponytail and a coverage guide.
- **Code Quality 0.1.0:** added `audit-code` for readability and maintainability as code grows. Reports include all supported findings, grouped by root cause and ranked by impact, with suggested refactors and estimated effort.
- **Linear Workflows 0.4.0:** `wrap-up-linear-issue` saves and verifies a short TL;DR before an agent makes an authorized transition to Done. It preserves the original task and links decisive evidence.
- The wrap-up skill's description supplies the completion trigger; no personal preset change is required.

### Changed

- Evaluation documentation retains reproducible test evidence and excludes personal context, live setup records, and temporary paths.
- Custom audits now save reports under the audited repository's `docs/audits/`: `YYYY-MM-DD.md` for combined audits, with `-code`, `-scale`, or `-security` for standalone audits. New runs preserve existing reports and honor an explicit destination or chat-only request.
- New audit reports are ignored by Git by default through scoped `.gitignore` entries. Requested tracking, already tracked reports, and explicit include exceptions take precedence; unrelated rules and files are preserved.
- GitHub validation uses `requirements-dev.txt` for its pip cache so setup can reach the repository checks.
- **Code Quality 0.1.1:** made file and folder organization explicit in `audit-code`. Proposed splits, merges, moves, and renames follow repository conventions and account for imports, exports, registrations, configuration, assets, and build/test discovery.
- Research comments use short, consequential discoveries in the relevant thread. Single-comment requests and narrow edits retain their scope.

## 2026-10-23

### Changed

- **Linear Workflows 0.3.0:** added explicit Bug, Feature, Research, and Chore definitions and concise issue skeletons. Select one purpose from the final deliverable; Review remains a workflow status.
- Issue writing honors required team templates and existing label equivalents. Bugs may have an unknown cause; research may conclude with insufficient evidence. These defaults do not migrate workspace labels.

## 2026-10-21

### Added

- `write-linear-issue`: research available context, improve matching issues, link distinct work, apply appropriate labels, and save unless a draft is requested.
- **Linear Workflows 0.2.0:** `write-linear-comment` for requested updates, decisions, blockers, and handoffs. Code-dependent comments require verified published commit permalinks.
- **Git Workflows 0.1.0:** `write-commit` creates small commits, preserves unrelated changes, respects repository checks, and credits the contributing coding agent. Public or unknown-visibility repositories omit Linear references.

### Changed

- **Linear Workflows 0.2.1:** concise prose and useful bullets are explicit writing preferences.
- The personal preset uses one shared `configs/personal/AGENTS.md`, with separate native reviewer definitions. It suggests one useful next action after completed work.

## 2026-10-17

### Added

- Optional personal instructions and a `personal-reviewer` agent for Codex, Claude Code, and OpenCode, selectable separately from skills.
- Preset previews, backups, repeat-install checks, and conflict detection preserve existing instructions and reviewer definitions.

## 2026-10-16

### Changed

- Rebuilt the repository as a personal marketplace combining custom plugins and selected upstream skills. Added matching Codex and Claude Code catalogs, portable installation, pinned upstream sources, and a Python setup coordinator.
- **Product Design 0.2.0:** `product-brief` distinguishes decisions that block implementation from research that can proceed in parallel; saving a file is no longer required by default.

### Removed

- Replaced custom `product-diagrams` and `product-wireframes` with upstream `archify` and `prototype`.
- Retired `product-design-review` after baseline checks found no demonstrated benefit. Existing installed copies are not removed automatically.

See the [setup guide](docs/setup.md), [plugin packaging guide](docs/adding-plugins.md), and [evaluation records](evals/results/) for implementation details and verification limits.
