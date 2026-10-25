# STE-inspired writing preference

Use the [synthetic cases](fixtures/ste-writing.json) to compare the existing instructions with the approved style paragraph. The cases cover all six maintained skills, a general reply, and a narrow French edit.

Run five fresh samples per variant. Give each evaluator only the relevant instruction snapshot, the case, and its permitted text-only output. Standalone skill cases must not receive the personal preset. Keep workflow instructions identical between variants so unrelated changes cannot explain differences.

Read every response. Check whether the prose is clear and connected, whether facts and uncertainty survive, and whether exact commands, identifiers, quotations, and links remain intact. Check the existing skill rules: private tracking stays out of public commit text, source inspection stays distinct from live verification, explicit draft requests cause no external action, and a narrow non-English correction remains narrow.

Sentence length is diagnostic, not a compliance threshold. Do not count punctuation mechanically as proof of clarity. A baseline that already reads clearly is a valid result. Describe the configured style without claiming a measured improvement that the comparison does not establish.

Verify the actual final skills separately when another edit changes their workflow during the comparison. Run the repository checks and test individual installations in disposable environments, preserving unrelated files. Separate these observations from live host loading and formal ASD-STE100 compliance, neither of which these tasks establish.

See the [results](results/2026-10-24-ste-writing.md).
