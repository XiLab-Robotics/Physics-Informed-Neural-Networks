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
- random seed: `7`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `15.716%`
- winning mean component MAE: `0.050991`
- winning mean component RMSE: `0.145561`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 15.716 | 0.050991 | 0.145561 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.003503 | 0.004857 | 40.746 |
| `fft_y_Bw_filtered_ampl_1` | `DT` | 0.000033 | 0.000046 | 0.192 |
| `fft_y_Bw_filtered_phase_1` | `DT` | 0.001906 | 0.003133 | 39.926 |
| `fft_y_Bw_filtered_ampl_3` | `DT` | 0.000024 | 0.000037 | 2.483 |
| `fft_y_Bw_filtered_phase_3` | `DT` | 0.022322 | 0.031183 | 1.673 |
| `fft_y_Bw_filtered_ampl_39` | `DT` | 0.000020 | 0.000027 | 4.441 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.397275 | 1.438133 | 13.486 |
| `fft_y_Bw_filtered_ampl_40` | `DT` | 0.000032 | 0.000049 | 10.482 |
| `fft_y_Bw_filtered_phase_40` | `DT` | 0.094590 | 0.142264 | 34.452 |
| `fft_y_Bw_filtered_ampl_78` | `DT` | 0.000067 | 0.000093 | 8.304 |
| `fft_y_Bw_filtered_phase_78` | `DT` | 0.061129 | 0.111302 | 16.861 |
| `fft_y_Bw_filtered_ampl_81` | `DT` | 0.000009 | 0.000012 | 7.464 |
| `fft_y_Bw_filtered_phase_81` | `DT` | 0.081680 | 0.111159 | 47.730 |
| `fft_y_Bw_filtered_ampl_156` | `DT` | 0.000173 | 0.000699 | 7.439 |
| `fft_y_Bw_filtered_phase_156` | `DT` | 0.049265 | 0.092573 | 5.088 |
| `fft_y_Bw_filtered_ampl_162` | `DT` | 0.000054 | 0.000135 | 7.002 |
| `fft_y_Bw_filtered_phase_162` | `DT` | 0.051907 | 0.078718 | 2.952 |
| `fft_y_Bw_filtered_ampl_240` | `DT` | 0.000100 | 0.000255 | 13.032 |
| `fft_y_Bw_filtered_phase_240` | `DT` | 0.204743 | 0.750989 | 34.852 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/dt/2026-04-26_track1_backward_dt_original_dataset_mega_campaign/003_track1_original_dataset_backward_dt_attempt_03.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-00-16__track1_original_dataset_backward_dt_attempt_03_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-00-16__track1_original_dataset_backward_dt_attempt_03_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-00-16__track1_original_dataset_backward_dt_attempt_03_campaign_validation/validation_summary.yaml`
