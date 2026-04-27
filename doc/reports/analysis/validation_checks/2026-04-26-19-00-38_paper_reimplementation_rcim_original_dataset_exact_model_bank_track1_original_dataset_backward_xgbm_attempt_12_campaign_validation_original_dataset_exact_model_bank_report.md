# Original-Dataset Exact RCIM Model Bank Validation Report

## Overview

This report covers the direction-specific exact-model-bank branch trained from the repository dataset under `data/datasets`.

- direction label: `backward`
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
- random seed: `27`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `28.352%`
- winning mean component MAE: `0.082384`
- winning mean component RMSE: `0.141745`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 28.352 | 0.082384 | 0.141745 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 18}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `XGBM` | 0.002461 | 0.002967 | 29.838 |
| `fft_y_Bw_filtered_ampl_1` | `XGBM` | 0.000061 | 0.000092 | 0.354 |
| `fft_y_Bw_filtered_phase_1` | `XGBM` | 0.001952 | 0.002719 | 36.926 |
| `fft_y_Bw_filtered_ampl_3` | `XGBM` | 0.000090 | 0.000111 | 9.340 |
| `fft_y_Bw_filtered_phase_3` | `XGBM` | 0.019487 | 0.024904 | 1.485 |
| `fft_y_Bw_filtered_ampl_39` | `XGBM` | 0.000091 | 0.000108 | 19.671 |
| `fft_y_Bw_filtered_phase_39` | `XGBM` | 0.367690 | 0.752824 | 14.003 |
| `fft_y_Bw_filtered_ampl_40` | `XGBM` | 0.000046 | 0.000057 | 15.772 |
| `fft_y_Bw_filtered_phase_40` | `XGBM` | 0.142938 | 0.207740 | 124.171 |
| `fft_y_Bw_filtered_ampl_78` | `XGBM` | 0.000141 | 0.000187 | 23.197 |
| `fft_y_Bw_filtered_phase_78` | `XGBM` | 0.073145 | 0.106471 | 36.609 |
| `fft_y_Bw_filtered_ampl_81` | `XGBM` | 0.000028 | 0.000034 | 24.072 |
| `fft_y_Bw_filtered_phase_81` | `XGBM` | 0.100495 | 0.129979 | 33.358 |
| `fft_y_Bw_filtered_ampl_156` | `XGBM` | 0.000471 | 0.001448 | 28.873 |
| `fft_y_Bw_filtered_phase_156` | `XGBM` | 0.178698 | 0.383208 | 15.247 |
| `fft_y_Bw_filtered_ampl_162` | `XGBM` | 0.000150 | 0.000234 | 29.720 |
| `fft_y_Bw_filtered_phase_162` | `XGBM` | 0.151022 | 0.275683 | 9.061 |
| `fft_y_Bw_filtered_ampl_240` | `XGBM` | 0.000302 | 0.000636 | 50.636 |
| `fft_y_Bw_filtered_phase_240` | `XGBM` | 0.526034 | 0.803756 | 36.350 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/xgbm/2026-04-26_track1_backward_xgbm_original_dataset_mega_campaign/012_track1_original_dataset_backward_xgbm_attempt_12.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-59-48__track1_original_dataset_backward_xgbm_attempt_12_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-59-48__track1_original_dataset_backward_xgbm_attempt_12_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-59-48__track1_original_dataset_backward_xgbm_attempt_12_campaign_validation/validation_summary.yaml`
