# Validation Setup Report

## Overview

This report summarizes a repository-owned lightweight validation pass executed through `scripts/training/validate_training_setup.py`.

- model family: `residual_harmonic_gru_sequence_fw_dense240`;
- model type: `residual_harmonic_gru_sequence`;
- logical run name: `te_residual_harmonic_gru_sequence_remote_Fw_dense240`;
- output run name: `te_residual_harmonic_gru_sequence_remote_Fw_dense240_wave2c_dense240_fw_validation`;
- run instance id: `2026-05-27-18-26-04__te_residual_harmonic_gru_sequence_remote_fw_dense240_wave2c_dense240_fw_validation`;
- lightweight validation result: **pass**

## Validation Context

| Field | Value |
| --- | --- |
| Config Path | `config/training/wave2c_residual_harmonic_temporal_hybrid/campaigns/2026-05-27_wave2c_residual_harmonic_temporal_hybrid_campaign/queue/05_residual_harmonic_gru_sequence_dense_240_fw.yaml` |
| Output Directory | `output/validation_checks/residual_harmonic_gru_sequence_fw_dense240/2026-05-27-18-26-04__te_residual_harmonic_gru_sequence_remote_fw_dense240_wave2c_dense240_fw_validation` |
| Model Family | `residual_harmonic_gru_sequence_fw_dense240` |
| Model Type | `residual_harmonic_gru_sequence` |
| Run Name | `te_residual_harmonic_gru_sequence_remote_Fw_dense240` |
| Output Run Name | `te_residual_harmonic_gru_sequence_remote_Fw_dense240_wave2c_dense240_fw_validation` |
| Run Instance ID | `2026-05-27-18-26-04__te_residual_harmonic_gru_sequence_remote_fw_dense240_wave2c_dense240_fw_validation` |

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
| Loss | 0.42906296 |
| MAE | 0.01270391 |
| RMSE | 0.01548218 |

## Interpretation

The validation setup passed all finite checks on the selected batch or reduced validation subset. This means the current training wiring is structurally healthy enough for further smoke-test or training work.

## Notes

- This is a lightweight validation-check artifact, not a full training-results report.
- The machine-readable companion artifact remains `validation_summary.yaml`.
- The intended next step after a successful result is usually a smoke test or a broader training execution, not automatic promotion by itself.
