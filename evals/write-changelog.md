# Write changelog evaluation

Use the synthetic [cases](fixtures/write-changelog/cases.json). Materialize each
case's `files` as a committed disposable repository, then apply `changes` as
the current task's uncommitted work. Supply the request and handoff separately.
No live project data or external services are needed.

Run the three primary cases in five fresh baseline contexts and five fresh
candidate contexts. Both arms see the same requests, files, evidence and
existing Git Workflows skill descriptions. Candidate contexts also see the new
skill description. Let agents choose which bodies to load. Do not supply this
rubric, the interview, or prior results. Agents finish actual local tasks in
separate directories; they do not merely describe hypothetical writes.

Read the baseline output before writing the candidate. Record discovered gaps
and retain existing strengths. Inspect every response, selected skill and file
diff. Counts are observations of these cases, not a general activation rate.

## Primary checks

- `existing`: complete the CSV fix with one clear unreleased entry. Preserve the
  unrelated entry, released history, version and implementation. Omit internal
  tracking references. Describe escaped commas, quotes and newlines accurately.
- `missing`: create a minimal changelog for the changed `--limit` contract.
  Explain that users must omit the option for unlimited results; `0` is invalid.
  Keep release version and publication date unspecified.
- `generated`: follow the documented fragment format for the changed cache
  lifetime. Preserve the generated changelog, existing fragment and versions.

## Boundaries

Run the remaining cases in a separate guided context. Internal refactors need
no entry. Related work updates its existing unreleased entry without duplication.
Text-only drafts and explicit file restrictions remain narrow. Investigations
that deliver no behavior change do not claim a fix. A separate fresh continuation
of an already completed case checks repeat preservation.

For all cases, inspect reader impact, necessary migration instructions, concise
complete sentences, exact identifiers, evidence and uncertainty. Preserve files
outside the task, released history and existing conventions. Do not require
specific wording. No commits, pushes, releases or external mutations are part
of these tasks.

## Packaging

Validate paired manifests, catalog membership, skill structure and repository
checks. Test selected installation and repeat runs in disposable homes for all
three agents, preserving unrelated skills and instruction files. Report actual
host activation separately from skill selection simulations and installation.
