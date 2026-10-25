# Marketplace rewrite observations

These are synthetic, matched behavioral checks and installations in disposable homes. They are not statistical performance measurements or a claim that every authenticated host session was tested.

## Product brief

Baseline used the five tasks in `evals/product-brief.md`, without the skill. The primary answer correctly separated HTTP 202 from completion, challenged the metric, and covered expiry, interruption and recovery. It grouped permissions, outcome source, retry contract, expiry, volumes and escalation under “Required decisions before delivery” without distinguishing decision blockers from parallel investigation. All four focused cases respected their requested scope.

The rewrite focuses on the observed distinction: state which decision an unknown blocks and which questions can proceed in parallel. It also removes the old default requirement to save a file. The with-skill answer tied permission, expiry and recovery questions to affected behavior, and explicitly allowed volume/baseline work in parallel. The four narrow counterexamples remained within scope.

Five fresh contexts per variant ran the primary task (the first of each also ran the four counterexamples). Controls 1, 3 and 4 grouped all unknowns under “Required decisions before delivery” or “Before release”; controls 2 and 5 distinguished parallel volume research. All five guided answers made the distinction and identified affected behavior. This small synthetic sample demonstrates more consistent handling here, not general superiority. A contaminated guided repetition read the criteria, stopped without an answer, and was excluded and replaced. Other primary behavior was already strong without guidance.

## Installation observations

- Verified npm metadata for Skills CLI 1.7.2 and its Node >=22.20.0 requirement.
- Installed the pinned upstream `tdd` skill with the actual CLI into a disposable Codex home; confirmed copied supporting files and source/ref/path lock metadata.
- Registered this checkout and installed its original product plugin with actual Codex and temporary Claude Code 2.1.301 CLIs in a disposable home. These probes exercise host contracts, not yet the final rewritten packages.
- Real probes exposed Codex's source-checkout path versus installed cache path and Claude's separate marketplace source registry. Added regression tests that failed before the fixes and passed afterward.
- On 2026-10-17, the final 13-skill catalog installed with the actual Skills CLI into fresh disposable global and project environments for Codex, Claude Code and OpenCode. Both full repetitions returned success with zero new installations. Unrelated sentinel files were unchanged. OpenCode correctly reused compatible shared copies.
- Every installed Codex portable skill, including all supporting resources, matched the corresponding pinned upstream checkout or local source fingerprint exactly.
- Actual native coordinator installs and repeats passed for product-design 0.2.0 on Codex global and Claude Code user/project. Ponytail native 5.3.2 installed on all three supported combinations and remained needs-setup for explicit hook/reload verification; trust was not approved.
- A project-scope regression failed before inventory was filtered by project path. The correction excludes plugins belonging to other projects while retaining disabled plugins in the current project.
- Codex app-server skills/list and OpenCode debug skill each discovered all 13 portable catalog skills in isolated homes. OpenCode also supplied its own built-in skill. This checks discovery, not authenticated model execution.
- Selective OpenCode installation and repetition passed with customized configuration and state roots. Adding Claude skills preserved existing content; shared discovery avoided duplicate installation. A locally edited skill was reported as a conflict and remained unchanged.
- A real missing-commit failure after a successful custom install preserved that success. Retrying with the selected upstream commit installed only the unresolved skill; the following repeat installed nothing. Sentinel bytes stayed unchanged. A lock symlink introduced after preview was rejected without writing the unrelated target.
- Observed tools: Node 22.23.1, Python 3.14.4, Skills CLI 1.7.2, Codex CLI 0.163.0, Claude Code 2.1.301, OpenCode 1.18.34. Pinned portable Ponytail remains independent of the current native plugin version.
- Authenticated agent conversations, native hook activation and macOS/Windows runtime behavior were not tested. No user installation, external issue, Git branch, commit or PR was changed/created.

## Final review and regression checks

An independent reviewer ran the then-current 31 tests and package validator. The review found unsafe installer lock redirection, incomplete upstream content incorrectly counted as present on retry, and ignored `XDG_STATE_HOME` lock metadata. Each finding received a failing regression before the shared implementation was fixed. Related checks preserve hardlinked lock files and unknown project lock fields, and fresh upstream installs must report the selected commit and skill path before receiving a coordinator receipt.

A real OpenCode-only install also exposed its canonical shared destination; inventory and installation now agree on that path. The final run passed all 38 deterministic tests and marketplace validation: two matching catalogs, one local plugin, one local skill. This validates the fixes; no second independent review or authenticated execution is claimed.

## Product design review — candidate omitted

Three independent no-guidance primary runs identified both RC12 task failures, treated duplicate execution as an unobserved risk, and kept the RC11 keyboard finding outside confirmed RC12 defects. Control 1 also passed the screenshot, narrow-copy, current-trace and no-findings counterexamples. Representative verbatim baseline: “The keyboard failure is confirmed for RC11, not RC12. It cannot honestly appear among confirmed RC12 blockers.” No useful gap was demonstrated. Following the agreed candidate gate, do not rewrite or ship this redundant custom skill. Ordinary design-review requests remain available without a dedicated skill. No guided comparison or improvement is claimed.

## Engineering contracts — candidate omitted

Three independent primary controls repaired the producer, Web adapter, replay path and CLI ingress; used independent fixtures; preserved missing/null/empty distinctions and request/execution identity; and refused speculative historical repair. Control 1 passed the four narrow cases. Representative baseline: “previously collapsed label intent or conflated request IDs cannot be reconstructed without independent evidence.” No demonstrated gap; no custom guidance authored or improvement claimed. Retain upstream engineering tools instead.

## Engineering migrations — candidate omitted

Three independent controls rejected circular parity fixtures, destructive conversion with binary-only rollback, and unsafe worker overlap. They required preserved originals, independent expected behavior, a bounded transition and observable stop/recovery conditions. Control 1 also kept the private rename small, refused fabricated recovery of deleted values, and permitted a documented security fix as a parity exception. Representative baseline: “Binary rollback restores software only; data restoration and compensation for downstream effects require separate verified procedures.” No demonstrated gap; no custom guidance authored or improvement claimed.

## Engineering validation — candidate omitted

Three primary controls bound claims to the tested revision/environment, distinguished mocks/skips/builds from native acceptance, and requested only relevant checks on the changed revision. Control 1 handled the documentation-only case, partial native coverage, timed-out check versus mocked substitute, and complete supplied evidence proportionately. Representative baseline: “B’s successful macOS build establishes that the package builds, not that it launches or its native behavior works.” No demonstrated gap; no custom guidance authored or improvement claimed.

## Upstream replacement exercises

At the pinned Archify revision, authored an illustrative maintenance lifecycle with distinct acceptance, execution, success, expiry and failure. Validation, delivery, strict artifact check and automated browser checks passed. Inspected the 1440×900 light and 2048×1320 dark captures: labels and transitions are legible, with no overlapping nodes or clipped primary flow. The default browser wrapper could not access local files; rerunning with local Chromium resolved the environmental failure without changing upstream code.

Applied the pinned Prototype UI instructions to a synthetic approval screen in a disposable folder (there is no existing application page). Three structurally different variants use one URL and a floating switcher. At widths 390 and 1440, all variants passed keyboard activation/cycling, the text-input arrow exception, reload-stable URL state, and zero horizontal overflow/page errors. Inspected narrow queue/detail and wide outcome-overview captures. No winner, user research result, production integration, or external issue update is claimed. Small source fixtures are retained under `evals/fixtures/`; generated output stays outside the plugin packages.
