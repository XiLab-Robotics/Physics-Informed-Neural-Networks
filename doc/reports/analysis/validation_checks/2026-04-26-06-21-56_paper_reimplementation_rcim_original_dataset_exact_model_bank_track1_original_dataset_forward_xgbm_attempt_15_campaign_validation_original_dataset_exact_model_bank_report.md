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
- random seed: `37`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `58.292%`
- winning mean component MAE: `0.117137`
- winning mean component RMSE: `0.194252`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 58.292 | 0.117137 | 0.194252 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `XGBM` | 0.002571 | 0.003218 | 5.430 |
| `fft_y_Fw_filtered_ampl_1` | `XGBM` | 0.000046 | 0.000058 | 0.266 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.001932 | 0.002690 | 48.450 |
| `fft_y_Fw_filtered_ampl_3` | `XGBM` | 0.000081 | 0.000098 | 11.141 |
| `fft_y_Fw_filtered_phase_3` | `XGBM` | 0.023381 | 0.030478 | 1.305 |
| `fft_y_Fw_filtered_ampl_39` | `XGBM` | 0.000106 | 0.000129 | 10.158 |
| `fft_y_Fw_filtered_phase_39` | `XGBM` | 0.024446 | 0.032586 | 2.018 |
| `fft_y_Fw_filtered_ampl_40` | `XGBM` | 0.000061 | 0.000081 | 7.711 |
| `fft_y_Fw_filtered_phase_40` | `XGBM` | 0.047148 | 0.063266 | 77.422 |
| `fft_y_Fw_filtered_ampl_78` | `XGBM` | 0.000117 | 0.000152 | 41.534 |
| `fft_y_Fw_filtered_phase_78` | `XGBM` | 0.132115 | 0.216929 | 324.563 |
| `fft_y_Fw_filtered_ampl_81` | `XGBM` | 0.000048 | 0.000060 | 16.638 |
| `fft_y_Fw_filtered_phase_81` | `XGBM` | 0.082586 | 0.112984 | 11.559 |
| `fft_y_Fw_filtered_ampl_156` | `XGBM` | 0.000266 | 0.000792 | 101.432 |
| `fft_y_Fw_filtered_phase_156` | `XGBM` | 0.918941 | 1.416482 | 49.288 |
| `fft_y_Fw_filtered_ampl_162` | `XGBM` | 0.000161 | 0.000688 | 37.856 |
| `fft_y_Fw_filtered_phase_162` | `XGBM` | 0.597567 | 1.070603 | 26.245 |
| `fft_y_Fw_filtered_ampl_240` | `XGBM` | 0.000146 | 0.000220 | 73.336 |
| `fft_y_Fw_filtered_phase_240` | `XGBM` | 0.393893 | 0.739277 | 261.188 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/xgbm/2026-04-26_track1_forward_xgbm_original_dataset_mega_campaign/015_track1_original_dataset_forward_xgbm_attempt_15.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-21-04__track1_original_dataset_forward_xgbm_attempt_15_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-21-04__track1_original_dataset_forward_xgbm_attempt_15_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-21-04__track1_original_dataset_forward_xgbm_attempt_15_campaign_validation/validation_summary.yaml`
