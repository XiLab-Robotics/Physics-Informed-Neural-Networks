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
- random seed: `23`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `21.539%`
- winning mean component MAE: `0.080441`
- winning mean component RMSE: `0.178839`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 21.539 | 0.080441 | 0.178839 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 4, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.003245 | 0.003774 | 6.292 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000028 | 0.000038 | 0.165 |
| `fft_y_Fw_filtered_phase_1` | `ERT` | 0.002004 | 0.002883 | 32.119 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000025 | 0.000033 | 3.025 |
| `fft_y_Fw_filtered_phase_3` | `ERT` | 0.022071 | 0.030409 | 1.229 |
| `fft_y_Fw_filtered_ampl_39` | `ERT` | 0.000029 | 0.000039 | 2.586 |
| `fft_y_Fw_filtered_phase_39` | `ERT` | 0.023973 | 0.039395 | 1.973 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000023 | 0.000035 | 3.085 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.036770 | 0.052925 | 175.519 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000041 | 0.000057 | 8.601 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.066940 | 0.141551 | 61.841 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000010 | 0.000014 | 3.339 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.056114 | 0.086162 | 6.063 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000055 | 0.000223 | 22.438 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.699082 | 1.399580 | 31.192 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000093 | 0.000554 | 10.010 |
| `fft_y_Fw_filtered_phase_162` | `ERT` | 0.392354 | 1.073256 | 15.706 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000036 | 0.000062 | 8.850 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | 0.225481 | 0.566948 | 15.212 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/ert/2026-04-26_track1_forward_ert_original_dataset_mega_campaign/011_track1_original_dataset_forward_ert_attempt_11.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-20-33__track1_original_dataset_forward_ert_attempt_11_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-20-33__track1_original_dataset_forward_ert_attempt_11_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-20-33__track1_original_dataset_forward_ert_attempt_11_campaign_validation/validation_summary.yaml`
