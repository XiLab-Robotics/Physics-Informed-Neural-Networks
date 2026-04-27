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
- random seed: `15`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `82.032%`
- winning mean component MAE: `0.185621`
- winning mean component RMSE: `0.254225`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 82.032 | 0.185621 | 0.254225 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.01, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `XGBM` | 0.009683 | 0.011980 | 39.881 |
| `fft_y_Fw_filtered_ampl_1` | `XGBM` | 0.000050 | 0.000066 | 0.292 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.003321 | 0.004985 | 62.393 |
| `fft_y_Fw_filtered_ampl_3` | `XGBM` | 0.000087 | 0.000109 | 11.902 |
| `fft_y_Fw_filtered_phase_3` | `XGBM` | 0.069677 | 0.087471 | 3.950 |
| `fft_y_Fw_filtered_ampl_39` | `XGBM` | 0.000176 | 0.000204 | 17.403 |
| `fft_y_Fw_filtered_phase_39` | `XGBM` | 0.118073 | 0.149678 | 9.720 |
| `fft_y_Fw_filtered_ampl_40` | `XGBM` | 0.000061 | 0.000083 | 8.060 |
| `fft_y_Fw_filtered_phase_40` | `XGBM` | 0.096599 | 0.129969 | 222.364 |
| `fft_y_Fw_filtered_ampl_78` | `XGBM` | 0.000299 | 0.000357 | 235.354 |
| `fft_y_Fw_filtered_phase_78` | `XGBM` | 0.249256 | 0.403112 | 85.289 |
| `fft_y_Fw_filtered_ampl_81` | `XGBM` | 0.000045 | 0.000057 | 14.725 |
| `fft_y_Fw_filtered_phase_81` | `XGBM` | 0.244850 | 0.310045 | 47.618 |
| `fft_y_Fw_filtered_ampl_156` | `XGBM` | 0.000503 | 0.001065 | 360.638 |
| `fft_y_Fw_filtered_phase_156` | `XGBM` | 1.452403 | 1.692879 | 73.133 |
| `fft_y_Fw_filtered_ampl_162` | `XGBM` | 0.000716 | 0.002023 | 205.470 |
| `fft_y_Fw_filtered_phase_162` | `XGBM` | 0.792415 | 1.101923 | 52.873 |
| `fft_y_Fw_filtered_ampl_240` | `XGBM` | 0.000231 | 0.000411 | 82.800 |
| `fft_y_Fw_filtered_phase_240` | `XGBM` | 0.488360 | 0.933851 | 24.745 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/xgbm/2026-04-26_track1_forward_xgbm_original_dataset_mega_campaign/007_track1_original_dataset_forward_xgbm_attempt_07.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-13-03__track1_original_dataset_forward_xgbm_attempt_07_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-13-03__track1_original_dataset_forward_xgbm_attempt_07_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-13-03__track1_original_dataset_forward_xgbm_attempt_07_campaign_validation/validation_summary.yaml`
