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
- random seed: `27`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `17.192%`
- winning mean component MAE: `0.066198`
- winning mean component RMSE: `0.122313`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 17.192 | 0.066198 | 0.122313 | `{'estimator__learning_rate': 0.2, 'estimator__max_depth': 10, 'estimator__num_leaves': 10, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `LGBM` | 0.002313 | 0.002943 | 31.186 |
| `fft_y_Bw_filtered_ampl_1` | `LGBM` | 0.000025 | 0.000034 | 0.148 |
| `fft_y_Bw_filtered_phase_1` | `LGBM` | 0.001888 | 0.002537 | 38.890 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000023 | 0.000035 | 2.256 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.019037 | 0.023994 | 1.455 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000015 | 0.000023 | 3.497 |
| `fft_y_Bw_filtered_phase_39` | `LGBM` | 0.268393 | 0.654804 | 9.557 |
| `fft_y_Bw_filtered_ampl_40` | `LGBM` | 0.000028 | 0.000038 | 9.474 |
| `fft_y_Bw_filtered_phase_40` | `LGBM` | 0.090958 | 0.140965 | 39.069 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000028 | 0.000038 | 4.029 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.060894 | 0.097008 | 31.311 |
| `fft_y_Bw_filtered_ampl_81` | `LGBM` | 0.000010 | 0.000014 | 8.394 |
| `fft_y_Bw_filtered_phase_81` | `LGBM` | 0.098699 | 0.130353 | 34.552 |
| `fft_y_Bw_filtered_ampl_156` | `LGBM` | 0.000367 | 0.001116 | 15.918 |
| `fft_y_Bw_filtered_phase_156` | `LGBM` | 0.156918 | 0.345862 | 13.042 |
| `fft_y_Bw_filtered_ampl_162` | `LGBM` | 0.000209 | 0.000407 | 24.561 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.120503 | 0.210514 | 7.167 |
| `fft_y_Bw_filtered_ampl_240` | `LGBM` | 0.000159 | 0.000269 | 25.637 |
| `fft_y_Bw_filtered_phase_240` | `LGBM` | 0.437299 | 0.712987 | 26.497 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/lgbm/2026-04-26_track1_backward_lgbm_original_dataset_mega_campaign/012_track1_original_dataset_backward_lgbm_attempt_12.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-23-11-00__track1_original_dataset_backward_lgbm_attempt_12_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-23-11-00__track1_original_dataset_backward_lgbm_attempt_12_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-23-11-00__track1_original_dataset_backward_lgbm_attempt_12_campaign_validation/validation_summary.yaml`
