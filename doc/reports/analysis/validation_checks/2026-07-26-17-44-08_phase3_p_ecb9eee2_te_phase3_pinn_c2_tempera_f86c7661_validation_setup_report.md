# Validation Setup Report

## Overview

This report summarizes a repository-owned lightweight validation pass executed through `scripts/training/validate_training_setup.py`.

- model family: `phase3_pinn_c2_temperature_compliance_soft_fw`;
- model type: `quasi_static_compliance_pinn`;
- logical run name: `te_phase3_pinn_c2_temperature_compliance_soft_fw__polished_setpoints`;
- output run name: `te_phase3_pinn_c2_temperature_compliance_soft_fw__polished_setpoints_validation_check`;
- run instance id: `2026-07-26-17-44-05__te_phase3_pinn_c2_temperature_compliance_soft_fw__polished_setpoints_validation_check`;
- lightweight validation result: **pass**

## Validation Context

| Field | Value |
| --- | --- |
| Config Path | `config/training/quasi_static_compliance_pinn/campaigns/2026-07-26_phase3_quasi_static_compliance_pinn/queue/006_c2_temperature_compliance_soft_fw.yaml` |
| Output Directory | `output/validation_checks/phase3_pinn_c2_temperature_compliance_soft_fw/2026-07-26-17-44-05__te_phase3_pinn_c2_temperature_compliance_soft_fw__polished_setpoints_validation_check` |
| Model Family | `phase3_pinn_c2_temperature_compliance_soft_fw` |
| Model Type | `quasi_static_compliance_pinn` |
| Run Name | `te_phase3_pinn_c2_temperature_compliance_soft_fw__polished_setpoints` |
| Output Run Name | `te_phase3_pinn_c2_temperature_compliance_soft_fw__polished_setpoints_validation_check` |
| Run Instance ID | `2026-07-26-17-44-05__te_phase3_pinn_c2_temperature_compliance_soft_fw__polished_setpoints_validation_check` |

## Batch Structure

| Field | Value |
| --- | --- |
| Batch Mode | `point` |
| Point Batch Size | 2209 |
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
| Loss | 12.29700565 |
| MAE | 0.04254784 |
| RMSE | 0.04617401 |

## Interpretation

The validation setup passed all finite checks on the selected batch or reduced validation subset. This means the current training wiring is structurally healthy enough for further smoke-test or training work.

## Notes

- This is a lightweight validation-check artifact, not a full training-results report.
- The machine-readable companion artifact remains `validation_summary.yaml`.
- The intended next step after a successful result is usually a smoke test or a broader training execution, not automatic promotion by itself.
