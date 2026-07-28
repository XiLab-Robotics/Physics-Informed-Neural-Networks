# Validation Setup Report

## Overview

This report summarizes a repository-owned lightweight validation pass executed through `scripts/training/validate_training_setup.py`.

- model family: `stage4_c03_r1_compact`;
- model type: `data_only_residual_capacity`;
- logical run name: `te_stage4_c03_r1_compact__polished_setpoints_fw`;
- output run name: `te_stage4_c03_r1_compact__polished_setpoints_fw_validation_check`;
- run instance id: `2026-07-28-09-57-28__te_stage4_c03_r1_compact__polished_setpoints_fw_validation_check`;
- lightweight validation result: **pass**

## Validation Context

| Field | Value |
| --- | --- |
| Config Path | `config/training/data_only_residual_capacity/campaigns/2026-07-28_wave52r_stage4_data_only_residual_capacity/queue/003_c03_r1_compact.yaml` |
| Output Directory | `output/validation_checks/stage4_c03_r1_compact/2026-07-28-09-57-28__te_stage4_c03_r1_compact__polished_setpoints_fw_validation_check` |
| Model Family | `stage4_c03_r1_compact` |
| Model Type | `data_only_residual_capacity` |
| Run Name | `te_stage4_c03_r1_compact__polished_setpoints_fw` |
| Output Run Name | `te_stage4_c03_r1_compact__polished_setpoints_fw_validation_check` |
| Run Instance ID | `2026-07-28-09-57-28__te_stage4_c03_r1_compact__polished_setpoints_fw_validation_check` |

## Batch Structure

| Field | Value |
| --- | --- |
| Batch Mode | `point` |
| Point Batch Size | 1430 |
| Sequence Batch Size | 0 |
| Sequence Length | 0 |
| Input Feature Dim | 5 |
| Target Feature Dim | 1 |
| Curve Count | 1 |

## Dataset Split

| Split | Curve Count |
| --- | ---: |
| Train | 675 |
| Validation | 194 |
| Test | 97 |

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
| Loss | 16.92215538 |
| MAE | 0.05595514 |
| RMSE | 0.05733729 |

## Interpretation

The validation setup passed all finite checks on the selected batch or reduced validation subset. This means the current training wiring is structurally healthy enough for further smoke-test or training work.

## Notes

- This is a lightweight validation-check artifact, not a full training-results report.
- The machine-readable companion artifact remains `validation_summary.yaml`.
- The intended next step after a successful result is usually a smoke test or a broader training execution, not automatic promotion by itself.
