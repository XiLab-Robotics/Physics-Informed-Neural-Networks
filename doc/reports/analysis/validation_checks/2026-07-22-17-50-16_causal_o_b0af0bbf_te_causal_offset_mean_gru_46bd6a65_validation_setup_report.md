# Validation Setup Report

## Overview

This report summarizes a repository-owned lightweight validation pass executed through `scripts/training/validate_training_setup.py`.

- model family: `causal_offset_mean_gru_sequence_fw`;
- model type: `sequential_residual_offset_probe`;
- logical run name: `te_causal_offset_mean_gru_sequence_fw__polished_setpoints`;
- output run name: `te_causal_offset_mean_gru_sequence_fw__polished_setpoints_validation_check`;
- run instance id: `2026-07-22-17-50-15__te_causal_offset_mean_gru_sequence_fw__polished_setpoints_validation_check`;
- lightweight validation result: **pass**

## Validation Context

| Field | Value |
| --- | --- |
| Config Path | `config/training/causal_offset_mean_calibration/campaigns/2026-07-22_causal_offset_mean_calibration_pilot/queue/001_causal_offset_mean_gru_sequence_fw.yaml` |
| Output Directory | `output/validation_checks/causal_offset_mean_gru_sequence_fw/2026-07-22-17-50-15__te_causal_offset_mean_gru_sequence_fw__polished_setpoints_validation_check` |
| Model Family | `causal_offset_mean_gru_sequence_fw` |
| Model Type | `sequential_residual_offset_probe` |
| Run Name | `te_causal_offset_mean_gru_sequence_fw__polished_setpoints` |
| Output Run Name | `te_causal_offset_mean_gru_sequence_fw__polished_setpoints_validation_check` |
| Run Instance ID | `2026-07-22-17-50-15__te_causal_offset_mean_gru_sequence_fw__polished_setpoints_validation_check` |

## Batch Structure

| Field | Value |
| --- | --- |
| Batch Mode | `sequence` |
| Point Batch Size | 0 |
| Sequence Batch Size | 96 |
| Sequence Length | 33 |
| Input Feature Dim | 5 |
| Target Feature Dim | 1 |
| Curve Count | 1 |

## Finite Checks

| Check | Status |
| --- | --- |
| Finite Loss | Pass |
| Finite MAE | Pass |
| Finite RMSE | Pass |
| Finite Prediction Tensor | Pass |

## Metrics

| Metric | Value |
| --- | ---: |
| Loss | 0.58745372 |
| MAE | 0.01203489 |
| RMSE | 0.01445077 |

## Interpretation

The validation setup passed all finite checks on the selected batch or reduced validation subset. This means the current training wiring is structurally healthy enough for further smoke-test or training work.

## Notes

- This is a lightweight validation-check artifact, not a full training-results report.
- The machine-readable companion artifact remains `validation_summary.yaml`.
- The intended next step after a successful result is usually a smoke test or a broader training execution, not automatic promotion by itself.
