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
- random seed: `27`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `20.998%`
- winning mean component MAE: `0.065489`
- winning mean component RMSE: `0.142518`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 20.998 | 0.065489 | 0.142518 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.003098 | 0.003761 | 6.108 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000027 | 0.000037 | 0.160 |
| `fft_y_Fw_filtered_phase_1` | `ERT` | 0.002508 | 0.003517 | 31.484 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000022 | 0.000032 | 2.688 |
| `fft_y_Fw_filtered_phase_3` | `ERT` | 0.025613 | 0.033745 | 1.397 |
| `fft_y_Fw_filtered_ampl_39` | `ERT` | 0.000026 | 0.000036 | 2.234 |
| `fft_y_Fw_filtered_phase_39` | `ERT` | 0.026887 | 0.048849 | 2.251 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000027 | 0.000047 | 3.346 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.042027 | 0.061868 | 78.173 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000038 | 0.000053 | 5.867 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.046777 | 0.096494 | 147.086 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000009 | 0.000012 | 2.861 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.056761 | 0.087098 | 5.399 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000055 | 0.000178 | 12.843 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.645911 | 1.201879 | 37.934 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000034 | 0.000115 | 6.898 |
| `fft_y_Fw_filtered_phase_162` | `ERT` | 0.234120 | 0.784818 | 9.645 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000029 | 0.000046 | 6.961 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | 0.160316 | 0.385260 | 35.629 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/ert/2026-04-26_track1_forward_ert_original_dataset_mega_campaign/012_track1_original_dataset_forward_ert_attempt_12.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-23-45__track1_original_dataset_forward_ert_attempt_12_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-23-45__track1_original_dataset_forward_ert_attempt_12_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-23-45__track1_original_dataset_forward_ert_attempt_12_campaign_validation/validation_summary.yaml`
