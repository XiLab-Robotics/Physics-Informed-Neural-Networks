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
- random seed: `61`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `31.152%`
- winning mean component MAE: `0.087744`
- winning mean component RMSE: `0.171832`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 31.152 | 0.087744 | 0.171832 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `XGBM` | 0.002603 | 0.003160 | 38.992 |
| `fft_y_Bw_filtered_ampl_1` | `XGBM` | 0.000069 | 0.000098 | 0.402 |
| `fft_y_Bw_filtered_phase_1` | `XGBM` | 0.002231 | 0.003226 | 52.997 |
| `fft_y_Bw_filtered_ampl_3` | `XGBM` | 0.000074 | 0.000096 | 8.135 |
| `fft_y_Bw_filtered_phase_3` | `XGBM` | 0.021447 | 0.028765 | 1.592 |
| `fft_y_Bw_filtered_ampl_39` | `XGBM` | 0.000086 | 0.000104 | 19.266 |
| `fft_y_Bw_filtered_phase_39` | `XGBM` | 0.358351 | 0.858552 | 13.780 |
| `fft_y_Bw_filtered_ampl_40` | `XGBM` | 0.000041 | 0.000055 | 12.852 |
| `fft_y_Bw_filtered_phase_40` | `XGBM` | 0.169981 | 0.244798 | 78.972 |
| `fft_y_Bw_filtered_ampl_78` | `XGBM` | 0.000131 | 0.000182 | 24.976 |
| `fft_y_Bw_filtered_phase_78` | `XGBM` | 0.080762 | 0.116744 | 69.296 |
| `fft_y_Bw_filtered_ampl_81` | `XGBM` | 0.000025 | 0.000032 | 20.725 |
| `fft_y_Bw_filtered_phase_81` | `XGBM` | 0.098896 | 0.127519 | 89.763 |
| `fft_y_Bw_filtered_ampl_156` | `XGBM` | 0.000553 | 0.001864 | 46.325 |
| `fft_y_Bw_filtered_phase_156` | `XGBM` | 0.214574 | 0.553593 | 16.229 |
| `fft_y_Bw_filtered_ampl_162` | `XGBM` | 0.000196 | 0.000466 | 26.203 |
| `fft_y_Bw_filtered_phase_162` | `XGBM` | 0.221087 | 0.557583 | 12.318 |
| `fft_y_Bw_filtered_ampl_240` | `XGBM` | 0.000177 | 0.000375 | 30.167 |
| `fft_y_Bw_filtered_phase_240` | `XGBM` | 0.495857 | 0.767596 | 28.908 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/xgbm/2026-04-26_track1_backward_xgbm_original_dataset_mega_campaign/020_track1_original_dataset_backward_xgbm_attempt_20.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-07-52__track1_original_dataset_backward_xgbm_attempt_20_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-07-52__track1_original_dataset_backward_xgbm_attempt_20_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-07-52__track1_original_dataset_backward_xgbm_attempt_20_campaign_validation/validation_summary.yaml`
