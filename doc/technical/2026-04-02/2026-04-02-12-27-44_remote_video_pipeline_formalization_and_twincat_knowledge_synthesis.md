# Remote Video Pipeline Formalization And TwinCAT Knowledge Synthesis

## Overview

This scope consolidates the completed remote high-quality TwinCAT/TestRig
video-analysis campaign into repository-owned engineering knowledge.

The objective is threefold:

1. re-read and qualitatively review the promoted artifacts for all 11 videos;
2. extract implementation-facing TwinCAT/TestRig knowledge that complements the
   code already analyzed in previous repository work;
3. formalize the remote-strong analysis pipeline so it can be rerun, audited,
   and reused as a standard knowledge-ingestion workflow for future model and
   deployment work.

The target runtime remains the validated remote-strong path:

- remote `lan_ai_node_server.py`;
- remote `faster-whisper` with `large-v3`;
- remote `LM Studio`;
- remote `openai/gpt-oss-20b` for cleanup and report synthesis;
- local OCR fallback.

The resulting documentation should help future implementation work on TE models,
TwinCAT-friendly export paths, and TestRig integration by making the video
knowledge explicit, reviewable, and easy to retrieve.

## Technical Approach

The work will proceed in four connected layers.

First, the promoted canonical artifacts under
`doc/reference_codes/video_guides/` will be reviewed as a coherent batch. This
includes transcript quality, report quality, selected snapshots, and the degree
to which each video clarifies PLC structure, data flow, timing, variable
mapping, state-machine logic, and ML deployment details.

Second, the reviewed video knowledge will be synthesized against existing
repository understanding of TwinCAT/TestRig code. The synthesis will separate:

- direct evidence coming from the video artifacts;
- repository facts already documented from code analysis;
- engineering inferences that are plausible but not yet proven by code or
  artifacts.

Third, the remote-strong video-analysis workflow itself will be formalized into
a reusable repository process. This includes runtime topology, environment
variables, launcher usage, per-video tracking, expected outputs, quality gates,
failure modes, and rerun/resume strategy.

Fourth, if the synthesis reveals a durable repeated workflow, a repository skill
may be added to standardize future video-knowledge refreshes and TwinCAT/TestRig
artifact synthesis. This is optional, but it is in scope if the workflow is
stable enough to merit dedicated instructions.

## Involved Components

- `doc/reference_codes/video_guides/`
  Canonical promoted transcripts, reports, and snapshots for the 11 videos.
- `doc/reference_codes/video_guides/REMOTE_HIGH_QUALITY_RERUN_README.md`
  Provenance note for the promoted artifacts.
- `doc/running/remote_high_quality_video_rerun_status.json`
  Persistent campaign state for the tracked rerun.
- `doc/running/remote_high_quality_video_rerun_checklist.md`
  Per-video completion checklist for the tracked rerun.
- `scripts/tooling/extract_video_guide_knowledge.py`
  Main orchestration entry point for transcript/report generation.
- `scripts/tooling/lan_ai_node_server.py`
  Remote transcription and OCR node.
- `scripts/tooling/lan_ai_node_client.py`
  Client-side LM Studio and LAN-node integration logic.
- `scripts/tooling/run_remote_high_quality_video_rerun.ps1`
  One-video-at-a-time launcher for the remote-strong batch.
- `doc/scripts/tooling/run_remote_high_quality_video_rerun.md`
  Launcher usage documentation.
- `doc/guide/project_usage_guide.md`
  User-facing usage guide to update with the formalized workflow.
- `README.md`
  Main project entry point that must reference the new formalized material.
- relevant TwinCAT/TestRig summaries already present in `doc/reference_codes/`
  and `doc/technical/`
  Context needed to connect the videos to implementation work.
- optional new skill under `.codex/skills/`
  Only if the workflow proves stable enough for a dedicated repository skill.

## Implementation Steps

1. Review all 11 promoted transcripts, reports, and reference snapshots and
   record qualitative findings per video.
2. Build a cross-video TwinCAT/TestRig knowledge synthesis focused on
   deployment-relevant code details, variable semantics, timing structure,
   state-machine behavior, and ML integration boundaries.
3. Compare the synthesized video evidence against the repository's existing
   TwinCAT/TestRig code understanding and explicitly label confirmed facts,
   inferred conclusions, and open questions.
4. Write a repository-owned campaign sum-up report describing the remote-strong
   rerun, its quality level, observed strengths/weaknesses, and why it is the
   current preferred baseline.
5. Create formal pipeline documentation that describes the remote-strong
   runtime, launcher flow, output locations, quality checks, recovery path, and
   reuse procedure.
6. Update repository reference and guide documents so the new process and the
   resulting knowledge are discoverable from the main documentation entry
   points.
7. If justified by stability and reuse value, create a dedicated skill for
   future video-pipeline execution and knowledge synthesis.
