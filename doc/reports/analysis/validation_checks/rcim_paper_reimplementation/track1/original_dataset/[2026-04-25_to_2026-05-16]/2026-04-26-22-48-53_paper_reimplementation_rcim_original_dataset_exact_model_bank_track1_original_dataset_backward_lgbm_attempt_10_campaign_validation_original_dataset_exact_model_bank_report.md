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
- random seed: `21`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `60.508%`
- winning mean component MAE: `0.154432`
- winning mean component RMSE: `0.224343`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 60.508 | 0.154432 | 0.224343 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 11, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `LGBM` | 0.006693 | 0.007743 | 186.429 |
| `fft_y_Bw_filtered_ampl_1` | `LGBM` | 0.000027 | 0.000037 | 0.158 |
| `fft_y_Bw_filtered_phase_1` | `LGBM` | 0.002780 | 0.003848 | 250.455 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000050 | 0.000067 | 5.181 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.075246 | 0.089199 | 5.526 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000044 | 0.000055 | 9.585 |
| `fft_y_Bw_filtered_phase_39` | `LGBM` | 0.954599 | 1.252368 | 36.309 |
| `fft_y_Bw_filtered_ampl_40` | `LGBM` | 0.000032 | 0.000046 | 11.193 |
| `fft_y_Bw_filtered_phase_40` | `LGBM` | 0.162706 | 0.227130 | 71.796 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000247 | 0.000294 | 41.630 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.127973 | 0.192527 | 51.310 |
| `fft_y_Bw_filtered_ampl_81` | `LGBM` | 0.000015 | 0.000023 | 13.159 |
| `fft_y_Bw_filtered_phase_81` | `LGBM` | 0.184600 | 0.233216 | 67.456 |
| `fft_y_Bw_filtered_ampl_156` | `LGBM` | 0.000627 | 0.001445 | 94.485 |
| `fft_y_Bw_filtered_phase_156` | `LGBM` | 0.440787 | 0.775747 | 47.424 |
| `fft_y_Bw_filtered_ampl_162` | `LGBM` | 0.000516 | 0.000950 | 149.581 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.492325 | 0.786471 | 25.348 |
| `fft_y_Bw_filtered_ampl_240` | `LGBM` | 0.000313 | 0.000844 | 49.208 |
| `fft_y_Bw_filtered_phase_240` | `LGBM` | 0.484625 | 0.690506 | 33.422 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/lgbm/2026-04-26_track1_backward_lgbm_original_dataset_mega_campaign/010_track1_original_dataset_backward_lgbm_attempt_10.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-22-26-54__track1_original_dataset_backward_lgbm_attempt_10_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-22-26-54__track1_original_dataset_backward_lgbm_attempt_10_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-22-26-54__track1_original_dataset_backward_lgbm_attempt_10_campaign_validation/validation_summary.yaml`
