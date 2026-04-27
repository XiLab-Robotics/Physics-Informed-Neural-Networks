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
- random seed: `15`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `37.538%`
- winning mean component MAE: `0.095348`
- winning mean component RMSE: `0.179547`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 37.538 | 0.095348 | 0.179547 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.3, 'estimator__max_depth': 16}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `XGBM` | 0.002585 | 0.003598 | 31.104 |
| `fft_y_Bw_filtered_ampl_1` | `XGBM` | 0.000064 | 0.000112 | 0.370 |
| `fft_y_Bw_filtered_phase_1` | `XGBM` | 0.001798 | 0.002671 | 43.647 |
| `fft_y_Bw_filtered_ampl_3` | `XGBM` | 0.000076 | 0.000097 | 8.004 |
| `fft_y_Bw_filtered_phase_3` | `XGBM` | 0.022550 | 0.039729 | 1.652 |
| `fft_y_Bw_filtered_ampl_39` | `XGBM` | 0.000077 | 0.000095 | 18.191 |
| `fft_y_Bw_filtered_phase_39` | `XGBM` | 0.462988 | 0.837046 | 17.568 |
| `fft_y_Bw_filtered_ampl_40` | `XGBM` | 0.000042 | 0.000055 | 13.132 |
| `fft_y_Bw_filtered_phase_40` | `XGBM` | 0.165655 | 0.243243 | 81.841 |
| `fft_y_Bw_filtered_ampl_78` | `XGBM` | 0.000117 | 0.000159 | 25.216 |
| `fft_y_Bw_filtered_phase_78` | `XGBM` | 0.078274 | 0.101009 | 23.651 |
| `fft_y_Bw_filtered_ampl_81` | `XGBM` | 0.000025 | 0.000031 | 19.935 |
| `fft_y_Bw_filtered_phase_81` | `XGBM` | 0.109140 | 0.150545 | 221.981 |
| `fft_y_Bw_filtered_ampl_156` | `XGBM` | 0.000377 | 0.001582 | 31.792 |
| `fft_y_Bw_filtered_phase_156` | `XGBM` | 0.254428 | 0.668523 | 64.580 |
| `fft_y_Bw_filtered_ampl_162` | `XGBM` | 0.000391 | 0.001115 | 43.134 |
| `fft_y_Bw_filtered_phase_162` | `XGBM` | 0.195495 | 0.416862 | 11.536 |
| `fft_y_Bw_filtered_ampl_240` | `XGBM` | 0.000160 | 0.000241 | 31.658 |
| `fft_y_Bw_filtered_phase_240` | `XGBM` | 0.517367 | 0.944678 | 24.225 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/xgbm/2026-04-26_track1_backward_xgbm_original_dataset_mega_campaign/007_track1_original_dataset_backward_xgbm_attempt_07.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-55-00__track1_original_dataset_backward_xgbm_attempt_07_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-55-00__track1_original_dataset_backward_xgbm_attempt_07_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-55-00__track1_original_dataset_backward_xgbm_attempt_07_campaign_validation/validation_summary.yaml`
