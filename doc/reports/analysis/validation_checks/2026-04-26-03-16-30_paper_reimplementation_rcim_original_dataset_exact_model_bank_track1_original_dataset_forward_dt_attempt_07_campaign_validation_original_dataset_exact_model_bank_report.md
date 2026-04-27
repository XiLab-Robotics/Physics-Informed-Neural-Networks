# Original-Dataset Exact RCIM Model Bank Validation Report

## Overview

This report covers the direction-specific exact-model-bank branch trained from the repository dataset under `data/datasets`.

- direction label: `forward`
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
- random seed: `15`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `16.928%`
- winning mean component MAE: `0.074316`
- winning mean component RMSE: `0.194978`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 16.928 | 0.074316 | 0.194978 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 17, 'estimator__min_samples_split': 5}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.003708 | 0.005001 | 17.772 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000033 | 0.000045 | 0.192 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.002372 | 0.003632 | 35.676 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000025 | 0.000033 | 3.169 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.032188 | 0.041555 | 1.793 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000039 | 0.000051 | 3.443 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.033186 | 0.059422 | 2.593 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000032 | 0.000053 | 4.325 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.049348 | 0.076805 | 78.086 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000047 | 0.000069 | 16.138 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.122957 | 0.434345 | 47.525 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000012 | 0.000018 | 3.888 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.069181 | 0.093480 | 7.569 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000053 | 0.000147 | 16.542 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.499272 | 1.217507 | 35.465 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000047 | 0.000128 | 8.814 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.341251 | 0.967025 | 14.194 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000036 | 0.000061 | 12.403 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.258224 | 0.805208 | 12.038 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/dt/2026-04-26_track1_forward_dt_original_dataset_mega_campaign/007_track1_original_dataset_forward_dt_attempt_07.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-15-42__track1_original_dataset_forward_dt_attempt_07_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-15-42__track1_original_dataset_forward_dt_attempt_07_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-15-42__track1_original_dataset_forward_dt_attempt_07_campaign_validation/validation_summary.yaml`
