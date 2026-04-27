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
- random seed: `23`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `22.991%`
- winning mean component MAE: `0.085252`
- winning mean component RMSE: `0.186828`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 22.991 | 0.085252 | 0.186828 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 16, 'estimator__min_samples_split': 6, 'estimator__n_estimators': 50}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `RF` | 0.003211 | 0.003726 | 6.466 |
| `fft_y_Fw_filtered_ampl_1` | `RF` | 0.000029 | 0.000038 | 0.168 |
| `fft_y_Fw_filtered_phase_1` | `RF` | 0.001943 | 0.002568 | 35.290 |
| `fft_y_Fw_filtered_ampl_3` | `RF` | 0.000023 | 0.000032 | 2.794 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.018162 | 0.024868 | 1.006 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000028 | 0.000037 | 2.498 |
| `fft_y_Fw_filtered_phase_39` | `RF` | 0.024801 | 0.038077 | 2.086 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | 0.000023 | 0.000036 | 3.094 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.038403 | 0.053547 | 176.889 |
| `fft_y_Fw_filtered_ampl_78` | `RF` | 0.000047 | 0.000069 | 9.133 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.071570 | 0.134032 | 72.950 |
| `fft_y_Fw_filtered_ampl_81` | `RF` | 0.000010 | 0.000013 | 3.312 |
| `fft_y_Fw_filtered_phase_81` | `RF` | 0.050090 | 0.071302 | 5.266 |
| `fft_y_Fw_filtered_ampl_156` | `RF` | 0.000069 | 0.000224 | 24.185 |
| `fft_y_Fw_filtered_phase_156` | `RF` | 0.742269 | 1.463846 | 36.062 |
| `fft_y_Fw_filtered_ampl_162` | `RF` | 0.000106 | 0.000679 | 10.817 |
| `fft_y_Fw_filtered_phase_162` | `RF` | 0.383307 | 0.994387 | 15.957 |
| `fft_y_Fw_filtered_ampl_240` | `RF` | 0.000040 | 0.000061 | 10.742 |
| `fft_y_Fw_filtered_phase_240` | `RF` | 0.285662 | 0.762192 | 18.107 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/rf/2026-04-26_track1_forward_rf_original_dataset_mega_campaign/011_track1_original_dataset_forward_rf_attempt_11.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-36-43__track1_original_dataset_forward_rf_attempt_11_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-36-43__track1_original_dataset_forward_rf_attempt_11_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-36-43__track1_original_dataset_forward_rf_attempt_11_campaign_validation/validation_summary.yaml`
