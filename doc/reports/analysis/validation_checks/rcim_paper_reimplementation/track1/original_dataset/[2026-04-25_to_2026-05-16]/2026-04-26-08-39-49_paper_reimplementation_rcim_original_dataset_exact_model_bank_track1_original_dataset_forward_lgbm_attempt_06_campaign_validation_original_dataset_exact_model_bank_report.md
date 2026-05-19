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
- random seed: `13`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `66.284%`
- winning mean component MAE: `0.147099`
- winning mean component RMSE: `0.210166`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 66.284 | 0.147099 | 0.210166 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 10, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `LGBM` | 0.006535 | 0.007549 | 14.216 |
| `fft_y_Fw_filtered_ampl_1` | `LGBM` | 0.000026 | 0.000036 | 0.153 |
| `fft_y_Fw_filtered_phase_1` | `LGBM` | 0.002529 | 0.003617 | 139.357 |
| `fft_y_Fw_filtered_ampl_3` | `LGBM` | 0.000059 | 0.000075 | 7.349 |
| `fft_y_Fw_filtered_phase_3` | `LGBM` | 0.063061 | 0.073356 | 3.498 |
| `fft_y_Fw_filtered_ampl_39` | `LGBM` | 0.000114 | 0.000132 | 10.798 |
| `fft_y_Fw_filtered_phase_39` | `LGBM` | 0.082509 | 0.101520 | 7.229 |
| `fft_y_Fw_filtered_ampl_40` | `LGBM` | 0.000035 | 0.000050 | 4.516 |
| `fft_y_Fw_filtered_phase_40` | `LGBM` | 0.052399 | 0.068475 | 118.681 |
| `fft_y_Fw_filtered_ampl_78` | `LGBM` | 0.000204 | 0.000258 | 63.330 |
| `fft_y_Fw_filtered_phase_78` | `LGBM` | 0.168987 | 0.278762 | 87.649 |
| `fft_y_Fw_filtered_ampl_81` | `LGBM` | 0.000028 | 0.000038 | 9.352 |
| `fft_y_Fw_filtered_phase_81` | `LGBM` | 0.162081 | 0.209533 | 24.118 |
| `fft_y_Fw_filtered_ampl_156` | `LGBM` | 0.000396 | 0.000761 | 206.132 |
| `fft_y_Fw_filtered_phase_156` | `LGBM` | 1.269221 | 1.638265 | 56.696 |
| `fft_y_Fw_filtered_ampl_162` | `LGBM` | 0.000653 | 0.001628 | 125.115 |
| `fft_y_Fw_filtered_phase_162` | `LGBM` | 0.559824 | 0.871831 | 35.246 |
| `fft_y_Fw_filtered_ampl_240` | `LGBM` | 0.000126 | 0.000216 | 50.137 |
| `fft_y_Fw_filtered_phase_240` | `LGBM` | 0.426100 | 0.737056 | 295.824 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/lgbm/2026-04-26_track1_forward_lgbm_original_dataset_mega_campaign/006_track1_original_dataset_forward_lgbm_attempt_06.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-08-17-53__track1_original_dataset_forward_lgbm_attempt_06_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-08-17-53__track1_original_dataset_forward_lgbm_attempt_06_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-08-17-53__track1_original_dataset_forward_lgbm_attempt_06_campaign_validation/validation_summary.yaml`
