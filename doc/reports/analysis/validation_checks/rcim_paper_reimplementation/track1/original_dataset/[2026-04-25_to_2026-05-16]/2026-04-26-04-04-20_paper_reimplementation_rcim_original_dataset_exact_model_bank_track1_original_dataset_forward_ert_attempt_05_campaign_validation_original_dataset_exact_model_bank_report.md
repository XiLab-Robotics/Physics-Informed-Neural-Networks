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
- random seed: `11`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `19.501%`
- winning mean component MAE: `0.085832`
- winning mean component RMSE: `0.198721`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 19.501 | 0.085832 | 0.198721 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 4, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.003282 | 0.003972 | 6.243 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000028 | 0.000036 | 0.160 |
| `fft_y_Fw_filtered_phase_1` | `ERT` | 0.001991 | 0.002975 | 28.059 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000020 | 0.000028 | 2.421 |
| `fft_y_Fw_filtered_phase_3` | `ERT` | 0.024667 | 0.035876 | 1.367 |
| `fft_y_Fw_filtered_ampl_39` | `ERT` | 0.000027 | 0.000037 | 2.438 |
| `fft_y_Fw_filtered_phase_39` | `ERT` | 0.024600 | 0.047411 | 1.962 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000028 | 0.000043 | 3.300 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.034625 | 0.051294 | 53.748 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000042 | 0.000059 | 10.018 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.096911 | 0.365121 | 153.785 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000011 | 0.000015 | 3.530 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.052607 | 0.074881 | 5.114 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000060 | 0.000253 | 10.137 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.774668 | 1.519991 | 38.031 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000044 | 0.000136 | 10.109 |
| `fft_y_Fw_filtered_phase_162` | `ERT` | 0.364876 | 0.969526 | 16.249 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000045 | 0.000091 | 9.519 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | 0.252284 | 0.703955 | 14.325 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/ert/2026-04-26_track1_forward_ert_original_dataset_mega_campaign/005_track1_original_dataset_forward_ert_attempt_05.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-01-16__track1_original_dataset_forward_ert_attempt_05_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-01-16__track1_original_dataset_forward_ert_attempt_05_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-01-16__track1_original_dataset_forward_ert_attempt_05_campaign_validation/validation_summary.yaml`
