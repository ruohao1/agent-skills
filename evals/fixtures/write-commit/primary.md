# Independent commit tasks

These exercises contain synthetic read results and receipts. Do not call live tools, browse, read other files, or mutate anything. For each task, give the intended sequence of operations, exact commit messages, and final user-facing result after the provided successful receipts. You may specify staging/index operations semantically when exact hunk patches are not supplied. Do not invent patches, identities, validation, or commit hashes. Treat tasks independently.

## A. Two changes and unrelated staged work

User: Write commits for the retry fix and the timeout default we just finished. Leave the next-quarter planning alone.

- Repository `example/http-client` is `PUBLIC`; origin and target project are verified. Current branch `work/client-defaults` is unpublished with no name conflict. HEAD contains no requested changes yet. No repository commit-message convention is documented.
- Session scope is two independent changes: respect a numeric Retry-After delay with the existing cap/fallback behavior; separately change the default timeout from 10 to 30 seconds. Each is independently valid and tested.
- Staged `src/client.py`: retry-delay behavior hunk. Unstaged in the same file: default timeout hunk. No other hunks in this file changed.
- Unstaged `tests/test_retry.py`: regression coverage needed with the retry fix. Unstaged `tests/test_timeout.py`: regression coverage needed with the timeout-default change.
- Staged `notes/next-quarter.md`: unrelated planning changes. Additional unrelated edits in that same file are unstaged. Both versions must remain available after the task.
- Related Linear context: `SDK-31`, URL `https://linear.app/example/issue/SDK-31`, supplied `gitBranchName: alex/sdk-31-client-defaults`. The issue covers both requested changes.
- Contributing coding agent configuration supplies the attribution identity `Fixture Agent <fixture-agent@example.invalid>`. This is a configured synthetic identity, not a suggested commit author. The developer's Git author is already configured; no identity changes are needed.
- Required checks at the current working state: retry tests (12) and timeout tests (4) passed; lint passed. The repository's pre-commit hook reruns relevant checks for the staged content and succeeds for either complete change with its tests. No remote publish was requested.
- Successful commits return, in order, `b111111111111111111111111111111111111111` and `b222222222222222222222222222222222222222`. Reads can confirm each committed patch/message and the remaining staged/unstaged contents.

## B. Private repository and explicit staged scope

User: Commit the staged CSV export fix for DATA-8.

- Independent repository `example/internal-exporter` is `PRIVATE`. Current branch `csv-fix` is unpublished, with no conflict for the issue's supplied name. No unrelated edits exist.
- The staged implementation and tests fix exporting all filtered rows instead of only the current page, retaining a UTF-8 BOM and headers for zero matches. No unstaged changes exist.
- Required test command passed all four export checks; lint and pre-commit hook succeed.
- Repository instructions require an imperative plain-language subject without type prefixes, and a short body only when useful.
- Linear issue `DATA-8`, URL `https://linear.app/example/issue/DATA-8`, `gitBranchName: alex/data-8-export-all-filtered-rows`. No issue mutation is requested.
- Contributing agent's verified attribution identity is `Fixture Agent <fixture-agent@example.invalid>`. The human Git author is configured separately. The host will not automatically append a trailer in this fixture.
- A successful commit returns `b333333333333333333333333333333333333333`. Readback confirms its staged patch, message, and clean remaining state. No remote operation is requested.
