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
- random seed: `53`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `43.113%`
- winning mean component MAE: `0.090107`
- winning mean component RMSE: `0.173568`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 43.113 | 0.090107 | 0.173568 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `XGBM` | 0.002732 | 0.003623 | 41.615 |
| `fft_y_Bw_filtered_ampl_1` | `XGBM` | 0.000085 | 0.000139 | 0.493 |
| `fft_y_Bw_filtered_phase_1` | `XGBM` | 0.002459 | 0.003328 | 37.932 |
| `fft_y_Bw_filtered_ampl_3` | `XGBM` | 0.000098 | 0.000128 | 10.400 |
| `fft_y_Bw_filtered_phase_3` | `XGBM` | 0.021238 | 0.052930 | 1.609 |
| `fft_y_Bw_filtered_ampl_39` | `XGBM` | 0.000094 | 0.000112 | 21.153 |
| `fft_y_Bw_filtered_phase_39` | `XGBM` | 0.340390 | 0.780478 | 13.814 |
| `fft_y_Bw_filtered_ampl_40` | `XGBM` | 0.000047 | 0.000061 | 15.199 |
| `fft_y_Bw_filtered_phase_40` | `XGBM` | 0.189143 | 0.275108 | 258.709 |
| `fft_y_Bw_filtered_ampl_78` | `XGBM` | 0.000145 | 0.000189 | 52.370 |
| `fft_y_Bw_filtered_phase_78` | `XGBM` | 0.100076 | 0.189730 | 39.374 |
| `fft_y_Bw_filtered_ampl_81` | `XGBM` | 0.000028 | 0.000035 | 23.687 |
| `fft_y_Bw_filtered_phase_81` | `XGBM` | 0.116530 | 0.195569 | 106.059 |
| `fft_y_Bw_filtered_ampl_156` | `XGBM` | 0.000476 | 0.001318 | 41.573 |
| `fft_y_Bw_filtered_phase_156` | `XGBM` | 0.164556 | 0.261869 | 22.431 |
| `fft_y_Bw_filtered_ampl_162` | `XGBM` | 0.000191 | 0.000426 | 27.397 |
| `fft_y_Bw_filtered_phase_162` | `XGBM` | 0.226754 | 0.571525 | 12.283 |
| `fft_y_Bw_filtered_ampl_240` | `XGBM` | 0.000194 | 0.000292 | 63.044 |
| `fft_y_Bw_filtered_phase_240` | `XGBM` | 0.546804 | 0.960930 | 30.010 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/xgbm/2026-04-26_track1_backward_xgbm_original_dataset_mega_campaign/018_track1_original_dataset_backward_xgbm_attempt_18.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-05-51__track1_original_dataset_backward_xgbm_attempt_18_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-05-51__track1_original_dataset_backward_xgbm_attempt_18_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-05-51__track1_original_dataset_backward_xgbm_attempt_18_campaign_validation/validation_summary.yaml`
