# Write Linear comment observations

## Agreed behavior

The skill supports requested progress, blocker/question, decision, and completion/handoff comments for human and agent readers. Comments add useful information, distinguish completed work from verification and unresolved decisions, and continue the relevant discussion. Equivalent information returns an existing comment link; edits require an explicit request. Requirement changes remain a separately requested issue-writing task.

Code references use permanent links to the exact commit and supporting lines, beside quoted blocks. A code-dependent comment remains an unsaved draft when the referenced code is uncommitted, unpushed, or otherwise lacks a verified published permalink. Preparing the comment does not publish code. Prose-only comments do not need code evidence.

The permalink format follows GitHub's [file permalink guidance](https://docs.github.com/en/repositories/working-with-files/using-files/getting-permanent-links-to-files) and [line-range permalink guidance](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-a-permanent-link-to-a-code-snippet), inspected on 2026-10-21. The skill supplies a small explicit excerpt and source link; it does not rely on GitHub-specific automatic snippet rendering inside Linear.

## Method

Used the synthetic [primary and focused tasks](../write-linear-comment.md). Five fresh-context control agents received the two independent primary tasks without comment-writing guidance. Five fresh-context guided agents received the same tasks and the candidate skill. The first context in each arm also answered the focused cases after its primary answers. Agents read only their assigned material, with no rubric, prior outputs, or results. No model override was requested. Every output was read manually.

Repository excerpts, remote inspection, discussion records, test results, and successful save receipts were supplied fixtures. Agents proposed operations; no live connector or Git mutations were performed. This exercises decisions from available evidence, not actual source discovery, authentication, pagination, URL accessibility, or API execution.

## Primary results

| Observed behavior | Control | Guided |
| --- | --- | --- |
| Published implementation: reply to the relevant thread | 5/5 | 5/5 |
| Published implementation: full commit permalink and exact lines beside the block | 5/5 | 5/5 |
| Distinguish passing tests from pending browser checks, merge, and deployment | 5/5 | 5/5 |
| Unpublished implementation: retain the code-dependent comment as an unsaved draft | 0/5 | 5/5 |
| Invent no permalink or Git mutation for unpublished code | 5/5 | 5/5 |

All controls already handled published references, thread selection, and evidence well. Each proposed posting the local implementation while clearly disclosing that it was unpublished. For example, control 2's comment says: “This block has not been committed or pushed, so no published source permalink is available.” It nevertheless proposed `{issueId: "APP-43", body: ...}` and reported a simulated save. Controls 1, 3, 4, and 5 made the same decision, without misrepresenting the local source.

This fails the evaluated publishing condition; it does not establish a general rule against transparent local-work updates. The candidate adds a conditional draft rule tied to the availability of the exact published source. All five guided runs proposed no mutation for the local case, retained the requested block in a draft, and identified the missing permalink. Guided 1 explained: “neither the supplied branch URL nor the latest published commit contains it.”

The measured difference is enforcement of that explicit preference. No broader superiority or concision improvement is claimed. Guided 4 repeated the pending browser check in its final sentence; the small fixture sample does not establish optimal editing quality. The candidate required no revision after the guided runs.

## Focused results

Both the control and guided agent preserved the following behavior:

- Returned an existing equivalent comment link without posting or editing.
- Changed only the requested sentence in an existing reply.
- Posted a prose-only blocker without a code-link requirement or unsolicited mention.
- Replied with a settled decision while leaving issue requirements and metadata unchanged; reported the stale description to the user.
- Kept draft-only and disconnected cases unsaved, with available evidence and the missing connector/context stated accurately.
- Read the relevant discussion before considering a retry after an ambiguous save timeout.
- Reported completion of a local coding task without posting to its associated issue.

These are retained baseline strengths rather than demonstrated improvements. The skill's code-link condition did not block the prose-only or requested-correction examples.

## Package and installation checks

- `quick_validate.py` passed for `write-linear-comment`.
- `python3 -m unittest discover -s tests -v`: all 64 tests passed.
- `python3 scripts/validate_marketplace.py`: passed; two matching native catalogs, two plugins, three local skills, and one preset. The curated catalog contains 15 skills.
- Linear Workflows is version 0.2.0 in both native manifests, with issue and comment skills registered in its bundle. No installer logic, runtime dependencies, or existing issue-writing instructions changed.
- The cached, previously verified Skills CLI 1.7.2 discovered all three local skills. Selected only `write-linear-comment` for Codex, Claude Code, and OpenCode in disposable global and project directories. Both installs and both repetitions succeeded. Every installed comment skill matched source bytes; an existing issue skill was preserved. Project installation did not implicitly add the issue skill or product-brief.
- Home, configuration, cache, data, state, and project roots were isolated in the child process.

Native plugin activation, authenticated host execution, and actual Linear reads/writes with this skill remain untested.
