# Validation Setup Report

## Overview

This report summarizes a repository-owned lightweight validation pass executed through `scripts/training/validate_training_setup.py`.

- model family: `phase2_pinn_h1_oscillator_residual_bw`;
- model type: `harmonic_kinematic_pinn`;
- logical run name: `te_phase2_pinn_h1_oscillator_residual_bw__polished_setpoints`;
- output run name: `te_phase2_pinn_h1_oscillator_residual_bw__polished_setpoints_validation_check`;
- run instance id: `2026-07-26-14-02-29__te_phase2_pinn_h1_oscillator_residual_bw__polished_setpoints_validation_check`;
- lightweight validation result: **pass**

## Validation Context

| Field | Value |
| --- | --- |
| Config Path | `config/training/harmonic_kinematic_pinn/campaigns/2026-07-26_phase2_harmonic_kinematic_pinn/queue/004_h1_oscillator_residual_bw.yaml` |
| Output Directory | `output/validation_checks/phase2_pinn_h1_oscillator_residual_bw/2026-07-26-14-02-29__te_phase2_pinn_h1_oscillator_residual_bw__polished_setpoints_validation_check` |
| Model Family | `phase2_pinn_h1_oscillator_residual_bw` |
| Model Type | `harmonic_kinematic_pinn` |
| Run Name | `te_phase2_pinn_h1_oscillator_residual_bw__polished_setpoints` |
| Output Run Name | `te_phase2_pinn_h1_oscillator_residual_bw__polished_setpoints_validation_check` |
| Run Instance ID | `2026-07-26-14-02-29__te_phase2_pinn_h1_oscillator_residual_bw__polished_setpoints_validation_check` |

## Batch Structure

| Field | Value |
| --- | --- |
| Batch Mode | `point` |
| Point Batch Size | 1620 |
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
| Loss | 1.40440428 |
| MAE | 0.01124200 |
| RMSE | 0.01277633 |

## Interpretation

The validation setup passed all finite checks on the selected batch or reduced validation subset. This means the current training wiring is structurally healthy enough for further smoke-test or training work.

## Notes

- This is a lightweight validation-check artifact, not a full training-results report.
- The machine-readable companion artifact remains `validation_summary.yaml`.
- The intended next step after a successful result is usually a smoke test or a broader training execution, not automatic promotion by itself.
