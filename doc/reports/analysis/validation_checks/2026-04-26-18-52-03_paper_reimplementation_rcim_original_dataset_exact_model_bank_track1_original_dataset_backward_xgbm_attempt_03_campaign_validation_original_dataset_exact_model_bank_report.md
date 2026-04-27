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
- random seed: `7`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `27.927%`
- winning mean component MAE: `0.091395`
- winning mean component RMSE: `0.191487`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 27.927 | 0.091395 | 0.191487 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `XGBM` | 0.002838 | 0.003285 | 36.405 |
| `fft_y_Bw_filtered_ampl_1` | `XGBM` | 0.000065 | 0.000111 | 0.378 |
| `fft_y_Bw_filtered_phase_1` | `XGBM` | 0.001880 | 0.002644 | 49.174 |
| `fft_y_Bw_filtered_ampl_3` | `XGBM` | 0.000080 | 0.000112 | 8.091 |
| `fft_y_Bw_filtered_phase_3` | `XGBM` | 0.018062 | 0.026669 | 1.312 |
| `fft_y_Bw_filtered_ampl_39` | `XGBM` | 0.000094 | 0.000111 | 20.649 |
| `fft_y_Bw_filtered_phase_39` | `XGBM` | 0.422098 | 1.169703 | 15.113 |
| `fft_y_Bw_filtered_ampl_40` | `XGBM` | 0.000044 | 0.000057 | 14.446 |
| `fft_y_Bw_filtered_phase_40` | `XGBM` | 0.169366 | 0.237553 | 83.476 |
| `fft_y_Bw_filtered_ampl_78` | `XGBM` | 0.000134 | 0.000179 | 33.755 |
| `fft_y_Bw_filtered_phase_78` | `XGBM` | 0.082676 | 0.130382 | 23.595 |
| `fft_y_Bw_filtered_ampl_81` | `XGBM` | 0.000023 | 0.000030 | 19.466 |
| `fft_y_Bw_filtered_phase_81` | `XGBM` | 0.096808 | 0.130654 | 48.880 |
| `fft_y_Bw_filtered_ampl_156` | `XGBM` | 0.000510 | 0.002117 | 33.228 |
| `fft_y_Bw_filtered_phase_156` | `XGBM` | 0.226099 | 0.593331 | 17.562 |
| `fft_y_Bw_filtered_ampl_162` | `XGBM` | 0.000280 | 0.000957 | 28.912 |
| `fft_y_Bw_filtered_phase_162` | `XGBM` | 0.168215 | 0.319412 | 10.217 |
| `fft_y_Bw_filtered_ampl_240` | `XGBM` | 0.000297 | 0.000776 | 51.680 |
| `fft_y_Bw_filtered_phase_240` | `XGBM` | 0.546937 | 1.020179 | 34.274 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/xgbm/2026-04-26_track1_backward_xgbm_original_dataset_mega_campaign/003_track1_original_dataset_backward_xgbm_attempt_03.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-51-13__track1_original_dataset_backward_xgbm_attempt_03_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-51-13__track1_original_dataset_backward_xgbm_attempt_03_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-51-13__track1_original_dataset_backward_xgbm_attempt_03_campaign_validation/validation_summary.yaml`
