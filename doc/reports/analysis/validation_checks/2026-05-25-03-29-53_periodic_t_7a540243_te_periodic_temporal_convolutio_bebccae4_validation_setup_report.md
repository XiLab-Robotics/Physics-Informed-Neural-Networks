# Validation Setup Report

## Overview

This report summarizes a repository-owned lightweight validation pass executed through `scripts/training/validate_training_setup.py`.

- model family: `periodic_temporal_convolution`;
- model type: `periodic_temporal_convolution`;
- logical run name: `te_periodic_temporal_convolution_sequence_remote_Fw`;
- output run name: `te_periodic_temporal_convolution_sequence_remote_Fw_wave2b_probe`;
- run instance id: `2026-05-25-03-29-31__te_periodic_temporal_convolution_sequence_remote_fw_wave2b_probe`;
- lightweight validation result: **pass**

## Validation Context

| Field | Value |
| --- | --- |
| Config Path | `config/training/hydra/wave2/materialized/training_configs/periodic_temporal_convolution_fw.yaml` |
| Output Directory | `output/validation_checks/periodic_temporal_convolution/2026-05-25-03-29-31__te_periodic_temporal_convolution_sequence_remote_fw_wave2b_probe` |
| Model Family | `periodic_temporal_convolution` |
| Model Type | `periodic_temporal_convolution` |
| Run Name | `te_periodic_temporal_convolution_sequence_remote_Fw` |
| Output Run Name | `te_periodic_temporal_convolution_sequence_remote_Fw_wave2b_probe` |
| Run Instance ID | `2026-05-25-03-29-31__te_periodic_temporal_convolution_sequence_remote_fw_wave2b_probe` |

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
| Loss | 1.17821145 |
| MAE | 0.02164378 |
| RMSE | 0.02565566 |

## Interpretation

The validation setup passed all finite checks on the selected batch or reduced validation subset. This means the current training wiring is structurally healthy enough for further smoke-test or training work.

## Notes

- This is a lightweight validation-check artifact, not a full training-results report.
- The machine-readable companion artifact remains `validation_summary.yaml`.
- The intended next step after a successful result is usually a smoke test or a broader training execution, not automatic promotion by itself.
