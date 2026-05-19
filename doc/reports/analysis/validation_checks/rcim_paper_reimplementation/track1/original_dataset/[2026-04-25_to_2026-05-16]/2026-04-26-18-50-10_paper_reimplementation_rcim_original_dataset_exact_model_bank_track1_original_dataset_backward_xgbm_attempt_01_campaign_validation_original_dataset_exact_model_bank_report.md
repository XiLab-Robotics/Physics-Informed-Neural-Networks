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
- random seed: `0`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `33.708%`
- winning mean component MAE: `0.091234`
- winning mean component RMSE: `0.171916`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 33.708 | 0.091234 | 0.171916 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `XGBM` | 0.002818 | 0.003220 | 106.347 |
| `fft_y_Bw_filtered_ampl_1` | `XGBM` | 0.000065 | 0.000109 | 0.379 |
| `fft_y_Bw_filtered_phase_1` | `XGBM` | 0.001981 | 0.002903 | 26.271 |
| `fft_y_Bw_filtered_ampl_3` | `XGBM` | 0.000072 | 0.000094 | 7.811 |
| `fft_y_Bw_filtered_phase_3` | `XGBM` | 0.016603 | 0.022398 | 1.228 |
| `fft_y_Bw_filtered_ampl_39` | `XGBM` | 0.000079 | 0.000096 | 19.364 |
| `fft_y_Bw_filtered_phase_39` | `XGBM` | 0.475425 | 0.987990 | 17.487 |
| `fft_y_Bw_filtered_ampl_40` | `XGBM` | 0.000040 | 0.000050 | 13.303 |
| `fft_y_Bw_filtered_phase_40` | `XGBM` | 0.179249 | 0.255550 | 94.559 |
| `fft_y_Bw_filtered_ampl_78` | `XGBM` | 0.000105 | 0.000140 | 20.389 |
| `fft_y_Bw_filtered_phase_78` | `XGBM` | 0.074535 | 0.109275 | 40.117 |
| `fft_y_Bw_filtered_ampl_81` | `XGBM` | 0.000028 | 0.000033 | 24.566 |
| `fft_y_Bw_filtered_phase_81` | `XGBM` | 0.094915 | 0.126684 | 42.276 |
| `fft_y_Bw_filtered_ampl_156` | `XGBM` | 0.000394 | 0.001105 | 47.083 |
| `fft_y_Bw_filtered_phase_156` | `XGBM` | 0.196358 | 0.448025 | 31.670 |
| `fft_y_Bw_filtered_ampl_162` | `XGBM` | 0.000246 | 0.000598 | 35.854 |
| `fft_y_Bw_filtered_phase_162` | `XGBM` | 0.181141 | 0.342671 | 11.230 |
| `fft_y_Bw_filtered_ampl_240` | `XGBM` | 0.000339 | 0.000915 | 54.534 |
| `fft_y_Bw_filtered_phase_240` | `XGBM` | 0.509059 | 0.964551 | 45.987 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/xgbm/2026-04-26_track1_backward_xgbm_original_dataset_mega_campaign/001_track1_original_dataset_backward_xgbm_attempt_01.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-49-18__track1_original_dataset_backward_xgbm_attempt_01_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-49-18__track1_original_dataset_backward_xgbm_attempt_01_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-49-18__track1_original_dataset_backward_xgbm_attempt_01_campaign_validation/validation_summary.yaml`
