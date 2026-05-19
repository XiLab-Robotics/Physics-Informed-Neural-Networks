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
- random seed: `11`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `31.554%`
- winning mean component MAE: `0.080003`
- winning mean component RMSE: `0.185384`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 31.554 | 0.080003 | 0.185384 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 13, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 50}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `RF` | 0.003337 | 0.004127 | 6.315 |
| `fft_y_Fw_filtered_ampl_1` | `RF` | 0.000030 | 0.000039 | 0.175 |
| `fft_y_Fw_filtered_phase_1` | `RF` | 0.001919 | 0.002583 | 23.760 |
| `fft_y_Fw_filtered_ampl_3` | `RF` | 0.000018 | 0.000025 | 2.145 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.022807 | 0.032381 | 1.258 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000027 | 0.000037 | 2.375 |
| `fft_y_Fw_filtered_phase_39` | `RF` | 0.026524 | 0.049673 | 2.126 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | 0.000027 | 0.000043 | 3.292 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.037725 | 0.059361 | 56.590 |
| `fft_y_Fw_filtered_ampl_78` | `RF` | 0.000042 | 0.000055 | 10.345 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.083163 | 0.346257 | 383.505 |
| `fft_y_Fw_filtered_ampl_81` | `RF` | 0.000012 | 0.000016 | 3.853 |
| `fft_y_Fw_filtered_phase_81` | `RF` | 0.054378 | 0.078263 | 5.372 |
| `fft_y_Fw_filtered_ampl_156` | `RF` | 0.000060 | 0.000190 | 9.956 |
| `fft_y_Fw_filtered_phase_156` | `RF` | 0.732434 | 1.434392 | 36.772 |
| `fft_y_Fw_filtered_ampl_162` | `RF` | 0.000114 | 0.000362 | 14.739 |
| `fft_y_Fw_filtered_phase_162` | `RF` | 0.293981 | 0.801642 | 12.929 |
| `fft_y_Fw_filtered_ampl_240` | `RF` | 0.000049 | 0.000106 | 10.640 |
| `fft_y_Fw_filtered_phase_240` | `RF` | 0.263416 | 0.712751 | 13.380 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/rf/2026-04-26_track1_forward_rf_original_dataset_mega_campaign/005_track1_original_dataset_forward_rf_attempt_05.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-16-49__track1_original_dataset_forward_rf_attempt_05_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-16-49__track1_original_dataset_forward_rf_attempt_05_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-16-49__track1_original_dataset_forward_rf_attempt_05_campaign_validation/validation_summary.yaml`
