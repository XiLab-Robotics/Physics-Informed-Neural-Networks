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
- random seed: `47`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `42.787%`
- winning mean component MAE: `0.120700`
- winning mean component RMSE: `0.195391`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 42.787 | 0.120700 | 0.195391 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 16}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `XGBM` | 0.002865 | 0.004385 | 18.017 |
| `fft_y_Fw_filtered_ampl_1` | `XGBM` | 0.000053 | 0.000066 | 0.307 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.002152 | 0.003047 | 58.045 |
| `fft_y_Fw_filtered_ampl_3` | `XGBM` | 0.000091 | 0.000111 | 11.665 |
| `fft_y_Fw_filtered_phase_3` | `XGBM` | 0.025311 | 0.034793 | 1.411 |
| `fft_y_Fw_filtered_ampl_39` | `XGBM` | 0.000126 | 0.000156 | 11.976 |
| `fft_y_Fw_filtered_phase_39` | `XGBM` | 0.027424 | 0.039436 | 2.233 |
| `fft_y_Fw_filtered_ampl_40` | `XGBM` | 0.000065 | 0.000085 | 8.740 |
| `fft_y_Fw_filtered_phase_40` | `XGBM` | 0.057791 | 0.093991 | 194.375 |
| `fft_y_Fw_filtered_ampl_78` | `XGBM` | 0.000117 | 0.000158 | 23.775 |
| `fft_y_Fw_filtered_phase_78` | `XGBM` | 0.126589 | 0.208346 | 76.946 |
| `fft_y_Fw_filtered_ampl_81` | `XGBM` | 0.000045 | 0.000057 | 14.808 |
| `fft_y_Fw_filtered_phase_81` | `XGBM` | 0.080886 | 0.116123 | 8.152 |
| `fft_y_Fw_filtered_ampl_156` | `XGBM` | 0.000233 | 0.000707 | 68.290 |
| `fft_y_Fw_filtered_phase_156` | `XGBM` | 0.961576 | 1.493121 | 88.234 |
| `fft_y_Fw_filtered_ampl_162` | `XGBM` | 0.000222 | 0.000636 | 34.319 |
| `fft_y_Fw_filtered_phase_162` | `XGBM` | 0.526815 | 0.864783 | 25.569 |
| `fft_y_Fw_filtered_ampl_240` | `XGBM` | 0.000173 | 0.000314 | 108.161 |
| `fft_y_Fw_filtered_phase_240` | `XGBM` | 0.480769 | 0.852105 | 57.926 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/xgbm/2026-04-26_track1_forward_xgbm_original_dataset_mega_campaign/017_track1_original_dataset_forward_xgbm_attempt_17.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-23-07__track1_original_dataset_forward_xgbm_attempt_17_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-23-07__track1_original_dataset_forward_xgbm_attempt_17_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-23-07__track1_original_dataset_forward_xgbm_attempt_17_campaign_validation/validation_summary.yaml`
