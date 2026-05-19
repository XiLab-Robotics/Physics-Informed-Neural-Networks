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
- winning mean component MAPE: `1934.886%`
- winning mean component MAE: `0.212056`
- winning mean component RMSE: `0.294670`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 1934.886 | 0.212056 | 0.294670 | `{'estimator__activation': 'tanh', 'estimator__early_stopping': True, 'estimator__hidden_layer_sizes': (200, 50), 'estimator__learning_rate': 'adaptive', 'estimator__solver': 'adam'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `MLP` | 0.021657 | 0.029719 | 45.773 |
| `fft_y_Fw_filtered_ampl_1` | `MLP` | 0.014124 | 0.021429 | 82.165 |
| `fft_y_Fw_filtered_phase_1` | `MLP` | 0.010063 | 0.015193 | 332.205 |
| `fft_y_Fw_filtered_ampl_3` | `MLP` | 0.011750 | 0.019724 | 1571.655 |
| `fft_y_Fw_filtered_phase_3` | `MLP` | 0.073296 | 0.092004 | 4.033 |
| `fft_y_Fw_filtered_ampl_39` | `MLP` | 0.014020 | 0.022136 | 1423.059 |
| `fft_y_Fw_filtered_phase_39` | `MLP` | 0.095218 | 0.117154 | 8.666 |
| `fft_y_Fw_filtered_ampl_40` | `MLP` | 0.020299 | 0.033202 | 2502.003 |
| `fft_y_Fw_filtered_phase_40` | `MLP` | 0.076265 | 0.097546 | 103.480 |
| `fft_y_Fw_filtered_ampl_78` | `MLP` | 0.014506 | 0.023857 | 4218.719 |
| `fft_y_Fw_filtered_phase_78` | `MLP` | 0.203570 | 0.287177 | 448.388 |
| `fft_y_Fw_filtered_ampl_81` | `MLP` | 0.006502 | 0.012027 | 2165.889 |
| `fft_y_Fw_filtered_phase_81` | `MLP` | 0.172133 | 0.233855 | 17.335 |
| `fft_y_Fw_filtered_ampl_156` | `MLP` | 0.009218 | 0.014408 | 8357.069 |
| `fft_y_Fw_filtered_phase_156` | `MLP` | 1.697385 | 1.967759 | 80.146 |
| `fft_y_Fw_filtered_ampl_162` | `MLP` | 0.011904 | 0.020324 | 11746.107 |
| `fft_y_Fw_filtered_phase_162` | `MLP` | 0.860041 | 1.415097 | 39.343 |
| `fft_y_Fw_filtered_ampl_240` | `MLP` | 0.010430 | 0.018034 | 3268.685 |
| `fft_y_Fw_filtered_phase_240` | `MLP` | 0.706686 | 1.158094 | 348.113 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/forward_remote_diagnostic/mlp/2026-04-25_track1_forward_mlp_remote_diagnostic/001_track1_original_dataset_forward_mlp_remote_diagnostic.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_diagnostic/2026-04-25-16-16-45__track1_original_dataset_forward_mlp_remote_diagnostic_remote_diagnostic`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_diagnostic/2026-04-25-16-16-45__track1_original_dataset_forward_mlp_remote_diagnostic_remote_diagnostic/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_diagnostic/2026-04-25-16-16-45__track1_original_dataset_forward_mlp_remote_diagnostic_remote_diagnostic/validation_summary.yaml`
