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
- random seed: `27`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `12.503%`
- winning mean component MAE: `0.044753`
- winning mean component RMSE: `0.105487`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 12.503 | 0.044753 | 0.105487 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 12, 'estimator__min_samples_split': 6, 'estimator__n_estimators': 90}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `RF` | 0.002799 | 0.003385 | 39.087 |
| `fft_y_Bw_filtered_ampl_1` | `RF` | 0.000024 | 0.000033 | 0.141 |
| `fft_y_Bw_filtered_phase_1` | `RF` | 0.001571 | 0.002184 | 25.700 |
| `fft_y_Bw_filtered_ampl_3` | `RF` | 0.000022 | 0.000032 | 2.183 |
| `fft_y_Bw_filtered_phase_3` | `RF` | 0.022512 | 0.030614 | 1.711 |
| `fft_y_Bw_filtered_ampl_39` | `RF` | 0.000018 | 0.000026 | 4.001 |
| `fft_y_Bw_filtered_phase_39` | `RF` | 0.202236 | 0.716299 | 7.061 |
| `fft_y_Bw_filtered_ampl_40` | `RF` | 0.000026 | 0.000035 | 8.964 |
| `fft_y_Bw_filtered_phase_40` | `RF` | 0.081164 | 0.120553 | 29.164 |
| `fft_y_Bw_filtered_ampl_78` | `RF` | 0.000048 | 0.000066 | 5.872 |
| `fft_y_Bw_filtered_phase_78` | `RF` | 0.049805 | 0.084766 | 20.644 |
| `fft_y_Bw_filtered_ampl_81` | `RF` | 0.000010 | 0.000014 | 8.234 |
| `fft_y_Bw_filtered_phase_81` | `RF` | 0.093624 | 0.117401 | 27.832 |
| `fft_y_Bw_filtered_ampl_156` | `RF` | 0.000172 | 0.000483 | 7.374 |
| `fft_y_Bw_filtered_phase_156` | `RF` | 0.087855 | 0.258168 | 7.254 |
| `fft_y_Bw_filtered_ampl_162` | `RF` | 0.000058 | 0.000142 | 6.693 |
| `fft_y_Bw_filtered_phase_162` | `RF` | 0.071225 | 0.119508 | 4.084 |
| `fft_y_Bw_filtered_ampl_240` | `RF` | 0.000109 | 0.000263 | 14.392 |
| `fft_y_Bw_filtered_phase_240` | `RF` | 0.237023 | 0.550289 | 17.166 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/rf/2026-04-26_track1_backward_rf_original_dataset_mega_campaign/012_track1_original_dataset_backward_rf_attempt_12.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-28-55__track1_original_dataset_backward_rf_attempt_12_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-28-55__track1_original_dataset_backward_rf_attempt_12_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-28-55__track1_original_dataset_backward_rf_attempt_12_campaign_validation/validation_summary.yaml`
