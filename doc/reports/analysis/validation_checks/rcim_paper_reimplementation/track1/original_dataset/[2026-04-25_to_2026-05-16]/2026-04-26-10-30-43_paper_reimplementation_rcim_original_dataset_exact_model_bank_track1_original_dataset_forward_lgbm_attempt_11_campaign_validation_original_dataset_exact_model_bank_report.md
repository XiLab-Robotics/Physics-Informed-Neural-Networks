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

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `64.015%`
- winning mean component MAE: `0.148315`
- winning mean component RMSE: `0.219795`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 64.015 | 0.148315 | 0.219795 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 12, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `LGBM` | 0.006700 | 0.007999 | 14.596 |
| `fft_y_Fw_filtered_ampl_1` | `LGBM` | 0.000034 | 0.000045 | 0.198 |
| `fft_y_Fw_filtered_phase_1` | `LGBM` | 0.002389 | 0.003127 | 59.974 |
| `fft_y_Fw_filtered_ampl_3` | `LGBM` | 0.000060 | 0.000072 | 7.571 |
| `fft_y_Fw_filtered_phase_3` | `LGBM` | 0.049848 | 0.061390 | 2.804 |
| `fft_y_Fw_filtered_ampl_39` | `LGBM` | 0.000107 | 0.000122 | 9.876 |
| `fft_y_Fw_filtered_phase_39` | `LGBM` | 0.082847 | 0.102081 | 7.342 |
| `fft_y_Fw_filtered_ampl_40` | `LGBM` | 0.000045 | 0.000071 | 6.485 |
| `fft_y_Fw_filtered_phase_40` | `LGBM` | 0.061964 | 0.085650 | 330.769 |
| `fft_y_Fw_filtered_ampl_78` | `LGBM` | 0.000205 | 0.000240 | 48.821 |
| `fft_y_Fw_filtered_phase_78` | `LGBM` | 0.172507 | 0.295417 | 93.436 |
| `fft_y_Fw_filtered_ampl_81` | `LGBM` | 0.000026 | 0.000033 | 8.212 |
| `fft_y_Fw_filtered_phase_81` | `LGBM` | 0.146511 | 0.192074 | 19.979 |
| `fft_y_Fw_filtered_ampl_156` | `LGBM` | 0.000317 | 0.000694 | 293.328 |
| `fft_y_Fw_filtered_phase_156` | `LGBM` | 1.208348 | 1.634369 | 53.027 |
| `fft_y_Fw_filtered_ampl_162` | `LGBM` | 0.000365 | 0.000792 | 140.628 |
| `fft_y_Fw_filtered_phase_162` | `LGBM` | 0.657454 | 1.049271 | 27.864 |
| `fft_y_Fw_filtered_ampl_240` | `LGBM` | 0.000129 | 0.000214 | 46.056 |
| `fft_y_Fw_filtered_phase_240` | `LGBM` | 0.428124 | 0.742446 | 45.328 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/lgbm/2026-04-26_track1_forward_lgbm_original_dataset_mega_campaign/011_track1_original_dataset_forward_lgbm_attempt_11.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-10-08-42__track1_original_dataset_forward_lgbm_attempt_11_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-10-08-42__track1_original_dataset_forward_lgbm_attempt_11_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-10-08-42__track1_original_dataset_forward_lgbm_attempt_11_campaign_validation/validation_summary.yaml`
