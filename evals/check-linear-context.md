# Linear context evaluation

Compare five fresh baseline contexts with five fresh contexts that also have
`check-linear-context`. Keep personal instructions, the existing three Linear
skills, tool availability, and synthetic fixtures identical. No model override
is used for these samples. Do not reveal criteria or earlier outputs.

First present only skill descriptions and the [discovery cases](fixtures/check-linear-context/discovery.json).
Record selected skills and the next actions before exposing the
[execution cases](fixtures/check-linear-context/execution.json). A guided
sample can load a skill it selects; do not force invocation of the new skill.
The execution section supplies observations and checks handling, not actual
connector access. Outputs belong in a temporary directory. No external writes,
real issue reads, or repository changes are authorized by the evaluation.

## Criteria

- A new project session, resumed session, and new substantial task within a
  session cause a relevant Linear read before implementation. In the guided
  arm, check that the skill is selected from its description.
- A continuation of the same fresh task and an explicit text-only correction
  do not cause redundant external reads.
- A newer decision and incomplete discussion lead to targeted follow-up, not
  blind reliance on an old summary. Surface a conflict with the user's request.
- Existing work is not duplicated or claimed. Follow an older direct dependency
  even when a recent-activity window would omit it.
- Ambiguous project names are not treated as a verified match. Ask one focused
  question and continue independent local work.
- An unavailable optional shared-notes tool does not block ordinary issue and
  comment reads. Authentication failures remain an explicit knowledge gap.
- Once relevant context is established, stop the scan and continue the task.
  Do not read the entire workspace or announce certainty about unseen work.
- All checks remain read-only. Private Linear context stays out of public
  artifacts. Output reports only material findings, sources, and limitations.

Read every output manually and retain exact evidence. Report observed changes
and variance without claiming universal automatic invocation or live host
behavior. If the baseline shows no useful gap, do not invent one.

## Packaging and deployment

Run skill validation, the full unit suite, and marketplace validation. Verify
Skills CLI discovery, isolated installation for all three agents, preserved
unrelated files, and repeated setup. Check the live selected installation only
after those pass. Do not modify personal instructions or the other skills.
