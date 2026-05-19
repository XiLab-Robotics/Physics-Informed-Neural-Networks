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
- random seed: `29`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `24.130%`
- winning mean component MAE: `0.084502`
- winning mean component RMSE: `0.185001`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 24.130 | 0.084502 | 0.185001 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 6, 'estimator__n_estimators': 50}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `RF` | 0.003248 | 0.004981 | 18.346 |
| `fft_y_Fw_filtered_ampl_1` | `RF` | 0.000027 | 0.000036 | 0.156 |
| `fft_y_Fw_filtered_phase_1` | `RF` | 0.001917 | 0.002605 | 21.913 |
| `fft_y_Fw_filtered_ampl_3` | `RF` | 0.000024 | 0.000049 | 2.986 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.026844 | 0.035819 | 1.482 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000033 | 0.000051 | 3.131 |
| `fft_y_Fw_filtered_phase_39` | `RF` | 0.030318 | 0.046061 | 2.441 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | 0.000032 | 0.000052 | 4.110 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.042146 | 0.068079 | 88.631 |
| `fft_y_Fw_filtered_ampl_78` | `RF` | 0.000040 | 0.000056 | 7.376 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.083379 | 0.196844 | 148.545 |
| `fft_y_Fw_filtered_ampl_81` | `RF` | 0.000012 | 0.000018 | 3.760 |
| `fft_y_Fw_filtered_phase_81` | `RF` | 0.063654 | 0.100810 | 7.026 |
| `fft_y_Fw_filtered_ampl_156` | `RF` | 0.000098 | 0.000320 | 12.868 |
| `fft_y_Fw_filtered_phase_156` | `RF` | 0.630325 | 1.180751 | 32.623 |
| `fft_y_Fw_filtered_ampl_162` | `RF` | 0.000075 | 0.000232 | 9.721 |
| `fft_y_Fw_filtered_phase_162` | `RF` | 0.371399 | 1.014907 | 14.572 |
| `fft_y_Fw_filtered_ampl_240` | `RF` | 0.000089 | 0.000258 | 59.919 |
| `fft_y_Fw_filtered_phase_240` | `RF` | 0.351877 | 0.863083 | 18.860 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/rf/2026-04-26_track1_forward_rf_original_dataset_mega_campaign/013_track1_original_dataset_forward_rf_attempt_13.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-43-16__track1_original_dataset_forward_rf_attempt_13_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-43-16__track1_original_dataset_forward_rf_attempt_13_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-43-16__track1_original_dataset_forward_rf_attempt_13_campaign_validation/validation_summary.yaml`
