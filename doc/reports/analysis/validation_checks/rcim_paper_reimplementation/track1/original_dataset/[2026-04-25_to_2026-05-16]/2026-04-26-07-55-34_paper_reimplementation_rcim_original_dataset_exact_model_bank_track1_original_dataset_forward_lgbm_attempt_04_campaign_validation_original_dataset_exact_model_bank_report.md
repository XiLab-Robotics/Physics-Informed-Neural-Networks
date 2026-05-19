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
- random seed: `9`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `56.362%`
- winning mean component MAE: `0.156961`
- winning mean component RMSE: `0.235187`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 56.362 | 0.156961 | 0.235187 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 12, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `LGBM` | 0.005995 | 0.007033 | 13.438 |
| `fft_y_Fw_filtered_ampl_1` | `LGBM` | 0.000028 | 0.000038 | 0.166 |
| `fft_y_Fw_filtered_phase_1` | `LGBM` | 0.002799 | 0.003756 | 48.201 |
| `fft_y_Fw_filtered_ampl_3` | `LGBM` | 0.000054 | 0.000063 | 7.041 |
| `fft_y_Fw_filtered_phase_3` | `LGBM` | 0.055086 | 0.067683 | 3.051 |
| `fft_y_Fw_filtered_ampl_39` | `LGBM` | 0.000110 | 0.000133 | 10.159 |
| `fft_y_Fw_filtered_phase_39` | `LGBM` | 0.074843 | 0.089601 | 6.460 |
| `fft_y_Fw_filtered_ampl_40` | `LGBM` | 0.000044 | 0.000065 | 6.147 |
| `fft_y_Fw_filtered_phase_40` | `LGBM` | 0.063257 | 0.094620 | 142.699 |
| `fft_y_Fw_filtered_ampl_78` | `LGBM` | 0.000211 | 0.000257 | 118.039 |
| `fft_y_Fw_filtered_phase_78` | `LGBM` | 0.196156 | 0.384481 | 107.378 |
| `fft_y_Fw_filtered_ampl_81` | `LGBM` | 0.000024 | 0.000034 | 7.580 |
| `fft_y_Fw_filtered_phase_81` | `LGBM` | 0.153038 | 0.211745 | 41.366 |
| `fft_y_Fw_filtered_ampl_156` | `LGBM` | 0.000473 | 0.001032 | 232.377 |
| `fft_y_Fw_filtered_phase_156` | `LGBM` | 1.046527 | 1.385109 | 52.426 |
| `fft_y_Fw_filtered_ampl_162` | `LGBM` | 0.000534 | 0.001550 | 141.301 |
| `fft_y_Fw_filtered_phase_162` | `LGBM` | 0.845176 | 1.258230 | 38.575 |
| `fft_y_Fw_filtered_ampl_240` | `LGBM` | 0.000158 | 0.000266 | 67.027 |
| `fft_y_Fw_filtered_phase_240` | `LGBM` | 0.537751 | 0.962860 | 27.438 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/lgbm/2026-04-26_track1_forward_lgbm_original_dataset_mega_campaign/004_track1_original_dataset_forward_lgbm_attempt_04.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-07-33-33__track1_original_dataset_forward_lgbm_attempt_04_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-07-33-33__track1_original_dataset_forward_lgbm_attempt_04_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-07-33-33__track1_original_dataset_forward_lgbm_attempt_04_campaign_validation/validation_summary.yaml`
