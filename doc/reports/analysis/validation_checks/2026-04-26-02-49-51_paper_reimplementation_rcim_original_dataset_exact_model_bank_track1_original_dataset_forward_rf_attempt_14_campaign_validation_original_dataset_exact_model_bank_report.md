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

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `44.159%`
- winning mean component MAE: `0.083695`
- winning mean component RMSE: `0.200589`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 44.159 | 0.083695 | 0.200589 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 12, 'estimator__min_samples_split': 2, 'estimator__n_estimators': 60}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `RF` | 0.003461 | 0.004471 | 7.758 |
| `fft_y_Fw_filtered_ampl_1` | `RF` | 0.000028 | 0.000041 | 0.164 |
| `fft_y_Fw_filtered_phase_1` | `RF` | 0.002385 | 0.003837 | 50.563 |
| `fft_y_Fw_filtered_ampl_3` | `RF` | 0.000023 | 0.000052 | 2.804 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.025004 | 0.042425 | 1.369 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000029 | 0.000048 | 2.741 |
| `fft_y_Fw_filtered_phase_39` | `RF` | 0.029826 | 0.052861 | 2.383 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | 0.000026 | 0.000038 | 3.286 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.034216 | 0.058124 | 53.359 |
| `fft_y_Fw_filtered_ampl_78` | `RF` | 0.000038 | 0.000056 | 7.885 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.106980 | 0.411146 | 595.106 |
| `fft_y_Fw_filtered_ampl_81` | `RF` | 0.000011 | 0.000019 | 3.165 |
| `fft_y_Fw_filtered_phase_81` | `RF` | 0.059583 | 0.104631 | 6.514 |
| `fft_y_Fw_filtered_ampl_156` | `RF` | 0.000041 | 0.000111 | 17.431 |
| `fft_y_Fw_filtered_phase_156` | `RF` | 0.519268 | 0.994850 | 30.683 |
| `fft_y_Fw_filtered_ampl_162` | `RF` | 0.000050 | 0.000197 | 7.888 |
| `fft_y_Fw_filtered_phase_162` | `RF` | 0.411724 | 1.098411 | 14.953 |
| `fft_y_Fw_filtered_ampl_240` | `RF` | 0.000035 | 0.000053 | 13.424 |
| `fft_y_Fw_filtered_phase_240` | `RF` | 0.397480 | 1.039815 | 17.544 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/rf/2026-04-26_track1_forward_rf_original_dataset_mega_campaign/014_track1_original_dataset_forward_rf_attempt_14.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-46-35__track1_original_dataset_forward_rf_attempt_14_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-46-35__track1_original_dataset_forward_rf_attempt_14_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-46-35__track1_original_dataset_forward_rf_attempt_14_campaign_validation/validation_summary.yaml`
