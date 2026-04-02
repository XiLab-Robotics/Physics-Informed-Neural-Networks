---
name: twincat-video-knowledge-pipeline
description: Use when re-running, reviewing, or formalizing the repository-owned TwinCAT/TestRig video-analysis workflow in StandardML - Codex. This skill is for the remote high-quality video pipeline, per-video artifact review, cross-video TwinCAT/TestRig knowledge synthesis, and promotion of video-derived findings into canonical reference notes.
---

# TwinCAT Video Knowledge Pipeline

Use this skill when a task is about:

- rerunning the high-quality TwinCAT/TestRig video pipeline;
- reviewing promoted video-guide artifacts;
- extracting implementation-facing knowledge from the `11` canonical video
  reports;
- updating the canonical TwinCAT/TestRig reference notes after a rerun.

## Read First

1. `doc/reference_codes/video_guides/README.md`
2. `doc/scripts/tooling/remote_high_quality_video_pipeline.md`
3. `doc/reference_codes/testrig_twincat_video_guides_reference.md`
4. `doc/reference_codes/testrig_twincat_ml_reference.md`

## Runtime Baseline

Default to the strongest validated path unless the user explicitly narrows the
scope:

- remote `lan_ai_node_server.py`
- remote `faster-whisper` with `large-v3`
- remote `LM Studio`
- remote `openai/gpt-oss-20b`
- local OCR fallback

Prefer:

- `scripts/tooling/run_remote_high_quality_video_rerun.ps1`

over ad-hoc manual loops.

## Workflow

1. Check the active live tracking files in `doc/running/` if a rerun is still in progress.
2. For the completed canonical rerun, check `doc/reports/analysis/twincat_video_guides/[2026-04-02]/runtime_tracking/`.
3. If the runtime must be rerun, use the tracked launcher or a narrowly scoped
   per-video rerun with explicit URLs and models.
4. Review the canonical promoted outputs in
   `doc/reference_codes/video_guides/`.
5. Separate:
   - video-confirmed facts;
   - code-confirmed facts;
   - engineering inference.
6. Merge the resulting knowledge into:
   - `doc/reference_codes/testrig_twincat_video_guides_reference.md`
   - `doc/reference_codes/testrig_twincat_ml_reference.md`
   - relevant analysis reports under `doc/reports/analysis/`.

## Quality Rules

- Do not treat transcript text as proof when the report itself labels something
  as inference or uncertainty.
- Prefer cross-video consistency over any single noisy line.
- Keep task timing, feature ordering, variable mapping, and experiment-state
  logic explicit.
- Preserve the distinction between:
  - model export artifacts;
  - PLC-side orchestration;
  - TwinCAT/TestRig simulation or replay support.

## Output Pattern

Prefer this sequence:

1. campaign sum-up;
2. cross-video implementation findings;
3. pipeline formalization/update;
4. reference-note integration;
5. only then any new deployment or modeling conclusion.
