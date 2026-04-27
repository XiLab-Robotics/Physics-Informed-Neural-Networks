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

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `23.122%`
- winning mean component MAE: `0.055646`
- winning mean component RMSE: `0.172945`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 23.122 | 0.055646 | 0.172945 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.003333 | 0.004156 | 67.511 |
| `fft_y_Bw_filtered_ampl_1` | `DT` | 0.000028 | 0.000038 | 0.162 |
| `fft_y_Bw_filtered_phase_1` | `DT` | 0.001813 | 0.002412 | 53.088 |
| `fft_y_Bw_filtered_ampl_3` | `DT` | 0.000030 | 0.000048 | 2.898 |
| `fft_y_Bw_filtered_phase_3` | `DT` | 0.026803 | 0.035718 | 2.052 |
| `fft_y_Bw_filtered_ampl_39` | `DT` | 0.000025 | 0.000037 | 5.338 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.293885 | 1.227407 | 10.233 |
| `fft_y_Bw_filtered_ampl_40` | `DT` | 0.000038 | 0.000056 | 12.894 |
| `fft_y_Bw_filtered_phase_40` | `DT` | 0.100338 | 0.194286 | 33.488 |
| `fft_y_Bw_filtered_ampl_78` | `DT` | 0.000057 | 0.000077 | 8.231 |
| `fft_y_Bw_filtered_phase_78` | `DT` | 0.060647 | 0.124347 | 43.978 |
| `fft_y_Bw_filtered_ampl_81` | `DT` | 0.000010 | 0.000016 | 7.374 |
| `fft_y_Bw_filtered_phase_81` | `DT` | 0.115326 | 0.160242 | 144.719 |
| `fft_y_Bw_filtered_ampl_156` | `DT` | 0.000189 | 0.000948 | 7.200 |
| `fft_y_Bw_filtered_phase_156` | `DT` | 0.083390 | 0.360936 | 7.617 |
| `fft_y_Bw_filtered_ampl_162` | `DT` | 0.000055 | 0.000200 | 6.993 |
| `fft_y_Bw_filtered_phase_162` | `DT` | 0.078138 | 0.206350 | 3.923 |
| `fft_y_Bw_filtered_ampl_240` | `DT` | 0.000081 | 0.000177 | 9.436 |
| `fft_y_Bw_filtered_phase_240` | `DT` | 0.293082 | 0.968505 | 12.185 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/dt/2026-04-26_track1_backward_dt_original_dataset_mega_campaign/016_track1_original_dataset_backward_dt_attempt_16.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-12-09__track1_original_dataset_backward_dt_attempt_16_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-12-09__track1_original_dataset_backward_dt_attempt_16_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-12-09__track1_original_dataset_backward_dt_attempt_16_campaign_validation/validation_summary.yaml`
