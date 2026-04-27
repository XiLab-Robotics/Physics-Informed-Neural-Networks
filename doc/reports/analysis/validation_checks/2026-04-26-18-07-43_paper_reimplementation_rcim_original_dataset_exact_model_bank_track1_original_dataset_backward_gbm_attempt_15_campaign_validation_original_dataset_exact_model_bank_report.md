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
- random seed: `37`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `45.988%`
- winning mean component MAE: `0.066471`
- winning mean component RMSE: `0.158831`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 45.988 | 0.066471 | 0.158831 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 15, 'estimator__min_samples_split': 10, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `GBM` | 0.003283 | 0.003939 | 51.534 |
| `fft_y_Bw_filtered_ampl_1` | `GBM` | 0.000028 | 0.000040 | 0.164 |
| `fft_y_Bw_filtered_phase_1` | `GBM` | 0.001590 | 0.002509 | 257.960 |
| `fft_y_Bw_filtered_ampl_3` | `GBM` | 0.000026 | 0.000036 | 2.858 |
| `fft_y_Bw_filtered_phase_3` | `GBM` | 0.031386 | 0.038600 | 2.258 |
| `fft_y_Bw_filtered_ampl_39` | `GBM` | 0.000021 | 0.000028 | 4.636 |
| `fft_y_Bw_filtered_phase_39` | `GBM` | 0.370780 | 0.875993 | 13.814 |
| `fft_y_Bw_filtered_ampl_40` | `GBM` | 0.000028 | 0.000040 | 9.949 |
| `fft_y_Bw_filtered_phase_40` | `GBM` | 0.093005 | 0.131242 | 51.631 |
| `fft_y_Bw_filtered_ampl_78` | `GBM` | 0.000099 | 0.000120 | 23.113 |
| `fft_y_Bw_filtered_phase_78` | `GBM` | 0.092553 | 0.263918 | 28.582 |
| `fft_y_Bw_filtered_ampl_81` | `GBM` | 0.000009 | 0.000012 | 7.625 |
| `fft_y_Bw_filtered_phase_81` | `GBM` | 0.088926 | 0.113416 | 275.269 |
| `fft_y_Bw_filtered_ampl_156` | `GBM` | 0.000356 | 0.001151 | 33.290 |
| `fft_y_Bw_filtered_phase_156` | `GBM` | 0.160858 | 0.610991 | 20.278 |
| `fft_y_Bw_filtered_ampl_162` | `GBM` | 0.000136 | 0.000256 | 51.544 |
| `fft_y_Bw_filtered_phase_162` | `GBM` | 0.129266 | 0.191873 | 6.932 |
| `fft_y_Bw_filtered_ampl_240` | `GBM` | 0.000104 | 0.000220 | 18.477 |
| `fft_y_Bw_filtered_phase_240` | `GBM` | 0.290499 | 0.783407 | 13.856 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/gbm/2026-04-26_track1_backward_gbm_original_dataset_mega_campaign/015_track1_original_dataset_backward_gbm_attempt_15.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-05-51__track1_original_dataset_backward_gbm_attempt_15_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-05-51__track1_original_dataset_backward_gbm_attempt_15_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-05-51__track1_original_dataset_backward_gbm_attempt_15_campaign_validation/validation_summary.yaml`
