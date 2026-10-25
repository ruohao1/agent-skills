# Concise issue body observations

## Change

The issue writer now uses short factual Context bullets and states each requirement once. Scope and acceptance share a checklist when separate sections would repeat the same outcomes. Verified plans can carry implementation detail; the issue retains its outcome, consequential constraints, and observable completion checks. Unavailable references remain unverified, and known requirements remain in the issue. Before saving a rewrite, the writer compares it with the original for missing context, requirements, failure cases, and delivery details. Narrow corrections retain their original format.

The change was evaluated as Linear Workflows 0.4.2. A concurrent STE-inspired prose change advances the package to 0.4.3; it preserves these instructions.

## Comparison

The control reuses the five 0.4.1 guided outputs from the [assignment evaluation](2026-10-23-write-linear-issue-assignment.md). Before editing, the current skill was verified byte-for-byte against that evaluation's candidate. Five fresh agents then received the revised skill and the identical [assignment task](../fixtures/write-linear-issue/assignment.md), without prior outputs or grading criteria. No model override was used. All outputs were read manually.

| Behavior | Previous skill | Initial concision revision | Final combined skill |
| --- | --- | --- | --- |
| Context uses factual bullets | 0/5 | 5/5 | 5/5 |
| Omits a redundant standalone scope paragraph | 0/5 | 5/5 | 5/5 |
| Retains keyboard activation, existing action, mouse behavior, appearance, and verified pointer | 5/5 | 5/5 | 5/5 |
| Assigns the verified caller and uses the authorized destination, Bug label, and simulated save | 5/5 | 5/5 | 5/5 |

Description word counts were 89, 100, 99, 93, and 84 for the control; 62, 65, 62, 53, and 58 for the initial revision; and 59, 48, 56, 58, and 49 for the final combined skill. Medians were 93, 62, and 56. Counts split on whitespace after removing leading Markdown heading, bullet, and checkbox markers. They describe this small fixture, not a length limit or evidence about all issues. Some revised outputs still repeat the click-only fact briefly in their source bullet.

## Focused cases

One additional fresh agent used the [focused cases](../fixtures/write-linear-issue/concise-focused.md). The complex case retained automatic analysis, cache identity and validation, offline hits, concurrency and navigation guards, privacy, deployment constraints, migrations, real-model evidence, delivery requirements, and exclusions. It marked the unavailable plans and tentative timeout as unverified rather than treating the timeout as settled.

The verified-design case retained observable create, restore, rename, and delete checks, reload persistence, ownership, access rules, and exclusions. It linked the supplied immutable design without copying schema or endpoint details. The narrow correction changed only the requested sentence, preserving the prose Context and all omitted metadata.

## Combined-source check

A fresh compatibility sample used the combined concision and STE-inspired instructions. Its simple issue, verified-design case, and narrow correction kept the expected behavior. The complex issue preserved the guard against overwriting newer results but omitted its explicit protection for newer attempts still in progress. The generic instruction to preserve requirements was replaced with a final comparison against the original.

Five fresh agents then used the final combined skill with both fixtures. All five retained the explicit guard for newer attempts and results, the other complex-case requirements, the verified design link and its essential scope, and the exact narrow correction. All outputs were read manually. Independent parsing confirmed the create fields and caller assignment, description-only updates, and the exact corrected description. These small supplied-context checks do not guarantee that every future rewrite preserves every requirement.

## Verification

- All 65 repository unit tests passed with the combined 0.4.3 source.
- Marketplace validation passed: two catalogs, three plugins, six custom skills, one preset. Both Linear manifests declare 0.4.3.
- Skill creator's `quick_validate.py` passed.
- The source matches the final evaluated snapshot byte-for-byte.
- Behavioral checks use supplied reads and simulated writes. They do not establish automatic skill activation or live connector behavior. No live Linear issue was changed for this evaluation.
