# Remote High-Quality Video Guide Rerun And Comparison

## Overview

This scope covers a second full-pass analysis of the TwinCAT/TestRig video
guides using the stronger remote runtime path instead of the already validated
local fallback path.

The goal is to determine whether the stronger remote setup materially improves
the repository-owned video-guide outputs enough to justify using it as the
canonical workflow path going forward.

The comparison baseline is the current local batch refresh generated on
`2026-04-01` with:

- local `LM Studio`;
- local `lan_ai_node_server.py`;
- `tiny` Whisper transcription;
- local `nvidia/nemotron-3-nano-4b` cleanup/report generation.

The comparison target is a remote rerun using:

- remote `LM Studio`;
- remote `lan_ai_node_server.py`;
- a stronger remote transcription model;
- a stronger remote cleanup/report model when available.

## Technical Approach

The work will proceed in four stages.

First, restore a reliable remote runtime path. If the remote LAN AI node cannot
be launched robustly via non-interactive SSH, the user may start it manually on
the remote workstation. Once the remote node is reachable, its health and model
availability will be verified from the current workstation.

Second, rerun the high-quality extraction workflow against the remote path with
the best currently available practical model pairing. The preferred remote
configuration is:

- `large-v3` for transcription;
- `qwen/qwen3.5-9b` for cleanup/report if stable on the remote workstation;
- otherwise the strongest stable loaded model confirmed by `/v1/models`.

Third, compare the new remote outputs against the current local baseline. The
comparison will focus on:

- transcript coherence and terminology recovery;
- report completeness and engineering usefulness;
- snapshot quality and supporting OCR evidence;
- workflow stability, runtime cost, and operational friction.

Fourth, summarize whether the stronger remote path is worth adopting as the new
default for repository-owned video-guide analysis and identify any remaining
runtime blockers.

## Involved Components

- `scripts/tooling/extract_video_guide_knowledge.py`
- `scripts/tooling/lan_ai_node_server.py`
- `scripts/tooling/lan_ai_node_client.py`
- remote `LM Studio`
- remote `standard_ml_lan_node` environment
- `.temp/video_guides/_analysis_hq/`
- `doc/reference_codes/video_guides/`
- comparison notes or follow-up documentation generated from the rerun

## Implementation Steps

1. Verify the remote `LM Studio` server and the remote LAN AI node path.
2. If needed, coordinate with a manual remote-node start and confirm remote
   `/health` reachability.
3. Run a remote smoke test on one representative video with the stronger model
   pair.
4. If the smoke test is stable, run the full remote batch across the video
   guide set.
5. Compare the remote outputs against the current local baseline.
6. Summarize whether the stronger remote path is worth the added runtime cost
   and operational complexity.
7. Update the repository artifacts only after the comparison result is clear.
