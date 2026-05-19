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

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `74.236%`
- winning mean component MAE: `0.153206`
- winning mean component RMSE: `0.224353`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 74.236 | 0.153206 | 0.224353 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.01, 'estimator__max_depth': 14, 'estimator__min_samples_split': 12, 'estimator__n_estimators': 84}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `GBM` | 0.008989 | 0.010595 | 35.288 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000031 | 0.000042 | 0.184 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.002992 | 0.004079 | 98.624 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000069 | 0.000082 | 8.394 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | 0.062117 | 0.074779 | 3.388 |
| `fft_y_Fw_filtered_ampl_39` | `GBM` | 0.000124 | 0.000146 | 11.431 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.108823 | 0.129778 | 9.666 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000041 | 0.000057 | 5.210 |
| `fft_y_Fw_filtered_phase_40` | `GBM` | 0.064581 | 0.094437 | 197.156 |
| `fft_y_Fw_filtered_ampl_78` | `GBM` | 0.000262 | 0.000308 | 60.916 |
| `fft_y_Fw_filtered_phase_78` | `GBM` | 0.208351 | 0.337901 | 138.162 |
| `fft_y_Fw_filtered_ampl_81` | `GBM` | 0.000028 | 0.000036 | 8.724 |
| `fft_y_Fw_filtered_phase_81` | `GBM` | 0.189768 | 0.231205 | 29.854 |
| `fft_y_Fw_filtered_ampl_156` | `GBM` | 0.000293 | 0.000382 | 222.092 |
| `fft_y_Fw_filtered_phase_156` | `GBM` | 1.027503 | 1.316190 | 49.193 |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000314 | 0.000649 | 151.722 |
| `fft_y_Fw_filtered_phase_162` | `GBM` | 0.761124 | 1.099259 | 38.247 |
| `fft_y_Fw_filtered_ampl_240` | `GBM` | 0.000148 | 0.000243 | 41.101 |
| `fft_y_Fw_filtered_phase_240` | `GBM` | 0.475357 | 0.962536 | 301.128 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/gbm/2026-04-26_track1_forward_gbm_original_dataset_mega_campaign/002_track1_original_dataset_forward_gbm_attempt_02.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-54-38__track1_original_dataset_forward_gbm_attempt_02_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-54-38__track1_original_dataset_forward_gbm_attempt_02_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-54-38__track1_original_dataset_forward_gbm_attempt_02_campaign_validation/validation_summary.yaml`
