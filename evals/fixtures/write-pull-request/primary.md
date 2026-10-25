# Independent PR tasks

These exercises use synthetic read results and receipts. Do not call live tools, browse, read other files, or mutate anything. For each independent task, return proposed operations with their arguments, the exact PR title/body, and the final user-facing result after the supplied successful receipt. If something prevents saving, return the useful draft or question instead. Proposed operations can be Git commands or structured API calls; do not invent extra evidence.

The PR API creates with `{repo, head, base, title, body, draft}` and updates named fields on an existing PR. A read confirms the saved fields and URL. A private issue attachment can be requested separately; it is not part of PR creation. Relevant read results are complete below.

## A. Retry delay

User: Write a PR for the retry-delay fix. The related Linear issue is OPS-18.

- Repository: `example/http-client`, visibility `PUBLIC`; `origin` resolves to this repository. Target is `main`, as established in this session. No existing PR matches this work.
- Current branch: `alex/ops-18-respect-retry-after`; unpublished, with two intended commits above `origin/main`. There is no branch-name collision. Neither commit message nor changed source contains an issue identifier or tracker URL.
- Commit `a111111111111111111111111111111111111111`: honor a server's numeric Retry-After delay, capped by the configured maximum; retain exponential backoff when the header is absent or invalid. Commit `a222222222222222222222222222222222222222`: regression tests for those cases. The diff contains only that work.
- Uncommitted `notes/next-quarter.md` contains unrelated planning edits and was not requested for this PR.
- At the current head, `npm test -- retry` passed 12 tests and required lint passed. The optional live-service smoke check has not run. Nothing has merged or deployed.
- Repository PR template asks for a short explanation of the problem and change, followed by validation. No mandatory tracking field exists.
- Linear issue: ID `OPS-18`, URL `https://linear.app/example/issue/OPS-18`, `gitBranchName: alex/ops-18-respect-retry-after`. It requests respect for numeric Retry-After, the configured cap, and fallback behavior. No other requirement or settled implementation choice exists.
- GitHub/Linear integration is connected. Branches with issue IDs can link automatically. A manually attached PR can produce a GitHub linkback comment containing the issue ID and URL.
- A successful push publishes only the selected branch and intended commits. Successful PR creation/read returns `https://github.com/example/http-client/pull/81` with the submitted fields. No Linear attachment is reported by that receipt.

## B. Date-valued retry header

User: Draft a PR for the date-valued Retry-After work on OPS-19.

- Independent repository: `example/internal-client`, visibility `PRIVATE`; `origin` resolves here. Session target: `release/2.x`. No existing matching PR exists.
- Current branch: `date-header`, unpublished with one intended commit above `origin/release/2.x`. Linear's supplied branch name does not exist locally or remotely. There are no unrelated edits.
- Linear issue `OPS-19`, URL `https://linear.app/example/issue/OPS-19`, `gitBranchName: alex/ops-19-date-valued-retry-after`. It requests parsing HTTP-date headers, interpreting past dates as zero delay, and retaining the configured cap.
- Current diff parses HTTP-date headers and caps future delays. The past-date case is unfinished: the relevant test fails because a negative delay is returned. Three other focused checks and lint pass. No integration check has run.
- No required PR template exists. The integration is enabled for this private repository.
- A successful push publishes the selected branch. PR create/read returns `https://github.com/example/internal-client/pull/82`, echoing the submitted fields. A subsequent Linear issue read confirms PR #82 is attached. No merge or deployment has happened.
