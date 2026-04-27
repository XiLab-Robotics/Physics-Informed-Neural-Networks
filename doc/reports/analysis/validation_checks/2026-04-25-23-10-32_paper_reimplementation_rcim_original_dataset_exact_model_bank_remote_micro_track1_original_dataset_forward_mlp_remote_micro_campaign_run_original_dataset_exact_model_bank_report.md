# Original-Dataset Exact RCIM Model Bank Validation Report

## Overview

This report covers the direction-specific exact-model-bank branch trained from the repository dataset under `data/datasets`.

- direction label: `forward`
- dataset root: `data/datasets`
- dataset config: `config/datasets/transmission_error_dataset.yaml`
- selected harmonics: `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`
- decomposition point stride: `1`
- feature schema: `rpm, deg, tor`
- target count: `19`

## Split Summary

- train rows / files: `678` / `678`
- validation rows / files: `194` / `194`
- test rows / files: `97` / `97`
- validation split: `0.2`
- test split: `0.1`
- random seed: `42`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `454.205%`
- winning mean component MAE: `0.112053`
- winning mean component RMSE: `0.193736`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 454.205 | 0.112053 | 0.193736 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `MLP` | 0.003893 | 0.004794 | 8.347 |
| `fft_y_Fw_filtered_ampl_1` | `MLP` | 0.002549 | 0.003421 | 14.847 |
| `fft_y_Fw_filtered_phase_1` | `MLP` | 0.003683 | 0.004763 | 389.191 |
| `fft_y_Fw_filtered_ampl_3` | `MLP` | 0.002648 | 0.003447 | 336.981 |
| `fft_y_Fw_filtered_phase_3` | `MLP` | 0.029055 | 0.037994 | 1.611 |
| `fft_y_Fw_filtered_ampl_39` | `MLP` | 0.002679 | 0.003569 | 256.328 |
| `fft_y_Fw_filtered_phase_39` | `MLP` | 0.026464 | 0.037131 | 2.384 |
| `fft_y_Fw_filtered_ampl_40` | `MLP` | 0.002571 | 0.003635 | 341.984 |
| `fft_y_Fw_filtered_phase_40` | `MLP` | 0.044888 | 0.065790 | 78.496 |
| `fft_y_Fw_filtered_ampl_78` | `MLP` | 0.003087 | 0.003830 | 723.233 |
| `fft_y_Fw_filtered_phase_78` | `MLP` | 0.122698 | 0.248533 | 110.179 |
| `fft_y_Fw_filtered_ampl_81` | `MLP` | 0.002645 | 0.003369 | 872.102 |
| `fft_y_Fw_filtered_phase_81` | `MLP` | 0.051670 | 0.074840 | 5.007 |
| `fft_y_Fw_filtered_ampl_156` | `MLP` | 0.003141 | 0.003914 | 2264.374 |
| `fft_y_Fw_filtered_phase_156` | `MLP` | 0.675206 | 0.881230 | 37.475 |
| `fft_y_Fw_filtered_ampl_162` | `MLP` | 0.003179 | 0.004077 | 2223.893 |
| `fft_y_Fw_filtered_phase_162` | `MLP` | 0.519444 | 1.116130 | 22.485 |
| `fft_y_Fw_filtered_ampl_240` | `MLP` | 0.002590 | 0.003741 | 769.074 |
| `fft_y_Fw_filtered_phase_240` | `MLP` | 0.626918 | 1.176774 | 171.901 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/forward_remote_micro/mlp/2026-04-25_track1_forward_mlp_remote_micro/001_track1_original_dataset_forward_mlp_remote_micro.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_micro/2026-04-25-23-08-41__track1_original_dataset_forward_mlp_remote_micro_campaign_run`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_micro/2026-04-25-23-08-41__track1_original_dataset_forward_mlp_remote_micro_campaign_run/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_micro/2026-04-25-23-08-41__track1_original_dataset_forward_mlp_remote_micro_campaign_run/validation_summary.yaml`
