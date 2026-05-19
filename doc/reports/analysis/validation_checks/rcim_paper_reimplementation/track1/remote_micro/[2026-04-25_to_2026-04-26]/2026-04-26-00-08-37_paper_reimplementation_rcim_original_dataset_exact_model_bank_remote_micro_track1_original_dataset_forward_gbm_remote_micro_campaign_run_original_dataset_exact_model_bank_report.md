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
- random seed: `42`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `23.673%`
- winning mean component MAE: `0.085002`
- winning mean component RMSE: `0.172855`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 23.673 | 0.085002 | 0.172855 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 18, 'estimator__min_samples_split': 14, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `GBM` | 0.003527 | 0.004105 | 7.253 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000025 | 0.000031 | 0.144 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.001677 | 0.002434 | 48.850 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000025 | 0.000033 | 2.976 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | 0.026542 | 0.034751 | 1.471 |
| `fft_y_Fw_filtered_ampl_39` | `GBM` | 0.000041 | 0.000052 | 3.699 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.033133 | 0.043099 | 2.998 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000030 | 0.000051 | 3.825 |
| `fft_y_Fw_filtered_phase_40` | `GBM` | 0.046983 | 0.070309 | 46.058 |
| `fft_y_Fw_filtered_ampl_78` | `GBM` | 0.000085 | 0.000110 | 22.267 |
| `fft_y_Fw_filtered_phase_78` | `GBM` | 0.113701 | 0.280098 | 64.690 |
| `fft_y_Fw_filtered_ampl_81` | `GBM` | 0.000011 | 0.000015 | 3.623 |
| `fft_y_Fw_filtered_phase_81` | `GBM` | 0.067346 | 0.089357 | 7.510 |
| `fft_y_Fw_filtered_ampl_156` | `GBM` | 0.000123 | 0.000314 | 55.571 |
| `fft_y_Fw_filtered_phase_156` | `GBM` | 0.490354 | 0.850627 | 19.620 |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000124 | 0.000325 | 49.463 |
| `fft_y_Fw_filtered_phase_162` | `GBM` | 0.503093 | 1.117012 | 20.228 |
| `fft_y_Fw_filtered_ampl_240` | `GBM` | 0.000044 | 0.000068 | 12.990 |
| `fft_y_Fw_filtered_phase_240` | `GBM` | 0.328169 | 0.791447 | 76.554 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/forward_remote_micro/gbm/2026-04-25_track1_forward_gbm_remote_micro/001_track1_original_dataset_forward_gbm_remote_micro.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_micro/2026-04-26-00-06-45__track1_original_dataset_forward_gbm_remote_micro_campaign_run`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_micro/2026-04-26-00-06-45__track1_original_dataset_forward_gbm_remote_micro_campaign_run/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_micro/2026-04-26-00-06-45__track1_original_dataset_forward_gbm_remote_micro_campaign_run/validation_summary.yaml`
