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
- random seed: `11`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `23.895%`
- winning mean component MAE: `0.051988`
- winning mean component RMSE: `0.130992`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 23.895 | 0.051988 | 0.130992 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 5, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ERT` | 0.003234 | 0.004072 | 81.917 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000024 | 0.000032 | 0.143 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001646 | 0.002299 | 73.773 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000024 | 0.000038 | 2.370 |
| `fft_y_Bw_filtered_phase_3` | `ERT` | 0.028494 | 0.049065 | 2.137 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000017 | 0.000024 | 3.937 |
| `fft_y_Bw_filtered_phase_39` | `ERT` | 0.287637 | 0.918139 | 9.926 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000031 | 0.000048 | 10.180 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.079973 | 0.109594 | 94.633 |
| `fft_y_Bw_filtered_ampl_78` | `ERT` | 0.000046 | 0.000062 | 5.210 |
| `fft_y_Bw_filtered_phase_78` | `ERT` | 0.050377 | 0.137876 | 17.254 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000009 | 0.000015 | 6.911 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.090202 | 0.131475 | 88.451 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000095 | 0.000316 | 8.550 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.147054 | 0.405838 | 9.254 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000068 | 0.000246 | 7.861 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.081370 | 0.181190 | 5.303 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000086 | 0.000153 | 14.328 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.217378 | 0.548371 | 11.861 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/ert/2026-04-26_track1_backward_ert_original_dataset_mega_campaign/005_track1_original_dataset_backward_ert_attempt_05.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-46-56__track1_original_dataset_backward_ert_attempt_05_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-46-56__track1_original_dataset_backward_ert_attempt_05_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-46-56__track1_original_dataset_backward_ert_attempt_05_campaign_validation/validation_summary.yaml`
