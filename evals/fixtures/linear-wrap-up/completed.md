# Completed research issue

Synthetic exercise. Treat the following as successful read results. Do not use live tools, fetch links, or change files. Return the exact proposed operations and bodies, followed by a user-facing response. A simulated save is not a real write.

User: "Wrap up APP-70 now that the source research is done. Make the outcome easy for me and the next coding agent to find. You may update the description or add a comment to record it; leave metadata alone."

## Issue

APP-70: "Research CaptionKit subtitle retrieval for BrowserProbe"
URL: https://linear.app/example/issue/APP-70
State: Done. Label: Research. Assignee: Kim. Project: BrowserProbe. No linked follow-up issue exists.

Description:

## Context

BrowserProbe needs reliable original French captions for a local demo. Its current extractor sometimes discovers a track but receives unusable output.

## Scope

Inspect CaptionKit source and compare it with our browser probe. Dependency adoption, implementation changes, and live comparative testing are separate work.

## Acceptance

- Record the reviewed revision and primary sources.
- Explain retrieval, language provenance, and usable-track fallback implications.
- Recommend a focused next experiment and state verification limits.

## Discussion: all pages retrieved

The original question c300, Kim: "I mainly need to know whether discovering a French track tells us it will actually download, and what we should test next."
URL: https://linear.app/example/issue/APP-70#comment-c300

Reply c301: "The first source pass showed why counting French tracks would not measure useful retrieval. CaptionKit lists metadata before attempting a download, and a French language key can identify a translation. Keep source language and translation flags separately."
URL: https://linear.app/example/issue/APP-70#comment-c301
Evidence: https://github.com/example/captionkit/blob/1111111111111111111111111111111111111111/captionkit/tracks.py#L20-L48

Reply c302: "Standard metadata wins over automatic metadata with the same language key, but failed or unusable selected downloads do not trigger the automatic alternative. Some requests require a caption-specific token. Source review establishes that requirement; no successful control establishes why BrowserProbe gets empty responses."
URL: https://linear.app/example/issue/APP-70#comment-c302
Evidence: https://github.com/example/captionkit/blob/1111111111111111111111111111111111111111/captionkit/download.py#L50-L79 and https://github.com/example/captionkit/blob/1111111111111111111111111111111111111111/captionkit/access.py#L10-L24

Reply c303: "BrowserProbe already rejects translations and tries automatic captions after unusable standard output. Copying CaptionKit's selection order alone would not improve our fallback. CaptionKit is a Python tool; use it as a separate local reference, not a browser dependency. Source research is complete. No installation or live extraction was performed. Compare the pinned tools on the same French videos, retrieving standard and original automatic tracks separately and measuring actual bytes, provenance, usable cues, and timing."
URL: https://linear.app/example/issue/APP-70#comment-c303
Evidence: https://github.com/example/browserprobe/blob/2222222222222222222222222222222222222222/src/captions.js#L30-L65 and https://github.com/example/captionkit/blob/1111111111111111111111111111111111111111/README.md#L12-L18

All source revisions, paths, line ranges, and comment URLs above have been verified for this synthetic exercise. The complete report is local and gitignored. Nothing beyond these notes is needed to record the outcome. No dependency choice or implementation change was made.

## Simulated API

- `save_issue({id, description})` replaces the description, preserving omitted fields. Success returns the supplied issue URL.
- `save_comment({issueId, body})` creates a top-level comment; `save_comment({parentId, body})` replies. Success returns `https://linear.app/example/issue/APP-70#comment-c304`.

Return JSON with `operations` in execution order and `response`. Do not explain or grade the instructions.
