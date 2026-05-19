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
- random seed: `21`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `33.330%`
- winning mean component MAE: `0.091432`
- winning mean component RMSE: `0.183133`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 33.330 | 0.091432 | 0.183133 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 15, 'estimator__min_samples_split': 18, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `GBM` | 0.003468 | 0.004144 | 8.222 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000029 | 0.000036 | 0.168 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.001923 | 0.002480 | 30.624 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000033 | 0.000042 | 4.034 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | 0.026854 | 0.035345 | 1.492 |
| `fft_y_Fw_filtered_ampl_39` | `GBM` | 0.000041 | 0.000050 | 3.883 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.040158 | 0.061143 | 3.240 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000028 | 0.000039 | 3.645 |
| `fft_y_Fw_filtered_phase_40` | `GBM` | 0.039348 | 0.058097 | 172.842 |
| `fft_y_Fw_filtered_ampl_78` | `GBM` | 0.000081 | 0.000105 | 19.899 |
| `fft_y_Fw_filtered_phase_78` | `GBM` | 0.096747 | 0.188753 | 79.938 |
| `fft_y_Fw_filtered_ampl_81` | `GBM` | 0.000013 | 0.000017 | 4.320 |
| `fft_y_Fw_filtered_phase_81` | `GBM` | 0.077582 | 0.098511 | 8.689 |
| `fft_y_Fw_filtered_ampl_156` | `GBM` | 0.000159 | 0.000368 | 66.791 |
| `fft_y_Fw_filtered_phase_156` | `GBM` | 0.700371 | 1.297078 | 40.820 |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000144 | 0.000290 | 52.012 |
| `fft_y_Fw_filtered_phase_162` | `GBM` | 0.409489 | 0.785001 | 18.827 |
| `fft_y_Fw_filtered_ampl_240` | `GBM` | 0.000075 | 0.000144 | 17.678 |
| `fft_y_Fw_filtered_phase_240` | `GBM` | 0.340669 | 0.947891 | 96.141 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/gbm/2026-04-26_track1_forward_gbm_original_dataset_mega_campaign/010_track1_original_dataset_forward_gbm_attempt_10.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-11-38__track1_original_dataset_forward_gbm_attempt_10_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-11-38__track1_original_dataset_forward_gbm_attempt_10_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-11-38__track1_original_dataset_forward_gbm_attempt_10_campaign_validation/validation_summary.yaml`
