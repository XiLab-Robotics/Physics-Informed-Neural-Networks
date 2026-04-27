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
- random seed: `17`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `16.250%`
- winning mean component MAE: `0.052087`
- winning mean component RMSE: `0.124141`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 16.250 | 0.052087 | 0.124141 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 12, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 90}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `RF` | 0.003008 | 0.003597 | 5.617 |
| `fft_y_Fw_filtered_ampl_1` | `RF` | 0.000024 | 0.000033 | 0.142 |
| `fft_y_Fw_filtered_phase_1` | `RF` | 0.001912 | 0.002433 | 36.795 |
| `fft_y_Fw_filtered_ampl_3` | `RF` | 0.000021 | 0.000032 | 2.557 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.020719 | 0.026809 | 1.134 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000028 | 0.000036 | 2.444 |
| `fft_y_Fw_filtered_phase_39` | `RF` | 0.019414 | 0.028656 | 1.751 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | 0.000021 | 0.000029 | 2.603 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.038624 | 0.061916 | 79.221 |
| `fft_y_Fw_filtered_ampl_78` | `RF` | 0.000038 | 0.000054 | 10.112 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.054204 | 0.094089 | 93.552 |
| `fft_y_Fw_filtered_ampl_81` | `RF` | 0.000010 | 0.000013 | 3.289 |
| `fft_y_Fw_filtered_phase_81` | `RF` | 0.051588 | 0.068980 | 4.709 |
| `fft_y_Fw_filtered_ampl_156` | `RF` | 0.000043 | 0.000109 | 12.372 |
| `fft_y_Fw_filtered_phase_156` | `RF` | 0.455616 | 1.008904 | 22.585 |
| `fft_y_Fw_filtered_ampl_162` | `RF` | 0.000038 | 0.000092 | 6.097 |
| `fft_y_Fw_filtered_phase_162` | `RF` | 0.167809 | 0.499705 | 7.149 |
| `fft_y_Fw_filtered_ampl_240` | `RF` | 0.000033 | 0.000073 | 7.155 |
| `fft_y_Fw_filtered_phase_240` | `RF` | 0.176495 | 0.563109 | 9.470 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/rf/2026-04-26_track1_forward_rf_original_dataset_mega_campaign/008_track1_original_dataset_forward_rf_attempt_08.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-26-48__track1_original_dataset_forward_rf_attempt_08_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-26-48__track1_original_dataset_forward_rf_attempt_08_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-26-48__track1_original_dataset_forward_rf_attempt_08_campaign_validation/validation_summary.yaml`
