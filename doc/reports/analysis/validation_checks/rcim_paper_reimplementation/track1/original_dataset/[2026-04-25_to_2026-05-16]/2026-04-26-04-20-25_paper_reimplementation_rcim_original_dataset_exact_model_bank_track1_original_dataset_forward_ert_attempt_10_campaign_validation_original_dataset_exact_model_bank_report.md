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
- random seed: `21`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `21.430%`
- winning mean component MAE: `0.067238`
- winning mean component RMSE: `0.152512`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 21.430 | 0.067238 | 0.152512 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 4, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.002842 | 0.003607 | 5.853 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000029 | 0.000037 | 0.171 |
| `fft_y_Fw_filtered_phase_1` | `ERT` | 0.001905 | 0.002663 | 28.324 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000022 | 0.000030 | 2.701 |
| `fft_y_Fw_filtered_phase_3` | `ERT` | 0.025524 | 0.036862 | 1.408 |
| `fft_y_Fw_filtered_ampl_39` | `ERT` | 0.000028 | 0.000038 | 2.341 |
| `fft_y_Fw_filtered_phase_39` | `ERT` | 0.027088 | 0.050000 | 2.116 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000022 | 0.000034 | 2.839 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.032852 | 0.048661 | 139.284 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000045 | 0.000066 | 8.875 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.061870 | 0.127315 | 68.269 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000010 | 0.000014 | 3.284 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.057289 | 0.095789 | 4.843 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000067 | 0.000253 | 10.925 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.585985 | 1.160548 | 58.301 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000045 | 0.000104 | 8.290 |
| `fft_y_Fw_filtered_phase_162` | `ERT` | 0.207171 | 0.527340 | 8.312 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000053 | 0.000124 | 8.552 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | 0.274673 | 0.844234 | 42.485 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/ert/2026-04-26_track1_forward_ert_original_dataset_mega_campaign/010_track1_original_dataset_forward_ert_attempt_10.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-17-20__track1_original_dataset_forward_ert_attempt_10_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-17-20__track1_original_dataset_forward_ert_attempt_10_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-17-20__track1_original_dataset_forward_ert_attempt_10_campaign_validation/validation_summary.yaml`
