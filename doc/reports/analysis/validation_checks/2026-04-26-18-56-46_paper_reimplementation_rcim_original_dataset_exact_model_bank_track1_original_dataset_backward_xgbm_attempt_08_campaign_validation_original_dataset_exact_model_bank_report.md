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
- random seed: `17`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `29.536%`
- winning mean component MAE: `0.086856`
- winning mean component RMSE: `0.157315`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 29.536 | 0.086856 | 0.157315 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `XGBM` | 0.002296 | 0.002723 | 40.989 |
| `fft_y_Bw_filtered_ampl_1` | `XGBM` | 0.000062 | 0.000102 | 0.358 |
| `fft_y_Bw_filtered_phase_1` | `XGBM` | 0.001860 | 0.002719 | 46.555 |
| `fft_y_Bw_filtered_ampl_3` | `XGBM` | 0.000080 | 0.000101 | 8.364 |
| `fft_y_Bw_filtered_phase_3` | `XGBM` | 0.017963 | 0.022778 | 1.379 |
| `fft_y_Bw_filtered_ampl_39` | `XGBM` | 0.000093 | 0.000115 | 20.105 |
| `fft_y_Bw_filtered_phase_39` | `XGBM` | 0.411798 | 0.790168 | 14.982 |
| `fft_y_Bw_filtered_ampl_40` | `XGBM` | 0.000043 | 0.000056 | 13.168 |
| `fft_y_Bw_filtered_phase_40` | `XGBM` | 0.151935 | 0.198772 | 77.673 |
| `fft_y_Bw_filtered_ampl_78` | `XGBM` | 0.000156 | 0.000202 | 34.486 |
| `fft_y_Bw_filtered_phase_78` | `XGBM` | 0.075272 | 0.124272 | 31.831 |
| `fft_y_Bw_filtered_ampl_81` | `XGBM` | 0.000025 | 0.000031 | 23.341 |
| `fft_y_Bw_filtered_phase_81` | `XGBM` | 0.106234 | 0.146117 | 79.980 |
| `fft_y_Bw_filtered_ampl_156` | `XGBM` | 0.000387 | 0.000799 | 45.363 |
| `fft_y_Bw_filtered_phase_156` | `XGBM` | 0.182077 | 0.387350 | 15.216 |
| `fft_y_Bw_filtered_ampl_162` | `XGBM` | 0.000306 | 0.000857 | 35.874 |
| `fft_y_Bw_filtered_phase_162` | `XGBM` | 0.204200 | 0.492293 | 10.330 |
| `fft_y_Bw_filtered_ampl_240` | `XGBM` | 0.000220 | 0.000447 | 36.883 |
| `fft_y_Bw_filtered_phase_240` | `XGBM` | 0.495262 | 0.819087 | 24.302 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/xgbm/2026-04-26_track1_backward_xgbm_original_dataset_mega_campaign/008_track1_original_dataset_backward_xgbm_attempt_08.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-55-57__track1_original_dataset_backward_xgbm_attempt_08_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-55-57__track1_original_dataset_backward_xgbm_attempt_08_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-55-57__track1_original_dataset_backward_xgbm_attempt_08_campaign_validation/validation_summary.yaml`
