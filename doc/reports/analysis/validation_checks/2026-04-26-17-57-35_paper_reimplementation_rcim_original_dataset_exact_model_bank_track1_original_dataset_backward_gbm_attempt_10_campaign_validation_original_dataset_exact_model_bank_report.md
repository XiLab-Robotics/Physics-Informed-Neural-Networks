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
- random seed: `21`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `30.576%`
- winning mean component MAE: `0.073315`
- winning mean component RMSE: `0.145613`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 30.576 | 0.073315 | 0.145613 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 15, 'estimator__min_samples_split': 18, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `GBM` | 0.003826 | 0.004422 | 95.533 |
| `fft_y_Bw_filtered_ampl_1` | `GBM` | 0.000025 | 0.000033 | 0.148 |
| `fft_y_Bw_filtered_phase_1` | `GBM` | 0.001708 | 0.002319 | 137.817 |
| `fft_y_Bw_filtered_ampl_3` | `GBM` | 0.000027 | 0.000037 | 2.729 |
| `fft_y_Bw_filtered_phase_3` | `GBM` | 0.032038 | 0.040849 | 2.363 |
| `fft_y_Bw_filtered_ampl_39` | `GBM` | 0.000023 | 0.000030 | 5.143 |
| `fft_y_Bw_filtered_phase_39` | `GBM` | 0.470906 | 1.077512 | 17.109 |
| `fft_y_Bw_filtered_ampl_40` | `GBM` | 0.000030 | 0.000045 | 10.612 |
| `fft_y_Bw_filtered_phase_40` | `GBM` | 0.102176 | 0.148657 | 46.636 |
| `fft_y_Bw_filtered_ampl_78` | `GBM` | 0.000098 | 0.000119 | 15.162 |
| `fft_y_Bw_filtered_phase_78` | `GBM` | 0.065918 | 0.121232 | 25.604 |
| `fft_y_Bw_filtered_ampl_81` | `GBM` | 0.000011 | 0.000018 | 9.105 |
| `fft_y_Bw_filtered_phase_81` | `GBM` | 0.112013 | 0.150409 | 39.197 |
| `fft_y_Bw_filtered_ampl_156` | `GBM` | 0.000434 | 0.001377 | 35.697 |
| `fft_y_Bw_filtered_phase_156` | `GBM` | 0.229784 | 0.590780 | 34.762 |
| `fft_y_Bw_filtered_ampl_162` | `GBM` | 0.000223 | 0.000477 | 50.908 |
| `fft_y_Bw_filtered_phase_162` | `GBM` | 0.155135 | 0.229207 | 8.278 |
| `fft_y_Bw_filtered_ampl_240` | `GBM` | 0.000135 | 0.000359 | 24.938 |
| `fft_y_Bw_filtered_phase_240` | `GBM` | 0.218469 | 0.398768 | 19.194 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/gbm/2026-04-26_track1_backward_gbm_original_dataset_mega_campaign/010_track1_original_dataset_backward_gbm_attempt_10.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-55-42__track1_original_dataset_backward_gbm_attempt_10_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-55-42__track1_original_dataset_backward_gbm_attempt_10_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-55-42__track1_original_dataset_backward_gbm_attempt_10_campaign_validation/validation_summary.yaml`
