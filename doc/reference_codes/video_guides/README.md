# Video Guide Reports

This folder contains the canonical high-quality outputs generated from the
TwinCAT/TestRig video-guide workflow.

The current canonical artifact set comes from the completed remote strong rerun
that used:

- remote `lan_ai_node_server.py`;
- remote `faster-whisper` with `large-v3`;
- remote `LM Studio`;
- remote `openai/gpt-oss-20b` for transcript cleanup and report generation;
- local OCR fallback for snapshot evidence.

The promoted artifacts in this folder were copied from:

- `.temp/video_guides/_remote_gptoss_tracked_reports/`

The corresponding temporary analysis root used for raw transcript caches,
selected-frame provenance, and rerun support was:

- `.temp/video_guides/_analysis_hq_remote_gptoss_tracked/`

The closed-out rerun bookkeeping is archived in:

- `doc/reports/analysis/twincat_video_guides/[2026-04-02]/runtime_tracking/remote_high_quality_video_rerun_status.json`
- `doc/reports/analysis/twincat_video_guides/[2026-04-02]/runtime_tracking/remote_high_quality_video_rerun_checklist.md`

For each slug folder:

- `*_transcript.md`
  Canonical cleaned transcript in Italian.
- `*_report.md`
  Canonical English technical report synthesized from transcript evidence,
  selected snapshots, and OCR-assisted context.
- `assets/reference_*.png`
  Selected repository-owned reference snapshots copied from the rerun.

These are the Git-tracked deliverables of the promoted remote-strong rerun.
The raw intermediate caches in
`.temp/video_guides/_analysis_hq_remote_gptoss_tracked/` remain useful for
audit and rerun support, but they are not treated as canonical deliverables.

## Reports

- [automatic_exp_te_report](automatic_exp_te/automatic_exp_te_report.md)
- [controller_adrc_report](controller_adrc/controller_adrc_report.md)
- [fb_adrc_and_pid_report](fb_adrc_and_pid/fb_adrc_and_pid_report.md)
- [machine_learning_1_report](machine_learning_1/machine_learning_1_report.md)
- [machine_learning_2_report](machine_learning_2/machine_learning_2_report.md)
- [ml_simulation_and_generator_cam_report](ml_simulation_and_generator_cam/ml_simulation_and_generator_cam_report.md)
- [overview_test_rig_report](overview_test_rig/overview_test_rig_report.md)
- [testrig___machine_learning_1_report](testrig___machine_learning_1/testrig___machine_learning_1_report.md)
- [testrig___machine_learning_2_report](testrig___machine_learning_2/testrig___machine_learning_2_report.md)
- [testrig___overview_report](testrig___overview/testrig___overview_report.md)
- [video_errata_corrige_adrc_report](video_errata_corrige_adrc/video_errata_corrige_adrc_report.md)

## Corrected Transcripts

- [automatic_exp_te_transcript](automatic_exp_te/automatic_exp_te_transcript.md)
- [controller_adrc_transcript](controller_adrc/controller_adrc_transcript.md)
- [fb_adrc_and_pid_transcript](fb_adrc_and_pid/fb_adrc_and_pid_transcript.md)
- [machine_learning_1_transcript](machine_learning_1/machine_learning_1_transcript.md)
- [machine_learning_2_transcript](machine_learning_2/machine_learning_2_transcript.md)
- [ml_simulation_and_generator_cam_transcript](ml_simulation_and_generator_cam/ml_simulation_and_generator_cam_transcript.md)
- [overview_test_rig_transcript](overview_test_rig/overview_test_rig_transcript.md)
- [testrig___machine_learning_1_transcript](testrig___machine_learning_1/testrig___machine_learning_1_transcript.md)
- [testrig___machine_learning_2_transcript](testrig___machine_learning_2/testrig___machine_learning_2_transcript.md)
- [testrig___overview_transcript](testrig___overview/testrig___overview_transcript.md)
- [video_errata_corrige_adrc_transcript](video_errata_corrige_adrc/video_errata_corrige_adrc_transcript.md)
