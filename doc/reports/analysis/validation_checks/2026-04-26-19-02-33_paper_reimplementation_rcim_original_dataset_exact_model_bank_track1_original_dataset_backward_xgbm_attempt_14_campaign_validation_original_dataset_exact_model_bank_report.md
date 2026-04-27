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
- random seed: `31`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `34.091%`
- winning mean component MAE: `0.082775`
- winning mean component RMSE: `0.153587`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 34.091 | 0.082775 | 0.153587 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 18}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `XGBM` | 0.002848 | 0.003837 | 47.035 |
| `fft_y_Bw_filtered_ampl_1` | `XGBM` | 0.000079 | 0.000130 | 0.456 |
| `fft_y_Bw_filtered_phase_1` | `XGBM` | 0.002170 | 0.003840 | 133.808 |
| `fft_y_Bw_filtered_ampl_3` | `XGBM` | 0.000084 | 0.000114 | 8.981 |
| `fft_y_Bw_filtered_phase_3` | `XGBM` | 0.020845 | 0.031748 | 1.483 |
| `fft_y_Bw_filtered_ampl_39` | `XGBM` | 0.000082 | 0.000097 | 20.229 |
| `fft_y_Bw_filtered_phase_39` | `XGBM` | 0.303307 | 0.619980 | 12.139 |
| `fft_y_Bw_filtered_ampl_40` | `XGBM` | 0.000043 | 0.000056 | 15.861 |
| `fft_y_Bw_filtered_phase_40` | `XGBM` | 0.180320 | 0.257166 | 81.982 |
| `fft_y_Bw_filtered_ampl_78` | `XGBM` | 0.000156 | 0.000206 | 42.109 |
| `fft_y_Bw_filtered_phase_78` | `XGBM` | 0.101822 | 0.177883 | 35.597 |
| `fft_y_Bw_filtered_ampl_81` | `XGBM` | 0.000027 | 0.000035 | 20.628 |
| `fft_y_Bw_filtered_phase_81` | `XGBM` | 0.112311 | 0.158607 | 50.379 |
| `fft_y_Bw_filtered_ampl_156` | `XGBM` | 0.000418 | 0.001178 | 41.489 |
| `fft_y_Bw_filtered_phase_156` | `XGBM` | 0.183557 | 0.310479 | 21.485 |
| `fft_y_Bw_filtered_ampl_162` | `XGBM` | 0.000236 | 0.000672 | 31.422 |
| `fft_y_Bw_filtered_phase_162` | `XGBM` | 0.216508 | 0.456505 | 11.259 |
| `fft_y_Bw_filtered_ampl_240` | `XGBM` | 0.000141 | 0.000201 | 48.398 |
| `fft_y_Bw_filtered_phase_240` | `XGBM` | 0.447777 | 0.895427 | 22.988 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/xgbm/2026-04-26_track1_backward_xgbm_original_dataset_mega_campaign/014_track1_original_dataset_backward_xgbm_attempt_14.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-01-43__track1_original_dataset_backward_xgbm_attempt_14_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-01-43__track1_original_dataset_backward_xgbm_attempt_14_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-01-43__track1_original_dataset_backward_xgbm_attempt_14_campaign_validation/validation_summary.yaml`
