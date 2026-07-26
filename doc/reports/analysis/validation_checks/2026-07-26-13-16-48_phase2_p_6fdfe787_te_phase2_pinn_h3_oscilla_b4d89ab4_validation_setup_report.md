# Validation Setup Report

## Overview

This report summarizes a repository-owned lightweight validation pass executed through `scripts/training/validate_training_setup.py`.

- model family: `phase2_pinn_h3_oscillator_periodic_bauer_anchor_bw`;
- model type: `harmonic_kinematic_pinn`;
- logical run name: `te_phase2_pinn_h3_oscillator_periodic_bauer_anchor_bw__polished_setpoints`;
- output run name: `te_phase2_pinn_h3_oscillator_periodic_bauer_anchor_bw__polished_setpoints_validation_check`;
- run instance id: `2026-07-26-13-16-47__te_phase2_pinn_h3_oscillator_periodic_bauer_anchor_bw__polished_setpoints_validation_check`;
- lightweight validation result: **pass**

## Validation Context

| Field | Value |
| --- | --- |
| Config Path | `config/training/harmonic_kinematic_pinn/campaigns/2026-07-26_phase2_harmonic_kinematic_pinn/queue/008_h3_oscillator_periodic_bauer_anchor_bw.yaml` |
| Output Directory | `output/validation_checks/phase2_pinn_h3_oscillator_periodic_bauer_anchor_bw/2026-07-26-13-16-47__te_phase2_pinn_h3_oscillator_periodic_bauer_anchor_bw__polished_setpoints_validation_check` |
| Model Family | `phase2_pinn_h3_oscillator_periodic_bauer_anchor_bw` |
| Model Type | `harmonic_kinematic_pinn` |
| Run Name | `te_phase2_pinn_h3_oscillator_periodic_bauer_anchor_bw__polished_setpoints` |
| Output Run Name | `te_phase2_pinn_h3_oscillator_periodic_bauer_anchor_bw__polished_setpoints_validation_check` |
| Run Instance ID | `2026-07-26-13-16-47__te_phase2_pinn_h3_oscillator_periodic_bauer_anchor_bw__polished_setpoints_validation_check` |

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
| Loss | 3.48900318 |
| MAE | 0.03645262 |
| RMSE | 0.03864324 |

## Interpretation

The validation setup passed all finite checks on the selected batch or reduced validation subset. This means the current training wiring is structurally healthy enough for further smoke-test or training work.

## Notes

- This is a lightweight validation-check artifact, not a full training-results report.
- The machine-readable companion artifact remains `validation_summary.yaml`.
- The intended next step after a successful result is usually a smoke test or a broader training execution, not automatic promotion by itself.
