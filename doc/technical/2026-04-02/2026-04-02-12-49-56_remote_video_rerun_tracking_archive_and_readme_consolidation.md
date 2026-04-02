# Remote Video Rerun Tracking Archive And README Consolidation

## Overview

This scope fixes two packaging issues left after the remote high-quality
TwinCAT/TestRig video rerun was completed and promoted.

First, the live tracking files in `doc/running/` still look like active runtime
state even though the rerun is finished, and the Markdown checklist does not
fully reflect the final closed-out packaging expectations for the last three
processed videos.

Second, the promoted artifact provenance currently lives in a separate
`doc/reference_codes/video_guides/REMOTE_HIGH_QUALITY_RERUN_README.md`, but the
user wants that provenance consolidated into the canonical
`doc/reference_codes/video_guides/README.md` instead of keeping a second
README-like file in the same folder.

## Technical Approach

The fix will treat the finished remote high-quality rerun as a closed campaign
artifact bundle instead of a still-live running state.

The plan is:

1. archive the completed rerun bookkeeping from `doc/running/` into a dedicated
   repository-owned archive location for finished video-pipeline runs;
2. update the checklist content so the final eleven-video state is explicit and
   the three later `.mkv` videos are fully represented in the closed-out
   record;
3. keep `doc/running/` reserved for active or resumable state, not for already
   promoted completed reruns;
4. merge the provenance currently stored in
   `REMOTE_HIGH_QUALITY_RERUN_README.md` into the canonical
   `doc/reference_codes/video_guides/README.md`;
5. remove the redundant dedicated rerun README after its content is preserved in
   the canonical folder README.

## Involved Components

- `doc/running/remote_high_quality_video_rerun_checklist.md`
  Current live checklist that should be archived after closeout.
- `doc/running/remote_high_quality_video_rerun_status.json`
  Current live JSON status that should be archived after closeout.
- `doc/reference_codes/video_guides/README.md`
  Canonical tracked entry point for promoted per-video artifacts.
- `doc/reference_codes/video_guides/REMOTE_HIGH_QUALITY_RERUN_README.md`
  Redundant provenance note to be consolidated and then removed.
- `README.md`
  Main project index that must register this technical document.

## Implementation Steps

1. Create a dedicated archive location for completed remote video-rerun
   bookkeeping under `doc/running/`.
2. Move the completed rerun checklist and status JSON into that archive
   location.
3. Refresh the archived checklist text so it clearly records the final
   closed-out eleven-video rerun state, including the three `.mkv` videos.
4. Update `doc/reference_codes/video_guides/README.md` to absorb the provenance,
   source-runtime, source-path, and artifact-meaning notes that currently live
   in `REMOTE_HIGH_QUALITY_RERUN_README.md`.
5. Remove `REMOTE_HIGH_QUALITY_RERUN_README.md` after consolidation.
6. Run scoped Markdown checks on the touched Markdown files before closing the
   task.
