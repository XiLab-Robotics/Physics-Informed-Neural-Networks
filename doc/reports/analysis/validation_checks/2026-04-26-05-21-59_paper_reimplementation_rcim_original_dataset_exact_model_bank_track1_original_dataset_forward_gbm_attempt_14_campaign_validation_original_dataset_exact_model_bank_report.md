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
- random seed: `31`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `89.461%`
- winning mean component MAE: `0.165323`
- winning mean component RMSE: `0.245623`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 89.461 | 0.165323 | 0.245623 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.01, 'estimator__max_depth': 14, 'estimator__min_samples_split': 14, 'estimator__n_estimators': 84}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `GBM` | 0.007624 | 0.009410 | 19.006 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000037 | 0.000048 | 0.213 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.002845 | 0.004164 | 56.413 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000060 | 0.000074 | 7.850 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | 0.053233 | 0.065738 | 2.917 |
| `fft_y_Fw_filtered_ampl_39` | `GBM` | 0.000115 | 0.000135 | 11.353 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.095574 | 0.115684 | 8.045 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000040 | 0.000054 | 5.206 |
| `fft_y_Fw_filtered_phase_40` | `GBM` | 0.054723 | 0.070632 | 93.418 |
| `fft_y_Fw_filtered_ampl_78` | `GBM` | 0.000233 | 0.000279 | 82.050 |
| `fft_y_Fw_filtered_phase_78` | `GBM` | 0.233153 | 0.441646 | 680.792 |
| `fft_y_Fw_filtered_ampl_81` | `GBM` | 0.000025 | 0.000036 | 7.301 |
| `fft_y_Fw_filtered_phase_81` | `GBM` | 0.171772 | 0.211514 | 22.883 |
| `fft_y_Fw_filtered_ampl_156` | `GBM` | 0.000290 | 0.000344 | 310.705 |
| `fft_y_Fw_filtered_phase_156` | `GBM` | 1.135692 | 1.393519 | 55.186 |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000415 | 0.001026 | 190.036 |
| `fft_y_Fw_filtered_phase_162` | `GBM` | 0.806667 | 1.230662 | 34.532 |
| `fft_y_Fw_filtered_ampl_240` | `GBM` | 0.000133 | 0.000192 | 74.573 |
| `fft_y_Fw_filtered_phase_240` | `GBM` | 0.578504 | 1.121682 | 37.277 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/gbm/2026-04-26_track1_forward_gbm_original_dataset_mega_campaign/014_track1_original_dataset_forward_gbm_attempt_14.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-20-01__track1_original_dataset_forward_gbm_attempt_14_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-20-01__track1_original_dataset_forward_gbm_attempt_14_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-20-01__track1_original_dataset_forward_gbm_attempt_14_campaign_validation/validation_summary.yaml`
