# Validation Setup Report

## Overview

This report summarizes a repository-owned lightweight validation pass executed through `scripts/training/validate_training_setup.py`.

- model family: `periodic_gru_sequence_fw`;
- model type: `periodic_gru_sequence`;
- logical run name: `te_periodic_gru_sequence_remote_Fw`;
- output run name: `te_periodic_gru_sequence_remote_Fw_wave2b_package_final_validation`;
- run instance id: `2026-05-25-13-49-32__te_periodic_gru_sequence_remote_fw_wave2b_package_final_validation`;
- lightweight validation result: **pass**

## Validation Context

| Field | Value |
| --- | --- |
| Config Path | `config/training/wave2b_harmonic_temporal_hybrid/campaigns/2026-05-25_wave2b_harmonic_temporal_hybrid_campaign/queue/05_periodic_gru_sequence_fw.yaml` |
| Output Directory | `output/validation_checks/periodic_gru_sequence_fw/2026-05-25-13-49-32__te_periodic_gru_sequence_remote_fw_wave2b_package_final_validation` |
| Model Family | `periodic_gru_sequence_fw` |
| Model Type | `periodic_gru_sequence` |
| Run Name | `te_periodic_gru_sequence_remote_Fw` |
| Output Run Name | `te_periodic_gru_sequence_remote_Fw_wave2b_package_final_validation` |
| Run Instance ID | `2026-05-25-13-49-32__te_periodic_gru_sequence_remote_fw_wave2b_package_final_validation` |

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
| Loss | 1.37318456 |
| MAE | 0.02326995 |
| RMSE | 0.02769721 |

## Interpretation

The validation setup passed all finite checks on the selected batch or reduced validation subset. This means the current training wiring is structurally healthy enough for further smoke-test or training work.

## Notes

- This is a lightweight validation-check artifact, not a full training-results report.
- The machine-readable companion artifact remains `validation_summary.yaml`.
- The intended next step after a successful result is usually a smoke test or a broader training execution, not automatic promotion by itself.
