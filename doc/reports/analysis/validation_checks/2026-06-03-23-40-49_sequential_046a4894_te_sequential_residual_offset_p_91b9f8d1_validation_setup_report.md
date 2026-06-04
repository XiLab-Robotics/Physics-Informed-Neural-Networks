# Validation Setup Report

## Overview

This report summarizes a repository-owned lightweight validation pass executed through `scripts/training/validate_training_setup.py`.

- model family: `sequential_residual_offset_probe`;
- model type: `sequential_residual_offset_probe`;
- logical run name: `te_sequential_residual_offset_probe_remote_global`;
- output run name: `te_sequential_residual_offset_probe_remote_global_validation_check`;
- run instance id: `2026-06-03-23-40-24__te_sequential_residual_offset_probe_remote_global_validation_check`;
- lightweight validation result: **pass**

## Validation Context

| Field | Value |
| --- | --- |
| Config Path | `config/training/track2f_offset_aware_probe/campaigns/2026-06-03_track2f_offset_aware_probe_campaign/queue/01_sequential_residual_offset_probe_global.yaml` |
| Output Directory | `output/validation_checks/sequential_residual_offset_probe/2026-06-03-23-40-24__te_sequential_residual_offset_probe_remote_global_validation_check` |
| Model Family | `sequential_residual_offset_probe` |
| Model Type | `sequential_residual_offset_probe` |
| Run Name | `te_sequential_residual_offset_probe_remote_global` |
| Output Run Name | `te_sequential_residual_offset_probe_remote_global_validation_check` |
| Run Instance ID | `2026-06-03-23-40-24__te_sequential_residual_offset_probe_remote_global_validation_check` |

## Batch Structure

| Field | Value |
| --- | --- |
| Batch Mode | `sequence` |
| Point Batch Size | 0 |
| Sequence Batch Size | 384 |
| Sequence Length | 33 |
| Input Feature Dim | 5 |
| Target Feature Dim | 1 |
| Curve Count | 2 |

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
| Loss | 0.71396095 |
| MAE | 0.03373976 |
| RMSE | 0.03930778 |

## Interpretation

The validation setup passed all finite checks on the selected batch or reduced validation subset. This means the current training wiring is structurally healthy enough for further smoke-test or training work.

## Notes

- This is a lightweight validation-check artifact, not a full training-results report.
- The machine-readable companion artifact remains `validation_summary.yaml`.
- The intended next step after a successful result is usually a smoke test or a broader training execution, not automatic promotion by itself.
