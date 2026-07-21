# Validation Setup Report

## Overview

This report summarizes a repository-owned lightweight validation pass executed through `scripts/training/validate_training_setup.py`.

- model family: `shape_objective_curve_aware_residual_fw`;
- model type: `curve_aware_harmonic_residual_offset_probe`;
- logical run name: `te_shape_objective_curve_aware_residual_fw__polished_setpoints`;
- output run name: `te_shape_objective_curve_aware_residual_fw__polished_setpoints_validation_check`;
- run instance id: `2026-07-21-18-48-51__te_shape_objective_curve_aware_residual_fw__polished_setpoints_validation_check`;
- lightweight validation result: **pass**

## Validation Context

| Field | Value |
| --- | --- |
| Config Path | `config/training/shape_objective_followup/campaigns/2026-07-21_parallel_shape_objective_followup/queue/003_shape_objective_curve_aware_residual_fw.yaml` |
| Output Directory | `output/validation_checks/shape_objective_curve_aware_residual_fw/2026-07-21-18-48-51__te_shape_objective_curve_aware_residual_fw__polished_setpoints_validation_check` |
| Model Family | `shape_objective_curve_aware_residual_fw` |
| Model Type | `curve_aware_harmonic_residual_offset_probe` |
| Run Name | `te_shape_objective_curve_aware_residual_fw__polished_setpoints` |
| Output Run Name | `te_shape_objective_curve_aware_residual_fw__polished_setpoints_validation_check` |
| Run Instance ID | `2026-07-21-18-48-51__te_shape_objective_curve_aware_residual_fw__polished_setpoints_validation_check` |

## Batch Structure

| Field | Value |
| --- | --- |
| Batch Mode | `sequence` |
| Point Batch Size | 0 |
| Sequence Batch Size | 64 |
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
| Loss | 146050053662834688.00000000 |
| MAE | 5081742.00000000 |
| RMSE | 6147453.50000000 |

## Interpretation

The validation setup passed all finite checks on the selected batch or reduced validation subset. This means the current training wiring is structurally healthy enough for further smoke-test or training work.

## Notes

- This is a lightweight validation-check artifact, not a full training-results report.
- The machine-readable companion artifact remains `validation_summary.yaml`.
- The intended next step after a successful result is usually a smoke test or a broader training execution, not automatic promotion by itself.
