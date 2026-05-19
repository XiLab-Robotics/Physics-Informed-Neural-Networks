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
- random seed: `53`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `189.600%`
- winning mean component MAE: `0.156205`
- winning mean component RMSE: `0.232100`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 189.600 | 0.156205 | 0.232100 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.01, 'estimator__max_depth': 15, 'estimator__min_samples_split': 18, 'estimator__n_estimators': 84}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `GBM` | 0.008846 | 0.010461 | 26.333 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000040 | 0.000052 | 0.234 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.003060 | 0.004200 | 2579.511 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000065 | 0.000077 | 8.488 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | 0.062889 | 0.086022 | 3.494 |
| `fft_y_Fw_filtered_ampl_39` | `GBM` | 0.000123 | 0.000144 | 12.175 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.103124 | 0.130942 | 8.180 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000049 | 0.000073 | 6.565 |
| `fft_y_Fw_filtered_phase_40` | `GBM` | 0.057795 | 0.083848 | 71.750 |
| `fft_y_Fw_filtered_ampl_78` | `GBM` | 0.000247 | 0.000292 | 86.701 |
| `fft_y_Fw_filtered_phase_78` | `GBM` | 0.175755 | 0.297540 | 183.888 |
| `fft_y_Fw_filtered_ampl_81` | `GBM` | 0.000028 | 0.000035 | 9.133 |
| `fft_y_Fw_filtered_phase_81` | `GBM` | 0.180014 | 0.229784 | 38.673 |
| `fft_y_Fw_filtered_ampl_156` | `GBM` | 0.000405 | 0.000718 | 214.267 |
| `fft_y_Fw_filtered_phase_156` | `GBM` | 1.062536 | 1.302958 | 58.838 |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000397 | 0.000751 | 161.822 |
| `fft_y_Fw_filtered_phase_162` | `GBM` | 0.736162 | 1.164718 | 34.204 |
| `fft_y_Fw_filtered_ampl_240` | `GBM` | 0.000137 | 0.000225 | 57.947 |
| `fft_y_Fw_filtered_phase_240` | `GBM` | 0.576215 | 1.097059 | 40.187 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/gbm/2026-04-26_track1_forward_gbm_original_dataset_mega_campaign/018_track1_original_dataset_forward_gbm_attempt_18.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-28-13__track1_original_dataset_forward_gbm_attempt_18_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-28-13__track1_original_dataset_forward_gbm_attempt_18_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-28-13__track1_original_dataset_forward_gbm_attempt_18_campaign_validation/validation_summary.yaml`
