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

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `23.552%`
- winning mean component MAE: `0.098102`
- winning mean component RMSE: `0.268916`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 23.552 | 0.098102 | 0.268916 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 16, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.003867 | 0.005056 | 8.390 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000033 | 0.000051 | 0.193 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.002788 | 0.004624 | 66.239 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000029 | 0.000060 | 3.465 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.028280 | 0.039682 | 1.544 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000042 | 0.000063 | 3.863 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.035966 | 0.061351 | 2.868 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000028 | 0.000038 | 3.552 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.045047 | 0.079783 | 58.765 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000051 | 0.000072 | 11.084 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.152522 | 0.541606 | 155.775 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000015 | 0.000024 | 4.394 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.075047 | 0.132358 | 8.607 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000051 | 0.000208 | 19.993 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.536286 | 1.344628 | 34.474 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000058 | 0.000192 | 8.724 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.540222 | 1.590396 | 19.524 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000042 | 0.000065 | 15.336 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.443555 | 1.309153 | 20.693 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/dt/2026-04-26_track1_forward_dt_original_dataset_mega_campaign/014_track1_original_dataset_forward_dt_attempt_14.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-22-12__track1_original_dataset_forward_dt_attempt_14_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-22-12__track1_original_dataset_forward_dt_attempt_14_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-22-12__track1_original_dataset_forward_dt_attempt_14_campaign_validation/validation_summary.yaml`
