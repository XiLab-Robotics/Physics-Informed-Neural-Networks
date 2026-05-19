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
- random seed: `29`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `40.473%`
- winning mean component MAE: `0.093970`
- winning mean component RMSE: `0.165614`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 40.473 | 0.093970 | 0.165614 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `XGBM` | 0.002993 | 0.004426 | 89.101 |
| `fft_y_Bw_filtered_ampl_1` | `XGBM` | 0.000063 | 0.000093 | 0.367 |
| `fft_y_Bw_filtered_phase_1` | `XGBM` | 0.002073 | 0.002769 | 95.278 |
| `fft_y_Bw_filtered_ampl_3` | `XGBM` | 0.000090 | 0.000116 | 9.696 |
| `fft_y_Bw_filtered_phase_3` | `XGBM` | 0.021723 | 0.040778 | 1.597 |
| `fft_y_Bw_filtered_ampl_39` | `XGBM` | 0.000100 | 0.000119 | 23.015 |
| `fft_y_Bw_filtered_phase_39` | `XGBM` | 0.427272 | 0.930800 | 16.088 |
| `fft_y_Bw_filtered_ampl_40` | `XGBM` | 0.000045 | 0.000063 | 15.126 |
| `fft_y_Bw_filtered_phase_40` | `XGBM` | 0.198548 | 0.286914 | 90.108 |
| `fft_y_Bw_filtered_ampl_78` | `XGBM` | 0.000146 | 0.000183 | 29.090 |
| `fft_y_Bw_filtered_phase_78` | `XGBM` | 0.086877 | 0.131343 | 26.358 |
| `fft_y_Bw_filtered_ampl_81` | `XGBM` | 0.000026 | 0.000034 | 20.960 |
| `fft_y_Bw_filtered_phase_81` | `XGBM` | 0.113677 | 0.165517 | 141.700 |
| `fft_y_Bw_filtered_ampl_156` | `XGBM` | 0.000495 | 0.001580 | 38.471 |
| `fft_y_Bw_filtered_phase_156` | `XGBM` | 0.220596 | 0.383869 | 24.889 |
| `fft_y_Bw_filtered_ampl_162` | `XGBM` | 0.000180 | 0.000386 | 36.890 |
| `fft_y_Bw_filtered_phase_162` | `XGBM` | 0.159245 | 0.251146 | 9.462 |
| `fft_y_Bw_filtered_ampl_240` | `XGBM` | 0.000238 | 0.000464 | 69.878 |
| `fft_y_Bw_filtered_phase_240` | `XGBM` | 0.551037 | 0.946072 | 30.914 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/xgbm/2026-04-26_track1_backward_xgbm_original_dataset_mega_campaign/013_track1_original_dataset_backward_xgbm_attempt_13.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-00-45__track1_original_dataset_backward_xgbm_attempt_13_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-00-45__track1_original_dataset_backward_xgbm_attempt_13_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-00-45__track1_original_dataset_backward_xgbm_attempt_13_campaign_validation/validation_summary.yaml`
