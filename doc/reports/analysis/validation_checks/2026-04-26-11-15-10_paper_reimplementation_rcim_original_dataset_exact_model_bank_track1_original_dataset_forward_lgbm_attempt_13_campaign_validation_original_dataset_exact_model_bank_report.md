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
- random seed: `29`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `60.990%`
- winning mean component MAE: `0.159621`
- winning mean component RMSE: `0.241457`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 60.990 | 0.159621 | 0.241457 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 12, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `LGBM` | 0.007933 | 0.009995 | 35.290 |
| `fft_y_Fw_filtered_ampl_1` | `LGBM` | 0.000032 | 0.000040 | 0.186 |
| `fft_y_Fw_filtered_phase_1` | `LGBM` | 0.002254 | 0.002940 | 30.910 |
| `fft_y_Fw_filtered_ampl_3` | `LGBM` | 0.000059 | 0.000072 | 7.893 |
| `fft_y_Fw_filtered_phase_3` | `LGBM` | 0.055902 | 0.067129 | 3.119 |
| `fft_y_Fw_filtered_ampl_39` | `LGBM` | 0.000121 | 0.000141 | 11.765 |
| `fft_y_Fw_filtered_phase_39` | `LGBM` | 0.082852 | 0.097320 | 6.964 |
| `fft_y_Fw_filtered_ampl_40` | `LGBM` | 0.000047 | 0.000066 | 6.247 |
| `fft_y_Fw_filtered_phase_40` | `LGBM` | 0.057892 | 0.087645 | 269.780 |
| `fft_y_Fw_filtered_ampl_78` | `LGBM` | 0.000203 | 0.000241 | 54.137 |
| `fft_y_Fw_filtered_phase_78` | `LGBM` | 0.180441 | 0.298671 | 100.254 |
| `fft_y_Fw_filtered_ampl_81` | `LGBM` | 0.000025 | 0.000032 | 7.847 |
| `fft_y_Fw_filtered_phase_81` | `LGBM` | 0.156605 | 0.204326 | 17.852 |
| `fft_y_Fw_filtered_ampl_156` | `LGBM` | 0.000422 | 0.000883 | 191.079 |
| `fft_y_Fw_filtered_phase_156` | `LGBM` | 1.115122 | 1.482727 | 58.858 |
| `fft_y_Fw_filtered_ampl_162` | `LGBM` | 0.000322 | 0.000704 | 139.528 |
| `fft_y_Fw_filtered_phase_162` | `LGBM` | 0.854716 | 1.338701 | 38.209 |
| `fft_y_Fw_filtered_ampl_240` | `LGBM` | 0.000178 | 0.000344 | 139.848 |
| `fft_y_Fw_filtered_phase_240` | `LGBM` | 0.517668 | 0.995701 | 39.039 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/lgbm/2026-04-26_track1_forward_lgbm_original_dataset_mega_campaign/013_track1_original_dataset_forward_lgbm_attempt_13.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-10-53-02__track1_original_dataset_forward_lgbm_attempt_13_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-10-53-02__track1_original_dataset_forward_lgbm_attempt_13_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-10-53-02__track1_original_dataset_forward_lgbm_attempt_13_campaign_validation/validation_summary.yaml`
