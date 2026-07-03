# Validation Setup Report

## Overview

This report summarizes a repository-owned lightweight validation pass executed through `scripts/training/validate_training_setup.py`.

- model family: `temporal_convolution_fw`;
- model type: `temporal_convolution`;
- logical run name: `te_temporal_convolution_sequence_remote_Fw`;
- output run name: `te_temporal_convolution_sequence_remote_Fw_validation_check`;
- run instance id: `2026-05-24-11-05-51__te_temporal_convolution_sequence_remote_fw_validation_check`;
- lightweight validation result: **pass**

## Validation Context

| Field | Value |
| --- | --- |
| Config Path | `config/training/wave2_temporal_model_entry/campaigns/2026-05-24_wave2_temporal_model_entry_campaign/queue/02_temporal_convolution_fw.yaml` |
| Output Directory | `output/validation_checks/temporal_convolution_fw/2026-05-24-11-05-51__te_temporal_convolution_sequence_remote_fw_validation_check` |
| Model Family | `temporal_convolution_fw` |
| Model Type | `temporal_convolution` |
| Run Name | `te_temporal_convolution_sequence_remote_Fw` |
| Output Run Name | `te_temporal_convolution_sequence_remote_Fw_validation_check` |
| Run Instance ID | `2026-05-24-11-05-51__te_temporal_convolution_sequence_remote_fw_validation_check` |

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
| Loss | 1.28190696 |
| MAE | 0.02249249 |
| RMSE | 0.02676084 |

## Interpretation

The validation setup passed all finite checks on the selected batch or reduced validation subset. This means the current training wiring is structurally healthy enough for further smoke-test or training work.

## Notes

- This is a lightweight validation-check artifact, not a full training-results report.
- The machine-readable companion artifact remains `validation_summary.yaml`.
- The intended next step after a successful result is usually a smoke test or a broader training execution, not automatic promotion by itself.
