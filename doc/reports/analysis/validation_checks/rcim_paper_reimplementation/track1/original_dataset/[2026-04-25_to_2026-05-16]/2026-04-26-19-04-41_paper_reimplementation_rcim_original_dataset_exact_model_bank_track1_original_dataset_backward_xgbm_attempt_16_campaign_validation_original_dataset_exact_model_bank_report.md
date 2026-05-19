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
- random seed: `42`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `34.848%`
- winning mean component MAE: `0.088851`
- winning mean component RMSE: `0.148022`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 34.848 | 0.088851 | 0.148022 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 16}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `XGBM` | 0.003064 | 0.003511 | 56.529 |
| `fft_y_Bw_filtered_ampl_1` | `XGBM` | 0.000061 | 0.000098 | 0.357 |
| `fft_y_Bw_filtered_phase_1` | `XGBM` | 0.001917 | 0.002594 | 40.045 |
| `fft_y_Bw_filtered_ampl_3` | `XGBM` | 0.000084 | 0.000121 | 8.167 |
| `fft_y_Bw_filtered_phase_3` | `XGBM` | 0.021444 | 0.029391 | 1.587 |
| `fft_y_Bw_filtered_ampl_39` | `XGBM` | 0.000084 | 0.000102 | 18.415 |
| `fft_y_Bw_filtered_phase_39` | `XGBM` | 0.475716 | 0.888992 | 17.982 |
| `fft_y_Bw_filtered_ampl_40` | `XGBM` | 0.000047 | 0.000058 | 16.186 |
| `fft_y_Bw_filtered_phase_40` | `XGBM` | 0.185984 | 0.279088 | 140.027 |
| `fft_y_Bw_filtered_ampl_78` | `XGBM` | 0.000128 | 0.000165 | 28.371 |
| `fft_y_Bw_filtered_phase_78` | `XGBM` | 0.092370 | 0.152902 | 54.080 |
| `fft_y_Bw_filtered_ampl_81` | `XGBM` | 0.000027 | 0.000037 | 23.025 |
| `fft_y_Bw_filtered_phase_81` | `XGBM` | 0.094671 | 0.121210 | 104.385 |
| `fft_y_Bw_filtered_ampl_156` | `XGBM` | 0.000353 | 0.000939 | 35.571 |
| `fft_y_Bw_filtered_phase_156` | `XGBM` | 0.157072 | 0.236763 | 14.098 |
| `fft_y_Bw_filtered_ampl_162` | `XGBM` | 0.000203 | 0.000533 | 26.577 |
| `fft_y_Bw_filtered_phase_162` | `XGBM` | 0.157057 | 0.305274 | 9.066 |
| `fft_y_Bw_filtered_ampl_240` | `XGBM` | 0.000236 | 0.000656 | 38.125 |
| `fft_y_Bw_filtered_phase_240` | `XGBM` | 0.497639 | 0.789994 | 29.521 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/xgbm/2026-04-26_track1_backward_xgbm_original_dataset_mega_campaign/016_track1_original_dataset_backward_xgbm_attempt_16.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-03-43__track1_original_dataset_backward_xgbm_attempt_16_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-03-43__track1_original_dataset_backward_xgbm_attempt_16_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-03-43__track1_original_dataset_backward_xgbm_attempt_16_campaign_validation/validation_summary.yaml`
