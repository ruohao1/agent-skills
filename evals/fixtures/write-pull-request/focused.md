# Independent focused PR tasks

Synthetic exercises only. Do not use live tools or mutate anything. For each case, give the next operations and concise user-facing result. Successful writes are confirmed only when the case supplies a receipt.

1. User: "Draft the PR text here; don't publish." Public repository, neutral branch, intended diff adds an optional timeout with regression coverage. Tests passed. No base branch has been selected. Return the title/body and any operation needed.

2. User: "Write the PR for ENG-7." Repository lookup returned `full_name: example/tool` without visibility; a second permitted lookup cannot determine it. The intended source `fix/timeout` and base `main` are known, the branch is already published, all messages/source are free of tracker references, no matching PR exists, checks passed, and create/read access is available. The issue URL and generated branch `sam/eng-7-timeout` are available. A save would return `https://github.com/example/tool/pull/7`.

3. User: "In PR #12, change only 'Browser check passed' to 'Browser check pending'." Private repo; published branch `legacy-retry`, base `main`; a Linear issue supplies another branch name. Existing PR is ready, with title "Honor retry delay" and body "Honor the header. Browser check passed. Keep the existing deployment note." The updated PR receipt confirms only the requested sentence changed. No source/branch mutation or validation run is requested.

4. User: "Write a PR for this fix." Public repository, neutral published source and clean history; both `main` and `release/2.x` are supported targets. Neither session nor repo instructions settle the target, and the diff applies to both. Ask only what is needed before creating.

5. A private PR create request timed out after submission. Source, base, and intended body are known. Read/search tools remain available; no reconciliation read has happened. State the next operation, without assuming either success or failure.

6. User: "Write the PR." Public repository, neutral source `fix/retry`, unpublished commit message `fix: respect retry delay (OPS-18)`, correct target known. The user has not requested amending or rewriting history. Explain the next action before any push.

7. User: "Write a PR for the finished change." The local diff and test results are available, but GitHub authentication is unavailable and destination repository/target cannot be verified. No remote write can succeed. Return the useful result without inventing a URL or completed publication.
