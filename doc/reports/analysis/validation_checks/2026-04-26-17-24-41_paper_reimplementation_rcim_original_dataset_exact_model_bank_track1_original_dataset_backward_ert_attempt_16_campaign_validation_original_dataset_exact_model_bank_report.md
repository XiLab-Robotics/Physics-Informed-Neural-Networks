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
- random seed: `42`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `15.251%`
- winning mean component MAE: `0.038971`
- winning mean component RMSE: `0.096757`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 15.251 | 0.038971 | 0.096757 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ERT` | 0.002994 | 0.003630 | 36.812 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000023 | 0.000031 | 0.131 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001516 | 0.001986 | 44.052 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000024 | 0.000036 | 2.295 |
| `fft_y_Bw_filtered_phase_3` | `ERT` | 0.024482 | 0.031334 | 1.883 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000021 | 0.000033 | 4.557 |
| `fft_y_Bw_filtered_phase_39` | `ERT` | 0.194416 | 0.573174 | 6.759 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000030 | 0.000042 | 9.720 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.089096 | 0.157626 | 52.912 |
| `fft_y_Bw_filtered_ampl_78` | `ERT` | 0.000035 | 0.000047 | 4.675 |
| `fft_y_Bw_filtered_phase_78` | `ERT` | 0.072840 | 0.191143 | 41.856 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000009 | 0.000016 | 7.133 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.077338 | 0.107468 | 40.058 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000071 | 0.000288 | 5.487 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.072247 | 0.232333 | 6.463 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000032 | 0.000089 | 5.547 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.057301 | 0.117245 | 3.016 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000068 | 0.000177 | 8.870 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.147901 | 0.421678 | 7.544 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/ert/2026-04-26_track1_backward_ert_original_dataset_mega_campaign/016_track1_original_dataset_backward_ert_attempt_16.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-21-42__track1_original_dataset_backward_ert_attempt_16_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-21-42__track1_original_dataset_backward_ert_attempt_16_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-21-42__track1_original_dataset_backward_ert_attempt_16_campaign_validation/validation_summary.yaml`
