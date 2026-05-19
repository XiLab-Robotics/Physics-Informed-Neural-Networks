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
- random seed: `19`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `28.475%`
- winning mean component MAE: `0.067236`
- winning mean component RMSE: `0.171604`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 28.475 | 0.067236 | 0.171604 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 2, 'estimator__n_estimators': 50}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `RF` | 0.002959 | 0.004067 | 14.299 |
| `fft_y_Fw_filtered_ampl_1` | `RF` | 0.000024 | 0.000037 | 0.141 |
| `fft_y_Fw_filtered_phase_1` | `RF` | 0.001756 | 0.002629 | 132.146 |
| `fft_y_Fw_filtered_ampl_3` | `RF` | 0.000019 | 0.000029 | 2.358 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.024097 | 0.039721 | 1.335 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000029 | 0.000041 | 2.534 |
| `fft_y_Fw_filtered_phase_39` | `RF` | 0.025425 | 0.045055 | 2.079 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | 0.000023 | 0.000035 | 2.943 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.039118 | 0.060075 | 71.621 |
| `fft_y_Fw_filtered_ampl_78` | `RF` | 0.000037 | 0.000054 | 11.092 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.063717 | 0.137417 | 190.601 |
| `fft_y_Fw_filtered_ampl_81` | `RF` | 0.000009 | 0.000013 | 3.226 |
| `fft_y_Fw_filtered_phase_81` | `RF` | 0.055343 | 0.090278 | 4.703 |
| `fft_y_Fw_filtered_ampl_156` | `RF` | 0.000072 | 0.000242 | 13.066 |
| `fft_y_Fw_filtered_phase_156` | `RF` | 0.529504 | 1.262828 | 26.307 |
| `fft_y_Fw_filtered_ampl_162` | `RF` | 0.000060 | 0.000166 | 10.690 |
| `fft_y_Fw_filtered_phase_162` | `RF` | 0.246283 | 0.751541 | 10.295 |
| `fft_y_Fw_filtered_ampl_240` | `RF` | 0.000046 | 0.000136 | 28.674 |
| `fft_y_Fw_filtered_phase_240` | `RF` | 0.288972 | 0.866117 | 12.905 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/rf/2026-04-26_track1_forward_rf_original_dataset_mega_campaign/009_track1_original_dataset_forward_rf_attempt_09.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-30-06__track1_original_dataset_forward_rf_attempt_09_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-30-06__track1_original_dataset_forward_rf_attempt_09_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-30-06__track1_original_dataset_forward_rf_attempt_09_campaign_validation/validation_summary.yaml`
