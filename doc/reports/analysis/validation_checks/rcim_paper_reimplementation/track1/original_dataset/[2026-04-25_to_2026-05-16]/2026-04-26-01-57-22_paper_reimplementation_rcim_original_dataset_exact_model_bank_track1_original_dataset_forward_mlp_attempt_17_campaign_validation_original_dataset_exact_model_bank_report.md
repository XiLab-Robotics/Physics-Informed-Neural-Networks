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
- random seed: `47`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `429.912%`
- winning mean component MAE: `0.137773`
- winning mean component RMSE: `0.222552`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 429.912 | 0.137773 | 0.222552 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `MLP` | 0.004812 | 0.006338 | 21.973 |
| `fft_y_Fw_filtered_ampl_1` | `MLP` | 0.002995 | 0.003771 | 17.433 |
| `fft_y_Fw_filtered_phase_1` | `MLP` | 0.003918 | 0.005321 | 86.543 |
| `fft_y_Fw_filtered_ampl_3` | `MLP` | 0.002969 | 0.003766 | 390.520 |
| `fft_y_Fw_filtered_phase_3` | `MLP` | 0.028726 | 0.039371 | 1.595 |
| `fft_y_Fw_filtered_ampl_39` | `MLP` | 0.002945 | 0.003742 | 307.024 |
| `fft_y_Fw_filtered_phase_39` | `MLP` | 0.029652 | 0.047953 | 2.398 |
| `fft_y_Fw_filtered_ampl_40` | `MLP` | 0.002958 | 0.003751 | 366.924 |
| `fft_y_Fw_filtered_phase_40` | `MLP` | 0.046707 | 0.078651 | 95.579 |
| `fft_y_Fw_filtered_ampl_78` | `MLP` | 0.002966 | 0.003771 | 560.232 |
| `fft_y_Fw_filtered_phase_78` | `MLP` | 0.085359 | 0.131595 | 70.213 |
| `fft_y_Fw_filtered_ampl_81` | `MLP` | 0.002976 | 0.003777 | 1000.068 |
| `fft_y_Fw_filtered_phase_81` | `MLP` | 0.079220 | 0.118604 | 9.478 |
| `fft_y_Fw_filtered_ampl_156` | `MLP` | 0.002949 | 0.003721 | 2299.333 |
| `fft_y_Fw_filtered_phase_156` | `MLP` | 1.073897 | 1.698061 | 108.579 |
| `fft_y_Fw_filtered_ampl_162` | `MLP` | 0.003309 | 0.004240 | 1664.077 |
| `fft_y_Fw_filtered_phase_162` | `MLP` | 0.592296 | 0.919322 | 30.473 |
| `fft_y_Fw_filtered_ampl_240` | `MLP` | 0.003006 | 0.003802 | 1085.840 |
| `fft_y_Fw_filtered_phase_240` | `MLP` | 0.646028 | 1.148934 | 50.041 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/mlp/2026-04-26_track1_forward_mlp_original_dataset_mega_campaign/017_track1_original_dataset_forward_mlp_attempt_17.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-55-26__track1_original_dataset_forward_mlp_attempt_17_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-55-26__track1_original_dataset_forward_mlp_attempt_17_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-55-26__track1_original_dataset_forward_mlp_attempt_17_campaign_validation/validation_summary.yaml`
