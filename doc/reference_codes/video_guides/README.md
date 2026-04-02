# Video Guide Reports

This folder contains the canonical high-quality outputs generated from the
TwinCAT/TestRig video-guide workflow.

The current canonical artifact set comes from the completed remote strong rerun
that used:

* remote `lan_ai_node_server.py`;
* remote `faster-whisper` with `large-v3`;
* remote `LM Studio`;
* remote `openai/gpt-oss-20b` for transcript cleanup and report generation;
* local OCR fallback for snapshot evidence.

The canonical tracked source media bundle for this workflow now lives under:

* `reference/video_guides/source_bundle/`
* `reference/video_guides/source_bundle/README.md`
* `reference/video_guides/source_bundle/source_manifest.json`

The promoted artifacts in this folder were copied from:

* `.temp/video_guides/_remote_gptoss_tracked_reports/`

The corresponding temporary analysis root used for raw transcript caches,
selected-frame provenance, and rerun support was:

* `.temp/video_guides/_analysis_hq_remote_gptoss_tracked/`

The closed-out rerun bookkeeping is archived in:

* `doc/reports/analysis/twincat_video_guides/[2026-04-02]/runtime_tracking/remote_high_quality_video_rerun_status.json`
* `doc/reports/analysis/twincat_video_guides/[2026-04-02]/runtime_tracking/remote_high_quality_video_rerun_checklist.md`

For each slug folder:

* `*_transcript.md`
  Canonical cleaned transcript in Italian.
* `*_report.md`
  Canonical English technical report synthesized from transcript evidence,
  selected snapshots, and OCR-assisted context.
* `assets/reference_*.png`
  Selected repository-owned reference snapshots copied from the rerun.

These are the Git-tracked deliverables of the promoted remote-strong rerun.
The raw intermediate caches in
`.temp/video_guides/_analysis_hq_remote_gptoss_tracked/` remain useful for
audit and rerun support, but they are not treated as canonical deliverables.

A later repository-owned recheck reran the canonical source bundle through the
same strong runtime and compared the results against this promoted guide tree.
That reconciliation is recorded in:

* `doc/reports/analysis/twincat_video_guides/[2026-04-02]/final_video_guide_reconciliation.md`

The final decision was to keep this canonical guide tree as the baseline,
while selectively merging newly confirmed factual corrections into the reports
and TwinCAT/TestRig reference notes.

After source-bundle deduplication, the canonical promoted tree now covers `8`
unique source videos. The original tracked rerun processed `11` source files,
but three of those were byte-identical filename aliases and are no longer kept
as separate canonical guide folders.

## Canonical Source Map

| Slug | Canonical source video |
| --- | --- |
| `automatic_exp_te` | [`automatic_exp_te.mp4`](../../../reference/video_guides/source_bundle/automatic_exp_te.mp4) |
| `controller_adrc` | [`controller_adrc.mkv`](../../../reference/video_guides/source_bundle/controller_adrc.mkv) |
| `fb_adrc_and_pid` | [`fb_adrc_and_pid.mp4`](../../../reference/video_guides/source_bundle/fb_adrc_and_pid.mp4) |
| `machine_learning_1` | [`machine_learning_1.mp4`](../../../reference/video_guides/source_bundle/machine_learning_1.mp4) |
| `machine_learning_2` | [`machine_learning_2.mp4`](../../../reference/video_guides/source_bundle/machine_learning_2.mp4) |
| `ml_simulation_and_generator_cam` | [`ml_simulation_and_generator_cam.mkv`](../../../reference/video_guides/source_bundle/ml_simulation_and_generator_cam.mkv) |
| `overview_test_rig` | [`overview_test_rig.mp4`](../../../reference/video_guides/source_bundle/overview_test_rig.mp4) |
| `video_errata_corrige_adrc` | [`video_errata_corrige_adrc.mkv`](../../../reference/video_guides/source_bundle/video_errata_corrige_adrc.mkv) |

## Reports

* [automatic_exp_te_report](automatic_exp_te/automatic_exp_te_report.md)
* [controller_adrc_report](controller_adrc/controller_adrc_report.md)
* [fb_adrc_and_pid_report](fb_adrc_and_pid/fb_adrc_and_pid_report.md)
* [machine_learning_1_report](machine_learning_1/machine_learning_1_report.md)
* [machine_learning_2_report](machine_learning_2/machine_learning_2_report.md)
* [ml_simulation_and_generator_cam_report](ml_simulation_and_generator_cam/ml_simulation_and_generator_cam_report.md)
* [overview_test_rig_report](overview_test_rig/overview_test_rig_report.md)
* [video_errata_corrige_adrc_report](video_errata_corrige_adrc/video_errata_corrige_adrc_report.md)

## Corrected Transcripts

* [automatic_exp_te_transcript](automatic_exp_te/automatic_exp_te_transcript.md)
* [controller_adrc_transcript](controller_adrc/controller_adrc_transcript.md)
* [fb_adrc_and_pid_transcript](fb_adrc_and_pid/fb_adrc_and_pid_transcript.md)
* [machine_learning_1_transcript](machine_learning_1/machine_learning_1_transcript.md)
* [machine_learning_2_transcript](machine_learning_2/machine_learning_2_transcript.md)
* [ml_simulation_and_generator_cam_transcript](ml_simulation_and_generator_cam/ml_simulation_and_generator_cam_transcript.md)
* [overview_test_rig_transcript](overview_test_rig/overview_test_rig_transcript.md)
* [video_errata_corrige_adrc_transcript](video_errata_corrige_adrc/video_errata_corrige_adrc_transcript.md)
