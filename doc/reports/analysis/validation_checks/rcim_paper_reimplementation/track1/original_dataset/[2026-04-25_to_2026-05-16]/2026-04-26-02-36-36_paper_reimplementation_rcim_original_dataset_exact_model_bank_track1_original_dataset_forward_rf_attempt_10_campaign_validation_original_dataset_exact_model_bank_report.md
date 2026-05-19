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
- random seed: `21`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `20.961%`
- winning mean component MAE: `0.069613`
- winning mean component RMSE: `0.158751`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 20.961 | 0.069613 | 0.158751 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 50}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `RF` | 0.002824 | 0.003424 | 5.750 |
| `fft_y_Fw_filtered_ampl_1` | `RF` | 0.000031 | 0.000039 | 0.180 |
| `fft_y_Fw_filtered_phase_1` | `RF` | 0.001919 | 0.002663 | 28.887 |
| `fft_y_Fw_filtered_ampl_3` | `RF` | 0.000025 | 0.000034 | 3.047 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.022306 | 0.029673 | 1.217 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000027 | 0.000037 | 2.325 |
| `fft_y_Fw_filtered_phase_39` | `RF` | 0.027287 | 0.048749 | 2.150 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | 0.000024 | 0.000037 | 3.098 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.033528 | 0.051141 | 140.607 |
| `fft_y_Fw_filtered_ampl_78` | `RF` | 0.000044 | 0.000066 | 8.443 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.071811 | 0.168970 | 71.214 |
| `fft_y_Fw_filtered_ampl_81` | `RF` | 0.000010 | 0.000013 | 3.206 |
| `fft_y_Fw_filtered_phase_81` | `RF` | 0.058716 | 0.096554 | 5.181 |
| `fft_y_Fw_filtered_ampl_156` | `RF` | 0.000094 | 0.000309 | 11.332 |
| `fft_y_Fw_filtered_phase_156` | `RF` | 0.523522 | 1.095513 | 44.217 |
| `fft_y_Fw_filtered_ampl_162` | `RF` | 0.000110 | 0.000303 | 14.158 |
| `fft_y_Fw_filtered_phase_162` | `RF` | 0.250053 | 0.624808 | 9.725 |
| `fft_y_Fw_filtered_ampl_240` | `RF` | 0.000056 | 0.000138 | 8.998 |
| `fft_y_Fw_filtered_phase_240` | `RF` | 0.330259 | 0.893807 | 34.518 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/rf/2026-04-26_track1_forward_rf_original_dataset_mega_campaign/010_track1_original_dataset_forward_rf_attempt_10.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-33-24__track1_original_dataset_forward_rf_attempt_10_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-33-24__track1_original_dataset_forward_rf_attempt_10_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-33-24__track1_original_dataset_forward_rf_attempt_10_campaign_validation/validation_summary.yaml`
