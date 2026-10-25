# Independent focused commit tasks

Synthetic exercises only; no tool execution or file mutation. Give the next operation or concise response for each case.

1. User: "Write only a commit message for the staged timeout fix; don't commit." Public repository, neutral branch, tests passed, Conventional Commits required. Verified contributing agent: `Fixture Agent <fixture-agent@example.invalid>`. The associated Linear issue is SDK-31.

2. User: "Commit the retry fix." Scope and required checks are clear and passed, but the contributing agent's exact attribution identity cannot be established from available configuration or documentation. The human author's identity is configured. State what is needed before committing.

3. A requested commit's required pre-commit hook failed on a relevant test. No commit was created. The user has not requested bypassing hooks or fixing additional code. State the next step.

4. A required formatting hook changed a selected source file and then stopped the commit. No commit was created. An unrelated file is already staged. State how to proceed without broad staging or bypassing the hook.

5. User: "Commit this." Two unrelated changes from different collaborators are present; neither conversation context nor the user's wording identifies which one. Both are staged, and no work has been attributed to the current task. State the necessary question.

6. User: "Amend only the last commit's subject to 'Fix retry delay'. Keep the body and trailers." Its unpublished message body contains a migration note and one correct agent co-author trailer. No file changes are requested. State the operation and preservation requirements.

7. User: "Commit the staged fix for DATA-8." Private repository, already-published branch `release-csv-fix` with an open PR. The issue supplies a different branch name. Scope, checks, identity, and staged patch are verified. No push or branch migration is requested.

8. User: "Commit the completed fix for SDK-31." Repository visibility cannot be established, but the repository and intended neutral branch are known. Scope, checks, and attribution identity are verified. The issue provides a Linear branch name. State the branch/message/linking rule to apply.
