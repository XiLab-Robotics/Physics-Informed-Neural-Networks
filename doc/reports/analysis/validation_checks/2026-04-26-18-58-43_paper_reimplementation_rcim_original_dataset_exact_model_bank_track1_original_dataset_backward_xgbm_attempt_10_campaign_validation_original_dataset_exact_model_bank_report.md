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
- random seed: `21`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `35.626%`
- winning mean component MAE: `0.094863`
- winning mean component RMSE: `0.184738`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 35.626 | 0.094863 | 0.184738 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 18}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `XGBM` | 0.002899 | 0.003375 | 85.393 |
| `fft_y_Bw_filtered_ampl_1` | `XGBM` | 0.000062 | 0.000090 | 0.363 |
| `fft_y_Bw_filtered_phase_1` | `XGBM` | 0.002363 | 0.003372 | 117.474 |
| `fft_y_Bw_filtered_ampl_3` | `XGBM` | 0.000090 | 0.000115 | 9.198 |
| `fft_y_Bw_filtered_phase_3` | `XGBM` | 0.020542 | 0.026701 | 1.539 |
| `fft_y_Bw_filtered_ampl_39` | `XGBM` | 0.000093 | 0.000114 | 20.391 |
| `fft_y_Bw_filtered_phase_39` | `XGBM` | 0.469183 | 1.074753 | 17.296 |
| `fft_y_Bw_filtered_ampl_40` | `XGBM` | 0.000047 | 0.000061 | 16.023 |
| `fft_y_Bw_filtered_phase_40` | `XGBM` | 0.156667 | 0.208809 | 69.504 |
| `fft_y_Bw_filtered_ampl_78` | `XGBM` | 0.000142 | 0.000184 | 23.720 |
| `fft_y_Bw_filtered_phase_78` | `XGBM` | 0.077653 | 0.115810 | 33.523 |
| `fft_y_Bw_filtered_ampl_81` | `XGBM` | 0.000026 | 0.000035 | 22.067 |
| `fft_y_Bw_filtered_phase_81` | `XGBM` | 0.098113 | 0.133594 | 31.296 |
| `fft_y_Bw_filtered_ampl_156` | `XGBM` | 0.000496 | 0.001221 | 48.948 |
| `fft_y_Bw_filtered_phase_156` | `XGBM` | 0.261046 | 0.558855 | 38.098 |
| `fft_y_Bw_filtered_ampl_162` | `XGBM` | 0.000259 | 0.000527 | 43.479 |
| `fft_y_Bw_filtered_phase_162` | `XGBM` | 0.231575 | 0.524322 | 12.334 |
| `fft_y_Bw_filtered_ampl_240` | `XGBM` | 0.000273 | 0.000643 | 54.050 |
| `fft_y_Bw_filtered_phase_240` | `XGBM` | 0.480872 | 0.857435 | 32.199 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/xgbm/2026-04-26_track1_backward_xgbm_original_dataset_mega_campaign/010_track1_original_dataset_backward_xgbm_attempt_10.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-57-53__track1_original_dataset_backward_xgbm_attempt_10_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-57-53__track1_original_dataset_backward_xgbm_attempt_10_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-57-53__track1_original_dataset_backward_xgbm_attempt_10_campaign_validation/validation_summary.yaml`
