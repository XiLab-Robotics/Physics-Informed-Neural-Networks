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
- random seed: `53`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `85.506%`
- winning mean component MAE: `0.072022`
- winning mean component RMSE: `0.173028`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 85.506 | 0.072022 | 0.173028 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 13, 'estimator__min_samples_split': 2, 'estimator__n_estimators': 90}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `RF` | 0.002878 | 0.003543 | 7.615 |
| `fft_y_Fw_filtered_ampl_1` | `RF` | 0.000027 | 0.000043 | 0.160 |
| `fft_y_Fw_filtered_phase_1` | `RF` | 0.002528 | 0.003641 | 1313.806 |
| `fft_y_Fw_filtered_ampl_3` | `RF` | 0.000024 | 0.000038 | 3.031 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.029892 | 0.065566 | 1.607 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000028 | 0.000041 | 2.489 |
| `fft_y_Fw_filtered_phase_39` | `RF` | 0.030492 | 0.059446 | 2.292 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | 0.000030 | 0.000051 | 3.883 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.044626 | 0.073588 | 86.978 |
| `fft_y_Fw_filtered_ampl_78` | `RF` | 0.000044 | 0.000059 | 12.151 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.104388 | 0.257238 | 69.700 |
| `fft_y_Fw_filtered_ampl_81` | `RF` | 0.000011 | 0.000018 | 3.699 |
| `fft_y_Fw_filtered_phase_81` | `RF` | 0.057072 | 0.096003 | 5.552 |
| `fft_y_Fw_filtered_ampl_156` | `RF` | 0.000096 | 0.000286 | 14.227 |
| `fft_y_Fw_filtered_phase_156` | `RF` | 0.415141 | 0.891299 | 47.392 |
| `fft_y_Fw_filtered_ampl_162` | `RF` | 0.000055 | 0.000135 | 9.193 |
| `fft_y_Fw_filtered_phase_162` | `RF` | 0.327878 | 0.935662 | 14.493 |
| `fft_y_Fw_filtered_ampl_240` | `RF` | 0.000029 | 0.000044 | 9.843 |
| `fft_y_Fw_filtered_phase_240` | `RF` | 0.353170 | 0.900821 | 16.504 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/rf/2026-04-26_track1_forward_rf_original_dataset_mega_campaign/018_track1_original_dataset_forward_rf_attempt_18.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-00-03__track1_original_dataset_forward_rf_attempt_18_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-00-03__track1_original_dataset_forward_rf_attempt_18_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-00-03__track1_original_dataset_forward_rf_attempt_18_campaign_validation/validation_summary.yaml`
