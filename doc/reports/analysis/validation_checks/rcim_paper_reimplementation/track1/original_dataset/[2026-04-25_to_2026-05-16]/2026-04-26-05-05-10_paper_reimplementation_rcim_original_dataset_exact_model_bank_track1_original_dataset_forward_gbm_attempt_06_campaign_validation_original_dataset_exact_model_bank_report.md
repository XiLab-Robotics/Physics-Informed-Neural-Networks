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
- random seed: `13`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `28.461%`
- winning mean component MAE: `0.075754`
- winning mean component RMSE: `0.143918`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 28.461 | 0.075754 | 0.143918 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 14, 'estimator__min_samples_split': 14, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `GBM` | 0.003340 | 0.003955 | 6.888 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000024 | 0.000033 | 0.137 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.002104 | 0.002782 | 40.132 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000029 | 0.000037 | 3.592 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | 0.026450 | 0.035228 | 1.477 |
| `fft_y_Fw_filtered_ampl_39` | `GBM` | 0.000047 | 0.000060 | 4.386 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.031353 | 0.041869 | 2.785 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000027 | 0.000037 | 3.359 |
| `fft_y_Fw_filtered_phase_40` | `GBM` | 0.034636 | 0.045880 | 84.556 |
| `fft_y_Fw_filtered_ampl_78` | `GBM` | 0.000078 | 0.000106 | 23.283 |
| `fft_y_Fw_filtered_phase_78` | `GBM` | 0.075557 | 0.115937 | 61.900 |
| `fft_y_Fw_filtered_ampl_81` | `GBM` | 0.000013 | 0.000018 | 4.396 |
| `fft_y_Fw_filtered_phase_81` | `GBM` | 0.075606 | 0.099214 | 10.622 |
| `fft_y_Fw_filtered_ampl_156` | `GBM` | 0.000157 | 0.000338 | 72.329 |
| `fft_y_Fw_filtered_phase_156` | `GBM` | 0.702527 | 1.341498 | 35.228 |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000166 | 0.000420 | 37.030 |
| `fft_y_Fw_filtered_phase_162` | `GBM` | 0.268041 | 0.606710 | 13.334 |
| `fft_y_Fw_filtered_ampl_240` | `GBM` | 0.000055 | 0.000079 | 21.022 |
| `fft_y_Fw_filtered_phase_240` | `GBM` | 0.219106 | 0.440246 | 114.308 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/gbm/2026-04-26_track1_forward_gbm_original_dataset_mega_campaign/006_track1_original_dataset_forward_gbm_attempt_06.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-03-13__track1_original_dataset_forward_gbm_attempt_06_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-03-13__track1_original_dataset_forward_gbm_attempt_06_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-03-13__track1_original_dataset_forward_gbm_attempt_06_campaign_validation/validation_summary.yaml`
