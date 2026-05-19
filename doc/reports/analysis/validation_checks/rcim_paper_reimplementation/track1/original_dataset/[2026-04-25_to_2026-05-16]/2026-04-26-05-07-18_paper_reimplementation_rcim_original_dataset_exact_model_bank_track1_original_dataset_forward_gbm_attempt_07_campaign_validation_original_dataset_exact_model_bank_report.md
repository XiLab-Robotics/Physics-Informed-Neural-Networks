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
- random seed: `15`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `59.321%`
- winning mean component MAE: `0.146839`
- winning mean component RMSE: `0.215757`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 59.321 | 0.146839 | 0.215757 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.01, 'estimator__max_depth': 14, 'estimator__min_samples_split': 18, 'estimator__n_estimators': 84}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `GBM` | 0.007442 | 0.009306 | 32.950 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000031 | 0.000041 | 0.180 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.002773 | 0.004136 | 48.765 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000054 | 0.000066 | 7.304 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | 0.054406 | 0.068014 | 3.090 |
| `fft_y_Fw_filtered_ampl_39` | `GBM` | 0.000118 | 0.000134 | 11.611 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.091086 | 0.114118 | 7.545 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000037 | 0.000052 | 4.948 |
| `fft_y_Fw_filtered_phase_40` | `GBM` | 0.072970 | 0.103481 | 155.178 |
| `fft_y_Fw_filtered_ampl_78` | `GBM` | 0.000208 | 0.000246 | 152.097 |
| `fft_y_Fw_filtered_phase_78` | `GBM` | 0.204459 | 0.391604 | 77.682 |
| `fft_y_Fw_filtered_ampl_81` | `GBM` | 0.000024 | 0.000030 | 7.809 |
| `fft_y_Fw_filtered_phase_81` | `GBM` | 0.180059 | 0.219777 | 30.781 |
| `fft_y_Fw_filtered_ampl_156` | `GBM` | 0.000364 | 0.000690 | 269.072 |
| `fft_y_Fw_filtered_phase_156` | `GBM` | 1.119415 | 1.364453 | 57.585 |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000445 | 0.001193 | 150.240 |
| `fft_y_Fw_filtered_phase_162` | `GBM` | 0.659425 | 0.975854 | 38.337 |
| `fft_y_Fw_filtered_ampl_240` | `GBM` | 0.000144 | 0.000243 | 52.463 |
| `fft_y_Fw_filtered_phase_240` | `GBM` | 0.396485 | 0.845942 | 19.460 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/gbm/2026-04-26_track1_forward_gbm_original_dataset_mega_campaign/007_track1_original_dataset_forward_gbm_attempt_07.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-05-17__track1_original_dataset_forward_gbm_attempt_07_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-05-17__track1_original_dataset_forward_gbm_attempt_07_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-05-17__track1_original_dataset_forward_gbm_attempt_07_campaign_validation/validation_summary.yaml`
