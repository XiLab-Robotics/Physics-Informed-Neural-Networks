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
- random seed: `9`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `24.733%`
- winning mean component MAE: `0.072751`
- winning mean component RMSE: `0.140437`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 24.733 | 0.072751 | 0.140437 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 15, 'estimator__min_samples_split': 14, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `GBM` | 0.003644 | 0.004311 | 112.515 |
| `fft_y_Bw_filtered_ampl_1` | `GBM` | 0.000027 | 0.000043 | 0.160 |
| `fft_y_Bw_filtered_phase_1` | `GBM` | 0.001853 | 0.003044 | 39.204 |
| `fft_y_Bw_filtered_ampl_3` | `GBM` | 0.000022 | 0.000030 | 2.366 |
| `fft_y_Bw_filtered_phase_3` | `GBM` | 0.033525 | 0.040833 | 2.493 |
| `fft_y_Bw_filtered_ampl_39` | `GBM` | 0.000022 | 0.000030 | 4.550 |
| `fft_y_Bw_filtered_phase_39` | `GBM` | 0.446783 | 0.909080 | 16.035 |
| `fft_y_Bw_filtered_ampl_40` | `GBM` | 0.000026 | 0.000038 | 8.683 |
| `fft_y_Bw_filtered_phase_40` | `GBM` | 0.108859 | 0.189944 | 23.911 |
| `fft_y_Bw_filtered_ampl_78` | `GBM` | 0.000095 | 0.000119 | 35.577 |
| `fft_y_Bw_filtered_phase_78` | `GBM` | 0.076360 | 0.235961 | 36.884 |
| `fft_y_Bw_filtered_ampl_81` | `GBM` | 0.000011 | 0.000015 | 7.776 |
| `fft_y_Bw_filtered_phase_81` | `GBM` | 0.101856 | 0.136086 | 43.791 |
| `fft_y_Bw_filtered_ampl_156` | `GBM` | 0.000385 | 0.001281 | 35.649 |
| `fft_y_Bw_filtered_phase_156` | `GBM` | 0.139312 | 0.287710 | 12.196 |
| `fft_y_Bw_filtered_ampl_162` | `GBM` | 0.000228 | 0.000614 | 51.173 |
| `fft_y_Bw_filtered_phase_162` | `GBM` | 0.148777 | 0.197558 | 7.914 |
| `fft_y_Bw_filtered_ampl_240` | `GBM` | 0.000124 | 0.000399 | 12.555 |
| `fft_y_Bw_filtered_phase_240` | `GBM` | 0.320350 | 0.661202 | 16.488 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/gbm/2026-04-26_track1_backward_gbm_original_dataset_mega_campaign/004_track1_original_dataset_backward_gbm_attempt_04.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-43-36__track1_original_dataset_backward_gbm_attempt_04_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-43-36__track1_original_dataset_backward_gbm_attempt_04_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-43-36__track1_original_dataset_backward_gbm_attempt_04_campaign_validation/validation_summary.yaml`
