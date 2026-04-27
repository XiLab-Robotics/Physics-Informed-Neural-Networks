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
- random seed: `11`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `49.184%`
- winning mean component MAE: `0.094384`
- winning mean component RMSE: `0.167533`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 49.184 | 0.094384 | 0.167533 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 16}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `XGBM` | 0.002936 | 0.003291 | 92.825 |
| `fft_y_Bw_filtered_ampl_1` | `XGBM` | 0.000059 | 0.000107 | 0.343 |
| `fft_y_Bw_filtered_phase_1` | `XGBM` | 0.002178 | 0.003306 | 75.868 |
| `fft_y_Bw_filtered_ampl_3` | `XGBM` | 0.000090 | 0.000115 | 9.074 |
| `fft_y_Bw_filtered_phase_3` | `XGBM` | 0.021988 | 0.029726 | 1.639 |
| `fft_y_Bw_filtered_ampl_39` | `XGBM` | 0.000092 | 0.000114 | 19.955 |
| `fft_y_Bw_filtered_phase_39` | `XGBM` | 0.497378 | 1.051830 | 18.180 |
| `fft_y_Bw_filtered_ampl_40` | `XGBM` | 0.000047 | 0.000059 | 15.768 |
| `fft_y_Bw_filtered_phase_40` | `XGBM` | 0.150226 | 0.198078 | 154.595 |
| `fft_y_Bw_filtered_ampl_78` | `XGBM` | 0.000154 | 0.000188 | 27.075 |
| `fft_y_Bw_filtered_phase_78` | `XGBM` | 0.077537 | 0.114375 | 28.398 |
| `fft_y_Bw_filtered_ampl_81` | `XGBM` | 0.000027 | 0.000035 | 22.201 |
| `fft_y_Bw_filtered_phase_81` | `XGBM` | 0.104245 | 0.141531 | 286.543 |
| `fft_y_Bw_filtered_ampl_156` | `XGBM` | 0.000528 | 0.001411 | 46.761 |
| `fft_y_Bw_filtered_phase_156` | `XGBM` | 0.215599 | 0.424572 | 16.560 |
| `fft_y_Bw_filtered_ampl_162` | `XGBM` | 0.000326 | 0.001049 | 30.971 |
| `fft_y_Bw_filtered_phase_162` | `XGBM` | 0.176817 | 0.324844 | 11.108 |
| `fft_y_Bw_filtered_ampl_240` | `XGBM` | 0.000239 | 0.000561 | 39.495 |
| `fft_y_Bw_filtered_phase_240` | `XGBM` | 0.542826 | 0.887928 | 37.131 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/xgbm/2026-04-26_track1_backward_xgbm_original_dataset_mega_campaign/005_track1_original_dataset_backward_xgbm_attempt_05.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-53-06__track1_original_dataset_backward_xgbm_attempt_05_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-53-06__track1_original_dataset_backward_xgbm_attempt_05_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-53-06__track1_original_dataset_backward_xgbm_attempt_05_campaign_validation/validation_summary.yaml`
