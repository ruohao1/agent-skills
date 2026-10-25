# STE-inspired writing observations

## Scope

The evaluated style uses STE-inspired principles for clear English prose, with no strict dictionary enforcement. Each of the six maintained skills contains its own guidance. The optional personal preset carries the same style for general replies across Codex, Claude Code, and OpenCode.

## Method

Five fresh baseline agents received the original instruction snapshots and eight [synthetic tasks](../fixtures/ste-writing.json). Five fresh guided agents received the same snapshots with only the style paragraph added. Each case used its relevant skill, or the personal instructions for the general reply. Agents received no grading criteria, prior outputs, or comparison conclusions, and made no external updates. No model override was used for the samples. All 80 responses were read manually; exact artifacts were also compared mechanically.

A concurrent edit changed the Linear issue layout during this work. The comparison held that workflow fixed at the baseline version. A fresh reviewer also exercised the actual combined skill: its 109-word response retained the receipt outcomes and request identifier, used factual Context bullets, and combined scope with acceptance checks. A later concurrent sentence strengthened requirement preservation; it was inspected and synced without changing the style paragraph.

## Writing observations

Both variants preserved the supplied facts and uncertainty. The baseline prose was already generally clear, with some longer sentences joining related points. The baseline did not establish a missing capability that the new paragraph fixes.

| Observation | Baseline | With guidance |
| --- | --- | --- |
| Facts and uncertainty retained across all eight cases | 5/5 runs | 5/5 runs |
| Exact command, error quotation, code permalink, and comment link retained | 5/5 | 5/5 |
| French spelling correction remained exact and narrow | 5/5 | 5/5 |
| Public commit omitted internal tracking and retained attribution | 5/5 | 5/5 |
| PR stated receipt lookup and manual review in separate sentences | 0/5 | 4/5 |

The last observation shows a limited change in sentence structure. It does not establish that readers understand the text better. The paragraph defines a style; it is not presented as a new capability or a general measured improvement. All cases use one receipt/timeout scenario, so broader writing quality remains unmeasured.

## Packaging and installation

- Repository checks passed: 65 unit tests; marketplace validation for two catalogs, three plugins, six skills, and one preset.
- The paired plugin versions are Product Design 0.2.1, Git Workflows 0.2.1, and Linear Workflows 0.4.3. The latter preserves concurrent issue-writing changes.
- A fresh review found no issues in the guidance, standalone packaging, or preservation of existing workflow instructions.
- Actual Skills CLI 1.7.2 installed each of the six skills separately in disposable global environments for all three agents. Each run copied exactly the selected skill, retained an unrelated skill, and installed no personal instructions. A separate project-scope PR-skill installation also matched the source.
- Disposable preset checks verified previews, the OpenCode fallback conflict, preservation after explicit reconciliation, backups, and unchanged bytes and modification times on repeat.

The reusable cases, protocol, and observations are in the repository. Raw samples and installer logs are not distributed. These retained checks do not verify authenticated host behavior. No live GitHub or Linear content was changed by these evaluations. No formal ASD-STE100 compliance is claimed.
