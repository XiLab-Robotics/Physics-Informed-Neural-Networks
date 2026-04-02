# Remote High-Quality Video-Guide Artifacts

This note tracks the canonical video-guide artifacts promoted from the completed
remote high-quality rerun.

## Source Runtime

The promoted artifacts were generated with:

- remote `lan_ai_node_server.py`;
- remote `faster-whisper` using `large-v3`;
- remote `LM Studio`;
- remote `openai/gpt-oss-20b` for transcript cleanup and report generation;
- local OCR fallback for snapshot evidence.

## Promotion Source

The canonical Git-tracked artifacts in this folder were promoted from:

- `.temp/video_guides/_remote_gptoss_tracked_reports/`

The corresponding temporary analysis root used for transcript caches, raw
transcripts, selected-frame provenance, and rerun support is:

- `.temp/video_guides/_analysis_hq_remote_gptoss_tracked/`

The tracked batch state for that rerun is recorded in:

- `doc/running/remote_high_quality_video_rerun_status.json`
- `doc/running/remote_high_quality_video_rerun_checklist.md`

## Artifact Scope

The promoted slug folders are:

- `automatic_exp_te`
- `controller_adrc`
- `fb_adrc_and_pid`
- `machine_learning_1`
- `machine_learning_2`
- `ml_simulation_and_generator_cam`
- `overview_test_rig`
- `testrig___machine_learning_1`
- `testrig___machine_learning_2`
- `testrig___overview`
- `video_errata_corrige_adrc`

## Artifact Meaning

For each slug folder:

- `*_transcript.md`
  Canonical cleaned transcript in Italian.
- `*_report.md`
  Canonical English technical report synthesized from transcript evidence,
  selected snapshots, and OCR-assisted context.
- `assets/reference_*.png`
  Selected repository-owned reference snapshots copied from the rerun.

These are the Git-tracked deliverables of the remote-strong rerun. The raw
intermediate caches in `.temp/video_guides/_analysis_hq_remote_gptoss_tracked/`
remain useful for audit and rerun support, but they are not treated as
canonical reference-code deliverables.
