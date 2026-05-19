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
- random seed: `9`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `28.059%`
- winning mean component MAE: `0.040897`
- winning mean component RMSE: `0.104524`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 28.059 | 0.040897 | 0.104524 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 12, 'estimator__min_samples_split': 2, 'estimator__n_estimators': 60}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `RF` | 0.002847 | 0.003385 | 65.900 |
| `fft_y_Bw_filtered_ampl_1` | `RF` | 0.000025 | 0.000036 | 0.148 |
| `fft_y_Bw_filtered_phase_1` | `RF` | 0.001802 | 0.002785 | 32.421 |
| `fft_y_Bw_filtered_ampl_3` | `RF` | 0.000019 | 0.000027 | 1.990 |
| `fft_y_Bw_filtered_phase_3` | `RF` | 0.024439 | 0.032599 | 1.852 |
| `fft_y_Bw_filtered_ampl_39` | `RF` | 0.000017 | 0.000024 | 3.754 |
| `fft_y_Bw_filtered_phase_39` | `RF` | 0.246770 | 0.882278 | 8.470 |
| `fft_y_Bw_filtered_ampl_40` | `RF` | 0.000025 | 0.000037 | 8.237 |
| `fft_y_Bw_filtered_phase_40` | `RF` | 0.099877 | 0.191706 | 21.994 |
| `fft_y_Bw_filtered_ampl_78` | `RF` | 0.000041 | 0.000055 | 13.844 |
| `fft_y_Bw_filtered_phase_78` | `RF` | 0.068761 | 0.249351 | 15.975 |
| `fft_y_Bw_filtered_ampl_81` | `RF` | 0.000009 | 0.000013 | 6.844 |
| `fft_y_Bw_filtered_phase_81` | `RF` | 0.086826 | 0.121218 | 313.388 |
| `fft_y_Bw_filtered_ampl_156` | `RF` | 0.000225 | 0.000741 | 8.313 |
| `fft_y_Bw_filtered_phase_156` | `RF` | 0.068614 | 0.152665 | 7.098 |
| `fft_y_Bw_filtered_ampl_162` | `RF` | 0.000061 | 0.000218 | 5.485 |
| `fft_y_Bw_filtered_phase_162` | `RF` | 0.051429 | 0.072535 | 3.018 |
| `fft_y_Bw_filtered_ampl_240` | `RF` | 0.000070 | 0.000179 | 8.473 |
| `fft_y_Bw_filtered_phase_240` | `RF` | 0.125185 | 0.276099 | 5.919 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/rf/2026-04-26_track1_backward_rf_original_dataset_mega_campaign/004_track1_original_dataset_backward_rf_attempt_04.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-02-35__track1_original_dataset_backward_rf_attempt_04_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-02-35__track1_original_dataset_backward_rf_attempt_04_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-02-35__track1_original_dataset_backward_rf_attempt_04_campaign_validation/validation_summary.yaml`
