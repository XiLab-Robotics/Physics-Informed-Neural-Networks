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
- random seed: `59`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `36.091%`
- winning mean component MAE: `0.094307`
- winning mean component RMSE: `0.163597`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 36.091 | 0.094307 | 0.163597 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.3, 'estimator__max_depth': 18}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `XGBM` | 0.002636 | 0.003088 | 70.737 |
| `fft_y_Bw_filtered_ampl_1` | `XGBM` | 0.000073 | 0.000111 | 0.426 |
| `fft_y_Bw_filtered_phase_1` | `XGBM` | 0.002344 | 0.003666 | 111.461 |
| `fft_y_Bw_filtered_ampl_3` | `XGBM` | 0.000092 | 0.000125 | 9.290 |
| `fft_y_Bw_filtered_phase_3` | `XGBM` | 0.021551 | 0.027941 | 1.611 |
| `fft_y_Bw_filtered_ampl_39` | `XGBM` | 0.000081 | 0.000098 | 18.285 |
| `fft_y_Bw_filtered_phase_39` | `XGBM` | 0.461324 | 0.895781 | 17.516 |
| `fft_y_Bw_filtered_ampl_40` | `XGBM` | 0.000045 | 0.000057 | 15.042 |
| `fft_y_Bw_filtered_phase_40` | `XGBM` | 0.188546 | 0.257242 | 132.932 |
| `fft_y_Bw_filtered_ampl_78` | `XGBM` | 0.000148 | 0.000193 | 26.638 |
| `fft_y_Bw_filtered_phase_78` | `XGBM` | 0.097531 | 0.145990 | 25.397 |
| `fft_y_Bw_filtered_ampl_81` | `XGBM` | 0.000029 | 0.000036 | 23.513 |
| `fft_y_Bw_filtered_phase_81` | `XGBM` | 0.104132 | 0.135384 | 43.186 |
| `fft_y_Bw_filtered_ampl_156` | `XGBM` | 0.000426 | 0.001149 | 38.734 |
| `fft_y_Bw_filtered_phase_156` | `XGBM` | 0.179765 | 0.342056 | 45.850 |
| `fft_y_Bw_filtered_ampl_162` | `XGBM` | 0.000176 | 0.000331 | 33.145 |
| `fft_y_Bw_filtered_phase_162` | `XGBM` | 0.216696 | 0.439187 | 13.130 |
| `fft_y_Bw_filtered_ampl_240` | `XGBM` | 0.000171 | 0.000388 | 28.721 |
| `fft_y_Bw_filtered_phase_240` | `XGBM` | 0.516070 | 0.855517 | 30.123 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/xgbm/2026-04-26_track1_backward_xgbm_original_dataset_mega_campaign/019_track1_original_dataset_backward_xgbm_attempt_19.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-06-55__track1_original_dataset_backward_xgbm_attempt_19_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-06-55__track1_original_dataset_backward_xgbm_attempt_19_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-06-55__track1_original_dataset_backward_xgbm_attempt_19_campaign_validation/validation_summary.yaml`
