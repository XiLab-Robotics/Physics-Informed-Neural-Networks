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
- random seed: `0`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `24.025%`
- winning mean component MAE: `0.067018`
- winning mean component RMSE: `0.139720`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 24.025 | 0.067018 | 0.139720 | `{'estimator__learning_rate': 0.58, 'estimator__max_depth': 10, 'estimator__num_leaves': 10, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `LGBM` | 0.002450 | 0.003226 | 132.777 |
| `fft_y_Bw_filtered_ampl_1` | `LGBM` | 0.000023 | 0.000033 | 0.132 |
| `fft_y_Bw_filtered_phase_1` | `LGBM` | 0.001740 | 0.002336 | 25.334 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000021 | 0.000029 | 2.165 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.018025 | 0.027299 | 1.286 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000017 | 0.000022 | 3.998 |
| `fft_y_Bw_filtered_phase_39` | `LGBM` | 0.368428 | 0.938005 | 12.961 |
| `fft_y_Bw_filtered_ampl_40` | `LGBM` | 0.000025 | 0.000034 | 8.463 |
| `fft_y_Bw_filtered_phase_40` | `LGBM` | 0.097513 | 0.129080 | 49.388 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000027 | 0.000036 | 3.491 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.046931 | 0.071647 | 57.835 |
| `fft_y_Bw_filtered_ampl_81` | `LGBM` | 0.000010 | 0.000014 | 8.416 |
| `fft_y_Bw_filtered_phase_81` | `LGBM` | 0.081427 | 0.105663 | 31.682 |
| `fft_y_Bw_filtered_ampl_156` | `LGBM` | 0.000291 | 0.000995 | 21.781 |
| `fft_y_Bw_filtered_phase_156` | `LGBM` | 0.179082 | 0.458084 | 29.824 |
| `fft_y_Bw_filtered_ampl_162` | `LGBM` | 0.000094 | 0.000232 | 13.218 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.092763 | 0.145162 | 5.409 |
| `fft_y_Bw_filtered_ampl_240` | `LGBM` | 0.000117 | 0.000225 | 26.877 |
| `fft_y_Bw_filtered_phase_240` | `LGBM` | 0.384359 | 0.772565 | 21.447 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/lgbm/2026-04-26_track1_backward_lgbm_original_dataset_mega_campaign/001_track1_original_dataset_backward_lgbm_attempt_01.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-08-51__track1_original_dataset_backward_lgbm_attempt_01_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-08-51__track1_original_dataset_backward_lgbm_attempt_01_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-08-51__track1_original_dataset_backward_lgbm_attempt_01_campaign_validation/validation_summary.yaml`
