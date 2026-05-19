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

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `24.044%`
- winning mean component MAE: `0.058803`
- winning mean component RMSE: `0.147195`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 24.044 | 0.058803 | 0.147195 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 12, 'estimator__min_samples_split': 6, 'estimator__n_estimators': 60}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `RF` | 0.003058 | 0.004081 | 31.282 |
| `fft_y_Bw_filtered_ampl_1` | `RF` | 0.000019 | 0.000027 | 0.112 |
| `fft_y_Bw_filtered_phase_1` | `RF` | 0.001778 | 0.002551 | 43.169 |
| `fft_y_Bw_filtered_ampl_3` | `RF` | 0.000024 | 0.000034 | 2.513 |
| `fft_y_Bw_filtered_phase_3` | `RF` | 0.023739 | 0.040605 | 1.782 |
| `fft_y_Bw_filtered_ampl_39` | `RF` | 0.000021 | 0.000029 | 4.751 |
| `fft_y_Bw_filtered_phase_39` | `RF` | 0.277286 | 0.831349 | 9.622 |
| `fft_y_Bw_filtered_ampl_40` | `RF` | 0.000025 | 0.000037 | 7.956 |
| `fft_y_Bw_filtered_phase_40` | `RF` | 0.087823 | 0.148109 | 33.077 |
| `fft_y_Bw_filtered_ampl_78` | `RF` | 0.000053 | 0.000075 | 5.979 |
| `fft_y_Bw_filtered_phase_78` | `RF` | 0.051536 | 0.082409 | 15.608 |
| `fft_y_Bw_filtered_ampl_81` | `RF` | 0.000009 | 0.000014 | 7.450 |
| `fft_y_Bw_filtered_phase_81` | `RF` | 0.099324 | 0.148275 | 203.144 |
| `fft_y_Bw_filtered_ampl_156` | `RF` | 0.000166 | 0.000803 | 8.438 |
| `fft_y_Bw_filtered_phase_156` | `RF` | 0.153490 | 0.587929 | 41.312 |
| `fft_y_Bw_filtered_ampl_162` | `RF` | 0.000106 | 0.000334 | 9.372 |
| `fft_y_Bw_filtered_phase_162` | `RF` | 0.068745 | 0.140726 | 4.084 |
| `fft_y_Bw_filtered_ampl_240` | `RF` | 0.000078 | 0.000171 | 11.128 |
| `fft_y_Bw_filtered_phase_240` | `RF` | 0.349979 | 0.809140 | 16.064 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/rf/2026-04-26_track1_backward_rf_original_dataset_mega_campaign/007_track1_original_dataset_backward_rf_attempt_07.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-12-35__track1_original_dataset_backward_rf_attempt_07_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-12-35__track1_original_dataset_backward_rf_attempt_07_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-12-35__track1_original_dataset_backward_rf_attempt_07_campaign_validation/validation_summary.yaml`
