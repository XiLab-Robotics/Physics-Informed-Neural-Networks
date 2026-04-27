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
- random seed: `0`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `64.770%`
- winning mean component MAE: `0.148417`
- winning mean component RMSE: `0.222652`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 64.770 | 0.148417 | 0.222652 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 12, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `LGBM` | 0.006088 | 0.007663 | 13.681 |
| `fft_y_Fw_filtered_ampl_1` | `LGBM` | 0.000035 | 0.000046 | 0.206 |
| `fft_y_Fw_filtered_phase_1` | `LGBM` | 0.002610 | 0.003622 | 164.247 |
| `fft_y_Fw_filtered_ampl_3` | `LGBM` | 0.000052 | 0.000065 | 6.906 |
| `fft_y_Fw_filtered_phase_3` | `LGBM` | 0.045093 | 0.053539 | 2.500 |
| `fft_y_Fw_filtered_ampl_39` | `LGBM` | 0.000108 | 0.000125 | 10.059 |
| `fft_y_Fw_filtered_phase_39` | `LGBM` | 0.077429 | 0.101550 | 6.576 |
| `fft_y_Fw_filtered_ampl_40` | `LGBM` | 0.000037 | 0.000055 | 5.028 |
| `fft_y_Fw_filtered_phase_40` | `LGBM` | 0.064033 | 0.087144 | 121.433 |
| `fft_y_Fw_filtered_ampl_78` | `LGBM` | 0.000177 | 0.000210 | 98.056 |
| `fft_y_Fw_filtered_phase_78` | `LGBM` | 0.144583 | 0.259432 | 209.450 |
| `fft_y_Fw_filtered_ampl_81` | `LGBM` | 0.000024 | 0.000030 | 8.439 |
| `fft_y_Fw_filtered_phase_81` | `LGBM` | 0.149051 | 0.191343 | 17.657 |
| `fft_y_Fw_filtered_ampl_156` | `LGBM` | 0.000335 | 0.000543 | 224.828 |
| `fft_y_Fw_filtered_phase_156` | `LGBM` | 1.220087 | 1.546208 | 111.417 |
| `fft_y_Fw_filtered_ampl_162` | `LGBM` | 0.000453 | 0.001171 | 125.536 |
| `fft_y_Fw_filtered_phase_162` | `LGBM` | 0.632576 | 1.027077 | 31.643 |
| `fft_y_Fw_filtered_ampl_240` | `LGBM` | 0.000153 | 0.000292 | 50.304 |
| `fft_y_Fw_filtered_phase_240` | `LGBM` | 0.476992 | 0.950281 | 22.664 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/lgbm/2026-04-26_track1_forward_lgbm_original_dataset_mega_campaign/001_track1_original_dataset_forward_lgbm_attempt_01.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-27-08__track1_original_dataset_forward_lgbm_attempt_01_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-27-08__track1_original_dataset_forward_lgbm_attempt_01_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-27-08__track1_original_dataset_forward_lgbm_attempt_01_campaign_validation/validation_summary.yaml`
