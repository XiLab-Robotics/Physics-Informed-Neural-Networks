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
- random seed: `47`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `18.213%`
- winning mean component MAE: `0.084868`
- winning mean component RMSE: `0.182658`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 18.213 | 0.084868 | 0.182658 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.003686 | 0.004565 | 14.685 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000028 | 0.000038 | 0.161 |
| `fft_y_Fw_filtered_phase_1` | `ERT` | 0.002050 | 0.002900 | 58.592 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000021 | 0.000030 | 2.713 |
| `fft_y_Fw_filtered_phase_3` | `ERT` | 0.025323 | 0.042597 | 1.418 |
| `fft_y_Fw_filtered_ampl_39` | `ERT` | 0.000030 | 0.000046 | 2.629 |
| `fft_y_Fw_filtered_phase_39` | `ERT` | 0.028675 | 0.047879 | 2.327 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000027 | 0.000046 | 3.564 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.038681 | 0.066601 | 88.051 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000040 | 0.000062 | 6.187 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.055732 | 0.123309 | 26.037 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000011 | 0.000019 | 3.380 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.059748 | 0.101422 | 8.209 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000050 | 0.000159 | 10.159 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.635331 | 1.273004 | 43.189 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000115 | 0.000604 | 6.999 |
| `fft_y_Fw_filtered_phase_162` | `ERT` | 0.310418 | 0.812431 | 14.883 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000034 | 0.000077 | 12.169 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | 0.452502 | 0.994715 | 40.702 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/ert/2026-04-26_track1_forward_ert_original_dataset_mega_campaign/017_track1_original_dataset_forward_ert_attempt_17.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-39-39__track1_original_dataset_forward_ert_attempt_17_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-39-39__track1_original_dataset_forward_ert_attempt_17_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-39-39__track1_original_dataset_forward_ert_attempt_17_campaign_validation/validation_summary.yaml`
