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

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `12.957%`
- winning mean component MAE: `0.050007`
- winning mean component RMSE: `0.140488`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 12.957 | 0.050007 | 0.140488 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 12, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 50}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `RF` | 0.002844 | 0.003441 | 35.320 |
| `fft_y_Bw_filtered_ampl_1` | `RF` | 0.000028 | 0.000038 | 0.164 |
| `fft_y_Bw_filtered_phase_1` | `RF` | 0.001683 | 0.002660 | 41.470 |
| `fft_y_Bw_filtered_ampl_3` | `RF` | 0.000022 | 0.000034 | 2.290 |
| `fft_y_Bw_filtered_phase_3` | `RF` | 0.020259 | 0.029553 | 1.488 |
| `fft_y_Bw_filtered_ampl_39` | `RF` | 0.000015 | 0.000020 | 3.386 |
| `fft_y_Bw_filtered_phase_39` | `RF` | 0.335900 | 1.217101 | 11.356 |
| `fft_y_Bw_filtered_ampl_40` | `RF` | 0.000027 | 0.000039 | 8.824 |
| `fft_y_Bw_filtered_phase_40` | `RF` | 0.075375 | 0.113560 | 27.461 |
| `fft_y_Bw_filtered_ampl_78` | `RF` | 0.000050 | 0.000067 | 6.744 |
| `fft_y_Bw_filtered_phase_78` | `RF` | 0.048945 | 0.104939 | 15.418 |
| `fft_y_Bw_filtered_ampl_81` | `RF` | 0.000007 | 0.000010 | 5.523 |
| `fft_y_Bw_filtered_phase_81` | `RF` | 0.072562 | 0.097616 | 31.948 |
| `fft_y_Bw_filtered_ampl_156` | `RF` | 0.000162 | 0.000840 | 6.927 |
| `fft_y_Bw_filtered_phase_156` | `RF` | 0.086236 | 0.268378 | 6.091 |
| `fft_y_Bw_filtered_ampl_162` | `RF` | 0.000068 | 0.000237 | 7.086 |
| `fft_y_Bw_filtered_phase_162` | `RF` | 0.059362 | 0.098381 | 3.417 |
| `fft_y_Bw_filtered_ampl_240` | `RF` | 0.000096 | 0.000258 | 13.395 |
| `fft_y_Bw_filtered_phase_240` | `RF` | 0.246490 | 0.732092 | 17.878 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/rf/2026-04-26_track1_backward_rf_original_dataset_mega_campaign/003_track1_original_dataset_backward_rf_attempt_03.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-59-14__track1_original_dataset_backward_rf_attempt_03_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-59-14__track1_original_dataset_backward_rf_attempt_03_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-59-14__track1_original_dataset_backward_rf_attempt_03_campaign_validation/validation_summary.yaml`
