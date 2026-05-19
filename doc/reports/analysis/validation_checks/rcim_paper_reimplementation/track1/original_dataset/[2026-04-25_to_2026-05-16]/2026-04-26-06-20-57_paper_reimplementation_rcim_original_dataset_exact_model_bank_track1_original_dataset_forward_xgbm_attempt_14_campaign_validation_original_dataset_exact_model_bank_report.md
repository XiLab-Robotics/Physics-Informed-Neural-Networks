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
- random seed: `31`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `88.196%`
- winning mean component MAE: `0.209178`
- winning mean component RMSE: `0.290036`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 88.196 | 0.209178 | 0.290036 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.01, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `XGBM` | 0.010025 | 0.012390 | 24.940 |
| `fft_y_Fw_filtered_ampl_1` | `XGBM` | 0.000062 | 0.000076 | 0.360 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.003423 | 0.004941 | 72.133 |
| `fft_y_Fw_filtered_ampl_3` | `XGBM` | 0.000096 | 0.000117 | 12.849 |
| `fft_y_Fw_filtered_phase_3` | `XGBM` | 0.068215 | 0.083250 | 3.747 |
| `fft_y_Fw_filtered_ampl_39` | `XGBM` | 0.000172 | 0.000207 | 16.884 |
| `fft_y_Fw_filtered_phase_39` | `XGBM` | 0.124953 | 0.152103 | 10.551 |
| `fft_y_Fw_filtered_ampl_40` | `XGBM` | 0.000071 | 0.000090 | 9.188 |
| `fft_y_Fw_filtered_phase_40` | `XGBM` | 0.076357 | 0.095712 | 155.609 |
| `fft_y_Fw_filtered_ampl_78` | `XGBM` | 0.000336 | 0.000412 | 126.165 |
| `fft_y_Fw_filtered_phase_78` | `XGBM` | 0.274025 | 0.470480 | 238.569 |
| `fft_y_Fw_filtered_ampl_81` | `XGBM` | 0.000052 | 0.000069 | 15.238 |
| `fft_y_Fw_filtered_phase_81` | `XGBM` | 0.222819 | 0.290482 | 33.696 |
| `fft_y_Fw_filtered_ampl_156` | `XGBM` | 0.000386 | 0.000482 | 415.902 |
| `fft_y_Fw_filtered_phase_156` | `XGBM` | 1.518567 | 1.779434 | 68.437 |
| `fft_y_Fw_filtered_ampl_162` | `XGBM` | 0.000617 | 0.001685 | 255.148 |
| `fft_y_Fw_filtered_phase_162` | `XGBM` | 0.937157 | 1.313550 | 41.579 |
| `fft_y_Fw_filtered_ampl_240` | `XGBM` | 0.000212 | 0.000326 | 121.426 |
| `fft_y_Fw_filtered_phase_240` | `XGBM` | 0.736829 | 1.304876 | 53.302 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/xgbm/2026-04-26_track1_forward_xgbm_original_dataset_mega_campaign/014_track1_original_dataset_forward_xgbm_attempt_14.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-20-03__track1_original_dataset_forward_xgbm_attempt_14_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-20-03__track1_original_dataset_forward_xgbm_attempt_14_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-20-03__track1_original_dataset_forward_xgbm_attempt_14_campaign_validation/validation_summary.yaml`
