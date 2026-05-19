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
- random seed: `5`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `27.007%`
- winning mean component MAE: `0.085117`
- winning mean component RMSE: `0.185323`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 27.007 | 0.085117 | 0.185323 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 16, 'estimator__min_samples_split': 6, 'estimator__n_estimators': 50}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `RF` | 0.002747 | 0.004328 | 17.441 |
| `fft_y_Fw_filtered_ampl_1` | `RF` | 0.000026 | 0.000035 | 0.149 |
| `fft_y_Fw_filtered_phase_1` | `RF` | 0.002296 | 0.003309 | 38.108 |
| `fft_y_Fw_filtered_ampl_3` | `RF` | 0.000026 | 0.000037 | 3.104 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.028067 | 0.036300 | 1.540 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000035 | 0.000047 | 3.102 |
| `fft_y_Fw_filtered_phase_39` | `RF` | 0.030383 | 0.051768 | 2.590 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | 0.000031 | 0.000045 | 3.848 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.046910 | 0.075216 | 119.589 |
| `fft_y_Fw_filtered_ampl_78` | `RF` | 0.000049 | 0.000074 | 7.900 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.109488 | 0.279667 | 70.862 |
| `fft_y_Fw_filtered_ampl_81` | `RF` | 0.000013 | 0.000018 | 3.870 |
| `fft_y_Fw_filtered_phase_81` | `RF` | 0.065954 | 0.111187 | 7.630 |
| `fft_y_Fw_filtered_ampl_156` | `RF` | 0.000049 | 0.000162 | 13.103 |
| `fft_y_Fw_filtered_phase_156` | `RF` | 0.564276 | 1.109917 | 32.413 |
| `fft_y_Fw_filtered_ampl_162` | `RF` | 0.000097 | 0.000335 | 15.174 |
| `fft_y_Fw_filtered_phase_162` | `RF` | 0.440090 | 1.010102 | 16.798 |
| `fft_y_Fw_filtered_ampl_240` | `RF` | 0.000053 | 0.000081 | 11.344 |
| `fft_y_Fw_filtered_phase_240` | `RF` | 0.326634 | 0.838515 | 144.573 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/rf/2026-04-26_track1_forward_rf_original_dataset_mega_campaign/002_track1_original_dataset_forward_rf_attempt_02.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-06-58__track1_original_dataset_forward_rf_attempt_02_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-06-58__track1_original_dataset_forward_rf_attempt_02_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-06-58__track1_original_dataset_forward_rf_attempt_02_campaign_validation/validation_summary.yaml`
