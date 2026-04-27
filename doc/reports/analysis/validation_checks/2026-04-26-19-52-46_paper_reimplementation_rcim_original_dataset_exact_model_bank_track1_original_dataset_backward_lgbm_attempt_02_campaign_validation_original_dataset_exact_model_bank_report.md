# Original-Dataset Exact RCIM Model Bank Validation Report

## Overview

This report covers the direction-specific exact-model-bank branch trained from the repository dataset under `data/datasets`.

- direction label: `backward`
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

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `51.828%`
- winning mean component MAE: `0.167468`
- winning mean component RMSE: `0.250728`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 51.828 | 0.167468 | 0.250728 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 11, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `LGBM` | 0.005771 | 0.007282 | 132.413 |
| `fft_y_Bw_filtered_ampl_1` | `LGBM` | 0.000044 | 0.000067 | 0.254 |
| `fft_y_Bw_filtered_phase_1` | `LGBM` | 0.002862 | 0.003962 | 125.777 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000053 | 0.000075 | 5.088 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.087040 | 0.102340 | 6.864 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000045 | 0.000057 | 9.607 |
| `fft_y_Bw_filtered_phase_39` | `LGBM` | 0.966747 | 1.183118 | 36.417 |
| `fft_y_Bw_filtered_ampl_40` | `LGBM` | 0.000031 | 0.000043 | 10.859 |
| `fft_y_Bw_filtered_phase_40` | `LGBM` | 0.185584 | 0.277947 | 85.739 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000273 | 0.000321 | 55.645 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.160306 | 0.269053 | 38.682 |
| `fft_y_Bw_filtered_ampl_81` | `LGBM` | 0.000018 | 0.000025 | 14.699 |
| `fft_y_Bw_filtered_phase_81` | `LGBM` | 0.172853 | 0.217842 | 62.388 |
| `fft_y_Bw_filtered_ampl_156` | `LGBM` | 0.000497 | 0.000780 | 107.519 |
| `fft_y_Bw_filtered_phase_156` | `LGBM` | 0.395721 | 0.790362 | 36.763 |
| `fft_y_Bw_filtered_ampl_162` | `LGBM` | 0.000488 | 0.000919 | 148.336 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.472685 | 0.789188 | 24.075 |
| `fft_y_Bw_filtered_ampl_240` | `LGBM` | 0.000259 | 0.000558 | 48.521 |
| `fft_y_Bw_filtered_phase_240` | `LGBM` | 0.730610 | 1.119892 | 35.091 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/lgbm/2026-04-26_track1_backward_lgbm_original_dataset_mega_campaign/002_track1_original_dataset_backward_lgbm_attempt_02.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-30-53__track1_original_dataset_backward_lgbm_attempt_02_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-30-53__track1_original_dataset_backward_lgbm_attempt_02_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-30-53__track1_original_dataset_backward_lgbm_attempt_02_campaign_validation/validation_summary.yaml`
