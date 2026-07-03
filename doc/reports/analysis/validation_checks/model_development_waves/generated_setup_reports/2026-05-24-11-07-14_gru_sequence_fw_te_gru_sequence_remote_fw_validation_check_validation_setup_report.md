# Validation Setup Report

## Overview

This report summarizes a repository-owned lightweight validation pass executed through `scripts/training/validate_training_setup.py`.

- model family: `gru_sequence_fw`;
- model type: `gru_sequence`;
- logical run name: `te_gru_sequence_remote_Fw`;
- output run name: `te_gru_sequence_remote_Fw_validation_check`;
- run instance id: `2026-05-24-11-06-58__te_gru_sequence_remote_fw_validation_check`;
- lightweight validation result: **pass**

## Validation Context

| Field | Value |
| --- | --- |
| Config Path | `config/training/wave2_temporal_model_entry/campaigns/2026-05-24_wave2_temporal_model_entry_campaign/queue/05_gru_sequence_fw.yaml` |
| Output Directory | `output/validation_checks/gru_sequence_fw/2026-05-24-11-06-58__te_gru_sequence_remote_fw_validation_check` |
| Model Family | `gru_sequence_fw` |
| Model Type | `gru_sequence` |
| Run Name | `te_gru_sequence_remote_Fw` |
| Output Run Name | `te_gru_sequence_remote_Fw_validation_check` |
| Run Instance ID | `2026-05-24-11-06-58__te_gru_sequence_remote_fw_validation_check` |

## Batch Structure

| Field | Value |
| --- | ---: |
| Point Batch Size | 0 |
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
| Loss | 0.43670830 |
| MAE | 0.01285022 |
| RMSE | 0.01561950 |

## Interpretation

The validation setup passed all finite checks on the selected batch or reduced validation subset. This means the current training wiring is structurally healthy enough for further smoke-test or training work.

## Notes

- This is a lightweight validation-check artifact, not a full training-results report.
- The machine-readable companion artifact remains `validation_summary.yaml`.
- The intended next step after a successful result is usually a smoke test or a broader training execution, not automatic promotion by itself.
