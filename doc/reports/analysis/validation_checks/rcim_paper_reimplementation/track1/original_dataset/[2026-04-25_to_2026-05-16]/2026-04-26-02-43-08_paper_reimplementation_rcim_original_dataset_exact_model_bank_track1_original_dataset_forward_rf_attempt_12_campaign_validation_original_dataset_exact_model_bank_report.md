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
- random seed: `27`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `58.520%`
- winning mean component MAE: `0.064749`
- winning mean component RMSE: `0.141490`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 58.520 | 0.064749 | 0.141490 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 16, 'estimator__min_samples_split': 5, 'estimator__n_estimators': 90}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `RF` | 0.002981 | 0.003535 | 5.814 |
| `fft_y_Fw_filtered_ampl_1` | `RF` | 0.000029 | 0.000038 | 0.167 |
| `fft_y_Fw_filtered_phase_1` | `RF` | 0.002339 | 0.003088 | 32.629 |
| `fft_y_Fw_filtered_ampl_3` | `RF` | 0.000019 | 0.000027 | 2.327 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.022159 | 0.028475 | 1.202 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000027 | 0.000038 | 2.323 |
| `fft_y_Fw_filtered_phase_39` | `RF` | 0.025963 | 0.041188 | 2.189 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | 0.000028 | 0.000046 | 3.519 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.044119 | 0.064341 | 79.804 |
| `fft_y_Fw_filtered_ampl_78` | `RF` | 0.000047 | 0.000066 | 7.056 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.049969 | 0.091349 | 836.311 |
| `fft_y_Fw_filtered_ampl_81` | `RF` | 0.000010 | 0.000013 | 3.235 |
| `fft_y_Fw_filtered_phase_81` | `RF` | 0.061436 | 0.094240 | 6.014 |
| `fft_y_Fw_filtered_ampl_156` | `RF` | 0.000068 | 0.000167 | 17.062 |
| `fft_y_Fw_filtered_phase_156` | `RF` | 0.584955 | 1.057441 | 34.056 |
| `fft_y_Fw_filtered_ampl_162` | `RF` | 0.000049 | 0.000163 | 7.946 |
| `fft_y_Fw_filtered_phase_162` | `RF` | 0.233764 | 0.784910 | 9.878 |
| `fft_y_Fw_filtered_ampl_240` | `RF` | 0.000037 | 0.000063 | 9.050 |
| `fft_y_Fw_filtered_phase_240` | `RF` | 0.202226 | 0.519126 | 51.291 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/rf/2026-04-26_track1_forward_rf_original_dataset_mega_campaign/012_track1_original_dataset_forward_rf_attempt_12.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-40-01__track1_original_dataset_forward_rf_attempt_12_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-40-01__track1_original_dataset_forward_rf_attempt_12_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-40-01__track1_original_dataset_forward_rf_attempt_12_campaign_validation/validation_summary.yaml`
