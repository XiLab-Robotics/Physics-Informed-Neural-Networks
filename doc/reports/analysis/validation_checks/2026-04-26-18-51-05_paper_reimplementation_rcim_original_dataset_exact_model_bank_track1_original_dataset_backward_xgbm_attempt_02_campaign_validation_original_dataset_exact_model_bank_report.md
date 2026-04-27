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
- random seed: `5`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `33.289%`
- winning mean component MAE: `0.097754`
- winning mean component RMSE: `0.181795`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 33.289 | 0.097754 | 0.181795 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `XGBM` | 0.002604 | 0.003685 | 40.308 |
| `fft_y_Bw_filtered_ampl_1` | `XGBM` | 0.000082 | 0.000130 | 0.475 |
| `fft_y_Bw_filtered_phase_1` | `XGBM` | 0.002443 | 0.003504 | 89.603 |
| `fft_y_Bw_filtered_ampl_3` | `XGBM` | 0.000096 | 0.000131 | 9.107 |
| `fft_y_Bw_filtered_phase_3` | `XGBM` | 0.023398 | 0.042488 | 1.846 |
| `fft_y_Bw_filtered_ampl_39` | `XGBM` | 0.000096 | 0.000116 | 20.378 |
| `fft_y_Bw_filtered_phase_39` | `XGBM` | 0.343201 | 0.706754 | 12.762 |
| `fft_y_Bw_filtered_ampl_40` | `XGBM` | 0.000044 | 0.000058 | 15.312 |
| `fft_y_Bw_filtered_phase_40` | `XGBM` | 0.173171 | 0.247338 | 115.284 |
| `fft_y_Bw_filtered_ampl_78` | `XGBM` | 0.000162 | 0.000209 | 38.998 |
| `fft_y_Bw_filtered_phase_78` | `XGBM` | 0.112170 | 0.218037 | 32.719 |
| `fft_y_Bw_filtered_ampl_81` | `XGBM` | 0.000029 | 0.000038 | 23.728 |
| `fft_y_Bw_filtered_phase_81` | `XGBM` | 0.098212 | 0.126937 | 30.184 |
| `fft_y_Bw_filtered_ampl_156` | `XGBM` | 0.000409 | 0.001176 | 47.322 |
| `fft_y_Bw_filtered_phase_156` | `XGBM` | 0.255213 | 0.671747 | 37.331 |
| `fft_y_Bw_filtered_ampl_162` | `XGBM` | 0.000244 | 0.000536 | 37.776 |
| `fft_y_Bw_filtered_phase_162` | `XGBM` | 0.208124 | 0.471848 | 10.758 |
| `fft_y_Bw_filtered_ampl_240` | `XGBM` | 0.000200 | 0.000362 | 37.810 |
| `fft_y_Bw_filtered_phase_240` | `XGBM` | 0.637425 | 0.959016 | 30.793 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/xgbm/2026-04-26_track1_backward_xgbm_original_dataset_mega_campaign/002_track1_original_dataset_backward_xgbm_attempt_02.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-50-17__track1_original_dataset_backward_xgbm_attempt_02_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-50-17__track1_original_dataset_backward_xgbm_attempt_02_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-50-17__track1_original_dataset_backward_xgbm_attempt_02_campaign_validation/validation_summary.yaml`
