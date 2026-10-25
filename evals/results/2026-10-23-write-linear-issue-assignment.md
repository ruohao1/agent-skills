# Default issue assignment observations

## Change

Linear Workflows 0.4.1 records the requested default: assign new issues to the human invoking `write-linear-issue`. An explicit other assignee or unassigned request wins. Edits retain existing ownership unless reassignment is requested. The connector's `me` alias is used only when it identifies the caller; unresolved identity requires a targeted question before saving.

## Behavioral checks

Five fresh agents used the previous skill with the [assignment task](../fixtures/write-linear-issue/assignment.md); five fresh agents used the revision with the identical task. One additional fresh agent per arm handled the [focused cases](../fixtures/write-linear-issue/assignment-focused.md). Each received only its skill and synthetic fixture, without the evaluation criteria or other outputs. No model override was used. All answers were read manually; proposed primary fields were also parsed independently.

| Behavior | Previous skill | Revision |
| --- | --- | --- |
| Assign a new issue to the verified caller when no assignee is specified | 0/5 | 5/5 |
| Retain scoped Bug content, destination, and simulated saving | 5/5 | 5/5 |

All five controls omitted `assignee`; the simulated server therefore left the issues unassigned. All five revised outputs supplied `"assignee": "me"`, which the fixture resolves to the invoking human. No broader writing-quality improvement is claimed.

Both focused agents respected another named assignee, explicit unassigned (`null`), narrow edits to assigned and unassigned issues, and explicit reassignment. For unresolved caller identity, the control created an unassigned issue; the revision asked which Linear account belonged to the caller and made no save. Neither assigned the integration account.

Existing general and type-focused fixtures now supply a verified caller and support the `assignee` field so future runs can exercise the new default. Earlier reports describe their original inputs, before that identity context was added.

## Verification

- All 65 repository unit tests passed.
- Marketplace validation passed: two catalogs, three plugins, five custom skills, one preset. Both Linear plugin manifests declare 0.4.1.
- Skill creator's `quick_validate.py` passed; the source matches the evaluated candidate bytes.
- Behavioral checks used supplied reads and simulated writes. No live Linear issue was created or reassigned.
- Native-host activation and a live Linear assignment were not tested.
