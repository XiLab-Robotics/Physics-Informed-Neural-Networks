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
- random seed: `13`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `24.820%`
- winning mean component MAE: `0.082400`
- winning mean component RMSE: `0.155447`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 24.820 | 0.082400 | 0.155447 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 16, 'estimator__min_samples_split': 18, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `GBM` | 0.003233 | 0.004091 | 59.308 |
| `fft_y_Bw_filtered_ampl_1` | `GBM` | 0.000028 | 0.000042 | 0.165 |
| `fft_y_Bw_filtered_phase_1` | `GBM` | 0.001723 | 0.002511 | 88.399 |
| `fft_y_Bw_filtered_ampl_3` | `GBM` | 0.000021 | 0.000028 | 2.099 |
| `fft_y_Bw_filtered_phase_3` | `GBM` | 0.031350 | 0.038275 | 2.377 |
| `fft_y_Bw_filtered_ampl_39` | `GBM` | 0.000022 | 0.000030 | 4.657 |
| `fft_y_Bw_filtered_phase_39` | `GBM` | 0.372973 | 0.698295 | 13.705 |
| `fft_y_Bw_filtered_ampl_40` | `GBM` | 0.000030 | 0.000042 | 9.798 |
| `fft_y_Bw_filtered_phase_40` | `GBM` | 0.096946 | 0.132292 | 41.050 |
| `fft_y_Bw_filtered_ampl_78` | `GBM` | 0.000093 | 0.000115 | 16.791 |
| `fft_y_Bw_filtered_phase_78` | `GBM` | 0.074595 | 0.134308 | 23.177 |
| `fft_y_Bw_filtered_ampl_81` | `GBM` | 0.000011 | 0.000016 | 8.488 |
| `fft_y_Bw_filtered_phase_81` | `GBM` | 0.106722 | 0.137747 | 70.458 |
| `fft_y_Bw_filtered_ampl_156` | `GBM` | 0.000243 | 0.000636 | 29.923 |
| `fft_y_Bw_filtered_phase_156` | `GBM` | 0.152909 | 0.368980 | 14.100 |
| `fft_y_Bw_filtered_ampl_162` | `GBM` | 0.000192 | 0.000400 | 39.234 |
| `fft_y_Bw_filtered_phase_162` | `GBM` | 0.159761 | 0.237716 | 8.380 |
| `fft_y_Bw_filtered_ampl_240` | `GBM` | 0.000127 | 0.000445 | 17.131 |
| `fft_y_Bw_filtered_phase_240` | `GBM` | 0.564628 | 1.197522 | 22.344 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/gbm/2026-04-26_track1_backward_gbm_original_dataset_mega_campaign/006_track1_original_dataset_backward_gbm_attempt_06.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-47-35__track1_original_dataset_backward_gbm_attempt_06_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-47-35__track1_original_dataset_backward_gbm_attempt_06_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-47-35__track1_original_dataset_backward_gbm_attempt_06_campaign_validation/validation_summary.yaml`
