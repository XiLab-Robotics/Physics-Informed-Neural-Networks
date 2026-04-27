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
- random seed: `23`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `32.297%`
- winning mean component MAE: `0.061549`
- winning mean component RMSE: `0.123789`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 32.297 | 0.061549 | 0.123789 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 16, 'estimator__min_samples_split': 12, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `GBM` | 0.003792 | 0.004510 | 117.921 |
| `fft_y_Bw_filtered_ampl_1` | `GBM` | 0.000027 | 0.000035 | 0.155 |
| `fft_y_Bw_filtered_phase_1` | `GBM` | 0.001970 | 0.003121 | 140.401 |
| `fft_y_Bw_filtered_ampl_3` | `GBM` | 0.000023 | 0.000031 | 2.273 |
| `fft_y_Bw_filtered_phase_3` | `GBM` | 0.031349 | 0.040273 | 2.418 |
| `fft_y_Bw_filtered_ampl_39` | `GBM` | 0.000023 | 0.000029 | 5.496 |
| `fft_y_Bw_filtered_phase_39` | `GBM` | 0.382005 | 0.753772 | 14.030 |
| `fft_y_Bw_filtered_ampl_40` | `GBM` | 0.000031 | 0.000045 | 10.376 |
| `fft_y_Bw_filtered_phase_40` | `GBM` | 0.092750 | 0.129342 | 40.838 |
| `fft_y_Bw_filtered_ampl_78` | `GBM` | 0.000095 | 0.000114 | 14.898 |
| `fft_y_Bw_filtered_phase_78` | `GBM` | 0.055433 | 0.085432 | 18.470 |
| `fft_y_Bw_filtered_ampl_81` | `GBM` | 0.000010 | 0.000014 | 8.633 |
| `fft_y_Bw_filtered_phase_81` | `GBM` | 0.104303 | 0.132014 | 101.124 |
| `fft_y_Bw_filtered_ampl_156` | `GBM` | 0.000221 | 0.000592 | 34.851 |
| `fft_y_Bw_filtered_phase_156` | `GBM` | 0.120517 | 0.265418 | 19.623 |
| `fft_y_Bw_filtered_ampl_162` | `GBM` | 0.000195 | 0.000669 | 45.660 |
| `fft_y_Bw_filtered_phase_162` | `GBM` | 0.137227 | 0.218693 | 7.784 |
| `fft_y_Bw_filtered_ampl_240` | `GBM` | 0.000084 | 0.000136 | 15.241 |
| `fft_y_Bw_filtered_phase_240` | `GBM` | 0.239370 | 0.717752 | 13.459 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/gbm/2026-04-26_track1_backward_gbm_original_dataset_mega_campaign/011_track1_original_dataset_backward_gbm_attempt_11.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-57-42__track1_original_dataset_backward_gbm_attempt_11_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-57-42__track1_original_dataset_backward_gbm_attempt_11_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-57-42__track1_original_dataset_backward_gbm_attempt_11_campaign_validation/validation_summary.yaml`
