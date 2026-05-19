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
- random seed: `5`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `53.729%`
- winning mean component MAE: `0.116730`
- winning mean component RMSE: `0.190015`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 53.729 | 0.116730 | 0.190015 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 16}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `XGBM` | 0.002613 | 0.004110 | 16.993 |
| `fft_y_Fw_filtered_ampl_1` | `XGBM` | 0.000051 | 0.000068 | 0.295 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.002289 | 0.003306 | 29.148 |
| `fft_y_Fw_filtered_ampl_3` | `XGBM` | 0.000090 | 0.000112 | 10.888 |
| `fft_y_Fw_filtered_phase_3` | `XGBM` | 0.028180 | 0.037421 | 1.538 |
| `fft_y_Fw_filtered_ampl_39` | `XGBM` | 0.000126 | 0.000160 | 11.349 |
| `fft_y_Fw_filtered_phase_39` | `XGBM` | 0.031118 | 0.044216 | 2.729 |
| `fft_y_Fw_filtered_ampl_40` | `XGBM` | 0.000068 | 0.000088 | 8.747 |
| `fft_y_Fw_filtered_phase_40` | `XGBM` | 0.063306 | 0.095188 | 175.396 |
| `fft_y_Fw_filtered_ampl_78` | `XGBM` | 0.000148 | 0.000188 | 36.928 |
| `fft_y_Fw_filtered_phase_78` | `XGBM` | 0.154729 | 0.307694 | 117.878 |
| `fft_y_Fw_filtered_ampl_81` | `XGBM` | 0.000052 | 0.000069 | 16.133 |
| `fft_y_Fw_filtered_phase_81` | `XGBM` | 0.081693 | 0.126524 | 11.020 |
| `fft_y_Fw_filtered_ampl_156` | `XGBM` | 0.000200 | 0.000408 | 74.025 |
| `fft_y_Fw_filtered_phase_156` | `XGBM` | 0.801792 | 1.168713 | 43.432 |
| `fft_y_Fw_filtered_ampl_162` | `XGBM` | 0.000189 | 0.000429 | 50.102 |
| `fft_y_Fw_filtered_phase_162` | `XGBM` | 0.626766 | 0.995252 | 32.036 |
| `fft_y_Fw_filtered_ampl_240` | `XGBM` | 0.000148 | 0.000211 | 41.825 |
| `fft_y_Fw_filtered_phase_240` | `XGBM` | 0.424320 | 0.826133 | 340.384 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/xgbm/2026-04-26_track1_forward_xgbm_original_dataset_mega_campaign/002_track1_original_dataset_forward_xgbm_attempt_02.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-07-47__track1_original_dataset_forward_xgbm_attempt_02_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-07-47__track1_original_dataset_forward_xgbm_attempt_02_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-07-47__track1_original_dataset_forward_xgbm_attempt_02_campaign_validation/validation_summary.yaml`
