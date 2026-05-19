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
- random seed: `29`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `21.380%`
- winning mean component MAE: `0.076779`
- winning mean component RMSE: `0.183445`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 21.380 | 0.076779 | 0.183445 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 5, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.003422 | 0.005047 | 17.800 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000029 | 0.000038 | 0.167 |
| `fft_y_Fw_filtered_phase_1` | `ERT` | 0.001953 | 0.002855 | 20.849 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000025 | 0.000048 | 3.113 |
| `fft_y_Fw_filtered_phase_3` | `ERT` | 0.030461 | 0.044662 | 1.699 |
| `fft_y_Fw_filtered_ampl_39` | `ERT` | 0.000029 | 0.000045 | 2.806 |
| `fft_y_Fw_filtered_phase_39` | `ERT` | 0.021231 | 0.032903 | 1.751 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000029 | 0.000050 | 3.752 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.038790 | 0.067058 | 90.358 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000038 | 0.000051 | 6.666 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.083503 | 0.194736 | 102.296 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000013 | 0.000019 | 4.042 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.053162 | 0.082595 | 5.683 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000086 | 0.000245 | 11.743 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.545558 | 1.104660 | 30.716 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000052 | 0.000207 | 7.311 |
| `fft_y_Fw_filtered_phase_162` | `ERT` | 0.375397 | 1.104003 | 14.268 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000063 | 0.000211 | 65.801 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | 0.304964 | 0.846029 | 15.405 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/ert/2026-04-26_track1_forward_ert_original_dataset_mega_campaign/013_track1_original_dataset_forward_ert_attempt_13.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-27-00__track1_original_dataset_forward_ert_attempt_13_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-27-00__track1_original_dataset_forward_ert_attempt_13_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-27-00__track1_original_dataset_forward_ert_attempt_13_campaign_validation/validation_summary.yaml`
