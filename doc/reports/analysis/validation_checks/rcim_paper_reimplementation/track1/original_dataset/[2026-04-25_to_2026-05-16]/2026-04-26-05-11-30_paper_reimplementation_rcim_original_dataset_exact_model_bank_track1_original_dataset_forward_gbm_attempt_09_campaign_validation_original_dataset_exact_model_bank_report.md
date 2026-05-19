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

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `65.314%`
- winning mean component MAE: `0.147482`
- winning mean component RMSE: `0.212742`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 65.314 | 0.147482 | 0.212742 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.01, 'estimator__max_depth': 14, 'estimator__min_samples_split': 12, 'estimator__n_estimators': 84}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `GBM` | 0.008430 | 0.010101 | 34.058 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000029 | 0.000037 | 0.171 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.001756 | 0.002551 | 94.121 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000065 | 0.000077 | 8.433 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | 0.056143 | 0.068008 | 3.117 |
| `fft_y_Fw_filtered_ampl_39` | `GBM` | 0.000106 | 0.000125 | 9.814 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.090971 | 0.109591 | 7.861 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000033 | 0.000042 | 4.143 |
| `fft_y_Fw_filtered_phase_40` | `GBM` | 0.056007 | 0.076933 | 104.816 |
| `fft_y_Fw_filtered_ampl_78` | `GBM` | 0.000239 | 0.000278 | 73.168 |
| `fft_y_Fw_filtered_phase_78` | `GBM` | 0.146392 | 0.212377 | 307.146 |
| `fft_y_Fw_filtered_ampl_81` | `GBM` | 0.000027 | 0.000033 | 9.479 |
| `fft_y_Fw_filtered_phase_81` | `GBM` | 0.154708 | 0.190484 | 15.731 |
| `fft_y_Fw_filtered_ampl_156` | `GBM` | 0.000382 | 0.000664 | 228.977 |
| `fft_y_Fw_filtered_phase_156` | `GBM` | 1.232717 | 1.514527 | 54.155 |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000482 | 0.001212 | 148.670 |
| `fft_y_Fw_filtered_phase_162` | `GBM` | 0.596395 | 0.935859 | 30.628 |
| `fft_y_Fw_filtered_ampl_240` | `GBM` | 0.000129 | 0.000200 | 73.074 |
| `fft_y_Fw_filtered_phase_240` | `GBM` | 0.457143 | 0.918989 | 33.397 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/gbm/2026-04-26_track1_forward_gbm_original_dataset_mega_campaign/009_track1_original_dataset_forward_gbm_attempt_09.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-09-32__track1_original_dataset_forward_gbm_attempt_09_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-09-32__track1_original_dataset_forward_gbm_attempt_09_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-09-32__track1_original_dataset_forward_gbm_attempt_09_campaign_validation/validation_summary.yaml`
