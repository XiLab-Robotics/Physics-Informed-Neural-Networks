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

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `52.493%`
- winning mean component MAE: `0.109144`
- winning mean component RMSE: `0.187126`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 52.493 | 0.109144 | 0.187126 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `XGBM` | 0.002570 | 0.003143 | 5.508 |
| `fft_y_Fw_filtered_ampl_1` | `XGBM` | 0.000055 | 0.000069 | 0.319 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.002188 | 0.003135 | 34.317 |
| `fft_y_Fw_filtered_ampl_3` | `XGBM` | 0.000089 | 0.000110 | 11.228 |
| `fft_y_Fw_filtered_phase_3` | `XGBM` | 0.023125 | 0.028152 | 1.276 |
| `fft_y_Fw_filtered_ampl_39` | `XGBM` | 0.000103 | 0.000130 | 9.736 |
| `fft_y_Fw_filtered_phase_39` | `XGBM` | 0.031999 | 0.049042 | 2.608 |
| `fft_y_Fw_filtered_ampl_40` | `XGBM` | 0.000066 | 0.000086 | 8.805 |
| `fft_y_Fw_filtered_phase_40` | `XGBM` | 0.054358 | 0.079691 | 206.738 |
| `fft_y_Fw_filtered_ampl_78` | `XGBM` | 0.000129 | 0.000171 | 36.302 |
| `fft_y_Fw_filtered_phase_78` | `XGBM` | 0.122787 | 0.189319 | 146.610 |
| `fft_y_Fw_filtered_ampl_81` | `XGBM` | 0.000044 | 0.000054 | 14.927 |
| `fft_y_Fw_filtered_phase_81` | `XGBM` | 0.089862 | 0.133244 | 11.568 |
| `fft_y_Fw_filtered_ampl_156` | `XGBM` | 0.000247 | 0.000536 | 90.247 |
| `fft_y_Fw_filtered_phase_156` | `XGBM` | 0.846765 | 1.328976 | 63.696 |
| `fft_y_Fw_filtered_ampl_162` | `XGBM` | 0.000186 | 0.000393 | 52.488 |
| `fft_y_Fw_filtered_phase_162` | `XGBM` | 0.517524 | 0.817284 | 24.640 |
| `fft_y_Fw_filtered_ampl_240` | `XGBM` | 0.000202 | 0.000360 | 58.193 |
| `fft_y_Fw_filtered_phase_240` | `XGBM` | 0.381436 | 0.921509 | 218.167 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/xgbm/2026-04-26_track1_forward_xgbm_original_dataset_mega_campaign/010_track1_original_dataset_forward_xgbm_attempt_10.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-16-02__track1_original_dataset_forward_xgbm_attempt_10_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-16-02__track1_original_dataset_forward_xgbm_attempt_10_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-16-02__track1_original_dataset_forward_xgbm_attempt_10_campaign_validation/validation_summary.yaml`
