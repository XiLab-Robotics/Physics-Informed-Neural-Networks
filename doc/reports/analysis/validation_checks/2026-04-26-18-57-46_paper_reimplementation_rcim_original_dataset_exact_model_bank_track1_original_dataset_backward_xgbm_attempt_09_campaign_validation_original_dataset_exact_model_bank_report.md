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
- random seed: `19`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `28.896%`
- winning mean component MAE: `0.085694`
- winning mean component RMSE: `0.161935`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 28.896 | 0.085694 | 0.161935 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.3, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `XGBM` | 0.002802 | 0.003875 | 44.565 |
| `fft_y_Bw_filtered_ampl_1` | `XGBM` | 0.000061 | 0.000103 | 0.356 |
| `fft_y_Bw_filtered_phase_1` | `XGBM` | 0.001823 | 0.002605 | 37.998 |
| `fft_y_Bw_filtered_ampl_3` | `XGBM` | 0.000069 | 0.000090 | 7.358 |
| `fft_y_Bw_filtered_phase_3` | `XGBM` | 0.020374 | 0.038499 | 1.537 |
| `fft_y_Bw_filtered_ampl_39` | `XGBM` | 0.000081 | 0.000099 | 18.502 |
| `fft_y_Bw_filtered_phase_39` | `XGBM` | 0.462687 | 1.102634 | 16.029 |
| `fft_y_Bw_filtered_ampl_40` | `XGBM` | 0.000037 | 0.000048 | 12.206 |
| `fft_y_Bw_filtered_phase_40` | `XGBM` | 0.166831 | 0.230266 | 73.255 |
| `fft_y_Bw_filtered_ampl_78` | `XGBM` | 0.000123 | 0.000161 | 26.901 |
| `fft_y_Bw_filtered_phase_78` | `XGBM` | 0.062394 | 0.089105 | 24.981 |
| `fft_y_Bw_filtered_ampl_81` | `XGBM` | 0.000025 | 0.000032 | 23.361 |
| `fft_y_Bw_filtered_phase_81` | `XGBM` | 0.096942 | 0.149727 | 90.166 |
| `fft_y_Bw_filtered_ampl_156` | `XGBM` | 0.000432 | 0.001473 | 34.625 |
| `fft_y_Bw_filtered_phase_156` | `XGBM` | 0.164398 | 0.364967 | 19.529 |
| `fft_y_Bw_filtered_ampl_162` | `XGBM` | 0.000345 | 0.000959 | 31.098 |
| `fft_y_Bw_filtered_phase_162` | `XGBM` | 0.177825 | 0.387700 | 9.815 |
| `fft_y_Bw_filtered_ampl_240` | `XGBM` | 0.000160 | 0.000296 | 46.968 |
| `fft_y_Bw_filtered_phase_240` | `XGBM` | 0.470777 | 0.704120 | 29.774 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/xgbm/2026-04-26_track1_backward_xgbm_original_dataset_mega_campaign/009_track1_original_dataset_backward_xgbm_attempt_09.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-56-54__track1_original_dataset_backward_xgbm_attempt_09_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-56-54__track1_original_dataset_backward_xgbm_attempt_09_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-56-54__track1_original_dataset_backward_xgbm_attempt_09_campaign_validation/validation_summary.yaml`
