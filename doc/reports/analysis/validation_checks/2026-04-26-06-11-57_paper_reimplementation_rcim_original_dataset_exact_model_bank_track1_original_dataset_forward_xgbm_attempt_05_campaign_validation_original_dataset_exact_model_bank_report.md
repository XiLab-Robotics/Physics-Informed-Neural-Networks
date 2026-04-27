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
- random seed: `11`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `55.514%`
- winning mean component MAE: `0.119240`
- winning mean component RMSE: `0.204374`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 55.514 | 0.119240 | 0.204374 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `XGBM` | 0.002579 | 0.003059 | 4.910 |
| `fft_y_Fw_filtered_ampl_1` | `XGBM` | 0.000056 | 0.000071 | 0.326 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.001967 | 0.002882 | 29.861 |
| `fft_y_Fw_filtered_ampl_3` | `XGBM` | 0.000080 | 0.000100 | 10.300 |
| `fft_y_Fw_filtered_phase_3` | `XGBM` | 0.019993 | 0.030880 | 1.115 |
| `fft_y_Fw_filtered_ampl_39` | `XGBM` | 0.000111 | 0.000139 | 10.331 |
| `fft_y_Fw_filtered_phase_39` | `XGBM` | 0.025709 | 0.040210 | 2.066 |
| `fft_y_Fw_filtered_ampl_40` | `XGBM` | 0.000066 | 0.000080 | 8.025 |
| `fft_y_Fw_filtered_phase_40` | `XGBM` | 0.054269 | 0.077277 | 125.984 |
| `fft_y_Fw_filtered_ampl_78` | `XGBM` | 0.000132 | 0.000174 | 70.991 |
| `fft_y_Fw_filtered_phase_78` | `XGBM` | 0.130868 | 0.343141 | 503.417 |
| `fft_y_Fw_filtered_ampl_81` | `XGBM` | 0.000047 | 0.000059 | 15.818 |
| `fft_y_Fw_filtered_phase_81` | `XGBM` | 0.078014 | 0.109083 | 8.100 |
| `fft_y_Fw_filtered_ampl_156` | `XGBM` | 0.000240 | 0.000536 | 69.394 |
| `fft_y_Fw_filtered_phase_156` | `XGBM` | 1.041571 | 1.564815 | 51.148 |
| `fft_y_Fw_filtered_ampl_162` | `XGBM` | 0.000278 | 0.001008 | 39.650 |
| `fft_y_Fw_filtered_phase_162` | `XGBM` | 0.508847 | 0.896283 | 24.671 |
| `fft_y_Fw_filtered_ampl_240` | `XGBM` | 0.000166 | 0.000282 | 51.569 |
| `fft_y_Fw_filtered_phase_240` | `XGBM` | 0.400562 | 0.813020 | 27.084 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/xgbm/2026-04-26_track1_forward_xgbm_original_dataset_mega_campaign/005_track1_original_dataset_forward_xgbm_attempt_05.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-10-59__track1_original_dataset_forward_xgbm_attempt_05_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-10-59__track1_original_dataset_forward_xgbm_attempt_05_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-10-59__track1_original_dataset_forward_xgbm_attempt_05_campaign_validation/validation_summary.yaml`
