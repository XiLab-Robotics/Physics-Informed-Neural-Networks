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
- random seed: `21`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `18.977%`
- winning mean component MAE: `0.067115`
- winning mean component RMSE: `0.200866`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 18.977 | 0.067115 | 0.200866 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.003395 | 0.005119 | 7.308 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000037 | 0.000050 | 0.217 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.002123 | 0.002965 | 37.516 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000024 | 0.000034 | 2.885 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.026610 | 0.034403 | 1.460 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000036 | 0.000048 | 3.074 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.027186 | 0.044900 | 2.191 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000030 | 0.000046 | 3.753 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.037542 | 0.051638 | 126.643 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000050 | 0.000077 | 9.060 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.100250 | 0.237218 | 74.339 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000011 | 0.000015 | 3.611 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.064257 | 0.096161 | 5.449 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000080 | 0.000293 | 13.127 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.453810 | 1.234224 | 23.756 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000056 | 0.000153 | 8.605 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.291907 | 1.056598 | 10.897 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000040 | 0.000057 | 9.848 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.267738 | 1.052449 | 16.827 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/dt/2026-04-26_track1_forward_dt_original_dataset_mega_campaign/010_track1_original_dataset_forward_dt_attempt_10.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-18-27__track1_original_dataset_forward_dt_attempt_10_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-18-27__track1_original_dataset_forward_dt_attempt_10_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-18-27__track1_original_dataset_forward_dt_attempt_10_campaign_validation/validation_summary.yaml`
