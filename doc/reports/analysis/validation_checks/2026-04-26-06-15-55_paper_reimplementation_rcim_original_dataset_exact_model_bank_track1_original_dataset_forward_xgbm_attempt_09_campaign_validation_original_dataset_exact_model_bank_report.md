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
- random seed: `19`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `45.036%`
- winning mean component MAE: `0.107841`
- winning mean component RMSE: `0.183384`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 45.036 | 0.107841 | 0.183384 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `XGBM` | 0.002630 | 0.004221 | 17.224 |
| `fft_y_Fw_filtered_ampl_1` | `XGBM` | 0.000047 | 0.000062 | 0.273 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.001782 | 0.002496 | 94.123 |
| `fft_y_Fw_filtered_ampl_3` | `XGBM` | 0.000082 | 0.000101 | 10.941 |
| `fft_y_Fw_filtered_phase_3` | `XGBM` | 0.023876 | 0.031940 | 1.316 |
| `fft_y_Fw_filtered_ampl_39` | `XGBM` | 0.000088 | 0.000115 | 8.134 |
| `fft_y_Fw_filtered_phase_39` | `XGBM` | 0.022019 | 0.033033 | 1.826 |
| `fft_y_Fw_filtered_ampl_40` | `XGBM` | 0.000062 | 0.000075 | 7.679 |
| `fft_y_Fw_filtered_phase_40` | `XGBM` | 0.052533 | 0.083528 | 90.879 |
| `fft_y_Fw_filtered_ampl_78` | `XGBM` | 0.000119 | 0.000154 | 44.096 |
| `fft_y_Fw_filtered_phase_78` | `XGBM` | 0.093200 | 0.135906 | 243.410 |
| `fft_y_Fw_filtered_ampl_81` | `XGBM` | 0.000056 | 0.000070 | 19.687 |
| `fft_y_Fw_filtered_phase_81` | `XGBM` | 0.083204 | 0.110345 | 7.005 |
| `fft_y_Fw_filtered_ampl_156` | `XGBM` | 0.000221 | 0.000601 | 76.881 |
| `fft_y_Fw_filtered_phase_156` | `XGBM` | 0.877331 | 1.326454 | 40.715 |
| `fft_y_Fw_filtered_ampl_162` | `XGBM` | 0.000359 | 0.001095 | 42.689 |
| `fft_y_Fw_filtered_phase_162` | `XGBM` | 0.461520 | 0.769127 | 23.292 |
| `fft_y_Fw_filtered_ampl_240` | `XGBM` | 0.000163 | 0.000278 | 96.156 |
| `fft_y_Fw_filtered_phase_240` | `XGBM` | 0.429693 | 0.984700 | 29.359 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/xgbm/2026-04-26_track1_forward_xgbm_original_dataset_mega_campaign/009_track1_original_dataset_forward_xgbm_attempt_09.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-15-04__track1_original_dataset_forward_xgbm_attempt_09_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-15-04__track1_original_dataset_forward_xgbm_attempt_09_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-15-04__track1_original_dataset_forward_xgbm_attempt_09_campaign_validation/validation_summary.yaml`
