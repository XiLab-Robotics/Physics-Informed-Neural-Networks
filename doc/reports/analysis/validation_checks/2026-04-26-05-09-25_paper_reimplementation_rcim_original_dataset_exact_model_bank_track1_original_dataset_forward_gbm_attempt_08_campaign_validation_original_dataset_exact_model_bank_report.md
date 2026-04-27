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
- random seed: `17`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `24.860%`
- winning mean component MAE: `0.068392`
- winning mean component RMSE: `0.130789`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 24.860 | 0.068392 | 0.130789 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 14, 'estimator__min_samples_split': 14, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `GBM` | 0.003569 | 0.004336 | 7.274 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000027 | 0.000036 | 0.155 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.001961 | 0.002508 | 47.067 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000030 | 0.000042 | 3.706 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | 0.026895 | 0.033566 | 1.487 |
| `fft_y_Fw_filtered_ampl_39` | `GBM` | 0.000045 | 0.000054 | 4.030 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.032725 | 0.042033 | 2.934 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000024 | 0.000032 | 2.976 |
| `fft_y_Fw_filtered_phase_40` | `GBM` | 0.042219 | 0.061640 | 87.183 |
| `fft_y_Fw_filtered_ampl_78` | `GBM` | 0.000079 | 0.000105 | 26.314 |
| `fft_y_Fw_filtered_phase_78` | `GBM` | 0.071375 | 0.106232 | 111.888 |
| `fft_y_Fw_filtered_ampl_81` | `GBM` | 0.000013 | 0.000017 | 4.495 |
| `fft_y_Fw_filtered_phase_81` | `GBM` | 0.079200 | 0.099646 | 7.859 |
| `fft_y_Fw_filtered_ampl_156` | `GBM` | 0.000116 | 0.000232 | 56.453 |
| `fft_y_Fw_filtered_phase_156` | `GBM` | 0.581460 | 1.021209 | 26.759 |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000146 | 0.000375 | 41.307 |
| `fft_y_Fw_filtered_phase_162` | `GBM` | 0.236174 | 0.485444 | 11.015 |
| `fft_y_Fw_filtered_ampl_240` | `GBM` | 0.000063 | 0.000104 | 17.030 |
| `fft_y_Fw_filtered_phase_240` | `GBM` | 0.223318 | 0.627378 | 12.402 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/gbm/2026-04-26_track1_forward_gbm_original_dataset_mega_campaign/008_track1_original_dataset_forward_gbm_attempt_08.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-07-26__track1_original_dataset_forward_gbm_attempt_08_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-07-26__track1_original_dataset_forward_gbm_attempt_08_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-07-26__track1_original_dataset_forward_gbm_attempt_08_campaign_validation/validation_summary.yaml`
