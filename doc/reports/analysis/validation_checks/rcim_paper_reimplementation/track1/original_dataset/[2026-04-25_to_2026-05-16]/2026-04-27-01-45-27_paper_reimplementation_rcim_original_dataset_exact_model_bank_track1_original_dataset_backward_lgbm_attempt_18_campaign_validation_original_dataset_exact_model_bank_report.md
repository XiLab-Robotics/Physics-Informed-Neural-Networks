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
- random seed: `53`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `31.685%`
- winning mean component MAE: `0.069584`
- winning mean component RMSE: `0.146952`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 31.685 | 0.069584 | 0.146952 | `{'estimator__learning_rate': 0.39, 'estimator__max_depth': 10, 'estimator__num_leaves': 10, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `LGBM` | 0.002533 | 0.003265 | 41.452 |
| `fft_y_Bw_filtered_ampl_1` | `LGBM` | 0.000027 | 0.000042 | 0.159 |
| `fft_y_Bw_filtered_phase_1` | `LGBM` | 0.002120 | 0.002955 | 38.995 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000024 | 0.000037 | 2.558 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.020560 | 0.052130 | 1.559 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000016 | 0.000022 | 3.607 |
| `fft_y_Bw_filtered_phase_39` | `LGBM` | 0.278041 | 0.836115 | 10.563 |
| `fft_y_Bw_filtered_ampl_40` | `LGBM` | 0.000027 | 0.000041 | 9.005 |
| `fft_y_Bw_filtered_phase_40` | `LGBM` | 0.112253 | 0.181202 | 199.977 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000030 | 0.000043 | 8.193 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.090339 | 0.167945 | 37.342 |
| `fft_y_Bw_filtered_ampl_81` | `LGBM` | 0.000009 | 0.000012 | 7.627 |
| `fft_y_Bw_filtered_phase_81` | `LGBM` | 0.114592 | 0.187797 | 116.867 |
| `fft_y_Bw_filtered_ampl_156` | `LGBM` | 0.000397 | 0.001324 | 25.456 |
| `fft_y_Bw_filtered_phase_156` | `LGBM` | 0.154455 | 0.275013 | 22.080 |
| `fft_y_Bw_filtered_ampl_162` | `LGBM` | 0.000123 | 0.000223 | 23.132 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.122917 | 0.298634 | 7.031 |
| `fft_y_Bw_filtered_ampl_240` | `LGBM` | 0.000088 | 0.000128 | 20.646 |
| `fft_y_Bw_filtered_phase_240` | `LGBM` | 0.423553 | 0.785165 | 25.771 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/lgbm/2026-04-26_track1_backward_lgbm_original_dataset_mega_campaign/018_track1_original_dataset_backward_lgbm_attempt_18.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-27-01-23-33__track1_original_dataset_backward_lgbm_attempt_18_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-27-01-23-33__track1_original_dataset_backward_lgbm_attempt_18_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-27-01-23-33__track1_original_dataset_backward_lgbm_attempt_18_campaign_validation/validation_summary.yaml`
