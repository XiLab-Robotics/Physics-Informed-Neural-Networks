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
- random seed: `47`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `20.770%`
- winning mean component MAE: `0.050373`
- winning mean component RMSE: `0.126370`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 20.770 | 0.050373 | 0.126370 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 12, 'estimator__min_samples_split': 6, 'estimator__n_estimators': 80}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `RF` | 0.003133 | 0.003876 | 73.537 |
| `fft_y_Bw_filtered_ampl_1` | `RF` | 0.000029 | 0.000037 | 0.170 |
| `fft_y_Bw_filtered_phase_1` | `RF` | 0.001934 | 0.002882 | 86.014 |
| `fft_y_Bw_filtered_ampl_3` | `RF` | 0.000020 | 0.000031 | 2.055 |
| `fft_y_Bw_filtered_phase_3` | `RF` | 0.021246 | 0.035687 | 1.585 |
| `fft_y_Bw_filtered_ampl_39` | `RF` | 0.000019 | 0.000027 | 4.394 |
| `fft_y_Bw_filtered_phase_39` | `RF` | 0.249750 | 0.807442 | 8.816 |
| `fft_y_Bw_filtered_ampl_40` | `RF` | 0.000029 | 0.000046 | 9.270 |
| `fft_y_Bw_filtered_phase_40` | `RF` | 0.105850 | 0.206051 | 35.372 |
| `fft_y_Bw_filtered_ampl_78` | `RF` | 0.000054 | 0.000074 | 6.657 |
| `fft_y_Bw_filtered_phase_78` | `RF` | 0.058317 | 0.105622 | 55.418 |
| `fft_y_Bw_filtered_ampl_81` | `RF` | 0.000011 | 0.000017 | 8.333 |
| `fft_y_Bw_filtered_phase_81` | `RF` | 0.098893 | 0.137166 | 42.595 |
| `fft_y_Bw_filtered_ampl_156` | `RF` | 0.000192 | 0.000881 | 7.758 |
| `fft_y_Bw_filtered_phase_156` | `RF` | 0.140584 | 0.465041 | 19.988 |
| `fft_y_Bw_filtered_ampl_162` | `RF` | 0.000167 | 0.000714 | 8.938 |
| `fft_y_Bw_filtered_phase_162` | `RF` | 0.067292 | 0.112293 | 3.695 |
| `fft_y_Bw_filtered_ampl_240` | `RF` | 0.000090 | 0.000259 | 10.262 |
| `fft_y_Bw_filtered_phase_240` | `RF` | 0.209472 | 0.522883 | 9.770 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/rf/2026-04-26_track1_backward_rf_original_dataset_mega_campaign/017_track1_original_dataset_backward_rf_attempt_17.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-45-22__track1_original_dataset_backward_rf_attempt_17_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-45-22__track1_original_dataset_backward_rf_attempt_17_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-45-22__track1_original_dataset_backward_rf_attempt_17_campaign_validation/validation_summary.yaml`
