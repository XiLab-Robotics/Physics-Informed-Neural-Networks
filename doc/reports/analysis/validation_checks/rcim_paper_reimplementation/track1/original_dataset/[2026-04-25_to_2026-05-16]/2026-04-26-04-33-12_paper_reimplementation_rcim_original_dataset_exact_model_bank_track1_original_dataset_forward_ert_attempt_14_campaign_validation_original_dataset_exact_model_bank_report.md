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
- random seed: `31`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `32.284%`
- winning mean component MAE: `0.092893`
- winning mean component RMSE: `0.196217`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 32.284 | 0.092893 | 0.196217 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 17, 'estimator__min_samples_split': 6, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.003318 | 0.004366 | 7.514 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000026 | 0.000039 | 0.151 |
| `fft_y_Fw_filtered_phase_1` | `ERT` | 0.002278 | 0.003667 | 42.054 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000024 | 0.000046 | 2.856 |
| `fft_y_Fw_filtered_phase_3` | `ERT` | 0.025155 | 0.037042 | 1.365 |
| `fft_y_Fw_filtered_ampl_39` | `ERT` | 0.000030 | 0.000048 | 2.799 |
| `fft_y_Fw_filtered_phase_39` | `ERT` | 0.026968 | 0.050690 | 2.208 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000026 | 0.000037 | 3.279 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.032978 | 0.056028 | 59.435 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000043 | 0.000068 | 7.970 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.135345 | 0.384533 | 361.675 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000012 | 0.000020 | 3.493 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.057578 | 0.100825 | 5.259 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000047 | 0.000159 | 17.489 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.608653 | 1.095567 | 32.905 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000052 | 0.000195 | 8.031 |
| `fft_y_Fw_filtered_phase_162` | `ERT` | 0.421857 | 1.025833 | 15.389 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000038 | 0.000059 | 15.512 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | 0.450537 | 0.968904 | 24.005 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/ert/2026-04-26_track1_forward_ert_original_dataset_mega_campaign/014_track1_original_dataset_forward_ert_attempt_14.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-30-09__track1_original_dataset_forward_ert_attempt_14_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-30-09__track1_original_dataset_forward_ert_attempt_14_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-30-09__track1_original_dataset_forward_ert_attempt_14_campaign_validation/validation_summary.yaml`
