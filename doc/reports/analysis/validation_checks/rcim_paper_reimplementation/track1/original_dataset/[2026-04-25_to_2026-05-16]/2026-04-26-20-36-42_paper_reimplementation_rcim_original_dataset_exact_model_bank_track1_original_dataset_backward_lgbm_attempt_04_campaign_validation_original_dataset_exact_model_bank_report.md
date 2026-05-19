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
- random seed: `9`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `53.805%`
- winning mean component MAE: `0.062823`
- winning mean component RMSE: `0.119529`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 53.805 | 0.062823 | 0.119529 | `{'estimator__learning_rate': 0.2, 'estimator__max_depth': 11, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `LGBM` | 0.002578 | 0.003121 | 63.278 |
| `fft_y_Bw_filtered_ampl_1` | `LGBM` | 0.000026 | 0.000038 | 0.150 |
| `fft_y_Bw_filtered_phase_1` | `LGBM` | 0.001796 | 0.002364 | 46.882 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000017 | 0.000025 | 1.812 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.018768 | 0.025253 | 1.399 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000016 | 0.000023 | 3.481 |
| `fft_y_Bw_filtered_phase_39` | `LGBM` | 0.307975 | 0.763503 | 10.610 |
| `fft_y_Bw_filtered_ampl_40` | `LGBM` | 0.000024 | 0.000036 | 7.841 |
| `fft_y_Bw_filtered_phase_40` | `LGBM` | 0.105625 | 0.166532 | 23.912 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000030 | 0.000044 | 23.886 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.082833 | 0.246063 | 26.856 |
| `fft_y_Bw_filtered_ampl_81` | `LGBM` | 0.000009 | 0.000013 | 7.238 |
| `fft_y_Bw_filtered_phase_81` | `LGBM` | 0.108814 | 0.146345 | 716.784 |
| `fft_y_Bw_filtered_ampl_156` | `LGBM` | 0.000411 | 0.001241 | 20.169 |
| `fft_y_Bw_filtered_phase_156` | `LGBM` | 0.143305 | 0.246366 | 17.205 |
| `fft_y_Bw_filtered_ampl_162` | `LGBM` | 0.000145 | 0.000439 | 13.906 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.098175 | 0.166039 | 6.506 |
| `fft_y_Bw_filtered_ampl_240` | `LGBM` | 0.000111 | 0.000338 | 14.155 |
| `fft_y_Bw_filtered_phase_240` | `LGBM` | 0.322970 | 0.503261 | 16.230 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/lgbm/2026-04-26_track1_backward_lgbm_original_dataset_mega_campaign/004_track1_original_dataset_backward_lgbm_attempt_04.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-20-14-55__track1_original_dataset_backward_lgbm_attempt_04_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-20-14-55__track1_original_dataset_backward_lgbm_attempt_04_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-20-14-55__track1_original_dataset_backward_lgbm_attempt_04_campaign_validation/validation_summary.yaml`
