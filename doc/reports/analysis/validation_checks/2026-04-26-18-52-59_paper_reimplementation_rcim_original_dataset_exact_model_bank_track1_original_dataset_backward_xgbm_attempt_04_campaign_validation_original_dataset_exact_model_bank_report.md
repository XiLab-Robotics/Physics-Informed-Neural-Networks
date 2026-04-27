# Original-Dataset Exact RCIM Model Bank Validation Report

## Overview

This report covers the direction-specific exact-model-bank branch trained from the repository dataset under `data/datasets`.

- direction label: `backward`
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
- random seed: `9`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `46.203%`
- winning mean component MAE: `0.080436`
- winning mean component RMSE: `0.144590`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 46.203 | 0.080436 | 0.144590 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `XGBM` | 0.002742 | 0.003183 | 67.009 |
| `fft_y_Bw_filtered_ampl_1` | `XGBM` | 0.000076 | 0.000133 | 0.442 |
| `fft_y_Bw_filtered_phase_1` | `XGBM` | 0.001860 | 0.002667 | 39.295 |
| `fft_y_Bw_filtered_ampl_3` | `XGBM` | 0.000074 | 0.000097 | 7.812 |
| `fft_y_Bw_filtered_phase_3` | `XGBM` | 0.021509 | 0.031030 | 1.616 |
| `fft_y_Bw_filtered_ampl_39` | `XGBM` | 0.000099 | 0.000118 | 21.156 |
| `fft_y_Bw_filtered_phase_39` | `XGBM` | 0.378506 | 0.819344 | 13.839 |
| `fft_y_Bw_filtered_ampl_40` | `XGBM` | 0.000044 | 0.000057 | 14.742 |
| `fft_y_Bw_filtered_phase_40` | `XGBM` | 0.152223 | 0.233423 | 37.931 |
| `fft_y_Bw_filtered_ampl_78` | `XGBM` | 0.000153 | 0.000208 | 74.124 |
| `fft_y_Bw_filtered_phase_78` | `XGBM` | 0.107601 | 0.246328 | 37.312 |
| `fft_y_Bw_filtered_ampl_81` | `XGBM` | 0.000026 | 0.000037 | 20.102 |
| `fft_y_Bw_filtered_phase_81` | `XGBM` | 0.112841 | 0.153086 | 387.255 |
| `fft_y_Bw_filtered_ampl_156` | `XGBM` | 0.000472 | 0.001507 | 44.828 |
| `fft_y_Bw_filtered_phase_156` | `XGBM` | 0.174863 | 0.254559 | 17.264 |
| `fft_y_Bw_filtered_ampl_162` | `XGBM` | 0.000280 | 0.000877 | 30.633 |
| `fft_y_Bw_filtered_phase_162` | `XGBM` | 0.162995 | 0.334736 | 10.919 |
| `fft_y_Bw_filtered_ampl_240` | `XGBM` | 0.000314 | 0.000931 | 33.009 |
| `fft_y_Bw_filtered_phase_240` | `XGBM` | 0.411611 | 0.664877 | 18.561 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/xgbm/2026-04-26_track1_backward_xgbm_original_dataset_mega_campaign/004_track1_original_dataset_backward_xgbm_attempt_04.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-52-10__track1_original_dataset_backward_xgbm_attempt_04_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-52-10__track1_original_dataset_backward_xgbm_attempt_04_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-52-10__track1_original_dataset_backward_xgbm_attempt_04_campaign_validation/validation_summary.yaml`
