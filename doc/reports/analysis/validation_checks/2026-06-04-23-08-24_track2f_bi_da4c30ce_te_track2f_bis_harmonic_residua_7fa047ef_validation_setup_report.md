# Validation Setup Report

## Overview

This report summarizes a repository-owned lightweight validation pass executed through `scripts/training/validate_training_setup.py`.

- model family: `track2f_bis_harmonic_residual_offset_global`;
- model type: `harmonic_residual_offset_probe`;
- logical run name: `te_track2f_bis_harmonic_residual_offset_global`;
- output run name: `te_track2f_bis_harmonic_residual_offset_global_track2f_bis_harmonic_global_validation`;
- run instance id: `2026-06-04-23-07-55__te_track2f_bis_harmonic_residual_offset_global_track2f_bis_harmonic_global_validation`;
- lightweight validation result: **pass**

## Validation Context

| Field | Value |
| --- | --- |
| Config Path | `config/training/track2f_bis_harmonic_offset_probe/campaigns/2026-06-04_track2f_bis_harmonic_offset_probe_campaign/queue/04_harmonic_residual_offset_probe_global.yaml` |
| Output Directory | `output/validation_checks/track2f_bis_harmonic_residual_offset_global/2026-06-04-23-07-55__te_track2f_bis_harmonic_residual_offset_global_track2f_bis_harmonic_global_validation` |
| Model Family | `track2f_bis_harmonic_residual_offset_global` |
| Model Type | `harmonic_residual_offset_probe` |
| Run Name | `te_track2f_bis_harmonic_residual_offset_global` |
| Output Run Name | `te_track2f_bis_harmonic_residual_offset_global_track2f_bis_harmonic_global_validation` |
| Run Instance ID | `2026-06-04-23-07-55__te_track2f_bis_harmonic_residual_offset_global_track2f_bis_harmonic_global_validation` |

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
| Loss | 4.19489241 |
| MAE | 0.07648151 |
| RMSE | 0.09528001 |

## Interpretation

The validation setup passed all finite checks on the selected batch or reduced validation subset. This means the current training wiring is structurally healthy enough for further smoke-test or training work.

## Notes

- This is a lightweight validation-check artifact, not a full training-results report.
- The machine-readable companion artifact remains `validation_summary.yaml`.
- The intended next step after a successful result is usually a smoke test or a broader training execution, not automatic promotion by itself.
