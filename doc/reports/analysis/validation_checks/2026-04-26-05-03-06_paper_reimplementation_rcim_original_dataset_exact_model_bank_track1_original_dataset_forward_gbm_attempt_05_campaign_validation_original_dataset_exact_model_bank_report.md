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
- random seed: `11`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `66.429%`
- winning mean component MAE: `0.152558`
- winning mean component RMSE: `0.228308`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 66.429 | 0.152558 | 0.228308 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.01, 'estimator__max_depth': 14, 'estimator__min_samples_split': 10, 'estimator__n_estimators': 84}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `GBM` | 0.007639 | 0.008892 | 16.317 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000037 | 0.000046 | 0.215 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.002367 | 0.003054 | 41.272 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000061 | 0.000072 | 7.737 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | 0.060135 | 0.070412 | 3.314 |
| `fft_y_Fw_filtered_ampl_39` | `GBM` | 0.000124 | 0.000138 | 11.656 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.092791 | 0.109012 | 7.873 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000040 | 0.000054 | 4.878 |
| `fft_y_Fw_filtered_phase_40` | `GBM` | 0.053547 | 0.068220 | 102.283 |
| `fft_y_Fw_filtered_ampl_78` | `GBM` | 0.000233 | 0.000268 | 98.777 |
| `fft_y_Fw_filtered_phase_78` | `GBM` | 0.171504 | 0.350542 | 446.451 |
| `fft_y_Fw_filtered_ampl_81` | `GBM` | 0.000022 | 0.000029 | 7.526 |
| `fft_y_Fw_filtered_phase_81` | `GBM` | 0.174012 | 0.213514 | 25.983 |
| `fft_y_Fw_filtered_ampl_156` | `GBM` | 0.000331 | 0.000521 | 192.628 |
| `fft_y_Fw_filtered_phase_156` | `GBM` | 1.244068 | 1.689401 | 66.428 |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000403 | 0.001168 | 131.768 |
| `fft_y_Fw_filtered_phase_162` | `GBM` | 0.702526 | 1.036923 | 33.866 |
| `fft_y_Fw_filtered_ampl_240` | `GBM` | 0.000140 | 0.000261 | 41.691 |
| `fft_y_Fw_filtered_phase_240` | `GBM` | 0.388618 | 0.785328 | 21.488 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/gbm/2026-04-26_track1_forward_gbm_original_dataset_mega_campaign/005_track1_original_dataset_forward_gbm_attempt_05.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-01-06__track1_original_dataset_forward_gbm_attempt_05_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-01-06__track1_original_dataset_forward_gbm_attempt_05_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-01-06__track1_original_dataset_forward_gbm_attempt_05_campaign_validation/validation_summary.yaml`
