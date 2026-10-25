# Code Quality

Version **0.2.0** provides three independent audits and one coordinator:

| Skill | Purpose |
| --- | --- |
| [audit-code](skills/audit-code/SKILL.md) | Keep code readable and easy to change as it grows. Review responsibilities, duplication, boundaries, and file and folder organization. |
| [audit-scale](skills/audit-scale/SKILL.md) | Find failures caused by growing data, concurrent work, retries, and interruptions, including within one process or at low traffic. |
| [audit-security](skills/audit-security/SKILL.md) | Trace security risks in application code, dependencies, CI, deployment configuration, and secret handling. |
| [audit-repo](skills/audit-repo/SKILL.md) | Run the three companion audits and combine their findings into one report. |

Each reviews the whole repository by default, or a named area. Reports include all supported findings, grouped by cause, with verified locations, the consequence, the smallest useful change, and relative effort. Scaling and security also state confidence separately from priority. Missing evidence remains explicit; a clean result is valid.

File and folder refactors must preserve imports, exports, registrations, configuration, assets, and build/test discovery. Scaling preserves required results and ordering; it excludes standalone performance problems unrelated to growth, concurrency, or recovery. Security separates an affected dependency from an established application exploit path. Combined audit reports merge shared causes and retain each consequence.

Audits save dated reports in `docs/audits/` inside the audited repository. Combined reports use `YYYY-MM-DD.md`; standalone reports use `YYYY-MM-DD-code.md`, `YYYY-MM-DD-scale.md`, or `YYYY-MM-DD-security.md`. A combined run saves only one report. New runs preserve existing reports with a numeric suffix. An explicit destination or chat-only request overrides the default.

New reports are ignored by Git unless tracking is requested or already established. Audits reuse effective ignore rules or add a literal entry for the report to `.gitignore`. Existing tracked files, explicit include exceptions, and other files' ignore status are preserved. Audits do not stage, commit, or untrack files. Chat-only output and reports outside Git need no ignore edits.

Applying fixes and creating issues require their own requested scope. Scaling and security can use bounded checks in disposable environments; sustained load tests and active tests against deployed systems need separately agreed targets and limits. No skill adds a connector, runtime dependency, or personal configuration requirement.

Install the complete set from this checkout:

```sh
python3 scripts/setup.py install --plugin code-quality --agent codex --scope global
```

The shared repository route is:

```sh
npx skills@latest add ruohao1/agent-skills --skill audit-code audit-scale audit-security audit-repo --agent codex claude-code opencode
```

For the complete native plugin on Codex or Claude Code, select `--plugin code-quality --route native`. Choose one installation route to avoid duplicate copies. See [setup](../../docs/setup.md) and the [coverage comparison with Ponytail](../../docs/audit-coverage.md).

The three focused audits can be installed individually. `audit-repo` requires all three companions; selecting only its directory does not install them automatically. If a companion is missing, it runs the available passes and marks coverage incomplete.

Evaluation tasks and recorded observations:

- [Maintainability](../../evals/audit-code.md) and [results](../../evals/results/2026-10-24-audit-code.md).
- [Runtime scaling](../../evals/audit-scale.md) and [security](../../evals/audit-security.md), with [comparison results](../../evals/results/2026-10-24-runtime-security-audits.md).
- [Combined reports and storage](../../evals/audit-repo.md), recorded in the same comparison results.
