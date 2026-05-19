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
- random seed: `23`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `29.125%`
- winning mean component MAE: `0.062919`
- winning mean component RMSE: `0.129604`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 29.125 | 0.062919 | 0.129604 | `{'estimator__learning_rate': 0.2, 'estimator__max_depth': 10, 'estimator__num_leaves': 10, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `LGBM` | 0.002622 | 0.003050 | 69.219 |
| `fft_y_Bw_filtered_ampl_1` | `LGBM` | 0.000024 | 0.000032 | 0.141 |
| `fft_y_Bw_filtered_phase_1` | `LGBM` | 0.001754 | 0.002559 | 98.209 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000018 | 0.000028 | 1.745 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.019300 | 0.024902 | 1.453 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000015 | 0.000021 | 3.558 |
| `fft_y_Bw_filtered_phase_39` | `LGBM` | 0.294370 | 0.705913 | 10.715 |
| `fft_y_Bw_filtered_ampl_40` | `LGBM` | 0.000028 | 0.000039 | 9.202 |
| `fft_y_Bw_filtered_phase_40` | `LGBM` | 0.101783 | 0.130227 | 48.812 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000029 | 0.000039 | 4.324 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.060634 | 0.102782 | 20.680 |
| `fft_y_Bw_filtered_ampl_81` | `LGBM` | 0.000010 | 0.000014 | 8.547 |
| `fft_y_Bw_filtered_phase_81` | `LGBM` | 0.097390 | 0.130585 | 173.137 |
| `fft_y_Bw_filtered_ampl_156` | `LGBM` | 0.000209 | 0.000687 | 23.132 |
| `fft_y_Bw_filtered_phase_156` | `LGBM` | 0.188209 | 0.434715 | 25.385 |
| `fft_y_Bw_filtered_ampl_162` | `LGBM` | 0.000088 | 0.000200 | 10.777 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.118435 | 0.293949 | 6.900 |
| `fft_y_Bw_filtered_ampl_240` | `LGBM` | 0.000125 | 0.000223 | 17.726 |
| `fft_y_Bw_filtered_phase_240` | `LGBM` | 0.310416 | 0.632508 | 19.721 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/lgbm/2026-04-26_track1_backward_lgbm_original_dataset_mega_campaign/011_track1_original_dataset_backward_lgbm_attempt_11.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-22-49-01__track1_original_dataset_backward_lgbm_attempt_11_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-22-49-01__track1_original_dataset_backward_lgbm_attempt_11_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-22-49-01__track1_original_dataset_backward_lgbm_attempt_11_campaign_validation/validation_summary.yaml`
