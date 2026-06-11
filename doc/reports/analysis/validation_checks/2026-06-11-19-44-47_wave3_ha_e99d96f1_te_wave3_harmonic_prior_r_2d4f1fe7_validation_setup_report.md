# Validation Setup Report

## Overview

This report summarizes a repository-owned lightweight validation pass executed through `scripts/training/validate_training_setup.py`.

- model family: `wave3_harmonic_prior_residual`;
- model type: `wave3_harmonic_prior_residual`;
- logical run name: `te_wave3_harmonic_prior_residual_training_smoke_ready`;
- output run name: `te_wave3_harmonic_prior_residual_training_smoke_ready_wave3_training_smoke_ready_final`;
- run instance id: `2026-06-11-19-44-20__te_wave3_harmonic_prior_residual_training_smoke_ready_wave3_training_smoke_ready_final`;
- lightweight validation result: **pass**

## Validation Context

| Field | Value |
| --- | --- |
| Config Path | `output/validation_checks/wave3_training_smoke_ready/generated_configs/wave3_harmonic_prior_residual_training_smoke_ready.yaml` |
| Output Directory | `output/validation_checks/wave3_harmonic_prior_residual/2026-06-11-19-44-20__te_wave3_harmonic_prior_residual_training_smoke_ready_wave3_training_smoke_ready_final` |
| Model Family | `wave3_harmonic_prior_residual` |
| Model Type | `wave3_harmonic_prior_residual` |
| Run Name | `te_wave3_harmonic_prior_residual_training_smoke_ready` |
| Output Run Name | `te_wave3_harmonic_prior_residual_training_smoke_ready_wave3_training_smoke_ready_final` |
| Run Instance ID | `2026-06-11-19-44-20__te_wave3_harmonic_prior_residual_training_smoke_ready_wave3_training_smoke_ready_final` |

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
| Loss | 6.78991079 |
| MAE | 0.09820018 |
| RMSE | 0.12121975 |

## Interpretation

The validation setup passed all finite checks on the selected batch or reduced validation subset. This means the current training wiring is structurally healthy enough for further smoke-test or training work.

## Notes

- This is a lightweight validation-check artifact, not a full training-results report.
- The machine-readable companion artifact remains `validation_summary.yaml`.
- The intended next step after a successful result is usually a smoke test or a broader training execution, not automatic promotion by itself.
