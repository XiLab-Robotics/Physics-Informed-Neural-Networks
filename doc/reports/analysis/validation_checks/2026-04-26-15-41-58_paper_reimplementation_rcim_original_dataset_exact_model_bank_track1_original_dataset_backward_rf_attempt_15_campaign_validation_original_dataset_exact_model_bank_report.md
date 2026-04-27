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
- random seed: `37`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `41.368%`
- winning mean component MAE: `0.050046`
- winning mean component RMSE: `0.130352`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 41.368 | 0.050046 | 0.130352 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 13, 'estimator__min_samples_split': 6, 'estimator__n_estimators': 60}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `RF` | 0.002837 | 0.003457 | 36.658 |
| `fft_y_Bw_filtered_ampl_1` | `RF` | 0.000025 | 0.000035 | 0.145 |
| `fft_y_Bw_filtered_phase_1` | `RF` | 0.001636 | 0.002327 | 146.312 |
| `fft_y_Bw_filtered_ampl_3` | `RF` | 0.000021 | 0.000032 | 2.230 |
| `fft_y_Bw_filtered_phase_3` | `RF` | 0.022076 | 0.027153 | 1.619 |
| `fft_y_Bw_filtered_ampl_39` | `RF` | 0.000015 | 0.000021 | 3.336 |
| `fft_y_Bw_filtered_phase_39` | `RF` | 0.193824 | 0.637609 | 6.792 |
| `fft_y_Bw_filtered_ampl_40` | `RF` | 0.000026 | 0.000040 | 9.238 |
| `fft_y_Bw_filtered_phase_40` | `RF` | 0.093839 | 0.142135 | 107.115 |
| `fft_y_Bw_filtered_ampl_78` | `RF` | 0.000056 | 0.000077 | 9.680 |
| `fft_y_Bw_filtered_phase_78` | `RF` | 0.075938 | 0.169300 | 26.990 |
| `fft_y_Bw_filtered_ampl_81` | `RF` | 0.000009 | 0.000014 | 7.664 |
| `fft_y_Bw_filtered_phase_81` | `RF` | 0.078829 | 0.103825 | 366.465 |
| `fft_y_Bw_filtered_ampl_156` | `RF` | 0.000200 | 0.000794 | 8.663 |
| `fft_y_Bw_filtered_phase_156` | `RF` | 0.100604 | 0.359952 | 15.415 |
| `fft_y_Bw_filtered_ampl_162` | `RF` | 0.000070 | 0.000213 | 7.389 |
| `fft_y_Bw_filtered_phase_162` | `RF` | 0.106651 | 0.355673 | 5.228 |
| `fft_y_Bw_filtered_ampl_240` | `RF` | 0.000088 | 0.000212 | 12.214 |
| `fft_y_Bw_filtered_phase_240` | `RF` | 0.274134 | 0.673827 | 12.841 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/rf/2026-04-26_track1_backward_rf_original_dataset_mega_campaign/015_track1_original_dataset_backward_rf_attempt_15.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-38-50__track1_original_dataset_backward_rf_attempt_15_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-38-50__track1_original_dataset_backward_rf_attempt_15_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-38-50__track1_original_dataset_backward_rf_attempt_15_campaign_validation/validation_summary.yaml`
