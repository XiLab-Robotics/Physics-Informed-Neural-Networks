# Validation Setup Report

## Overview

This report summarizes a repository-owned lightweight validation pass executed through `scripts/training/validate_training_setup.py`.

- model family: `shape_first_distilled_periodic_mlp_harmonic_fw`;
- model type: `periodic_mlp`;
- logical run name: `te_shape_first_distilled_periodic_mlp_harmonic_fw__polished_setpoints`;
- output run name: `te_shape_first_distilled_periodic_mlp_harmonic_fw__polished_setpoints_validation_check`;
- run instance id: `2026-07-22-13-18-38__te_shape_first_distilled_periodic_mlp_harmonic_fw__polished_setpoints_validation_check`;
- lightweight validation result: **pass**

## Validation Context

| Field | Value |
| --- | --- |
| Config Path | `config/training/shape_first_training_rule_distillation/campaigns/2026-07-22_shape_first_training_rule_distillation_pilot/queue/002_shape_first_distilled_periodic_mlp_harmonic_fw.yaml` |
| Output Directory | `output/validation_checks/shape_first_distilled_periodic_mlp_harmonic_fw/2026-07-22-13-18-38__te_shape_first_distilled_periodic_mlp_harmonic_fw__polished_setpoints_validation_check` |
| Model Family | `shape_first_distilled_periodic_mlp_harmonic_fw` |
| Model Type | `periodic_mlp` |
| Run Name | `te_shape_first_distilled_periodic_mlp_harmonic_fw__polished_setpoints` |
| Output Run Name | `te_shape_first_distilled_periodic_mlp_harmonic_fw__polished_setpoints_validation_check` |
| Run Instance ID | `2026-07-22-13-18-38__te_shape_first_distilled_periodic_mlp_harmonic_fw__polished_setpoints_validation_check` |

## Batch Structure

| Field | Value |
| --- | --- |
| Batch Mode | `point` |
| Point Batch Size | 256 |
| Sequence Batch Size | 0 |
| Sequence Length | 0 |
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
| Loss | 0.64721346 |
| MAE | 0.01233484 |
| RMSE | 0.01496146 |

## Interpretation

The validation setup passed all finite checks on the selected batch or reduced validation subset. This means the current training wiring is structurally healthy enough for further smoke-test or training work.

## Notes

- This is a lightweight validation-check artifact, not a full training-results report.
- The machine-readable companion artifact remains `validation_summary.yaml`.
- The intended next step after a successful result is usually a smoke test or a broader training execution, not automatic promotion by itself.
