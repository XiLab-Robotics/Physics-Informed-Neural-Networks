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
- random seed: `15`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `63.740%`
- winning mean component MAE: `0.155588`
- winning mean component RMSE: `0.229279`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 63.740 | 0.155588 | 0.229279 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 12, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `LGBM` | 0.006137 | 0.007127 | 92.912 |
| `fft_y_Bw_filtered_ampl_1` | `LGBM` | 0.000030 | 0.000061 | 0.177 |
| `fft_y_Bw_filtered_phase_1` | `LGBM` | 0.002558 | 0.003486 | 103.061 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000050 | 0.000066 | 5.213 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.076727 | 0.090312 | 5.660 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000037 | 0.000048 | 8.719 |
| `fft_y_Bw_filtered_phase_39` | `LGBM` | 0.997250 | 1.240832 | 37.611 |
| `fft_y_Bw_filtered_ampl_40` | `LGBM` | 0.000029 | 0.000040 | 8.946 |
| `fft_y_Bw_filtered_phase_40` | `LGBM` | 0.162089 | 0.261062 | 60.290 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000225 | 0.000265 | 41.975 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.136962 | 0.238099 | 35.464 |
| `fft_y_Bw_filtered_ampl_81` | `LGBM` | 0.000014 | 0.000019 | 10.823 |
| `fft_y_Bw_filtered_phase_81` | `LGBM` | 0.190216 | 0.242750 | 422.675 |
| `fft_y_Bw_filtered_ampl_156` | `LGBM` | 0.000683 | 0.002398 | 103.460 |
| `fft_y_Bw_filtered_phase_156` | `LGBM` | 0.393726 | 0.760962 | 46.962 |
| `fft_y_Bw_filtered_ampl_162` | `LGBM` | 0.000640 | 0.001623 | 137.860 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.417099 | 0.648618 | 23.813 |
| `fft_y_Bw_filtered_ampl_240` | `LGBM` | 0.000184 | 0.000301 | 37.675 |
| `fft_y_Bw_filtered_phase_240` | `LGBM` | 0.571507 | 0.858229 | 27.766 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/lgbm/2026-04-26_track1_backward_lgbm_original_dataset_mega_campaign/007_track1_original_dataset_backward_lgbm_attempt_07.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-21-20-45__track1_original_dataset_backward_lgbm_attempt_07_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-21-20-45__track1_original_dataset_backward_lgbm_attempt_07_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-21-20-45__track1_original_dataset_backward_lgbm_attempt_07_campaign_validation/validation_summary.yaml`
