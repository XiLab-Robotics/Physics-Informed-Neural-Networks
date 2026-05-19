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
- random seed: `7`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `46.507%`
- winning mean component MAE: `0.156206`
- winning mean component RMSE: `0.233455`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 46.507 | 0.156206 | 0.233455 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 10, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `LGBM` | 0.005600 | 0.006787 | 89.227 |
| `fft_y_Bw_filtered_ampl_1` | `LGBM` | 0.000035 | 0.000064 | 0.205 |
| `fft_y_Bw_filtered_phase_1` | `LGBM` | 0.002250 | 0.003340 | 91.861 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000050 | 0.000071 | 5.070 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.070642 | 0.084596 | 5.390 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000042 | 0.000050 | 9.090 |
| `fft_y_Bw_filtered_phase_39` | `LGBM` | 1.010915 | 1.376568 | 37.537 |
| `fft_y_Bw_filtered_ampl_40` | `LGBM` | 0.000032 | 0.000042 | 10.500 |
| `fft_y_Bw_filtered_phase_40` | `LGBM` | 0.165816 | 0.251629 | 60.553 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000218 | 0.000271 | 47.273 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.113378 | 0.216625 | 29.710 |
| `fft_y_Bw_filtered_ampl_81` | `LGBM` | 0.000014 | 0.000018 | 11.270 |
| `fft_y_Bw_filtered_phase_81` | `LGBM` | 0.158324 | 0.193907 | 102.948 |
| `fft_y_Bw_filtered_ampl_156` | `LGBM` | 0.000753 | 0.002754 | 92.801 |
| `fft_y_Bw_filtered_phase_156` | `LGBM` | 0.367895 | 0.715308 | 28.384 |
| `fft_y_Bw_filtered_ampl_162` | `LGBM` | 0.000553 | 0.001500 | 125.346 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.438320 | 0.604555 | 23.687 |
| `fft_y_Bw_filtered_ampl_240` | `LGBM` | 0.000370 | 0.001004 | 64.127 |
| `fft_y_Bw_filtered_phase_240` | `LGBM` | 0.632707 | 0.976561 | 48.649 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/lgbm/2026-04-26_track1_backward_lgbm_original_dataset_mega_campaign/003_track1_original_dataset_backward_lgbm_attempt_03.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-52-53__track1_original_dataset_backward_lgbm_attempt_03_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-52-53__track1_original_dataset_backward_lgbm_attempt_03_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-52-53__track1_original_dataset_backward_lgbm_attempt_03_campaign_validation/validation_summary.yaml`
