# Validation Setup Report

## Overview

This report summarizes a repository-owned lightweight validation pass executed through `scripts/training/validate_training_setup.py`.

- model family: `track2g_curve_aware_harmonic_residual_offset_pointwise_control_global`;
- model type: `curve_aware_harmonic_residual_offset_probe`;
- logical run name: `te_track2g_curve_aware_pointwise_control_global`;
- output run name: `te_track2g_curve_aware_pointwise_control_global_track2g_pointwise_control_setup_2026_06_08`;
- run instance id: `2026-06-08-18-13-58__te_track2g_curve_aware_pointwise_control_global_track2g_pointwise_control_setup_2026_06_08`;
- lightweight validation result: **pass**

## Validation Context

| Field | Value |
| --- | --- |
| Config Path | `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign/queue/01_pointwise_control_global.yaml` |
| Output Directory | `output/validation_checks/track2g_curve_aware_harmonic_residual_offset_pointwise_control_global/2026-06-08-18-13-58__te_track2g_curve_aware_pointwise_control_global_track2g_pointwise_control_setup_2026_06_08` |
| Model Family | `track2g_curve_aware_harmonic_residual_offset_pointwise_control_global` |
| Model Type | `curve_aware_harmonic_residual_offset_probe` |
| Run Name | `te_track2g_curve_aware_pointwise_control_global` |
| Output Run Name | `te_track2g_curve_aware_pointwise_control_global_track2g_pointwise_control_setup_2026_06_08` |
| Run Instance ID | `2026-06-08-18-13-58__te_track2g_curve_aware_pointwise_control_global_track2g_pointwise_control_setup_2026_06_08` |

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
| Loss | 5.80928946 |
| MAE | 0.08800610 |
| RMSE | 0.11212510 |

## Interpretation

The validation setup passed all finite checks on the selected batch or reduced validation subset. This means the current training wiring is structurally healthy enough for further smoke-test or training work.

## Notes

- This is a lightweight validation-check artifact, not a full training-results report.
- The machine-readable companion artifact remains `validation_summary.yaml`.
- The intended next step after a successful result is usually a smoke test or a broader training execution, not automatic promotion by itself.
