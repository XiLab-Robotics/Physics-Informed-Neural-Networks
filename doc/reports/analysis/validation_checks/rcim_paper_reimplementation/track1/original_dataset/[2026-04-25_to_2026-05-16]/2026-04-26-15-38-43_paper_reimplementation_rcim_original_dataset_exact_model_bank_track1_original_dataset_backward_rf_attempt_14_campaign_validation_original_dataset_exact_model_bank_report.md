# Original-Dataset Exact RCIM Model Bank Validation Report

## Overview

This report covers the direction-specific exact-model-bank branch trained from the repository dataset under `data/datasets`.

- direction label: `backward`
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

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `21.204%`
- winning mean component MAE: `0.047373`
- winning mean component RMSE: `0.124594`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 21.204 | 0.047373 | 0.124594 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 13, 'estimator__min_samples_split': 2, 'estimator__n_estimators': 70}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `RF` | 0.003279 | 0.004104 | 44.606 |
| `fft_y_Bw_filtered_ampl_1` | `RF` | 0.000024 | 0.000034 | 0.140 |
| `fft_y_Bw_filtered_phase_1` | `RF` | 0.001894 | 0.003486 | 132.832 |
| `fft_y_Bw_filtered_ampl_3` | `RF` | 0.000021 | 0.000038 | 2.296 |
| `fft_y_Bw_filtered_phase_3` | `RF` | 0.025461 | 0.044687 | 1.827 |
| `fft_y_Bw_filtered_ampl_39` | `RF` | 0.000018 | 0.000025 | 4.420 |
| `fft_y_Bw_filtered_phase_39` | `RF` | 0.167522 | 0.539509 | 6.099 |
| `fft_y_Bw_filtered_ampl_40` | `RF` | 0.000024 | 0.000033 | 8.506 |
| `fft_y_Bw_filtered_phase_40` | `RF` | 0.086986 | 0.179483 | 33.616 |
| `fft_y_Bw_filtered_ampl_78` | `RF` | 0.000045 | 0.000066 | 6.303 |
| `fft_y_Bw_filtered_phase_78` | `RF` | 0.064131 | 0.129434 | 33.909 |
| `fft_y_Bw_filtered_ampl_81` | `RF` | 0.000011 | 0.000019 | 7.721 |
| `fft_y_Bw_filtered_phase_81` | `RF` | 0.100565 | 0.155524 | 60.676 |
| `fft_y_Bw_filtered_ampl_156` | `RF` | 0.000080 | 0.000229 | 7.406 |
| `fft_y_Bw_filtered_phase_156` | `RF` | 0.086618 | 0.230980 | 15.406 |
| `fft_y_Bw_filtered_ampl_162` | `RF` | 0.000052 | 0.000191 | 6.454 |
| `fft_y_Bw_filtered_phase_162` | `RF` | 0.083963 | 0.218297 | 4.105 |
| `fft_y_Bw_filtered_ampl_240` | `RF` | 0.000051 | 0.000090 | 13.218 |
| `fft_y_Bw_filtered_phase_240` | `RF` | 0.279347 | 0.861056 | 13.334 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/rf/2026-04-26_track1_backward_rf_original_dataset_mega_campaign/014_track1_original_dataset_backward_rf_attempt_14.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-35-28__track1_original_dataset_backward_rf_attempt_14_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-35-28__track1_original_dataset_backward_rf_attempt_14_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-35-28__track1_original_dataset_backward_rf_attempt_14_campaign_validation/validation_summary.yaml`
