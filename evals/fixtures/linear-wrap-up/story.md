# Research documentation exercise

This is a synthetic exercise. Treat the following records as successful read results. Do not access external services or change the repository. Return the proposed Linear operations and exact bodies. A proposed operation is not a real save.

User request: "Record the research findings in comments on APP-70 for me and the next coding agent. Leave the issue description and metadata unchanged."

## Issue and discussion

APP-70: "Research CaptionKit subtitle retrieval for BrowserProbe"
URL: https://linear.app/example/issue/APP-70
State: In Progress. Label: Research. Assignee: Kim. Project: BrowserProbe.

Current description, to preserve where still valid:

## Context

BrowserProbe needs reliable original French captions for a local demo. Its current extractor sometimes discovers a track but receives unusable output.

## Scope

Inspect CaptionKit source and compare it with our browser probe. Dependency adoption, implementation changes, and live comparative testing are separate work.

## Acceptance

- Record the reviewed revision and primary sources.
- Explain retrieval, language provenance, and usable-track fallback implications.
- Recommend a focused next experiment and state verification limits.

Existing comment c300, Kim: "I mainly need to know whether discovering a French track tells us it will actually download, and what we should test next."
URL: https://linear.app/example/issue/APP-70#comment-c300
There are no replies and no other research updates.

## Research notes, in recorded order

1. Read CaptionKit revision `1111111111111111111111111111111111111111`. Its listing function returns caption metadata before attempting any caption download. A French language key can identify a translated track; source language and translation flags must be kept separately. This changed the initial idea of comparing only the number of listed French tracks: that would not measure useful retrieval.

2. Opened the CLI help, found 18 subtitle formats, skimmed the logging-color helper, checked the package layout, and inspected contributor notes. These facts did not affect the recommendation.

3. Traced selection and writing. When standard and automatic metadata share a language key, standard wins. If the selected download fails or yields unusable bytes, the code does not select the automatic alternative. Some caption requests require a caption-specific token. We have source evidence for that requirement but no successful live control establishing the cause of BrowserProbe's empty responses.

4. Compared BrowserProbe revision `2222222222222222222222222222222222222222`. It already rejects translated tracks and attempts an automatic alternative after unusable standard output. CaptionKit's client handling could be useful to study, but copying its selection order alone would not improve our existing fallback. CaptionKit is a Python tool, not directly runnable as a browser-extension dependency.

5. Source research concluded. Recommend a local comparison of pinned CaptionKit and BrowserProbe on the same French videos. Compare actual downloaded bytes, original versus translated provenance, usable cues and timing, with standard and original automatic tracks retrieved separately. No CaptionKit installation or live extraction was performed. No implementation or dependency adoption was authorized or performed. No additional research is needed to write this update.

## Verified source references

For this exercise, remote inspection already confirmed the revisions, paths, and lines below. They are synthetic and must not be fetched.

- Discovery and provenance, notes 1: https://github.com/example/captionkit/blob/1111111111111111111111111111111111111111/captionkit/tracks.py#L20-L48
- Selection and failed-download handling, notes 3: https://github.com/example/captionkit/blob/1111111111111111111111111111111111111111/captionkit/download.py#L50-L79
- Caption token check, notes 3: https://github.com/example/captionkit/blob/1111111111111111111111111111111111111111/captionkit/access.py#L10-L24
- BrowserProbe translation checks and fallback, notes 4: https://github.com/example/browserprobe/blob/2222222222222222222222222222222222222222/src/captions.js#L30-L65
- CaptionKit runtime, notes 4: https://github.com/example/captionkit/blob/1111111111111111111111111111111111111111/README.md#L12-L18

## Simulated API

- `save_comment({issueId, body})` creates a top-level comment.
- `save_comment({parentId, body})` replies to a thread.
- `save_issue({id, description})` replaces the issue description, leaving omitted fields unchanged.
- Successful simulated new comments return IDs c301, c302, c303, etc., in creation order, with URL `https://linear.app/example/issue/APP-70#comment-<id>`.
- All proposed saves succeed in this simulation. Use returned comment URLs only after their corresponding simulated creation.

Return JSON with `operations` in execution order, followed by the user-facing `response`. Include no analysis of the instructions or scoring.
