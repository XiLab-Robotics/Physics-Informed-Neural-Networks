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
- random seed: `0`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `48.045%`
- winning mean component MAE: `0.112455`
- winning mean component RMSE: `0.180153`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 48.045 | 0.112455 | 0.180153 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 16}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `XGBM` | 0.002560 | 0.002985 | 5.176 |
| `fft_y_Fw_filtered_ampl_1` | `XGBM` | 0.000059 | 0.000075 | 0.342 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.002104 | 0.002921 | 36.885 |
| `fft_y_Fw_filtered_ampl_3` | `XGBM` | 0.000070 | 0.000091 | 9.373 |
| `fft_y_Fw_filtered_phase_3` | `XGBM` | 0.020632 | 0.025911 | 1.132 |
| `fft_y_Fw_filtered_ampl_39` | `XGBM` | 0.000105 | 0.000131 | 10.044 |
| `fft_y_Fw_filtered_phase_39` | `XGBM` | 0.028339 | 0.041815 | 2.339 |
| `fft_y_Fw_filtered_ampl_40` | `XGBM` | 0.000065 | 0.000089 | 8.779 |
| `fft_y_Fw_filtered_phase_40` | `XGBM` | 0.062137 | 0.088541 | 83.487 |
| `fft_y_Fw_filtered_ampl_78` | `XGBM` | 0.000101 | 0.000140 | 72.798 |
| `fft_y_Fw_filtered_phase_78` | `XGBM` | 0.112860 | 0.154616 | 327.283 |
| `fft_y_Fw_filtered_ampl_81` | `XGBM` | 0.000048 | 0.000060 | 16.446 |
| `fft_y_Fw_filtered_phase_81` | `XGBM` | 0.080118 | 0.109452 | 6.909 |
| `fft_y_Fw_filtered_ampl_156` | `XGBM` | 0.000191 | 0.000410 | 91.798 |
| `fft_y_Fw_filtered_phase_156` | `XGBM` | 0.915424 | 1.337047 | 92.334 |
| `fft_y_Fw_filtered_ampl_162` | `XGBM` | 0.000216 | 0.000565 | 36.190 |
| `fft_y_Fw_filtered_phase_162` | `XGBM` | 0.471526 | 0.817108 | 22.527 |
| `fft_y_Fw_filtered_ampl_240` | `XGBM` | 0.000173 | 0.000308 | 64.443 |
| `fft_y_Fw_filtered_phase_240` | `XGBM` | 0.439922 | 0.840649 | 24.568 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/xgbm/2026-04-26_track1_forward_xgbm_original_dataset_mega_campaign/001_track1_original_dataset_forward_xgbm_attempt_01.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-06-48__track1_original_dataset_forward_xgbm_attempt_01_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-06-48__track1_original_dataset_forward_xgbm_attempt_01_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-06-48__track1_original_dataset_forward_xgbm_attempt_01_campaign_validation/validation_summary.yaml`
