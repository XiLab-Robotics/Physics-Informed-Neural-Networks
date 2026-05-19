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
- random seed: `53`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `41.417%`
- winning mean component MAE: `0.052275`
- winning mean component RMSE: `0.153481`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 41.417 | 0.052275 | 0.153481 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 6}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.003038 | 0.004223 | 39.713 |
| `fft_y_Bw_filtered_ampl_1` | `DT` | 0.000035 | 0.000053 | 0.204 |
| `fft_y_Bw_filtered_phase_1` | `DT` | 0.002479 | 0.003872 | 45.227 |
| `fft_y_Bw_filtered_ampl_3` | `DT` | 0.000024 | 0.000037 | 2.488 |
| `fft_y_Bw_filtered_phase_3` | `DT` | 0.028187 | 0.050605 | 2.085 |
| `fft_y_Bw_filtered_ampl_39` | `DT` | 0.000021 | 0.000030 | 4.738 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.181365 | 0.892319 | 6.706 |
| `fft_y_Bw_filtered_ampl_40` | `DT` | 0.000032 | 0.000048 | 10.727 |
| `fft_y_Bw_filtered_phase_40` | `DT` | 0.123333 | 0.231554 | 428.937 |
| `fft_y_Bw_filtered_ampl_78` | `DT` | 0.000066 | 0.000090 | 10.581 |
| `fft_y_Bw_filtered_phase_78` | `DT` | 0.110822 | 0.239780 | 47.400 |
| `fft_y_Bw_filtered_ampl_81` | `DT` | 0.000010 | 0.000014 | 8.131 |
| `fft_y_Bw_filtered_phase_81` | `DT` | 0.120373 | 0.206526 | 113.325 |
| `fft_y_Bw_filtered_ampl_156` | `DT` | 0.000192 | 0.000672 | 9.693 |
| `fft_y_Bw_filtered_phase_156` | `DT` | 0.115305 | 0.285585 | 11.877 |
| `fft_y_Bw_filtered_ampl_162` | `DT` | 0.000077 | 0.000202 | 8.223 |
| `fft_y_Bw_filtered_phase_162` | `DT` | 0.119788 | 0.505991 | 6.915 |
| `fft_y_Bw_filtered_ampl_240` | `DT` | 0.000073 | 0.000155 | 17.425 |
| `fft_y_Bw_filtered_phase_240` | `DT` | 0.187999 | 0.494385 | 12.533 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/dt/2026-04-26_track1_backward_dt_original_dataset_mega_campaign/018_track1_original_dataset_backward_dt_attempt_18.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-14-01__track1_original_dataset_backward_dt_attempt_18_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-14-01__track1_original_dataset_backward_dt_attempt_18_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-14-01__track1_original_dataset_backward_dt_attempt_18_campaign_validation/validation_summary.yaml`
