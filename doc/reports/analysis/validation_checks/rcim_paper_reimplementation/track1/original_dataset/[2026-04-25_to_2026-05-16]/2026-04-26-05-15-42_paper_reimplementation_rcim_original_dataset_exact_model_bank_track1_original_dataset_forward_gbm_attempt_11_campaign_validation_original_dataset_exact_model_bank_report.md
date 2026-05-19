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
- random seed: `23`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `29.662%`
- winning mean component MAE: `0.096713`
- winning mean component RMSE: `0.187516`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 29.662 | 0.096713 | 0.187516 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 16, 'estimator__min_samples_split': 18, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `GBM` | 0.003751 | 0.004355 | 7.891 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000029 | 0.000039 | 0.167 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.001954 | 0.002608 | 45.401 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000029 | 0.000038 | 3.634 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | 0.024213 | 0.032116 | 1.355 |
| `fft_y_Fw_filtered_ampl_39` | `GBM` | 0.000043 | 0.000052 | 4.077 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.037515 | 0.049769 | 3.297 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000028 | 0.000042 | 3.842 |
| `fft_y_Fw_filtered_phase_40` | `GBM` | 0.040618 | 0.054210 | 137.616 |
| `fft_y_Fw_filtered_ampl_78` | `GBM` | 0.000081 | 0.000103 | 19.458 |
| `fft_y_Fw_filtered_phase_78` | `GBM` | 0.082224 | 0.137014 | 68.382 |
| `fft_y_Fw_filtered_ampl_81` | `GBM` | 0.000013 | 0.000017 | 4.191 |
| `fft_y_Fw_filtered_phase_81` | `GBM` | 0.072836 | 0.104347 | 9.691 |
| `fft_y_Fw_filtered_ampl_156` | `GBM` | 0.000144 | 0.000356 | 104.316 |
| `fft_y_Fw_filtered_phase_156` | `GBM` | 0.770599 | 1.384515 | 34.820 |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000185 | 0.000761 | 48.122 |
| `fft_y_Fw_filtered_phase_162` | `GBM` | 0.482659 | 1.017554 | 20.510 |
| `fft_y_Fw_filtered_ampl_240` | `GBM` | 0.000058 | 0.000101 | 18.875 |
| `fft_y_Fw_filtered_phase_240` | `GBM` | 0.320569 | 0.774816 | 27.926 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/gbm/2026-04-26_track1_forward_gbm_original_dataset_mega_campaign/011_track1_original_dataset_forward_gbm_attempt_11.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-13-44__track1_original_dataset_forward_gbm_attempt_11_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-13-44__track1_original_dataset_forward_gbm_attempt_11_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-13-44__track1_original_dataset_forward_gbm_attempt_11_campaign_validation/validation_summary.yaml`
