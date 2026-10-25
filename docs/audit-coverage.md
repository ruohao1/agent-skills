# Audit coverage

The custom audits provide separate views of a repository. Ponytail provides a broad audit. The table describes their intended focus; it does not measure detection quality or imply that an agent cannot notice a problem outside that focus.

| Concern | Custom audit | Ponytail audit |
| --- | --- | --- |
| Readability, responsibilities, duplication, file and folder organization | `audit-code` | Covered by its lean-code and refactoring review |
| Growing data, queries, memory, queues, and workload | `audit-scale` | Covered by scale and speed review |
| Concurrent workers, retries, interruption, and recovery | `audit-scale` | Covered by correctness, data loss, and scale review |
| Security in code, dependencies, CI, deployment, and secret handling | `audit-security`, with explicit evidence and advisory rules | Broad security and risk review; it reads dependency and deployment context |
| General bugs unrelated to the focused scopes | No dedicated custom audit | Explicit bug review |
| Standalone latency or speed problems unrelated to growth, concurrency, or recovery | No dedicated custom audit | Explicit speed review |
| Regression checks | Included with each relevant custom finding | Also a dedicated missing-test category |

The custom suite therefore leaves general correctness and standalone performance as gaps in its dedicated coverage. Ponytail remains useful for a broad repository health check. A security consequence and a scaling consequence can share one cause; combined reports should merge that cause while retaining both consequences.

`audit-repo` is the combined entry point. It loads the three custom audits for the same scope, reuses verified context, and merges shared causes into one report. It adds coordination, not a fourth audit purpose. Install the full Code Quality bundle so its companion skills are available; missing passes make coverage incomplete.

## Report differences

All three custom audits request every supported finding, grouped by cause, with verified locations and relative effort estimates. The scaling and security audits also separate confidence from impact and likelihood. They use compact finding headings and four short bullets.

The compared Ponytail instructions use Must fix, Should fix, and Nice to have groups, with a default maximum of 20 findings. They explain the problem, proposed fix, and consequence of deferral. User instructions can override that default cap; the earlier maintainability check observed Ponytail reporting all 21 requested findings.

The custom audits save reports under `docs/audits/` in the audited repository by default. Combined reports use `YYYY-MM-DD.md`; standalone reports add `-code`, `-scale`, or `-security` before `.md`. New runs preserve existing reports; callers can request another location or chat-only output. Ponytail returns a report without this storage convention. Applying fixes or creating issues needs the corresponding requested scope. The two new focused audits allow bounded verification in disposable environments; sustained load tests and active tests against deployed systems need separately agreed targets and limits.

New custom reports are ignored by Git by default. Effective ignore rules are reused; otherwise, the audit adds an entry for that report alone to `.gitignore`. Requested tracking, already tracked reports, and explicit include exceptions take precedence. Other files' ignore status is preserved, and audits do not stage, commit, or untrack files.

## Evidence

The [maintainability observations](../evals/results/2026-10-24-audit-code.md) cover `audit-code` against installed Ponytail 5.3.2. Both found the main seeded problems. The demonstrated benefit was more consistent grouping and effort estimates, with no claim of general superiority in bug detection.

The [runtime and security comparison](../evals/results/2026-10-24-runtime-security-audits.md) records the separate, matched-input comparisons for the new skills, including report-length changes and remaining limits. These supplied-context evaluations do not establish effectiveness on large real repositories, live deployments, or untested languages. They also do not measure the cost or coverage of one combined three-skill audit against a single broad Ponytail run.
