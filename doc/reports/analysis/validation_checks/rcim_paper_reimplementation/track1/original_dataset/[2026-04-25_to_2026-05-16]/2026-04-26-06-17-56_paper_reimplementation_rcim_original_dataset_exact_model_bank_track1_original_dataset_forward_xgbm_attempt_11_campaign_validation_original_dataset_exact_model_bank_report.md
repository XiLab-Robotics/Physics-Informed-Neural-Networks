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
- random seed: `23`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `34.576%`
- winning mean component MAE: `0.115834`
- winning mean component RMSE: `0.193700`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 34.576 | 0.115834 | 0.193700 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 16}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `XGBM` | 0.002595 | 0.002963 | 5.234 |
| `fft_y_Fw_filtered_ampl_1` | `XGBM` | 0.000058 | 0.000075 | 0.338 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.001820 | 0.002450 | 26.735 |
| `fft_y_Fw_filtered_ampl_3` | `XGBM` | 0.000084 | 0.000104 | 10.823 |
| `fft_y_Fw_filtered_phase_3` | `XGBM` | 0.023400 | 0.030867 | 1.288 |
| `fft_y_Fw_filtered_ampl_39` | `XGBM` | 0.000101 | 0.000130 | 9.256 |
| `fft_y_Fw_filtered_phase_39` | `XGBM` | 0.025363 | 0.039656 | 2.206 |
| `fft_y_Fw_filtered_ampl_40` | `XGBM` | 0.000075 | 0.000101 | 10.528 |
| `fft_y_Fw_filtered_phase_40` | `XGBM` | 0.052740 | 0.074893 | 104.744 |
| `fft_y_Fw_filtered_ampl_78` | `XGBM` | 0.000123 | 0.000162 | 30.701 |
| `fft_y_Fw_filtered_phase_78` | `XGBM` | 0.130452 | 0.183996 | 111.448 |
| `fft_y_Fw_filtered_ampl_81` | `XGBM` | 0.000050 | 0.000063 | 15.899 |
| `fft_y_Fw_filtered_phase_81` | `XGBM` | 0.070750 | 0.104225 | 7.493 |
| `fft_y_Fw_filtered_ampl_156` | `XGBM` | 0.000220 | 0.000559 | 118.958 |
| `fft_y_Fw_filtered_phase_156` | `XGBM` | 0.961028 | 1.518571 | 44.211 |
| `fft_y_Fw_filtered_ampl_162` | `XGBM` | 0.000151 | 0.000286 | 42.290 |
| `fft_y_Fw_filtered_phase_162` | `XGBM` | 0.601682 | 1.044191 | 26.368 |
| `fft_y_Fw_filtered_ampl_240` | `XGBM` | 0.000147 | 0.000233 | 53.980 |
| `fft_y_Fw_filtered_phase_240` | `XGBM` | 0.330009 | 0.676785 | 34.435 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/xgbm/2026-04-26_track1_forward_xgbm_original_dataset_mega_campaign/011_track1_original_dataset_forward_xgbm_attempt_11.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-17-05__track1_original_dataset_forward_xgbm_attempt_11_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-17-05__track1_original_dataset_forward_xgbm_attempt_11_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-17-05__track1_original_dataset_forward_xgbm_attempt_11_campaign_validation/validation_summary.yaml`
