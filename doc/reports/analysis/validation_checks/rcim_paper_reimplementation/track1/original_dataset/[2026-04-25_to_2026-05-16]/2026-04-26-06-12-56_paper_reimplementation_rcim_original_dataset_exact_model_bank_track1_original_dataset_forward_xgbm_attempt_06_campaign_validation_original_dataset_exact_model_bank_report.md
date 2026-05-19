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
- random seed: `13`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `46.639%`
- winning mean component MAE: `0.114788`
- winning mean component RMSE: `0.179721`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 46.639 | 0.114788 | 0.179721 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `XGBM` | 0.002693 | 0.003171 | 5.497 |
| `fft_y_Fw_filtered_ampl_1` | `XGBM` | 0.000048 | 0.000061 | 0.277 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.002389 | 0.003292 | 85.827 |
| `fft_y_Fw_filtered_ampl_3` | `XGBM` | 0.000083 | 0.000107 | 10.557 |
| `fft_y_Fw_filtered_phase_3` | `XGBM` | 0.022456 | 0.030457 | 1.253 |
| `fft_y_Fw_filtered_ampl_39` | `XGBM` | 0.000108 | 0.000142 | 10.353 |
| `fft_y_Fw_filtered_phase_39` | `XGBM` | 0.027879 | 0.041229 | 2.560 |
| `fft_y_Fw_filtered_ampl_40` | `XGBM` | 0.000058 | 0.000078 | 7.372 |
| `fft_y_Fw_filtered_phase_40` | `XGBM` | 0.056755 | 0.079560 | 91.934 |
| `fft_y_Fw_filtered_ampl_78` | `XGBM` | 0.000120 | 0.000167 | 47.270 |
| `fft_y_Fw_filtered_phase_78` | `XGBM` | 0.118513 | 0.179518 | 114.740 |
| `fft_y_Fw_filtered_ampl_81` | `XGBM` | 0.000053 | 0.000066 | 17.716 |
| `fft_y_Fw_filtered_phase_81` | `XGBM` | 0.083805 | 0.116230 | 8.864 |
| `fft_y_Fw_filtered_ampl_156` | `XGBM` | 0.000259 | 0.000563 | 89.138 |
| `fft_y_Fw_filtered_phase_156` | `XGBM` | 1.103488 | 1.618391 | 53.775 |
| `fft_y_Fw_filtered_ampl_162` | `XGBM` | 0.000269 | 0.000697 | 36.652 |
| `fft_y_Fw_filtered_phase_162` | `XGBM` | 0.411338 | 0.727396 | 22.394 |
| `fft_y_Fw_filtered_ampl_240` | `XGBM` | 0.000143 | 0.000224 | 61.894 |
| `fft_y_Fw_filtered_phase_240` | `XGBM` | 0.350522 | 0.613353 | 218.067 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/xgbm/2026-04-26_track1_forward_xgbm_original_dataset_mega_campaign/006_track1_original_dataset_forward_xgbm_attempt_06.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-12-04__track1_original_dataset_forward_xgbm_attempt_06_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-12-04__track1_original_dataset_forward_xgbm_attempt_06_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-12-04__track1_original_dataset_forward_xgbm_attempt_06_campaign_validation/validation_summary.yaml`
