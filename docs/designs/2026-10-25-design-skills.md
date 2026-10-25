# Design Skills Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans inline. Fresh agents perform behavioral evaluations and one final review. Track task completion below.

**Goal:** Ship only independently usable design guidance that improves an observed gap.
**Architecture:** Reuse existing skills as the baseline. Add successful product guidance to Product Design and successful architecture/code guidance to Software Design. Preserve the installer and upstream pins.
**Tech Stack:** Markdown, JSON, existing Python validators, Skills CLI 1.7.2.
**Spec:** docs/designs/design-skills.md

## Global constraints

- Three independent design scopes; saved concise handoffs by default; no unauthorized production changes.
- docs/designs/<topic>.md is overridable. Keep designs with implementation; do not commit or publish as a side effect of designing.
- Preserve existing skills, callers, configuration, and installation routes.
- Use anonymous fixtures; keep raw outputs and local host details outside the repository.
- Self-contained skills, unique names, paired manifests and catalogs, and changelog updates.
- Keep this implementation plan and the approved design with the feature changes and implementation PR. The docs/superpowers directory remains ignored.

## Review focus

- Audit-only and fully specified implementation requests must not acquire a mandatory design stage.
- Existing design documents and custom destinations must be updated without duplicating or overwriting unrelated material.
- Partial outcomes and missing backend guarantees must remain explicit across product and architecture scopes.
- No-benefit candidates must be omitted; delivery improvements must not become claims of superior technical judgment.
- Selected installs must remain standalone and preserve unrelated files.

## Tasks

### Task 1: Freeze evidence and establish baseline
Files: evals/design-skills.md; evals/fixtures/design-skills/primary.json; focused.json.
Consumes: approved spec and frozen existing guidance. Produces: five baseline responses per primary case and a recorded gap for each justified candidate.
- [x] Validate synthetic fixture mechanisms.
- [x] Run five fresh baseline contexts; read every output and artifact.
- [x] Record source hashes, actual failures, and preservation results in private evaluation notes.

### Task 2: Product design candidate
Files: plugins/product-design/skills/design-product/SKILL.md if justified.
Consumes: product baseline gap. Produces: verified candidate or an explicit omission.
- [x] Write only guidance needed to implement the agreed scope and address observed gaps.
- [x] Run five fresh guided primary cases; inspect artifacts and scope.
- [x] Validate the skill. Revise only for observed regressions and repeat affected checks.

### Task 3: Architecture and code candidates
Files: plugins/software-design/skills/design-architecture/SKILL.md and design-code/SKILL.md if justified.
Consumes: respective baseline gaps. Produces: individually verified candidates or omissions.
- [x] Complete the architecture candidate's guided five-run check and validation.
- [x] Complete the code candidate's guided five-run check and validation.
- [x] Run focused selection and actual document-preservation checks for the final candidates.

### Task 4: Package, verify, and review
Files: paired plugin manifests and native catalogs, catalog.json, plugin READMEs, README.md, docs/setup.md, CHANGELOG.md, evals/results/2026-10-25-design-skills.md, and approved design status.
Consumes: successful candidate bytes and observed counts. Produces: complete local implementation and honest evaluation record.
- [x] Register only successful candidates and update affected versions, counts, and install documentation.
- [x] Run skill validators, unit tests, marketplace validator, links, and whitespace checks.
- [x] Run Skills CLI discovery and isolated installs/repeats for all three hosts; compare copied bytes and unrelated sentinels.
- [x] Perform one fresh whole-change review, address material findings, and report actual limits.
- [x] Leave commits, pushes, and active skill installation for an explicit follow-up.

## Progress

Implementation complete. All three candidates passed their matched comparisons, standalone document checks, skill validation, and isolated installation/repeat checks. Combined descriptions selected the intended skills, and all eight focused action cases retained scope. The catalog contains 25 selections and five custom plugins. The 73-test suite, marketplace validation, local links, and whitespace checks passed. One fresh whole-change review found no issues and independently checked manifests, source hashes, and preservation of 340 fixture files. Results and limits are recorded in evals/results/2026-10-25-design-skills.md. No runtime code changes were needed. The design and plan stay with this implementation. The follow-up authorizes committing and opening one implementation PR; active installation remains separate.
