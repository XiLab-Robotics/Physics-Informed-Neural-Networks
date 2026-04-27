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

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `25.879%`
- winning mean component MAE: `0.042259`
- winning mean component RMSE: `0.114903`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 25.879 | 0.042259 | 0.114903 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 12, 'estimator__min_samples_split': 6, 'estimator__n_estimators': 70}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `RF` | 0.003091 | 0.003573 | 78.911 |
| `fft_y_Bw_filtered_ampl_1` | `RF` | 0.000025 | 0.000033 | 0.146 |
| `fft_y_Bw_filtered_phase_1` | `RF` | 0.001827 | 0.002856 | 132.355 |
| `fft_y_Bw_filtered_ampl_3` | `RF` | 0.000019 | 0.000029 | 1.918 |
| `fft_y_Bw_filtered_phase_3` | `RF` | 0.020529 | 0.026606 | 1.585 |
| `fft_y_Bw_filtered_ampl_39` | `RF` | 0.000020 | 0.000026 | 4.598 |
| `fft_y_Bw_filtered_phase_39` | `RF` | 0.160350 | 0.635211 | 5.834 |
| `fft_y_Bw_filtered_ampl_40` | `RF` | 0.000029 | 0.000042 | 9.901 |
| `fft_y_Bw_filtered_phase_40` | `RF` | 0.080611 | 0.117115 | 48.437 |
| `fft_y_Bw_filtered_ampl_78` | `RF` | 0.000052 | 0.000073 | 6.191 |
| `fft_y_Bw_filtered_phase_78` | `RF` | 0.051677 | 0.092574 | 20.466 |
| `fft_y_Bw_filtered_ampl_81` | `RF` | 0.000009 | 0.000013 | 7.489 |
| `fft_y_Bw_filtered_phase_81` | `RF` | 0.100091 | 0.135689 | 112.743 |
| `fft_y_Bw_filtered_ampl_156` | `RF` | 0.000118 | 0.000421 | 10.189 |
| `fft_y_Bw_filtered_phase_156` | `RF` | 0.115283 | 0.323225 | 14.563 |
| `fft_y_Bw_filtered_ampl_162` | `RF` | 0.000114 | 0.000529 | 8.650 |
| `fft_y_Bw_filtered_phase_162` | `RF` | 0.086137 | 0.221858 | 5.148 |
| `fft_y_Bw_filtered_ampl_240` | `RF` | 0.000073 | 0.000162 | 9.914 |
| `fft_y_Bw_filtered_phase_240` | `RF` | 0.182861 | 0.623129 | 12.658 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/rf/2026-04-26_track1_backward_rf_original_dataset_mega_campaign/011_track1_original_dataset_backward_rf_attempt_11.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-25-40__track1_original_dataset_backward_rf_attempt_11_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-25-40__track1_original_dataset_backward_rf_attempt_11_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-25-40__track1_original_dataset_backward_rf_attempt_11_campaign_validation/validation_summary.yaml`
