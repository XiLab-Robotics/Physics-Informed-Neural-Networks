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
- random seed: `13`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `19.928%`
- winning mean component MAE: `0.065318`
- winning mean component RMSE: `0.136471`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 19.928 | 0.065318 | 0.136471 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 18, 'estimator__min_samples_split': 6, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.002637 | 0.003172 | 5.325 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000022 | 0.000030 | 0.130 |
| `fft_y_Fw_filtered_phase_1` | `ERT` | 0.002258 | 0.002887 | 38.018 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000023 | 0.000033 | 2.672 |
| `fft_y_Fw_filtered_phase_3` | `ERT` | 0.020385 | 0.027590 | 1.138 |
| `fft_y_Fw_filtered_ampl_39` | `ERT` | 0.000030 | 0.000043 | 2.663 |
| `fft_y_Fw_filtered_phase_39` | `ERT` | 0.020249 | 0.027940 | 1.797 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000025 | 0.000036 | 3.104 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.030169 | 0.043940 | 52.746 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000045 | 0.000064 | 8.675 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.069568 | 0.170873 | 45.029 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000011 | 0.000016 | 3.805 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.049593 | 0.074635 | 5.972 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000060 | 0.000183 | 18.386 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.675060 | 1.267169 | 35.139 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000081 | 0.000266 | 8.771 |
| `fft_y_Fw_filtered_phase_162` | `ERT` | 0.138940 | 0.413294 | 6.241 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000035 | 0.000050 | 12.241 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | 0.231860 | 0.560724 | 126.787 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/ert/2026-04-26_track1_forward_ert_original_dataset_mega_campaign/006_track1_original_dataset_forward_ert_attempt_06.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-04-28__track1_original_dataset_forward_ert_attempt_06_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-04-28__track1_original_dataset_forward_ert_attempt_06_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-04-28__track1_original_dataset_forward_ert_attempt_06_campaign_validation/validation_summary.yaml`
