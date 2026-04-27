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
- random seed: `9`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `38.903%`
- winning mean component MAE: `0.104080`
- winning mean component RMSE: `0.182892`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 38.903 | 0.104080 | 0.182892 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `XGBM` | 0.002322 | 0.002900 | 4.693 |
| `fft_y_Fw_filtered_ampl_1` | `XGBM` | 0.000049 | 0.000062 | 0.287 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.002121 | 0.003033 | 26.118 |
| `fft_y_Fw_filtered_ampl_3` | `XGBM` | 0.000078 | 0.000096 | 10.243 |
| `fft_y_Fw_filtered_phase_3` | `XGBM` | 0.023747 | 0.031571 | 1.320 |
| `fft_y_Fw_filtered_ampl_39` | `XGBM` | 0.000108 | 0.000141 | 9.774 |
| `fft_y_Fw_filtered_phase_39` | `XGBM` | 0.024362 | 0.036946 | 2.189 |
| `fft_y_Fw_filtered_ampl_40` | `XGBM` | 0.000072 | 0.000097 | 9.911 |
| `fft_y_Fw_filtered_phase_40` | `XGBM` | 0.058272 | 0.091190 | 130.137 |
| `fft_y_Fw_filtered_ampl_78` | `XGBM` | 0.000144 | 0.000190 | 97.098 |
| `fft_y_Fw_filtered_phase_78` | `XGBM` | 0.153333 | 0.357247 | 125.068 |
| `fft_y_Fw_filtered_ampl_81` | `XGBM` | 0.000047 | 0.000062 | 14.739 |
| `fft_y_Fw_filtered_phase_81` | `XGBM` | 0.076702 | 0.104392 | 14.276 |
| `fft_y_Fw_filtered_ampl_156` | `XGBM` | 0.000260 | 0.000683 | 90.079 |
| `fft_y_Fw_filtered_phase_156` | `XGBM` | 0.681762 | 1.099191 | 35.606 |
| `fft_y_Fw_filtered_ampl_162` | `XGBM` | 0.000257 | 0.000893 | 38.168 |
| `fft_y_Fw_filtered_phase_162` | `XGBM` | 0.546713 | 0.983333 | 23.649 |
| `fft_y_Fw_filtered_ampl_240` | `XGBM` | 0.000167 | 0.000277 | 78.621 |
| `fft_y_Fw_filtered_phase_240` | `XGBM` | 0.407012 | 0.762644 | 27.183 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/xgbm/2026-04-26_track1_forward_xgbm_original_dataset_mega_campaign/004_track1_original_dataset_forward_xgbm_attempt_04.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-09-54__track1_original_dataset_forward_xgbm_attempt_04_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-09-54__track1_original_dataset_forward_xgbm_attempt_04_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-09-54__track1_original_dataset_forward_xgbm_attempt_04_campaign_validation/validation_summary.yaml`
