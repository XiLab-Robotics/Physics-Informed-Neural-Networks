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
- random seed: `53`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `100.738%`
- winning mean component MAE: `0.121384`
- winning mean component RMSE: `0.206462`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 100.738 | 0.121384 | 0.206462 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `XGBM` | 0.002778 | 0.004032 | 9.556 |
| `fft_y_Fw_filtered_ampl_1` | `XGBM` | 0.000059 | 0.000078 | 0.345 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.002283 | 0.003304 | 1240.584 |
| `fft_y_Fw_filtered_ampl_3` | `XGBM` | 0.000088 | 0.000107 | 11.468 |
| `fft_y_Fw_filtered_phase_3` | `XGBM` | 0.030313 | 0.063490 | 1.639 |
| `fft_y_Fw_filtered_ampl_39` | `XGBM` | 0.000114 | 0.000137 | 11.280 |
| `fft_y_Fw_filtered_phase_39` | `XGBM` | 0.031226 | 0.053106 | 2.411 |
| `fft_y_Fw_filtered_ampl_40` | `XGBM` | 0.000076 | 0.000104 | 10.359 |
| `fft_y_Fw_filtered_phase_40` | `XGBM` | 0.055370 | 0.084552 | 66.877 |
| `fft_y_Fw_filtered_ampl_78` | `XGBM` | 0.000131 | 0.000174 | 55.708 |
| `fft_y_Fw_filtered_phase_78` | `XGBM` | 0.143584 | 0.228978 | 169.966 |
| `fft_y_Fw_filtered_ampl_81` | `XGBM` | 0.000054 | 0.000066 | 17.411 |
| `fft_y_Fw_filtered_phase_81` | `XGBM` | 0.095957 | 0.139713 | 14.923 |
| `fft_y_Fw_filtered_ampl_156` | `XGBM` | 0.000237 | 0.000559 | 68.419 |
| `fft_y_Fw_filtered_phase_156` | `XGBM` | 0.846526 | 1.334346 | 68.371 |
| `fft_y_Fw_filtered_ampl_162` | `XGBM` | 0.000167 | 0.000412 | 32.781 |
| `fft_y_Fw_filtered_phase_162` | `XGBM` | 0.602802 | 0.991297 | 28.409 |
| `fft_y_Fw_filtered_ampl_240` | `XGBM` | 0.000159 | 0.000261 | 67.224 |
| `fft_y_Fw_filtered_phase_240` | `XGBM` | 0.494368 | 1.018058 | 36.292 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/xgbm/2026-04-26_track1_forward_xgbm_original_dataset_mega_campaign/018_track1_original_dataset_forward_xgbm_attempt_18.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-24-07__track1_original_dataset_forward_xgbm_attempt_18_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-24-07__track1_original_dataset_forward_xgbm_attempt_18_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-24-07__track1_original_dataset_forward_xgbm_attempt_18_campaign_validation/validation_summary.yaml`
