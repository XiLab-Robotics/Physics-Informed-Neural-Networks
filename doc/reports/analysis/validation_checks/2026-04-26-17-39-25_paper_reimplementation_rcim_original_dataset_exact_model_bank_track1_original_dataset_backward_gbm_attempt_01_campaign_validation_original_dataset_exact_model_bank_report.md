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

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `29.805%`
- winning mean component MAE: `0.066208`
- winning mean component RMSE: `0.142681`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 29.805 | 0.066208 | 0.142681 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 15, 'estimator__min_samples_split': 10, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `GBM` | 0.003994 | 0.005189 | 207.192 |
| `fft_y_Bw_filtered_ampl_1` | `GBM` | 0.000026 | 0.000037 | 0.153 |
| `fft_y_Bw_filtered_phase_1` | `GBM` | 0.001851 | 0.002455 | 25.902 |
| `fft_y_Bw_filtered_ampl_3` | `GBM` | 0.000024 | 0.000033 | 2.481 |
| `fft_y_Bw_filtered_phase_3` | `GBM` | 0.033020 | 0.040939 | 2.418 |
| `fft_y_Bw_filtered_ampl_39` | `GBM` | 0.000019 | 0.000025 | 4.534 |
| `fft_y_Bw_filtered_phase_39` | `GBM` | 0.433991 | 0.936617 | 15.686 |
| `fft_y_Bw_filtered_ampl_40` | `GBM` | 0.000022 | 0.000029 | 7.294 |
| `fft_y_Bw_filtered_phase_40` | `GBM` | 0.090903 | 0.124739 | 42.193 |
| `fft_y_Bw_filtered_ampl_78` | `GBM` | 0.000073 | 0.000090 | 11.680 |
| `fft_y_Bw_filtered_phase_78` | `GBM` | 0.050181 | 0.090315 | 53.131 |
| `fft_y_Bw_filtered_ampl_81` | `GBM` | 0.000010 | 0.000015 | 8.883 |
| `fft_y_Bw_filtered_phase_81` | `GBM` | 0.095489 | 0.130809 | 42.680 |
| `fft_y_Bw_filtered_ampl_156` | `GBM` | 0.000273 | 0.000842 | 33.503 |
| `fft_y_Bw_filtered_phase_156` | `GBM` | 0.148575 | 0.476309 | 23.867 |
| `fft_y_Bw_filtered_ampl_162` | `GBM` | 0.000191 | 0.000631 | 39.999 |
| `fft_y_Bw_filtered_phase_162` | `GBM` | 0.139263 | 0.207539 | 7.330 |
| `fft_y_Bw_filtered_ampl_240` | `GBM` | 0.000138 | 0.000397 | 19.352 |
| `fft_y_Bw_filtered_phase_240` | `GBM` | 0.259900 | 0.693931 | 18.026 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/gbm/2026-04-26_track1_backward_gbm_original_dataset_mega_campaign/001_track1_original_dataset_backward_gbm_attempt_01.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-37-30__track1_original_dataset_backward_gbm_attempt_01_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-37-30__track1_original_dataset_backward_gbm_attempt_01_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-37-30__track1_original_dataset_backward_gbm_attempt_01_campaign_validation/validation_summary.yaml`
