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
- random seed: `37`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `89.796%`
- winning mean component MAE: `0.151392`
- winning mean component RMSE: `0.224161`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 89.796 | 0.151392 | 0.224161 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 11, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `LGBM` | 0.006660 | 0.007939 | 16.110 |
| `fft_y_Fw_filtered_ampl_1` | `LGBM` | 0.000024 | 0.000031 | 0.139 |
| `fft_y_Fw_filtered_phase_1` | `LGBM` | 0.002728 | 0.003745 | 233.328 |
| `fft_y_Fw_filtered_ampl_3` | `LGBM` | 0.000054 | 0.000063 | 7.287 |
| `fft_y_Fw_filtered_phase_3` | `LGBM` | 0.052102 | 0.063241 | 2.909 |
| `fft_y_Fw_filtered_ampl_39` | `LGBM` | 0.000104 | 0.000123 | 10.124 |
| `fft_y_Fw_filtered_phase_39` | `LGBM` | 0.079976 | 0.096663 | 6.421 |
| `fft_y_Fw_filtered_ampl_40` | `LGBM` | 0.000037 | 0.000055 | 4.664 |
| `fft_y_Fw_filtered_phase_40` | `LGBM` | 0.056492 | 0.072107 | 127.356 |
| `fft_y_Fw_filtered_ampl_78` | `LGBM` | 0.000196 | 0.000232 | 61.983 |
| `fft_y_Fw_filtered_phase_78` | `LGBM` | 0.170668 | 0.269266 | 301.328 |
| `fft_y_Fw_filtered_ampl_81` | `LGBM` | 0.000026 | 0.000034 | 8.945 |
| `fft_y_Fw_filtered_phase_81` | `LGBM` | 0.143187 | 0.190849 | 21.800 |
| `fft_y_Fw_filtered_ampl_156` | `LGBM` | 0.000474 | 0.001059 | 254.258 |
| `fft_y_Fw_filtered_phase_156` | `LGBM` | 1.180718 | 1.577027 | 56.916 |
| `fft_y_Fw_filtered_ampl_162` | `LGBM` | 0.000372 | 0.001106 | 153.634 |
| `fft_y_Fw_filtered_phase_162` | `LGBM` | 0.738550 | 1.194154 | 31.491 |
| `fft_y_Fw_filtered_ampl_240` | `LGBM` | 0.000134 | 0.000217 | 61.175 |
| `fft_y_Fw_filtered_phase_240` | `LGBM` | 0.443941 | 0.781141 | 346.246 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/lgbm/2026-04-26_track1_forward_lgbm_original_dataset_mega_campaign/015_track1_original_dataset_forward_lgbm_attempt_15.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-11-37-22__track1_original_dataset_forward_lgbm_attempt_15_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-11-37-22__track1_original_dataset_forward_lgbm_attempt_15_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-11-37-22__track1_original_dataset_forward_lgbm_attempt_15_campaign_validation/validation_summary.yaml`
