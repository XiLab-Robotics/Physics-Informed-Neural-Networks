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
- random seed: `0`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `19.139%`
- winning mean component MAE: `0.062617`
- winning mean component RMSE: `0.155831`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 19.139 | 0.062617 | 0.155831 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 12, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 50}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `RF` | 0.003244 | 0.003859 | 6.511 |
| `fft_y_Fw_filtered_ampl_1` | `RF` | 0.000031 | 0.000039 | 0.178 |
| `fft_y_Fw_filtered_phase_1` | `RF` | 0.002073 | 0.002938 | 54.137 |
| `fft_y_Fw_filtered_ampl_3` | `RF` | 0.000018 | 0.000024 | 2.274 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.019595 | 0.025996 | 1.075 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000025 | 0.000034 | 2.179 |
| `fft_y_Fw_filtered_phase_39` | `RF` | 0.025236 | 0.046199 | 2.013 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | 0.000023 | 0.000031 | 2.942 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.034028 | 0.051576 | 55.749 |
| `fft_y_Fw_filtered_ampl_78` | `RF` | 0.000037 | 0.000052 | 13.964 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.046562 | 0.086445 | 107.814 |
| `fft_y_Fw_filtered_ampl_81` | `RF` | 0.000011 | 0.000016 | 3.638 |
| `fft_y_Fw_filtered_phase_81` | `RF` | 0.047973 | 0.069032 | 4.159 |
| `fft_y_Fw_filtered_ampl_156` | `RF` | 0.000086 | 0.000257 | 19.059 |
| `fft_y_Fw_filtered_phase_156` | `RF` | 0.523777 | 1.109221 | 48.748 |
| `fft_y_Fw_filtered_ampl_162` | `RF` | 0.000066 | 0.000253 | 7.678 |
| `fft_y_Fw_filtered_phase_162` | `RF` | 0.202071 | 0.689873 | 8.375 |
| `fft_y_Fw_filtered_ampl_240` | `RF` | 0.000038 | 0.000069 | 9.277 |
| `fft_y_Fw_filtered_phase_240` | `RF` | 0.284830 | 0.874869 | 13.865 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/rf/2026-04-26_track1_forward_rf_original_dataset_mega_campaign/001_track1_original_dataset_forward_rf_attempt_01.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-03-39__track1_original_dataset_forward_rf_attempt_01_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-03-39__track1_original_dataset_forward_rf_attempt_01_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-03-39__track1_original_dataset_forward_rf_attempt_01_campaign_validation/validation_summary.yaml`
