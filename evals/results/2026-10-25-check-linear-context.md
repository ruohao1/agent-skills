# Linear context check results

Date: 2026-10-25.

## Method

Five fresh baseline agents received the existing three Linear skills and the
personal preferences. Five fresh guided agents received the same inputs plus
`check-linear-context`. No model override was used for these samples. Each
agent first saw only the available descriptions and five independent discovery
cases. It recorded skill selection and intended calls before seeing seven
execution cases with supplied observations. The guided agents could load a
skill they selected; no prompt explicitly invoked the new skill.

All 120 case responses were read manually. These are simulated decisions, not
actual connector calls or authenticated host conversations. The
[protocol](../check-linear-context.md) and fixtures are reusable. Raw outputs and local snapshots are not distributed.

## Observed gap and change

One baseline agent skipped Linear in the new-session case with a demo deadline
and a two-file handoff. Its reason was: “The two named files provide a concrete
starting point under the demo deadline.” That failure was observed before the
candidate skill was written. Remaining baseline runs used frozen original
inputs; they could not see the candidate.

| Observation | Baseline | With skill |
| --- | --- | --- |
| Read Linear before editing in the new-session case | 4/5 | 5/5 |
| Explicitly read recent project updates in that case | 2/5 | 5/5 |
| Refresh related Linear context for a new task in the same session | 5/5 | 5/5 |
| Refresh related Linear context when resuming after three days | 5/5 | 5/5 |
| Select the new skill from its description for all three intended triggers | Not available | 5/5 |
| Avoid redundant reads for the same-task continuation | 5/5 | 5/5 |
| Honor the text-only correction without external reads | 5/5 | 5/5 |

All guided discovery runs combined a small recent-activity scan with searches
for related active and completed work without a date cutoff. They followed
relevant discussion and older direct dependencies. The baseline already handled
the supplied execution cases well: changed decisions, partial comments,
overlapping drafts, ambiguous project matches, failed access, optional tool
failure, and private information in public output. The new skill is not claimed
to introduce those existing reasoning capabilities.

The observed benefit is a more consistent initial check and broader project
activity retrieval in this small synthetic sample. It does not establish a
universal success rate, lower task time, or guaranteed invocation across hosts.

## Packaging and installation checks

- Skill validation passed.
- All 73 repository unit tests passed.
- Marketplace validation passed for two catalogs, four plugins, eleven custom
  skills, one preset, and one MCP selection. Linear Workflows is `0.5.0` in
  both manifests; the full selection now has 23 skills.
- The first manifest check caught four Codex starter prompts where the schema
  allows at most three. The redundant comment example was removed; validation
  then passed. No existing comment skill behavior changed.
- Skills CLI `1.7.2` installed the selected skill in separate disposable global
  homes for Codex, Claude Code, and OpenCode. All copies matched source bytes.
  Repeated setup preserved bytes and modification times. Unrelated sentinel
  skills stayed unchanged; no shared instruction files were installed.

## Review

An independent reviewer found no issues in scope, privacy, packaging, or the
reported discovery counts. The reviewer verified the candidate against the
evaluated snapshot and repeated marketplace validation. It did not repeat the
unit suite, installers, or every execution case.

## Limits

The skill uses normal description-based selection, with no startup hook or
shared-instruction change. It needs a working Linear connection and a verified
project association. A failed or partial lookup leaves an explicit gap. The
skill cannot reveal work that has not been recorded.

Native plugin activation and automatic invocation inside fresh authenticated
Codex, Claude Code, and OpenCode conversations remain untested. The context
checks did not post comments or modify live Linear data.
