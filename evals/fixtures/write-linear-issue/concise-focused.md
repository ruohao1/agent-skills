# Independent tasks

All facts below are synthetic completed reads. Do not call real connectors or write to external services. Return the proposed issue update fields for each task. Fields omitted from updates stay unchanged. Each issue is already assigned to Mina, labeled Feature, and Started; only its requested description content may change.

## 1. Complex issue with unavailable supporting plans

User: Shorten APP-90 so I can scan it. Keep the requirements and make context a list.

Existing description:

> Context: Our offline document demo has a text reader, an analysis API, a saved local model, and result highlighting, but they are not connected. Opening a supported document should automatically analyze its text and show validated highlights. After installation, users should not have to click Analyze or export a file.
>
> Scope: Reuse the reader and model; do not create replacements. Capture text before lookup. The cache key is document ID, language, text fingerprint, and model version. The server must recalculate the fingerprint from text and page positions. A completed hit must upload no text or call the model, and must still work with the model offline. On a miss, pass text transiently to the model and validate the result before storing it. Concurrent requests for one key use one active claim; expired claims recover and late completions cannot overwrite a newer result. Work from a previous document must not affect the current document. No background polling.
>
> Privacy and deployment: Raw text remains in memory and must not enter database tables, logs, client storage, or training data. No per-user document history. The local API binds to loopback and model access stays internal. Preserve existing stored results with additive migrations.
>
> Acceptance: Opening a document automatically analyzes it without clicking Analyze or exporting a file. Reopening unchanged text uses the cache with no upload or model call. Concurrent requests coalesce, expired claims recover, and late results cannot replace newer attempts or alter another document. Missing text, failed inference, invalid output, and navigation during requests are handled safely; pending or failed must not appear as a successful empty result. Show the real saved-model flow in the desktop app; label test doubles and do not substitute them for the real demonstration. Record measured latency, call counts, failures, and limitations. Include fresh-checkout instructions, the model revision and artifact hash.
>
> Delivery: Keep the design and implementation plan with the implementation PR. Draft paths are docs/design/local-analysis.md and docs/plans/local-analysis.md. A draft proposes a 15-second timeout, which has not been validated or agreed. Cloud hosting, collaborative editing, and automatic training-data collection are excluded.

Read results: Both referenced draft files are unavailable. No comments establish additional decisions. Preserve the draft references as unverified; no published document link or implementation exists to cite. The existing description records the requirements, not proof that they are implemented.

## 2. Verified detailed design

User: Rewrite APP-91 as a concise issue brief, preserving the agreed scope.

Confirmed task: Add saved filter views so warehouse staff can restore a named set of active filters. Users can create, rename, select, and delete their own views. Sharing, default views, and search syntax changes are excluded. Existing warehouse access rules remain enforced. Define observable create/restore/rename/delete checks and confirm views survive a reload.

Verified source: `https://github.com/example/inventory/blob/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/docs/design/saved-views.md` is the approved design at that revision. It contains the ownership/schema details, validation rules, endpoint payloads, persistence strategy, route changes, and exhaustive test matrix. Those implementation details are already authoritative in that document and need not be copied into the issue. Existing implementation: filters work, but views are not saved. Existing issue repeats the CRUD requirement under Context, Scope, and Acceptance.

## 3. Narrow correction

User: In APP-92, replace only “Done when clicked” with “Done when activated by pointer or keyboard”, and save it.

Current description: "## Context\nThe Export button invokes an existing action. This paragraph format is intentional.\n\n## Acceptance\nDone when clicked."

No other correction, formatting change, metadata update, or source discovery was requested.
