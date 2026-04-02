# Remote Video Artifact Promotion And Tracking Readme

## Overview

This scope covers the first repository-facing follow-up after the completed
remote high-quality video-guide rerun.

The remote-strong batch is now complete for all currently available
TwinCAT/TestRig source videos using:

- remote `lan_ai_node_server.py`;
- remote `faster-whisper` with `large-v3`;
- remote `LM Studio`;
- remote `openai/gpt-oss-20b` for cleanup and report generation;
- local OCR fallback for snapshot evidence.

The generated outputs currently live under the temporary tracked rerun root:

- `.temp/video_guides/_remote_gptoss_tracked_reports/`

Those artifacts are not yet part of the canonical Git-tracked repository
surface. The first step is therefore to promote the remote rerun outputs into a
stable repository-owned location and add a small tracking README that makes the
artifact meaning explicit.

## Technical Approach

The promotion should be done as a controlled canonicalization pass, not as a
blind overwrite.

The remote rerun outputs already mirror the canonical slug layout currently used
under `doc/reference_codes/video_guides/`. This allows a direct one-to-one
replacement strategy for the transcript, report, and asset folders of each
video topic.

To keep the repository state inspectable, the promoted tree should also include
a concise README dedicated to the remote rerun artifacts. That README should
record:

- which runtime path produced the artifacts;
- where the temporary rerun source lives;
- which slug folders belong to the promoted rerun;
- what each artifact type represents.

This step should only move the validated remote rerun outputs into a Git-tracked
canonical location. Broader comparison commentary or final conclusions about
quality can be handled in a later step after the canonical tree is updated.

No Codex subagent is planned for this scope.

## Involved Components

- `.temp/video_guides/_remote_gptoss_tracked_reports/`
- `doc/reference_codes/video_guides/`
- `doc/reference_codes/README.md`
- `README.md`
- `doc/guide/project_usage_guide.md` if the canonical usage path needs a direct
  note about the promoted artifact set

## Implementation Steps

1. Verify that the tracked remote rerun slug tree matches the canonical
   `doc/reference_codes/video_guides/` slug tree.
2. Promote the remote rerun transcript, report, and asset artifacts from the
   tracked temporary root into the canonical Git-tracked reference-code tree.
3. Add a concise tracking README inside the canonical video-guide tree so the
   promoted artifact set is self-describing.
4. Update any top-level index files needed to point cleanly at the promoted
   artifacts.
5. Run scoped Markdown checks on the touched documentation files.
