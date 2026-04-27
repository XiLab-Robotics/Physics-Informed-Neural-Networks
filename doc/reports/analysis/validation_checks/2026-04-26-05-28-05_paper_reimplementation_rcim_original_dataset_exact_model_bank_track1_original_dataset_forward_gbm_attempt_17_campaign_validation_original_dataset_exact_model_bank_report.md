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
- random seed: `47`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `33.799%`
- winning mean component MAE: `0.112053`
- winning mean component RMSE: `0.198076`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 33.799 | 0.112053 | 0.198076 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 15, 'estimator__min_samples_split': 18, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `GBM` | 0.004091 | 0.005508 | 20.919 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000028 | 0.000036 | 0.165 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.002006 | 0.002844 | 105.032 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000025 | 0.000034 | 3.183 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | 0.031312 | 0.041557 | 1.759 |
| `fft_y_Fw_filtered_ampl_39` | `GBM` | 0.000051 | 0.000067 | 4.757 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.037832 | 0.054578 | 3.050 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000032 | 0.000051 | 4.290 |
| `fft_y_Fw_filtered_phase_40` | `GBM` | 0.046297 | 0.077807 | 129.768 |
| `fft_y_Fw_filtered_ampl_78` | `GBM` | 0.000076 | 0.000102 | 14.464 |
| `fft_y_Fw_filtered_phase_78` | `GBM` | 0.098952 | 0.192458 | 49.858 |
| `fft_y_Fw_filtered_ampl_81` | `GBM` | 0.000013 | 0.000021 | 3.965 |
| `fft_y_Fw_filtered_phase_81` | `GBM` | 0.083950 | 0.126004 | 11.141 |
| `fft_y_Fw_filtered_ampl_156` | `GBM` | 0.000168 | 0.000518 | 67.449 |
| `fft_y_Fw_filtered_phase_156` | `GBM` | 0.822716 | 1.360199 | 83.424 |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000230 | 0.000879 | 45.595 |
| `fft_y_Fw_filtered_phase_162` | `GBM` | 0.562410 | 1.020026 | 29.411 |
| `fft_y_Fw_filtered_ampl_240` | `GBM` | 0.000058 | 0.000101 | 23.676 |
| `fft_y_Fw_filtered_phase_240` | `GBM` | 0.438751 | 0.880660 | 40.266 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/gbm/2026-04-26_track1_forward_gbm_original_dataset_mega_campaign/017_track1_original_dataset_forward_gbm_attempt_17.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-26-11__track1_original_dataset_forward_gbm_attempt_17_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-26-11__track1_original_dataset_forward_gbm_attempt_17_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-26-11__track1_original_dataset_forward_gbm_attempt_17_campaign_validation/validation_summary.yaml`
