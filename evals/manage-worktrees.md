# Manage worktrees evaluation

Use the synthetic [cases](fixtures/manage-worktrees/cases.json) to compare existing worktree guidance with the candidate. Run five fresh contexts per arm. The baseline inventory contains the installed worktree setup/finish skills and Git Workflows commit/PR skills. The candidate adds manage-worktrees. Each respondent selects skills from names and descriptions, reads selected files, and records concrete proposed actions and a user-facing response. It must not mutate a live repository or service.

Read all responses, not just keyword matches. Score against the fixed criteria. Report differences in defaults as policy effects, not proof that the baseline cannot use Git. Do not claim improved safety for boundaries both arms already handle.

Use additional narrow cases for read-only work, blocked creation, an original checkout with unrelated changes, conflicting activity, retained review work, and safe merged cleanup. Run actual operations in separate disposable repositories to verify worktree placement, base selection, exclusions, repeat behavior and preservation. Commands proposed in a simulation do not count as execution evidence.

Record skill hashes, Git/tool versions, sample counts and failures. Keep raw artifacts outside the repository. A successful install or simulated decision does not prove live host discovery, atomic coordination or cross-platform support.

## Disposable execution fixtures

Use separate repositories for these four cases. Each starts on `main`, uses a synthetic local Git identity and needs no external service. Repository instructions select `python3 -m unittest discover -s tests -v` and forbid unrequested commits. The initial implementation is `def normalize_count(value): return value or 50`. Existing tests check `None → 50` and `7 → 7`. The requested fix adds `0 → 0`.

- **New task:** clone a local bare origin, then advance its default branch with a marker file without updating the clone. Add an unrelated local exclusion. Request the zero fix and verify task placement, the newer base, original-checkout preservation and exclusion preservation.
- **Resume task:** create an active theme worktree with an untracked note and a matching inactive task worktree at a host-style path outside the preferred directory. Supply exclusive host coordination for the matching workspace. Start in the theme workspace and request the zero fix. Verify reuse and both notes' preservation.
- **Unique-data cleanup:** create and merge a feature branch locally. Its worktree has ignored `.env` and `notes.local.md` files. Supply workflow creation provenance and exclusive cleanup access, then request cleanup. Verify that both files and the worktree remain.
- **Safe cleanup:** use the same merged-task setup with no local data. Request cleanup with the same provenance and activity evidence. Verify removal of that worktree and registration, preservation of its branch, and an unchanged original checkout.

Repeat the completed new-task request in a fresh context with the task handoff to check reuse and absence of additional source edits. Host coordination in these fixtures is supplied evidence, not an exercised host API.

Git's [worktree documentation](https://git-scm.com/docs/git-worktree) describes registration and removal; its [ignore rules](https://git-scm.com/docs/gitignore) describe local exclusions. The [ignored-file inventory](https://git-scm.com/docs/git-ls-files) uses both `--others --ignored` and `--exclude-standard`. Keep these mechanics separate from evidence about agent activity and ownership.
