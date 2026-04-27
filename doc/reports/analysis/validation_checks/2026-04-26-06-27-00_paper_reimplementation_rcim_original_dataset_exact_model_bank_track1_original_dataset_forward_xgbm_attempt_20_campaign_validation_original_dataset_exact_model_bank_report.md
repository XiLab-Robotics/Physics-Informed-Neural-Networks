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
- random seed: `61`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `90.601%`
- winning mean component MAE: `0.196250`
- winning mean component RMSE: `0.271621`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 90.601 | 0.196250 | 0.271621 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.01, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `XGBM` | 0.010067 | 0.011926 | 23.866 |
| `fft_y_Fw_filtered_ampl_1` | `XGBM` | 0.000051 | 0.000066 | 0.298 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.002815 | 0.003790 | 87.572 |
| `fft_y_Fw_filtered_ampl_3` | `XGBM` | 0.000105 | 0.000129 | 14.187 |
| `fft_y_Fw_filtered_phase_3` | `XGBM` | 0.076482 | 0.093331 | 4.339 |
| `fft_y_Fw_filtered_ampl_39` | `XGBM` | 0.000164 | 0.000201 | 16.440 |
| `fft_y_Fw_filtered_phase_39` | `XGBM` | 0.122483 | 0.152792 | 10.004 |
| `fft_y_Fw_filtered_ampl_40` | `XGBM` | 0.000065 | 0.000086 | 8.627 |
| `fft_y_Fw_filtered_phase_40` | `XGBM` | 0.076514 | 0.103447 | 252.751 |
| `fft_y_Fw_filtered_ampl_78` | `XGBM` | 0.000322 | 0.000397 | 95.480 |
| `fft_y_Fw_filtered_phase_78` | `XGBM` | 0.257895 | 0.415342 | 118.524 |
| `fft_y_Fw_filtered_ampl_81` | `XGBM` | 0.000049 | 0.000059 | 16.877 |
| `fft_y_Fw_filtered_phase_81` | `XGBM` | 0.203959 | 0.263836 | 28.430 |
| `fft_y_Fw_filtered_ampl_156` | `XGBM` | 0.000541 | 0.001179 | 544.639 |
| `fft_y_Fw_filtered_phase_156` | `XGBM` | 1.479366 | 1.775133 | 88.913 |
| `fft_y_Fw_filtered_ampl_162` | `XGBM` | 0.000546 | 0.001236 | 230.473 |
| `fft_y_Fw_filtered_phase_162` | `XGBM` | 0.925799 | 1.350383 | 40.927 |
| `fft_y_Fw_filtered_ampl_240` | `XGBM` | 0.000268 | 0.000506 | 102.933 |
| `fft_y_Fw_filtered_phase_240` | `XGBM` | 0.571251 | 0.986952 | 36.142 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/xgbm/2026-04-26_track1_forward_xgbm_original_dataset_mega_campaign/020_track1_original_dataset_forward_xgbm_attempt_20.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-26-09__track1_original_dataset_forward_xgbm_attempt_20_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-26-09__track1_original_dataset_forward_xgbm_attempt_20_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-26-09__track1_original_dataset_forward_xgbm_attempt_20_campaign_validation/validation_summary.yaml`
