# Validation Setup Report

## Overview

This report summarizes a repository-owned lightweight validation pass executed through `scripts/training/validate_training_setup.py`.

- model family: `track2h_dispersion_aware_mae_robust_global`;
- model type: `curve_aware_harmonic_residual_offset_probe`;
- logical run name: `te_track2h_mae_robust_global`;
- output run name: `te_track2h_mae_robust_global_track2h_mae_global_one_batch_validation`;
- run instance id: `2026-06-11-11-24-22__te_track2h_mae_robust_global_track2h_mae_global_one_batch_validation`;
- lightweight validation result: **pass**

## Validation Context

| Field | Value |
| --- | --- |
| Config Path | `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign/queue/01_mae_robust_global.yaml` |
| Output Directory | `output/validation_checks/track2h_dispersion_aware_mae_robust_global/2026-06-11-11-24-22__te_track2h_mae_robust_global_track2h_mae_global_one_batch_validation` |
| Model Family | `track2h_dispersion_aware_mae_robust_global` |
| Model Type | `curve_aware_harmonic_residual_offset_probe` |
| Run Name | `te_track2h_mae_robust_global` |
| Output Run Name | `te_track2h_mae_robust_global_track2h_mae_global_one_batch_validation` |
| Run Instance ID | `2026-06-11-11-24-22__te_track2h_mae_robust_global_track2h_mae_global_one_batch_validation` |

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
| Loss | 2.05355692 |
| MAE | 0.09553183 |
| RMSE | 0.11571940 |

## Interpretation

The validation setup passed all finite checks on the selected batch or reduced validation subset. This means the current training wiring is structurally healthy enough for further smoke-test or training work.

## Notes

- This is a lightweight validation-check artifact, not a full training-results report.
- The machine-readable companion artifact remains `validation_summary.yaml`.
- The intended next step after a successful result is usually a smoke test or a broader training execution, not automatic promotion by itself.
