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

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `58.622%`
- winning mean component MAE: `0.124975`
- winning mean component RMSE: `0.205900`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 58.622 | 0.124975 | 0.205900 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `XGBM` | 0.002822 | 0.004775 | 19.185 |
| `fft_y_Fw_filtered_ampl_1` | `XGBM` | 0.000056 | 0.000068 | 0.328 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.001901 | 0.002669 | 20.404 |
| `fft_y_Fw_filtered_ampl_3` | `XGBM` | 0.000086 | 0.000103 | 11.391 |
| `fft_y_Fw_filtered_phase_3` | `XGBM` | 0.025338 | 0.032190 | 1.414 |
| `fft_y_Fw_filtered_ampl_39` | `XGBM` | 0.000127 | 0.000155 | 11.927 |
| `fft_y_Fw_filtered_phase_39` | `XGBM` | 0.027279 | 0.036866 | 2.256 |
| `fft_y_Fw_filtered_ampl_40` | `XGBM` | 0.000075 | 0.000095 | 9.959 |
| `fft_y_Fw_filtered_phase_40` | `XGBM` | 0.062287 | 0.091909 | 233.238 |
| `fft_y_Fw_filtered_ampl_78` | `XGBM` | 0.000116 | 0.000152 | 34.678 |
| `fft_y_Fw_filtered_phase_78` | `XGBM` | 0.146997 | 0.226306 | 369.196 |
| `fft_y_Fw_filtered_ampl_81` | `XGBM` | 0.000044 | 0.000057 | 13.974 |
| `fft_y_Fw_filtered_phase_81` | `XGBM` | 0.080349 | 0.103980 | 7.261 |
| `fft_y_Fw_filtered_ampl_156` | `XGBM` | 0.000266 | 0.000695 | 76.617 |
| `fft_y_Fw_filtered_phase_156` | `XGBM` | 0.899384 | 1.396718 | 50.318 |
| `fft_y_Fw_filtered_ampl_162` | `XGBM` | 0.000151 | 0.000316 | 41.649 |
| `fft_y_Fw_filtered_phase_162` | `XGBM` | 0.671067 | 1.056417 | 28.543 |
| `fft_y_Fw_filtered_ampl_240` | `XGBM` | 0.000200 | 0.000355 | 147.361 |
| `fft_y_Fw_filtered_phase_240` | `XGBM` | 0.455981 | 0.958274 | 34.124 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/xgbm/2026-04-26_track1_forward_xgbm_original_dataset_mega_campaign/013_track1_original_dataset_forward_xgbm_attempt_13.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-19-05__track1_original_dataset_forward_xgbm_attempt_13_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-19-05__track1_original_dataset_forward_xgbm_attempt_13_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-19-05__track1_original_dataset_forward_xgbm_attempt_13_campaign_validation/validation_summary.yaml`
