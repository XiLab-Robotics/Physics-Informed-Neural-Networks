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
- random seed: `27`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `16.410%`
- winning mean component MAE: `0.046857`
- winning mean component RMSE: `0.126513`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 16.410 | 0.046857 | 0.126513 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 17, 'estimator__min_samples_split': 3}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.003197 | 0.004160 | 32.574 |
| `fft_y_Bw_filtered_ampl_1` | `ET` | 0.000031 | 0.000045 | 0.181 |
| `fft_y_Bw_filtered_phase_1` | `ET` | 0.002113 | 0.003058 | 38.958 |
| `fft_y_Bw_filtered_ampl_3` | `ET` | 0.000030 | 0.000046 | 3.035 |
| `fft_y_Bw_filtered_phase_3` | `ET` | 0.024633 | 0.035368 | 1.857 |
| `fft_y_Bw_filtered_ampl_39` | `ET` | 0.000023 | 0.000035 | 5.310 |
| `fft_y_Bw_filtered_phase_39` | `ET` | 0.114611 | 0.617398 | 4.202 |
| `fft_y_Bw_filtered_ampl_40` | `ET` | 0.000036 | 0.000051 | 12.543 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.109841 | 0.191428 | 47.549 |
| `fft_y_Bw_filtered_ampl_78` | `ET` | 0.000063 | 0.000083 | 7.896 |
| `fft_y_Bw_filtered_phase_78` | `ET` | 0.060634 | 0.125443 | 26.670 |
| `fft_y_Bw_filtered_ampl_81` | `ET` | 0.000011 | 0.000016 | 9.249 |
| `fft_y_Bw_filtered_phase_81` | `ET` | 0.126801 | 0.174557 | 42.268 |
| `fft_y_Bw_filtered_ampl_156` | `ET` | 0.000181 | 0.000562 | 7.074 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.065340 | 0.124204 | 6.461 |
| `fft_y_Bw_filtered_ampl_162` | `ET` | 0.000055 | 0.000126 | 7.285 |
| `fft_y_Bw_filtered_phase_162` | `ET` | 0.096183 | 0.209688 | 5.031 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000253 | 0.000935 | 29.024 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.286246 | 0.916538 | 24.616 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/et/2026-04-26_track1_backward_et_original_dataset_mega_campaign/012_track1_original_dataset_backward_et_attempt_12.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-26-26__track1_original_dataset_backward_et_attempt_12_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-26-26__track1_original_dataset_backward_et_attempt_12_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-26-26__track1_original_dataset_backward_et_attempt_12_campaign_validation/validation_summary.yaml`
