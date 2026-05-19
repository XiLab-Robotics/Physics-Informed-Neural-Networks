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
- random seed: `37`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `49.596%`
- winning mean component MAE: `0.082179`
- winning mean component RMSE: `0.168076`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 49.596 | 0.082179 | 0.168076 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `XGBM` | 0.002701 | 0.003162 | 43.833 |
| `fft_y_Bw_filtered_ampl_1` | `XGBM` | 0.000072 | 0.000117 | 0.418 |
| `fft_y_Bw_filtered_phase_1` | `XGBM` | 0.001819 | 0.002555 | 147.054 |
| `fft_y_Bw_filtered_ampl_3` | `XGBM` | 0.000076 | 0.000095 | 8.633 |
| `fft_y_Bw_filtered_phase_3` | `XGBM` | 0.020541 | 0.026818 | 1.512 |
| `fft_y_Bw_filtered_ampl_39` | `XGBM` | 0.000092 | 0.000112 | 20.177 |
| `fft_y_Bw_filtered_phase_39` | `XGBM` | 0.319840 | 0.818852 | 11.733 |
| `fft_y_Bw_filtered_ampl_40` | `XGBM` | 0.000047 | 0.000060 | 15.832 |
| `fft_y_Bw_filtered_phase_40` | `XGBM` | 0.137977 | 0.200606 | 77.183 |
| `fft_y_Bw_filtered_ampl_78` | `XGBM` | 0.000146 | 0.000194 | 43.007 |
| `fft_y_Bw_filtered_phase_78` | `XGBM` | 0.096608 | 0.219830 | 29.058 |
| `fft_y_Bw_filtered_ampl_81` | `XGBM` | 0.000026 | 0.000033 | 22.983 |
| `fft_y_Bw_filtered_phase_81` | `XGBM` | 0.086143 | 0.108707 | 344.183 |
| `fft_y_Bw_filtered_ampl_156` | `XGBM` | 0.000471 | 0.001651 | 24.114 |
| `fft_y_Bw_filtered_phase_156` | `XGBM` | 0.198639 | 0.568780 | 46.073 |
| `fft_y_Bw_filtered_ampl_162` | `XGBM` | 0.000180 | 0.000657 | 31.136 |
| `fft_y_Bw_filtered_phase_162` | `XGBM` | 0.179943 | 0.383101 | 10.085 |
| `fft_y_Bw_filtered_ampl_240` | `XGBM` | 0.000194 | 0.000380 | 37.162 |
| `fft_y_Bw_filtered_phase_240` | `XGBM` | 0.515890 | 0.857740 | 28.150 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/xgbm/2026-04-26_track1_backward_xgbm_original_dataset_mega_campaign/015_track1_original_dataset_backward_xgbm_attempt_15.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-02-40__track1_original_dataset_backward_xgbm_attempt_15_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-02-40__track1_original_dataset_backward_xgbm_attempt_15_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-02-40__track1_original_dataset_backward_xgbm_attempt_15_campaign_validation/validation_summary.yaml`
