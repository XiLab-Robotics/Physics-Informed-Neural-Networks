# Remote High-Quality Video Rerun Tracking And Launcher

## Overview

This scope upgrades the remote high-quality TwinCAT/TestRig video-guide rerun
from an ad-hoc smoke-test workflow into a controlled per-video batch process.

The target runtime remains the strongest validated path currently available:

- remote `lan_ai_node_server.py`;
- remote `faster-whisper` with `large-v3`;
- remote `LM Studio`;
- remote `openai/gpt-oss-20b` for cleanup and report generation;
- local OCR fallback when remote OCR is unstable.

The main goal is to regenerate every video-guide artifact with the highest
practical accuracy while preserving explicit progress tracking for each video.

The user requested that the process never become an opaque long-running batch.
Each video must expose a visible checklist that shows whether the following
stages are complete:

- transcript extraction;
- transcript cleanup;
- snapshot selection;
- OCR evidence extraction;
- report synthesis;
- final artifact validation.

## Technical Approach

The best approach is a hybrid of automation and strict per-video state
tracking.

The expensive workflow stages are deterministic enough to be launched by a
PowerShell wrapper, but the remote stack is still fragile enough that a fully
blind one-command batch would be a bad fit. The workflow should therefore be
restructured around:

1. a repository-owned per-video state file that records stage-level progress;
2. a launcher that processes one video at a time in a fixed order;
3. explicit resume behavior so a failed video restarts from the first missing
   stage instead of retranscribing everything;
4. visible terminal output that announces the current video, current stage, and
   whether the step is newly completed or restored from cache.

This gives the user the operational convenience of a prepared launcher without
losing the ability to inspect, pause, or recover the batch after a remote
timeout.

The rerun should not overwrite the existing canonical outputs until the remote
batch is complete enough to compare quality against the current local baseline.
The remote rerun will therefore write into its own dedicated analysis and report
roots first, together with a run-status file and a human-readable checklist
document.

If the remote runtime proves stable, the launcher can continue unattended while
still leaving a trustworthy per-video audit trail. If a stage repeatedly fails
for a specific video, the process should stop on that video, preserve the
partial state, and avoid silently skipping to the next item.

No Codex subagent is planned for this scope.

## Involved Components

- `scripts/tooling/extract_video_guide_knowledge.py`
- `scripts/tooling/lan_ai_node_client.py`
- `scripts/tooling/lan_ai_node_server.py`
- `scripts/tooling/`
- `scripts/campaigns/` or an equivalent repository-owned PowerShell launcher
  location for the rerun wrapper
- `doc/scripts/tooling/`
- `doc/running/`
- `.temp/video_guides/`
- `doc/reference_codes/video_guides/`
- remote `LM Studio`
- remote `standard_ml_lan_node`

## Implementation Steps

1. Design a persistent per-video checklist format for the remote rerun.
2. Add a repository-owned launcher that runs the approved remote-strong command
   one video at a time in a deterministic order.
3. Update the Python workflow so it can read and write per-video stage state
   without losing existing cache behavior.
4. Ensure the workflow stops on a failing video instead of silently continuing.
5. Run the remote rerun against one video as a tracked proof case.
6. If the tracked proof case is stable, continue the remaining videos with the
   same launcher and checklist state.
7. Compare the final remote outputs against the current local canonical
   baseline and decide whether the remote path should replace the current
   canonical artifacts.
