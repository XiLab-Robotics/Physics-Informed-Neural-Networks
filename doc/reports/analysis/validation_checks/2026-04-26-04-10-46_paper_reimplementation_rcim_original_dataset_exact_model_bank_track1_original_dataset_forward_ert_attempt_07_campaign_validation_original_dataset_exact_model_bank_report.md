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
- random seed: `15`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `15.796%`
- winning mean component MAE: `0.072748`
- winning mean component RMSE: `0.164148`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 15.796 | 0.072748 | 0.164148 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 6, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.003090 | 0.004331 | 16.899 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000028 | 0.000038 | 0.164 |
| `fft_y_Fw_filtered_phase_1` | `ERT` | 0.002200 | 0.003320 | 29.558 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000023 | 0.000032 | 2.987 |
| `fft_y_Fw_filtered_phase_3` | `ERT` | 0.024921 | 0.032475 | 1.401 |
| `fft_y_Fw_filtered_ampl_39` | `ERT` | 0.000033 | 0.000044 | 2.906 |
| `fft_y_Fw_filtered_phase_39` | `ERT` | 0.026886 | 0.046027 | 2.155 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000025 | 0.000038 | 3.265 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.039632 | 0.067707 | 67.092 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000043 | 0.000062 | 19.869 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.096186 | 0.369830 | 41.032 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000010 | 0.000014 | 3.394 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.059989 | 0.097637 | 6.073 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000053 | 0.000185 | 13.582 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.579750 | 1.009018 | 35.137 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000084 | 0.000390 | 13.539 |
| `fft_y_Fw_filtered_phase_162` | `ERT` | 0.300167 | 0.779310 | 16.413 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000042 | 0.000072 | 12.868 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | 0.249050 | 0.708279 | 11.796 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/ert/2026-04-26_track1_forward_ert_original_dataset_mega_campaign/007_track1_original_dataset_forward_ert_attempt_07.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-07-42__track1_original_dataset_forward_ert_attempt_07_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-07-42__track1_original_dataset_forward_ert_attempt_07_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-07-42__track1_original_dataset_forward_ert_attempt_07_campaign_validation/validation_summary.yaml`
