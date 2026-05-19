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
- random seed: `37`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `42.457%`
- winning mean component MAE: `0.089481`
- winning mean component RMSE: `0.164946`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 42.457 | 0.089481 | 0.164946 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 15, 'estimator__min_samples_split': 18, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `GBM` | 0.003518 | 0.004148 | 8.015 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000022 | 0.000029 | 0.131 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.001963 | 0.002545 | 82.832 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000025 | 0.000031 | 3.240 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | 0.027256 | 0.035483 | 1.517 |
| `fft_y_Fw_filtered_ampl_39` | `GBM` | 0.000044 | 0.000052 | 4.221 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.031481 | 0.040565 | 2.551 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000027 | 0.000041 | 3.380 |
| `fft_y_Fw_filtered_phase_40` | `GBM` | 0.034990 | 0.047861 | 61.140 |
| `fft_y_Fw_filtered_ampl_78` | `GBM` | 0.000080 | 0.000097 | 23.394 |
| `fft_y_Fw_filtered_phase_78` | `GBM` | 0.089887 | 0.170816 | 214.962 |
| `fft_y_Fw_filtered_ampl_81` | `GBM` | 0.000012 | 0.000017 | 4.069 |
| `fft_y_Fw_filtered_phase_81` | `GBM` | 0.075002 | 0.102263 | 10.188 |
| `fft_y_Fw_filtered_ampl_156` | `GBM` | 0.000202 | 0.000538 | 90.052 |
| `fft_y_Fw_filtered_phase_156` | `GBM` | 0.664049 | 1.163637 | 33.779 |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000119 | 0.000352 | 49.711 |
| `fft_y_Fw_filtered_phase_162` | `GBM` | 0.486786 | 0.954232 | 19.405 |
| `fft_y_Fw_filtered_ampl_240` | `GBM` | 0.000059 | 0.000092 | 23.501 |
| `fft_y_Fw_filtered_phase_240` | `GBM` | 0.284617 | 0.611171 | 170.592 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/gbm/2026-04-26_track1_forward_gbm_original_dataset_mega_campaign/015_track1_original_dataset_forward_gbm_attempt_15.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-22-06__track1_original_dataset_forward_gbm_attempt_15_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-22-06__track1_original_dataset_forward_gbm_attempt_15_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-22-06__track1_original_dataset_forward_gbm_attempt_15_campaign_validation/validation_summary.yaml`
