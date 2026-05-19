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
- random seed: `37`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `37.695%`
- winning mean component MAE: `0.049438`
- winning mean component RMSE: `0.158808`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 37.695 | 0.049438 | 0.158808 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 7}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.003144 | 0.003937 | 31.557 |
| `fft_y_Bw_filtered_ampl_1` | `DT` | 0.000031 | 0.000044 | 0.179 |
| `fft_y_Bw_filtered_phase_1` | `DT` | 0.001825 | 0.002840 | 283.032 |
| `fft_y_Bw_filtered_ampl_3` | `DT` | 0.000022 | 0.000036 | 2.318 |
| `fft_y_Bw_filtered_phase_3` | `DT` | 0.025582 | 0.033307 | 1.891 |
| `fft_y_Bw_filtered_ampl_39` | `DT` | 0.000020 | 0.000027 | 4.408 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.174273 | 0.894233 | 6.169 |
| `fft_y_Bw_filtered_ampl_40` | `DT` | 0.000032 | 0.000051 | 11.867 |
| `fft_y_Bw_filtered_phase_40` | `DT` | 0.113037 | 0.172682 | 56.522 |
| `fft_y_Bw_filtered_ampl_78` | `DT` | 0.000067 | 0.000086 | 11.087 |
| `fft_y_Bw_filtered_phase_78` | `DT` | 0.086857 | 0.262175 | 24.552 |
| `fft_y_Bw_filtered_ampl_81` | `DT` | 0.000009 | 0.000013 | 7.512 |
| `fft_y_Bw_filtered_phase_81` | `DT` | 0.089812 | 0.128125 | 218.300 |
| `fft_y_Bw_filtered_ampl_156` | `DT` | 0.000221 | 0.000746 | 8.878 |
| `fft_y_Bw_filtered_phase_156` | `DT` | 0.128396 | 0.633561 | 10.563 |
| `fft_y_Bw_filtered_ampl_162` | `DT` | 0.000056 | 0.000129 | 8.469 |
| `fft_y_Bw_filtered_phase_162` | `DT` | 0.062861 | 0.103915 | 3.532 |
| `fft_y_Bw_filtered_ampl_240` | `DT` | 0.000094 | 0.000217 | 13.381 |
| `fft_y_Bw_filtered_phase_240` | `DT` | 0.252980 | 0.781232 | 11.990 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/dt/2026-04-26_track1_backward_dt_original_dataset_mega_campaign/015_track1_original_dataset_backward_dt_attempt_15.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-11-16__track1_original_dataset_backward_dt_attempt_15_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-11-16__track1_original_dataset_backward_dt_attempt_15_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-11-16__track1_original_dataset_backward_dt_attempt_15_campaign_validation/validation_summary.yaml`
