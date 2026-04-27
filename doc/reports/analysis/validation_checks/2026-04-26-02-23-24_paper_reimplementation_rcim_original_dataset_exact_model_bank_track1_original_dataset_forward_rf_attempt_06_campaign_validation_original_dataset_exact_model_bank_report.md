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
- random seed: `13`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `18.708%`
- winning mean component MAE: `0.059381`
- winning mean component RMSE: `0.132668`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 18.708 | 0.059381 | 0.132668 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 12, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 70}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `RF` | 0.002741 | 0.003499 | 5.570 |
| `fft_y_Fw_filtered_ampl_1` | `RF` | 0.000024 | 0.000033 | 0.138 |
| `fft_y_Fw_filtered_phase_1` | `RF` | 0.002372 | 0.003007 | 87.557 |
| `fft_y_Fw_filtered_ampl_3` | `RF` | 0.000021 | 0.000032 | 2.554 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.018244 | 0.027354 | 1.017 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000030 | 0.000041 | 2.653 |
| `fft_y_Fw_filtered_phase_39` | `RF` | 0.023712 | 0.032766 | 2.049 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | 0.000025 | 0.000035 | 3.107 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.034237 | 0.048349 | 65.037 |
| `fft_y_Fw_filtered_ampl_78` | `RF` | 0.000042 | 0.000062 | 8.388 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.056076 | 0.104662 | 45.782 |
| `fft_y_Fw_filtered_ampl_81` | `RF` | 0.000011 | 0.000015 | 3.496 |
| `fft_y_Fw_filtered_phase_81` | `RF` | 0.053025 | 0.084273 | 6.282 |
| `fft_y_Fw_filtered_ampl_156` | `RF` | 0.000063 | 0.000207 | 15.991 |
| `fft_y_Fw_filtered_phase_156` | `RF` | 0.607398 | 1.283765 | 25.354 |
| `fft_y_Fw_filtered_ampl_162` | `RF` | 0.000088 | 0.000254 | 10.128 |
| `fft_y_Fw_filtered_phase_162` | `RF` | 0.131089 | 0.438288 | 5.464 |
| `fft_y_Fw_filtered_ampl_240` | `RF` | 0.000040 | 0.000063 | 13.857 |
| `fft_y_Fw_filtered_phase_240` | `RF` | 0.199006 | 0.493982 | 51.024 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/rf/2026-04-26_track1_forward_rf_original_dataset_mega_campaign/006_track1_original_dataset_forward_rf_attempt_06.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-20-08__track1_original_dataset_forward_rf_attempt_06_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-20-08__track1_original_dataset_forward_rf_attempt_06_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-20-08__track1_original_dataset_forward_rf_attempt_06_campaign_validation/validation_summary.yaml`
