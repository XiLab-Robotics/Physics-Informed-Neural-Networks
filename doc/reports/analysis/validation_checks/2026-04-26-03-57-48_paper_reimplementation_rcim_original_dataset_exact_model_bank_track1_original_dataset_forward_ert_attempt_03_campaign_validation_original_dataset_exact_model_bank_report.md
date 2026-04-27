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
- random seed: `7`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `15.476%`
- winning mean component MAE: `0.059499`
- winning mean component RMSE: `0.137652`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 15.476 | 0.059499 | 0.137652 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.003317 | 0.003901 | 6.379 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000026 | 0.000035 | 0.152 |
| `fft_y_Fw_filtered_phase_1` | `ERT` | 0.002161 | 0.002875 | 25.308 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000022 | 0.000030 | 2.795 |
| `fft_y_Fw_filtered_phase_3` | `ERT` | 0.025118 | 0.038088 | 1.410 |
| `fft_y_Fw_filtered_ampl_39` | `ERT` | 0.000030 | 0.000040 | 2.549 |
| `fft_y_Fw_filtered_phase_39` | `ERT` | 0.020334 | 0.031477 | 1.761 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000026 | 0.000042 | 3.243 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.032411 | 0.048766 | 41.564 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000031 | 0.000046 | 6.269 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.067607 | 0.223700 | 77.915 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000012 | 0.000016 | 4.093 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.048400 | 0.074012 | 6.263 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000072 | 0.000295 | 14.565 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.504346 | 1.022472 | 60.146 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000048 | 0.000133 | 7.696 |
| `fft_y_Fw_filtered_phase_162` | `ERT` | 0.287438 | 0.820065 | 10.895 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000033 | 0.000062 | 8.319 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | 0.139049 | 0.349334 | 12.722 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/ert/2026-04-26_track1_forward_ert_original_dataset_mega_campaign/003_track1_original_dataset_forward_ert_attempt_03.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-54-40__track1_original_dataset_forward_ert_attempt_03_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-54-40__track1_original_dataset_forward_ert_attempt_03_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-54-40__track1_original_dataset_forward_ert_attempt_03_campaign_validation/validation_summary.yaml`
