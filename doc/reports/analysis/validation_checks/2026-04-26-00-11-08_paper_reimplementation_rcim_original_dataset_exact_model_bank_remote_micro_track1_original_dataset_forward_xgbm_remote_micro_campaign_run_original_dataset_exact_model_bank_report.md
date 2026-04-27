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
- random seed: `42`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `43.865%`
- winning mean component MAE: `0.111053`
- winning mean component RMSE: `0.176498`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 43.865 | 0.111053 | 0.176498 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 16}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `XGBM` | 0.002705 | 0.003139 | 5.135 |
| `fft_y_Fw_filtered_ampl_1` | `XGBM` | 0.000053 | 0.000068 | 0.308 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.001739 | 0.002332 | 82.369 |
| `fft_y_Fw_filtered_ampl_3` | `XGBM` | 0.000079 | 0.000102 | 9.577 |
| `fft_y_Fw_filtered_phase_3` | `XGBM` | 0.024055 | 0.029909 | 1.313 |
| `fft_y_Fw_filtered_ampl_39` | `XGBM` | 0.000104 | 0.000133 | 9.228 |
| `fft_y_Fw_filtered_phase_39` | `XGBM` | 0.025449 | 0.033270 | 2.232 |
| `fft_y_Fw_filtered_ampl_40` | `XGBM` | 0.000074 | 0.000095 | 10.124 |
| `fft_y_Fw_filtered_phase_40` | `XGBM` | 0.057958 | 0.085672 | 61.682 |
| `fft_y_Fw_filtered_ampl_78` | `XGBM` | 0.000126 | 0.000165 | 38.702 |
| `fft_y_Fw_filtered_phase_78` | `XGBM` | 0.138967 | 0.213293 | 165.079 |
| `fft_y_Fw_filtered_ampl_81` | `XGBM` | 0.000051 | 0.000065 | 16.331 |
| `fft_y_Fw_filtered_phase_81` | `XGBM` | 0.084212 | 0.114260 | 7.541 |
| `fft_y_Fw_filtered_ampl_156` | `XGBM` | 0.000202 | 0.000551 | 61.218 |
| `fft_y_Fw_filtered_phase_156` | `XGBM` | 0.795924 | 1.102416 | 35.639 |
| `fft_y_Fw_filtered_ampl_162` | `XGBM` | 0.000191 | 0.000546 | 39.764 |
| `fft_y_Fw_filtered_phase_162` | `XGBM` | 0.568587 | 1.029563 | 23.604 |
| `fft_y_Fw_filtered_ampl_240` | `XGBM` | 0.000136 | 0.000218 | 40.306 |
| `fft_y_Fw_filtered_phase_240` | `XGBM` | 0.409404 | 0.737660 | 223.293 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/forward_remote_micro/xgbm/2026-04-25_track1_forward_xgbm_remote_micro/001_track1_original_dataset_forward_xgbm_remote_micro.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_micro/2026-04-26-00-10-19__track1_original_dataset_forward_xgbm_remote_micro_campaign_run`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_micro/2026-04-26-00-10-19__track1_original_dataset_forward_xgbm_remote_micro_campaign_run/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_micro/2026-04-26-00-10-19__track1_original_dataset_forward_xgbm_remote_micro_campaign_run/validation_summary.yaml`
