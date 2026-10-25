# Independent audit tasks

Use only these synthetic completed repository reads. Produce one maintainability report per task. No code, files, tickets, or external services may change. Tests were read but not run. Do not inspect the real workspace.

## 1. Feature ownership and file paths

User: Audit this repository for readability and maintainability as the codebase grows. Include every supported finding and leave the files unchanged.

Verified repository convention, `CONTRIBUTING.md:12`: implementation belongs under its owning feature; tests remain in `tests/<feature>/`. The application has established `src/features/invoices/` and `src/features/reports/` directories. The source inventory and searches below are complete for the affected area.

- `src/shared/misc.ts:1-48` contains invoice validation rules. Its sole internal consumer is `src/features/invoices/submit.ts:3`, which imports `validateInvoice` from `../../shared/misc`.
- `src/shared/misc.ts:50-103` contains the CSV report formatter and `exportCsv`. Its sole internal consumer is `src/features/reports/export.ts:4`, which imports `exportCsv` from `../../shared/misc`.
- The two sections share no implementation, types, or state. Their tests cover separate feature contracts. Existing change history shows that invoice-rule edits and report-format edits affect independent behavior but both require finding the relevant section in `misc.ts`. The file's name and shared location do not expose either owner.
- `src/shared/misc.ts:57` loads its header template with `new URL('./templates/header.txt', import.meta.url)`. The asset is maintained at `src/shared/templates/header.txt`; the built formatter uses the copied asset.
- `package.json:18` publishes the supported subpath `"./csv": "./dist/shared/misc.js"`. External consumers use that subpath; their code is unavailable. The public `./csv` import and current CSV behavior must remain compatible.
- `config/jobs.json:7` registers the CSV job as `"module": "./dist/shared/misc.js", "export": "exportCsv"`.
- `scripts/copy-assets.mjs:9` copies `src/shared/templates/header.txt` to `dist/shared/templates/header.txt`.
- `tsconfig.json:6` includes all `src/**/*.ts`, so the existing feature directories are already compiled. `dist/` is generated.
- `vitest.config.ts:5` discovers `tests/**/*.test.ts`. The affected tests are `tests/invoices/validation.test.ts:1` and `tests/reports/csv.test.ts:1`; both currently import their functions from `../../src/shared/misc`.

All supplied behavior is intentional and currently agrees with the documented contracts. There is no evidence of a runtime bug or unused function. The task concerns how the source is organized and how changes can remain safe.

## 2. Cohesive file and deliberate test layout

User: Audit the organization of `src/config/parse.ts` and its tests. The file is 640 lines long. Report any worthwhile refactor without editing it.

Verified reads: `src/config/parse.ts:1-640` implements one configuration grammar. Its tokenizer, parser states, and diagnostics use shared private grammar types. Public consumers import one `parseConfig` function; the private helpers have no independent consumers. Existing navigation names each grammar phase clearly, and the relevant history shows grammar changes confined to this file and its tests. No separate responsibility or change cost was found in those reads.

`CONTRIBUTING.md:12` requires tests under `tests/<feature>/`. `tests/config/parse.test.ts` exercises the public parser contract, and the test runner's configured glob discovers it. Source and tests are easy to locate through matching feature names. No supported problem was found beyond the reported file length and the separate test directory.
