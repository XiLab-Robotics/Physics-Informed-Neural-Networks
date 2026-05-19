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
- random seed: `7`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `45.020%`
- winning mean component MAE: `0.108963`
- winning mean component RMSE: `0.174495`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 45.020 | 0.108963 | 0.174495 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 18}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `XGBM` | 0.002415 | 0.002827 | 4.789 |
| `fft_y_Fw_filtered_ampl_1` | `XGBM` | 0.000047 | 0.000061 | 0.276 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.001922 | 0.002536 | 23.330 |
| `fft_y_Fw_filtered_ampl_3` | `XGBM` | 0.000079 | 0.000102 | 10.008 |
| `fft_y_Fw_filtered_phase_3` | `XGBM` | 0.025525 | 0.033628 | 1.427 |
| `fft_y_Fw_filtered_ampl_39` | `XGBM` | 0.000101 | 0.000129 | 9.399 |
| `fft_y_Fw_filtered_phase_39` | `XGBM` | 0.027885 | 0.037470 | 2.521 |
| `fft_y_Fw_filtered_ampl_40` | `XGBM` | 0.000068 | 0.000086 | 8.661 |
| `fft_y_Fw_filtered_phase_40` | `XGBM` | 0.053611 | 0.070170 | 81.917 |
| `fft_y_Fw_filtered_ampl_78` | `XGBM` | 0.000106 | 0.000153 | 42.745 |
| `fft_y_Fw_filtered_phase_78` | `XGBM` | 0.112976 | 0.230672 | 293.306 |
| `fft_y_Fw_filtered_ampl_81` | `XGBM` | 0.000047 | 0.000058 | 16.086 |
| `fft_y_Fw_filtered_phase_81` | `XGBM` | 0.079584 | 0.105223 | 10.605 |
| `fft_y_Fw_filtered_ampl_156` | `XGBM` | 0.000268 | 0.000815 | 94.551 |
| `fft_y_Fw_filtered_phase_156` | `XGBM` | 0.852695 | 1.243031 | 79.721 |
| `fft_y_Fw_filtered_ampl_162` | `XGBM` | 0.000257 | 0.000976 | 37.139 |
| `fft_y_Fw_filtered_phase_162` | `XGBM` | 0.590273 | 1.047272 | 25.396 |
| `fft_y_Fw_filtered_ampl_240` | `XGBM` | 0.000165 | 0.000272 | 64.901 |
| `fft_y_Fw_filtered_phase_240` | `XGBM` | 0.322277 | 0.539918 | 48.597 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/xgbm/2026-04-26_track1_forward_xgbm_original_dataset_mega_campaign/003_track1_original_dataset_forward_xgbm_attempt_03.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-08-50__track1_original_dataset_forward_xgbm_attempt_03_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-08-50__track1_original_dataset_forward_xgbm_attempt_03_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-08-50__track1_original_dataset_forward_xgbm_attempt_03_campaign_validation/validation_summary.yaml`
