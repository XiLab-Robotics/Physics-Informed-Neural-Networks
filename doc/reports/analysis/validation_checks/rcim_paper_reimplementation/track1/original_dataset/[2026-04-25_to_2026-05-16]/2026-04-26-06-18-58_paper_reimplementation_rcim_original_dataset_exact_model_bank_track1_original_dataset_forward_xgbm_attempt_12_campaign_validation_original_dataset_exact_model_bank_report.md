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
- random seed: `27`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `54.111%`
- winning mean component MAE: `0.101862`
- winning mean component RMSE: `0.169244`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 54.111 | 0.101862 | 0.169244 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 18}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `XGBM` | 0.002531 | 0.003021 | 4.982 |
| `fft_y_Fw_filtered_ampl_1` | `XGBM` | 0.000057 | 0.000070 | 0.330 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.002167 | 0.002999 | 25.170 |
| `fft_y_Fw_filtered_ampl_3` | `XGBM` | 0.000090 | 0.000110 | 11.016 |
| `fft_y_Fw_filtered_phase_3` | `XGBM` | 0.022304 | 0.028306 | 1.213 |
| `fft_y_Fw_filtered_ampl_39` | `XGBM` | 0.000128 | 0.000152 | 11.337 |
| `fft_y_Fw_filtered_phase_39` | `XGBM` | 0.026316 | 0.032692 | 2.369 |
| `fft_y_Fw_filtered_ampl_40` | `XGBM` | 0.000068 | 0.000091 | 9.268 |
| `fft_y_Fw_filtered_phase_40` | `XGBM` | 0.057559 | 0.075923 | 128.824 |
| `fft_y_Fw_filtered_ampl_78` | `XGBM` | 0.000134 | 0.000172 | 22.395 |
| `fft_y_Fw_filtered_phase_78` | `XGBM` | 0.096644 | 0.137617 | 463.858 |
| `fft_y_Fw_filtered_ampl_81` | `XGBM` | 0.000050 | 0.000061 | 16.276 |
| `fft_y_Fw_filtered_phase_81` | `XGBM` | 0.079541 | 0.108690 | 7.531 |
| `fft_y_Fw_filtered_ampl_156` | `XGBM` | 0.000275 | 0.000584 | 97.812 |
| `fft_y_Fw_filtered_phase_156` | `XGBM` | 0.863430 | 1.362399 | 44.316 |
| `fft_y_Fw_filtered_ampl_162` | `XGBM` | 0.000130 | 0.000197 | 37.289 |
| `fft_y_Fw_filtered_phase_162` | `XGBM` | 0.458336 | 0.879230 | 23.547 |
| `fft_y_Fw_filtered_ampl_240` | `XGBM` | 0.000179 | 0.000291 | 59.984 |
| `fft_y_Fw_filtered_phase_240` | `XGBM` | 0.325444 | 0.583038 | 60.593 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/xgbm/2026-04-26_track1_forward_xgbm_original_dataset_mega_campaign/012_track1_original_dataset_forward_xgbm_attempt_12.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-18-03__track1_original_dataset_forward_xgbm_attempt_12_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-18-03__track1_original_dataset_forward_xgbm_attempt_12_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-18-03__track1_original_dataset_forward_xgbm_attempt_12_campaign_validation/validation_summary.yaml`
