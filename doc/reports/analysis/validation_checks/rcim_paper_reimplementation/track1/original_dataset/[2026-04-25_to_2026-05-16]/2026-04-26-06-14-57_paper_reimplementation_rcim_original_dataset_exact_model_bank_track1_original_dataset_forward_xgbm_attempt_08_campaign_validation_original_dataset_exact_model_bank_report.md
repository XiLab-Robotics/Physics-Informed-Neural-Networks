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
- random seed: `17`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `46.092%`
- winning mean component MAE: `0.092549`
- winning mean component RMSE: `0.151072`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 46.092 | 0.092549 | 0.151072 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 16}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `XGBM` | 0.002605 | 0.003100 | 4.933 |
| `fft_y_Fw_filtered_ampl_1` | `XGBM` | 0.000056 | 0.000071 | 0.327 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.002017 | 0.002469 | 38.561 |
| `fft_y_Fw_filtered_ampl_3` | `XGBM` | 0.000083 | 0.000104 | 10.232 |
| `fft_y_Fw_filtered_phase_3` | `XGBM` | 0.022578 | 0.028086 | 1.235 |
| `fft_y_Fw_filtered_ampl_39` | `XGBM` | 0.000105 | 0.000135 | 9.231 |
| `fft_y_Fw_filtered_phase_39` | `XGBM` | 0.023660 | 0.032582 | 2.163 |
| `fft_y_Fw_filtered_ampl_40` | `XGBM` | 0.000059 | 0.000074 | 7.530 |
| `fft_y_Fw_filtered_phase_40` | `XGBM` | 0.056039 | 0.082111 | 118.588 |
| `fft_y_Fw_filtered_ampl_78` | `XGBM` | 0.000138 | 0.000187 | 50.143 |
| `fft_y_Fw_filtered_phase_78` | `XGBM` | 0.102487 | 0.138522 | 354.511 |
| `fft_y_Fw_filtered_ampl_81` | `XGBM` | 0.000050 | 0.000065 | 16.635 |
| `fft_y_Fw_filtered_phase_81` | `XGBM` | 0.068846 | 0.100681 | 5.814 |
| `fft_y_Fw_filtered_ampl_156` | `XGBM` | 0.000231 | 0.000463 | 80.921 |
| `fft_y_Fw_filtered_phase_156` | `XGBM` | 0.752872 | 1.204783 | 36.735 |
| `fft_y_Fw_filtered_ampl_162` | `XGBM` | 0.000268 | 0.000827 | 42.401 |
| `fft_y_Fw_filtered_phase_162` | `XGBM` | 0.420670 | 0.704201 | 20.832 |
| `fft_y_Fw_filtered_ampl_240` | `XGBM` | 0.000178 | 0.000293 | 53.926 |
| `fft_y_Fw_filtered_phase_240` | `XGBM` | 0.305486 | 0.571620 | 21.023 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/xgbm/2026-04-26_track1_forward_xgbm_original_dataset_mega_campaign/008_track1_original_dataset_forward_xgbm_attempt_08.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-14-01__track1_original_dataset_forward_xgbm_attempt_08_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-14-01__track1_original_dataset_forward_xgbm_attempt_08_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-14-01__track1_original_dataset_forward_xgbm_attempt_08_campaign_validation/validation_summary.yaml`
