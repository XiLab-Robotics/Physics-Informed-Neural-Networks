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
- random seed: `59`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `62.695%`
- winning mean component MAE: `0.125140`
- winning mean component RMSE: `0.209817`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 62.695 | 0.125140 | 0.209817 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `XGBM` | 0.002634 | 0.003127 | 5.676 |
| `fft_y_Fw_filtered_ampl_1` | `XGBM` | 0.000050 | 0.000063 | 0.293 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.002496 | 0.003628 | 44.496 |
| `fft_y_Fw_filtered_ampl_3` | `XGBM` | 0.000086 | 0.000107 | 11.030 |
| `fft_y_Fw_filtered_phase_3` | `XGBM` | 0.022169 | 0.031020 | 1.227 |
| `fft_y_Fw_filtered_ampl_39` | `XGBM` | 0.000121 | 0.000150 | 11.178 |
| `fft_y_Fw_filtered_phase_39` | `XGBM` | 0.030010 | 0.042043 | 2.622 |
| `fft_y_Fw_filtered_ampl_40` | `XGBM` | 0.000065 | 0.000085 | 8.436 |
| `fft_y_Fw_filtered_phase_40` | `XGBM` | 0.061100 | 0.088725 | 190.626 |
| `fft_y_Fw_filtered_ampl_78` | `XGBM` | 0.000130 | 0.000172 | 32.223 |
| `fft_y_Fw_filtered_phase_78` | `XGBM` | 0.146864 | 0.271156 | 153.240 |
| `fft_y_Fw_filtered_ampl_81` | `XGBM` | 0.000051 | 0.000068 | 16.552 |
| `fft_y_Fw_filtered_phase_81` | `XGBM` | 0.094930 | 0.131000 | 7.926 |
| `fft_y_Fw_filtered_ampl_156` | `XGBM` | 0.000181 | 0.000381 | 104.468 |
| `fft_y_Fw_filtered_phase_156` | `XGBM` | 0.936730 | 1.357602 | 64.229 |
| `fft_y_Fw_filtered_ampl_162` | `XGBM` | 0.000146 | 0.000330 | 37.509 |
| `fft_y_Fw_filtered_phase_162` | `XGBM` | 0.658441 | 1.210375 | 29.506 |
| `fft_y_Fw_filtered_ampl_240` | `XGBM` | 0.000140 | 0.000202 | 77.793 |
| `fft_y_Fw_filtered_phase_240` | `XGBM` | 0.421306 | 0.846289 | 392.176 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/xgbm/2026-04-26_track1_forward_xgbm_original_dataset_mega_campaign/019_track1_original_dataset_forward_xgbm_attempt_19.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-25-07__track1_original_dataset_forward_xgbm_attempt_19_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-25-07__track1_original_dataset_forward_xgbm_attempt_19_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-25-07__track1_original_dataset_forward_xgbm_attempt_19_campaign_validation/validation_summary.yaml`
