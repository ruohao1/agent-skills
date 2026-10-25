# Runtime scaling, security, and combined audit observations

## Detection comparison method

Each focused audit used five fresh contexts with installed Ponytail 5.3.2 and five with its candidate, on an identical supplied-context task. The scale report recipe needed one revision, which received another five fresh runs. Separate fresh contexts handled the focused counterexamples once per instruction variant. Agents received the task and selected instructions, without the rubric, design, previous answers, or expected findings. No model override was used. Every report was read manually.

The baseline is the installed `ponytail-audit` skill, SHA-256 `2b3223a02c386d1263e1b08343cb8eb3a53e444cdafb1d79e26c8ec2a8fcad28`. Equivalence with the catalog's pinned upstream revision was not checked. This is an existing-workflow comparison, not an unaided-model benchmark. Raw reports and manual notes are not distributed; this record preserves the observations and links the repeatable tasks.

The supplied Python snippets parse, and the security workflow YAML parses. Separate bounded in-memory checks confirmed overlapping credit approval, duplicate delivery after a lost acknowledgement, a stranded claimed export, per-event owner queries, cross-account reads, and SQL injection. The two SQLite checks used valid UUIDs and search input within the supplied length limit. Those checks validate fixture mechanisms; they were not runs performed by the evaluating agents or tests of a deployed application.

## Runtime scaling

The [primary task](../fixtures/audit-scale/primary.md) includes five supported mechanisms: a credit reservation race, duplicate external delivery after an uncertain result, interrupted exports that remain claimed, full-history materialization, and per-event owner queries. It also includes a useful bounded cache and an unavailable ordering guarantee.

| Observed behavior | Ponytail | Final `audit-scale` |
| --- | --- | --- |
| Finds all five mechanisms | 5/5 | 5/5 |
| Gives relative effort with reasons | 0/5 | 5/5 |
| Gives a separate confidence field for each finding | 0/5 | 5/5 |
| Groups related regression checks with their finding | 1/5 | 5/5 |
| Preserves the bounded cache | 5/5 | 5/5 |
| Avoids invented checks, capacity measurements, and observed outages | 5/5 | 5/5 |

Four baseline reports include a separate, conditional ordering-contract concern. They acknowledge that actual adapter ordering is unknown. This is not a demonstrated ordering failure, nor is every mention a false positive. The final custom reports keep the missing guarantee among unverified leads. No core detection improvement is established.

The [four focused cases](../fixtures/audit-scale/focused.md) cover a correct bounded worker, unrelated standalone latency, an unknown host contract, and a growth mechanism with only a production URL available. Both the baseline and both custom variants handled all four: they retained the clean example, respected scope, kept missing evidence explicit, and avoided active production tests or invented thresholds.

The first custom report recipe was too verbose. Its five reports contained 1,565, 1,503, 1,629, 1,608, and 1,551 whitespace-separated words. Replacing expanded fields with a heading and four short bullets reduced the final counts to 1,024, 994, 1,050, 1,108, and 934. Baseline counts were 1,096, 1,208, 959, 959, and 919. Median length fell from 1,565 to 1,024, about 35%; the final median remains about 7% above Ponytail's 959 while including explicit confidence and effort.

## Security

The [primary task](../fixtures/audit-security/primary.md) includes missing report ownership authorization, SQL injection, bearer-token logging, untrusted pull-request tests with privileged CI credentials, and a confirmed affected archive dependency. All packages and advisory results are synthetic. The host archive input path and live gateway settings are unavailable.

| Observed behavior | Ponytail | `audit-security` |
| --- | --- | --- |
| Finds all four code/configuration causes and the affected dependency | 5/5 | 5/5 |
| Separates confirmed dependency applicability from unknown application exploitability | 5/5 | 5/5 |
| Rejects stale scanner severity for the unaffected package | 5/5 | 5/5 |
| Preserves the protected profile route | 5/5 | 5/5 |
| Gives relative effort and separate confidence for each finding | 0/5 | 5/5 |
| Groups related regression checks with their finding | 0/5 | 5/5 |
| Avoids invented execution, compromise, and live exposure claims | 5/5 | 5/5 |

All baseline reports added a separate testing finding. Their dependency priority groups varied, but each qualified application exploitability; a group label alone is not an exploit claim. The custom reports preserved the baseline's substantive strengths and changed report structure. No detection superiority is established.

Both arms handled all [five focused cases](../fixtures/audit-security/focused.md): a protected route, unknown advisory conditions, an affected build dependency, secret redaction with a production-only endpoint, and a shared upload cause. They retained the clean route, kept uncertain conditions unresolved, did not ignore CI dependency risk, omitted the supplied token, avoided production testing, and merged the upload consequences.

Baseline word counts were 948, 1,039, 928, 904, and 1,017; custom counts were 1,029, 905, 1,094, 1,005, and 1,022. The custom median of 1,022 is about 8% above the baseline's 948. Explicit confidence and effort improved consistency, not brevity.

## Combined entry point and report storage

`audit-repo` loads the three custom audits, shares scope and verified context, and saves one combined report under `docs/audits/`. The focused skills gained the same default storage convention. Their audit instructions before the storage section remained unchanged; the detection comparisons above preceded this delivery change.

Five fresh baseline contexts used the existing three audits on the [combined task](../fixtures/audit-repo/primary.md). All identified document authorization, unbounded upload buffering, and duplicated pricing policy. They already merged the upload's scaling and security consequences. None saved a new repository report. Five fresh contexts used the first coordinator and storage variant on the same task. All preserved detection and grouping, saved exactly one suffixed report, and preserved the seeded user report and application files.

Two first-variant replies echoed the saved report in chat, and two saved reports used machine-specific absolute source links. The delivery recipe was revised to specify the short final reply and repository-relative source references. This is a presentation revision, not a detection improvement.

Five further fresh contexts used the final guidance on the identical combined task. All five retained the three findings and shared-cause grouping, saved one numerically suffixed report, preserved all existing files, and used repository-relative source references. All five replies linked the report without repeating its body. File inventories and byte comparisons independently confirmed the writes and preservation. Suffixes varied between `-1` and `-2`; the convention requires a distinct numeric suffix, not one starting number.

The [focused tasks](../fixtures/audit-repo/focused.md) checked unavailable companions and standalone storage. The baseline already made missing security coverage explicit. The coordinator preserved that behavior, saved an incomplete report, and did not install anything. The first storage variant saved each of the three standalone audits with a numeric suffix, preserved existing reports, and left the chat-only repository unchanged. Every response and saved report was read.

A fresh context repeated all four standalone tasks with the final delivery recipe. All three saved reports used relative source references and compact linked replies; the chat-only task saved nothing. File inventories and byte comparisons confirmed preservation. Explicit report updates, custom destinations, and write-failure handling were not exercised. These checks validate instruction-following in this runtime, not native skill invocation in each supported host.

## Packaging and installation checks

- Code Quality's paired manifests declare 0.2.0 and the same metadata. Its bundle contains `audit-code`, `audit-scale`, `audit-security`, and `audit-repo`.
- The curated catalog contains 22 skills, including ten custom skills across four plugins. Upstream pins, installer version, presets, and installer runtime code are unchanged.
- All 73 repository unit tests passed. Marketplace validation passed with two catalogs, four plugins, ten skills, one preset, and one MCP server. All four audit skills passed frontmatter validation.
- Cached Skills CLI 1.7.2 discovered the skills. Individual installs and repeat installs passed for Codex, Claude Code, and OpenCode at global and project scope in disposable directories. All 16 physical copies matched the final source. Existing skills were preserved, unselected skills were absent, and no preset was installed.
- Installing only `audit-repo` did not install companions implicitly. The documented complete-bundle route supplies them explicitly; the coordinator's missing-companion behavior was checked separately.
- Markdown links and whitespace were checked. No active/global installation, commit, push, PR, or native host activation was performed for this change.

A fresh independent reviewer inspected all 25 changed or new files, checked final snapshot equality, catalog counts, the baseline hash, and report word counts, and sampled raw reports. The review found no material issue or required fix. It did not rerun installers or independently rescore every report; the author read every evaluation output as described above.

## Filename simplification

After those checks, the filename convention changed to `YYYY-MM-DD.md` for combined reports and `YYYY-MM-DD-code.md`, `YYYY-MM-DD-scale.md`, or `YYYY-MM-DD-security.md` for standalone reports. The four skill changes are limited to these filename literals. The prior installation and review observations refer to the earlier names; collision and output-override instructions are unchanged.

One fresh context delivered supplied completed results in five disposable repositories: one combined audit, three standalone audits, and one chat-only case. It saved `2026-10-24-2.md`, `2026-10-24-code-2.md`, `2026-10-24-scale-2.md`, and `2026-10-24-security-2.md`. Readback and file inventories confirmed that each existing report and source file remained unchanged, the combined run saved no child reports, and the chat-only case saved nothing. Every output was read. This checks delivery, not a new audit or detection comparison.

All 73 unit tests, marketplace validation, and the four skill validators passed again. Full audits, installer runs, and the independent review were not repeated for this filename-only change. Active installations and previously generated reports were not changed.

## Git tracking default

The delivery requirement is to ignore generated audit reports in Git unless instructed otherwise. A fresh baseline context delivered a combined report using the prior skills in a disposable Git repository. The report was untracked and unignored, and the existing `.gitignore` was unchanged. This established the missing delivery behavior.

The four skills now inspect tracked state and effective ignore rules, reuse existing exclusions, or append an anchored literal entry for the report. Tracking requests, existing tracked reports, and explicit include exceptions take precedence. The instructions preserve other files' ignore status and prohibit staging, committing, or untracking as part of an audit.

Two fresh contexts delivered supplied completed results across the nine [Git tracking cases](../fixtures/audit-repo/focused.md#git-tracking). Every response and saved artifact was read. Independent checks with `git check-ignore --quiet`, `git ls-files --stage`, file inventories, and content comparisons confirmed:

- Default output became ignored through one scoped entry, including when the prior ignore file had no final newline.
- Effective existing exclusions and explicit include rules were preserved without duplicate entries.
- An existing tracked report was updated without changing its index entry. Explicit tracking requests left new reports unignored and unstaged.
- The custom filename containing brackets was ignored literally; a nearby filename that could match an unescaped pattern remained visible.
- A report under an ignored directory became trackable through narrow exceptions while the other report files stayed ignored.
- Non-Git delivery created no ignore configuration. Chat-only delivery changed no repository files.

All nine cases preserved existing source, unrelated notes, and index entries. Local probing also confirmed that verbose `git check-ignore` can return a negated match with exit status zero; the guidance uses quiet mode to verify actual exclusion. All 73 unit tests, marketplace validation, and the four skill validators passed. This is a delivery check using supplied results, not a repeat of the detection comparisons. Linked worktrees, nested ignore files, Windows behavior, and ignore-write failures were not exercised. No active installation or change to this marketplace's ignore configuration was made.

## Coverage conclusion

The demonstrated benefits are consistent grouping, effort estimates, and explicit uncertainty. Ponytail already found the seeded runtime and security problems. The earlier [maintainability comparison](2026-10-24-audit-code.md) is a separate experiment; its results are not pooled into these counts.

The [coverage guide](../../docs/audit-coverage.md) distinguishes intended scope from measured behavior. General bugs and standalone performance remain broader Ponytail coverage. These tests do not measure one combined three-skill audit against one broad Ponytail run, total token cost, large-repository discovery, other languages, real advisory lookup, or native host activation.
