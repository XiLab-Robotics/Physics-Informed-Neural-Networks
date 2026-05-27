# Validation Setup Report

## Overview

This report summarizes a repository-owned lightweight validation pass executed through `scripts/training/validate_training_setup.py`.

- model family: `residual_harmonic_lstm_sequence_bw_dense360`;
- model type: `residual_harmonic_lstm_sequence`;
- logical run name: `te_residual_harmonic_lstm_sequence_remote_Bw_dense360`;
- output run name: `te_residual_harmonic_lstm_sequence_remote_Bw_dense360_wave2c_dense360_bw_validation`;
- run instance id: `2026-05-27-18-26-04__te_residual_harmonic_lstm_sequence_remote_bw_dense360_wave2c_dense360_bw_validation`;
- lightweight validation result: **pass**

## Validation Context

| Field | Value |
| --- | --- |
| Config Path | `config/training/wave2c_residual_harmonic_temporal_hybrid/campaigns/2026-05-27_wave2c_residual_harmonic_temporal_hybrid_campaign/queue/18_residual_harmonic_lstm_sequence_dense_360_bw.yaml` |
| Output Directory | `output/validation_checks/residual_harmonic_lstm_sequence_bw_dense360/2026-05-27-18-26-04__te_residual_harmonic_lstm_sequence_remote_bw_dense360_wave2c_dense360_bw_validation` |
| Model Family | `residual_harmonic_lstm_sequence_bw_dense360` |
| Model Type | `residual_harmonic_lstm_sequence` |
| Run Name | `te_residual_harmonic_lstm_sequence_remote_Bw_dense360` |
| Output Run Name | `te_residual_harmonic_lstm_sequence_remote_Bw_dense360_wave2c_dense360_bw_validation` |
| Run Instance ID | `2026-05-27-18-26-04__te_residual_harmonic_lstm_sequence_remote_bw_dense360_wave2c_dense360_bw_validation` |

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
| Loss | 1.29352081 |
| MAE | 0.02395844 |
| RMSE | 0.02838474 |

## Interpretation

The validation setup passed all finite checks on the selected batch or reduced validation subset. This means the current training wiring is structurally healthy enough for further smoke-test or training work.

## Notes

- This is a lightweight validation-check artifact, not a full training-results report.
- The machine-readable companion artifact remains `validation_summary.yaml`.
- The intended next step after a successful result is usually a smoke test or a broader training execution, not automatic promotion by itself.
