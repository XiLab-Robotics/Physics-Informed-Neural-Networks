# Shape-Gate Loss Pilot Track 2 Shape Evaluation

## Overview

Evaluate the completed `shape_gate_loss_pilot_2026_07_20` checkpoint inside
the shape-gated `TE Curve Verification Pipeline` workflow and attempt to
generate the related Track 2 visual artifacts.

The candidate is intentionally narrow:

- dataset: `polished_dataset`;
- input mode: `setpoints`;
- surface: `Fw`;
- model type: `periodic_gru_sequence`;
- checkpoint:
  `output/training_runs/shape_gate_loss_pilot_periodic_gru_sequence/2026-07-20-19-59-14__te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints/checkpoints/periodic_gru_sequence-epoch=007-val_mae=0.00229675.ckpt`.

The evaluation must not promote the model from campaign scalar metrics. The
decision surface is the calibrated shape-gated reranker and, when available,
Track 2 curve visual evidence.

## Technical Approach

1. Inspect the existing `build_shape_gated_te_curve_reranker.py` and Track 2
   visual-report scripts to determine whether the completed PyTorch checkpoint
   can be evaluated directly or whether a narrow adapter/export path is needed.
2. Prefer a local, candidate-scoped evaluation over a full official matrix
   refresh because the pilot has only one `Fw` checkpoint and is not a full
   three-target, three-surface campaign.
3. Keep the existing calibrated gate thresholds and reduced selected-model
   comparison context intact.
4. Generate Track 2 plots only from complete curve predictions with matching
   angular-grid length. Do not compare truncated sequence-window centers
   against full measured curves.
5. Record the result as an exploratory shape-screening report unless the
   repository evidence supports a formal official verification refresh.

## Involved Components

- `scripts/reports/analysis/build_shape_gated_te_curve_reranker.py`
- `scripts/reports/analysis/build_track2_best_model_collage_report.py`
- `scripts/reports/analysis/build_track2_multi_model_curve_comparison_report.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
- `doc/running/active_training_campaign.yaml`
- `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/shape_gated_reranker/`
- `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/`
- `output/validation_checks/`

## Implementation Steps

1. Read the current shape-gated reranker inputs, candidate schemas, and output
   conventions.
2. Check whether the pilot checkpoint has enough metadata to reconstruct
   full-curve `polished_setpoints Fw` inference with the existing training
   datamodule/model loader.
3. If direct evaluation is supported, run a candidate-scoped shape-gated
   evaluation and write a dated report bundle.
4. If direct evaluation is not supported, implement the smallest checkpoint
   adapter needed to emit Track 2-compatible prediction curves for this one
   candidate.
5. Run the calibrated shape-gated reranker against the candidate and selected
   `polished_setpoints Fw` references.
6. Attempt Track 2 visual generation for the pilot candidate, keeping any
   generated plots under dated Track 2 report or validation-check roots.
7. Export and validate any final report PDFs that are produced.
8. Run scoped Markdown QA, Python compile checks for modified Python files,
   `git diff --check`, and Sphinx if documentation portal scope changes.

No subagent is planned for this task.
