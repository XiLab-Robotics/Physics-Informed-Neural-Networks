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

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `31.426%`
- winning mean component MAE: `0.079764`
- winning mean component RMSE: `0.155258`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 31.426 | 0.079764 | 0.155258 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 17, 'estimator__min_samples_split': 16, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `GBM` | 0.003665 | 0.004526 | 48.653 |
| `fft_y_Bw_filtered_ampl_1` | `GBM` | 0.000021 | 0.000030 | 0.122 |
| `fft_y_Bw_filtered_phase_1` | `GBM` | 0.001715 | 0.002445 | 38.831 |
| `fft_y_Bw_filtered_ampl_3` | `GBM` | 0.000026 | 0.000036 | 2.780 |
| `fft_y_Bw_filtered_phase_3` | `GBM` | 0.032949 | 0.045047 | 2.465 |
| `fft_y_Bw_filtered_ampl_39` | `GBM` | 0.000023 | 0.000032 | 5.228 |
| `fft_y_Bw_filtered_phase_39` | `GBM` | 0.423717 | 0.794148 | 15.554 |
| `fft_y_Bw_filtered_ampl_40` | `GBM` | 0.000026 | 0.000039 | 8.488 |
| `fft_y_Bw_filtered_phase_40` | `GBM` | 0.099122 | 0.179852 | 28.690 |
| `fft_y_Bw_filtered_ampl_78` | `GBM` | 0.000088 | 0.000109 | 14.667 |
| `fft_y_Bw_filtered_phase_78` | `GBM` | 0.061599 | 0.093267 | 17.540 |
| `fft_y_Bw_filtered_ampl_81` | `GBM` | 0.000010 | 0.000015 | 7.965 |
| `fft_y_Bw_filtered_phase_81` | `GBM` | 0.107149 | 0.149456 | 192.571 |
| `fft_y_Bw_filtered_ampl_156` | `GBM` | 0.000265 | 0.001053 | 34.989 |
| `fft_y_Bw_filtered_phase_156` | `GBM` | 0.208448 | 0.471596 | 93.213 |
| `fft_y_Bw_filtered_ampl_162` | `GBM` | 0.000159 | 0.000362 | 43.531 |
| `fft_y_Bw_filtered_phase_162` | `GBM` | 0.143808 | 0.218814 | 8.431 |
| `fft_y_Bw_filtered_ampl_240` | `GBM` | 0.000092 | 0.000173 | 15.001 |
| `fft_y_Bw_filtered_phase_240` | `GBM` | 0.432645 | 0.988906 | 18.376 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/gbm/2026-04-26_track1_backward_gbm_original_dataset_mega_campaign/007_track1_original_dataset_backward_gbm_attempt_07.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-49-37__track1_original_dataset_backward_gbm_attempt_07_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-49-37__track1_original_dataset_backward_gbm_attempt_07_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-49-37__track1_original_dataset_backward_gbm_attempt_07_campaign_validation/validation_summary.yaml`
