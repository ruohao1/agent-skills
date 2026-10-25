# Maintainability audit observations

## Scope and method

The evaluated skill audits maintainability as code grows: a report for the whole repository or a selected area, all supported findings grouped by root cause, maintenance-impact ordering, and relative effort estimates. Runtime traffic scaling is outside its purpose. Refactoring and issue creation remain separate requested work.

Five fresh agents received the installed Ponytail 5.3.2 `ponytail-audit` instructions and the [primary source fixture](../fixtures/audit-code/primary.md). Five fresh agents received the same fixture with `audit-code`. A separate fresh agent per arm handled the [focused cases](../fixtures/audit-code/focused.md). No model override, rubric, previous response, or expected finding list was supplied to primary agents. All reports were read manually. This comparison is against an existing audit workflow, not an unaided model. Equivalence between the installed baseline and the catalog's upstream commit was not checked.

Before the counted runs, fixture indentation errors were corrected and the initial three runs were interrupted and discarded. The corrected source snippets parse, and their six application tests pass when materialized in a disposable directory. Evaluating agents receive no test-execution result and must distinguish source inspection from test execution.

## Baseline observations

All five baseline reports identified duplicated pricing rules, redundant notification layers, misleading unit documentation, and the verified-unused legacy helper. Three identified the unclear status-label name. They retained the manifest-registered exporter, did not extract the clean orchestration guard, and did not merge the two small normalizers solely because their syntax matched. They distinguished hypothetical regressions from an observed production defect and accurately stated that they had not run tests.

None supplied effort estimates. All five reported the shared-pricing refactor and the screen's repeated quote load as separate findings even though they proposed the same extracted calculation as the remedy. They also produced separate pricing-test findings. These are mismatches with the agreed report structure, not proof that the existing audit misses code defects.

The focused baseline correctly returned no findings for the clean orchestrator, withheld removal of a callback with unavailable external configuration, and included all 21 supplied independent findings despite its normal 20-finding cap. No improvement in these behaviors is established by that baseline.

## Guided observations

| Behavior | Existing audit | Candidate |
| --- | --- | --- |
| Identifies duplicated pricing, redundant forwarding layers, misleading units, and verified-unused legacy code | 5/5 | 5/5 |
| Identifies the unclear status-label helper name with a maintenance consequence | 3/5 | 5/5 |
| Gives relative effort estimates with reasons | 0/5 | 5/5 |
| Groups pricing extraction, its loading caller, and related test changes into one refactoring finding | 0/5 | 5/5 |
| Retains the registered exporter, normal orchestration guard, and separate normalization concepts | 5/5 | 5/5 |
| Distinguishes source review from test execution and future regression risk from current failure | 5/5 | 5/5 |

The five guided reports each returned five root-cause findings. Their pricing finding included the screen's loaded-quote caller and relevant test changes. Each report preserved existing signatures, integer-cent behavior, and workflow order in its proposed direction. All supplied effort estimates were qualitative and explained by the affected callers or verification work. No candidate revision was needed after the guided runs.

The focused candidate retained both baseline strengths: leaving the clean orchestrator alone and declining to call an externally configured callback dead. It also included all 21 independently established findings, ranked by maintenance impact, with relative effort estimates. Both arms respected the report-only scope. No general superiority in defect detection, completeness, or brevity is claimed. The observed benefit is more consistent application of the maintainability scope and report requirements on these fixtures.

## Packaging and installation checks

- Code Quality 0.1.0 has matching Codex and Claude Code manifests and is registered in both native catalogs. Its bundle contains only `audit-code`.
- The curated catalog contains 19 skills. No installer code, runtime dependencies, upstream pins, or configuration presets changed.
- Skill creator's `quick_validate.py` passed.
- All 73 repository unit tests passed.
- Marketplace validation passed with two catalogs, four custom plugins, seven packaged skills, one preset, and one MCP server.
- Cached Skills CLI 1.7.2 discovered the new skill. Selected portable installations and repeats succeeded for Codex, Claude Code, and OpenCode at global and project scope in disposable roots. All four physical copies matched the evaluated source. Existing skills were preserved, unselected skills were absent, and no personal preset was installed.

## File and folder organization revision (0.1.1)

The revision explicitly covers file splits, merges, moves, renames, and grouping related code and tests according to repository conventions. The skill names that scope in its description and body. It also asks the auditor to trace imports, exports, registrations, configuration paths, build/test discovery, and relative resource paths before recommending a move.

Five fresh agents used the unchanged 0.1.0 skill with the [file-layout tasks](../fixtures/audit-code/file-layout.md), and five used the revision with identical inputs. Every output was read. Both arms recommended a cohesive split into established feature directories, addressed internal and test imports, preserved the public subpath, accounted for job registration and relative assets, and retained the repository's test layout. All ten reports left the cohesive 640-line parser alone. File length and separate test placement did not become automatic findings.

Four guided reports retained a compatibility entry point; one proposed updating the public subpath target and job registration while preserving the exported interfaces. An actual move would still need to verify the full export surface and downstream compatibility. No move was executed in this evaluation. The baseline already handled these cases, so this revision makes an approved scope explicit; no measured capability improvement is claimed.

Both plugin manifests and the plugin README declare 0.1.1. Skill validation, all 73 repository tests, and marketplace validation passed.

## Limits

These are supplied-context behavioral checks and portable file-installation checks. They do not establish native plugin activation, automatic skill selection in authenticated sessions, or quality across a real large repository or other languages. No application code or Linear issues were changed.
