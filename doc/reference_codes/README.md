# Reference Code Notes

This folder contains detailed notes extracted from the Git submodules stored under `reference/codes/`.

The purpose of these documents is to preserve the most useful implementation patterns from the reference repositories before developing the RV-reducer neural-network code in this project.

## Available Documents

- [blind_handover_controller_reference.md](./blind_handover_controller_reference.md)
  Main style baseline for naming, comments, progressive implementation, ROS node structure, and PyTorch Lightning training flow.
- [mediapipe_gesture_recognition_reference.md](./mediapipe_gesture_recognition_reference.md)
  Supporting reference for Hydra-based configuration, Lightning training structure, and reusable utility patterns.
- [multimodal_fusion_reference.md](./multimodal_fusion_reference.md)
  Supporting reference for compact multimodal ROS pipelines, explicit command mapping, and straightforward Lightning baselines.
- [testrig_twincat_ml_reference.md](./testrig_twincat_ml_reference.md)
  Reference note for the imported TestRig TwinCAT machine-learning pipeline,
  including the current `FB_MllPrediction` XML/BML workflow and the newer
  Beckhoff Machine Learning Server alternative.
- [testrig_twincat_video_guides_reference.md](./testrig_twincat_video_guides_reference.md)
  Reference note for the repository-local video-guide extraction workflow,
  companion-note errata, and reusable analysis path for TwinCAT/TestRig media.
- [video_guides/README.md](./video_guides/README.md)
  Repository-owned per-video report tree for the analyzed TwinCAT/TestRig
  video guides, including copied reference images.
- [video_guides/REMOTE_HIGH_QUALITY_RERUN_README.md](./video_guides/REMOTE_HIGH_QUALITY_RERUN_README.md)
  Provenance note for the promoted remote `large-v3` plus `openai/gpt-oss-20b`
  video-guide artifact set and its temporary tracked rerun roots.
- [../reports/analysis/twincat_video_guides/[2026-04-02]/remote_high_quality_video_campaign_sum_up.md](../reports/analysis/twincat_video_guides/%5B2026-04-02%5D/remote_high_quality_video_campaign_sum_up.md)
  Cross-video campaign sum-up for the current canonical remote-strong TwinCAT/TestRig video rerun.

## Usage

- Treat `blind_handover_controller_reference.md` as the strict default when implementation details are undecided.
- Use the other two documents to reinforce or confirm patterns already compatible with the main baseline.
- Use these notes together with `doc/reference_summaries/06_Programming_Style_Guide.md` when writing new ML or utility code in this repository.
