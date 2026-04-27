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
- random seed: `17`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `23.258%`
- winning mean component MAE: `0.071438`
- winning mean component RMSE: `0.137220`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 23.258 | 0.071438 | 0.137220 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 17, 'estimator__min_samples_split': 12, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `GBM` | 0.003403 | 0.004042 | 50.564 |
| `fft_y_Bw_filtered_ampl_1` | `GBM` | 0.000024 | 0.000035 | 0.142 |
| `fft_y_Bw_filtered_phase_1` | `GBM` | 0.001834 | 0.002658 | 45.239 |
| `fft_y_Bw_filtered_ampl_3` | `GBM` | 0.000025 | 0.000037 | 2.573 |
| `fft_y_Bw_filtered_phase_3` | `GBM` | 0.035430 | 0.045105 | 2.749 |
| `fft_y_Bw_filtered_ampl_39` | `GBM` | 0.000020 | 0.000033 | 4.149 |
| `fft_y_Bw_filtered_phase_39` | `GBM` | 0.427454 | 0.817242 | 15.441 |
| `fft_y_Bw_filtered_ampl_40` | `GBM` | 0.000030 | 0.000043 | 9.095 |
| `fft_y_Bw_filtered_phase_40` | `GBM` | 0.095503 | 0.134421 | 43.197 |
| `fft_y_Bw_filtered_ampl_78` | `GBM` | 0.000098 | 0.000119 | 17.878 |
| `fft_y_Bw_filtered_phase_78` | `GBM` | 0.062624 | 0.110555 | 39.661 |
| `fft_y_Bw_filtered_ampl_81` | `GBM` | 0.000009 | 0.000014 | 8.475 |
| `fft_y_Bw_filtered_phase_81` | `GBM` | 0.097333 | 0.138129 | 79.607 |
| `fft_y_Bw_filtered_ampl_156` | `GBM` | 0.000209 | 0.000413 | 33.298 |
| `fft_y_Bw_filtered_phase_156` | `GBM` | 0.120926 | 0.197606 | 10.293 |
| `fft_y_Bw_filtered_ampl_162` | `GBM` | 0.000177 | 0.000462 | 40.440 |
| `fft_y_Bw_filtered_phase_162` | `GBM` | 0.158804 | 0.241571 | 8.306 |
| `fft_y_Bw_filtered_ampl_240` | `GBM` | 0.000097 | 0.000234 | 15.150 |
| `fft_y_Bw_filtered_phase_240` | `GBM` | 0.353313 | 0.914459 | 15.648 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/gbm/2026-04-26_track1_backward_gbm_original_dataset_mega_campaign/008_track1_original_dataset_backward_gbm_attempt_08.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-51-39__track1_original_dataset_backward_gbm_attempt_08_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-51-39__track1_original_dataset_backward_gbm_attempt_08_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-51-39__track1_original_dataset_backward_gbm_attempt_08_campaign_validation/validation_summary.yaml`
