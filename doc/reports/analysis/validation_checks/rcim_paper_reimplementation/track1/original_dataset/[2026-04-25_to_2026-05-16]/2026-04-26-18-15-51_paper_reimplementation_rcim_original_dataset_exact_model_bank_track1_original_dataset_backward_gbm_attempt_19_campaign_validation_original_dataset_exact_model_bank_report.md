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
- random seed: `59`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `26.048%`
- winning mean component MAE: `0.067280`
- winning mean component RMSE: `0.121498`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 26.048 | 0.067280 | 0.121498 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 15, 'estimator__min_samples_split': 16, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `GBM` | 0.003419 | 0.004175 | 106.929 |
| `fft_y_Bw_filtered_ampl_1` | `GBM` | 0.000029 | 0.000041 | 0.167 |
| `fft_y_Bw_filtered_phase_1` | `GBM` | 0.002038 | 0.003383 | 96.453 |
| `fft_y_Bw_filtered_ampl_3` | `GBM` | 0.000028 | 0.000045 | 2.821 |
| `fft_y_Bw_filtered_phase_3` | `GBM` | 0.033207 | 0.040122 | 2.441 |
| `fft_y_Bw_filtered_ampl_39` | `GBM` | 0.000020 | 0.000028 | 4.463 |
| `fft_y_Bw_filtered_phase_39` | `GBM` | 0.460345 | 0.885685 | 16.780 |
| `fft_y_Bw_filtered_ampl_40` | `GBM` | 0.000029 | 0.000041 | 9.571 |
| `fft_y_Bw_filtered_phase_40` | `GBM` | 0.093650 | 0.127594 | 31.783 |
| `fft_y_Bw_filtered_ampl_78` | `GBM` | 0.000088 | 0.000115 | 15.159 |
| `fft_y_Bw_filtered_phase_78` | `GBM` | 0.071995 | 0.125585 | 16.786 |
| `fft_y_Bw_filtered_ampl_81` | `GBM` | 0.000013 | 0.000017 | 10.244 |
| `fft_y_Bw_filtered_phase_81` | `GBM` | 0.100773 | 0.130299 | 39.091 |
| `fft_y_Bw_filtered_ampl_156` | `GBM` | 0.000198 | 0.000374 | 32.509 |
| `fft_y_Bw_filtered_phase_156` | `GBM` | 0.121584 | 0.222965 | 22.940 |
| `fft_y_Bw_filtered_ampl_162` | `GBM` | 0.000135 | 0.000173 | 52.297 |
| `fft_y_Bw_filtered_phase_162` | `GBM` | 0.168497 | 0.270721 | 8.950 |
| `fft_y_Bw_filtered_ampl_240` | `GBM` | 0.000089 | 0.000189 | 14.845 |
| `fft_y_Bw_filtered_phase_240` | `GBM` | 0.222177 | 0.496912 | 10.672 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/gbm/2026-04-26_track1_backward_gbm_original_dataset_mega_campaign/019_track1_original_dataset_backward_gbm_attempt_19.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-13-55__track1_original_dataset_backward_gbm_attempt_19_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-13-55__track1_original_dataset_backward_gbm_attempt_19_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-13-55__track1_original_dataset_backward_gbm_attempt_19_campaign_validation/validation_summary.yaml`
