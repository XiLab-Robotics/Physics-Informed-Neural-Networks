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
- random seed: `0`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `17.636%`
- winning mean component MAE: `0.039916`
- winning mean component RMSE: `0.120494`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 17.636 | 0.039916 | 0.120494 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 13, 'estimator__min_samples_split': 2, 'estimator__n_estimators': 90}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `RF` | 0.003235 | 0.003949 | 129.837 |
| `fft_y_Bw_filtered_ampl_1` | `RF` | 0.000021 | 0.000030 | 0.124 |
| `fft_y_Bw_filtered_phase_1` | `RF` | 0.001533 | 0.002091 | 19.862 |
| `fft_y_Bw_filtered_ampl_3` | `RF` | 0.000020 | 0.000029 | 2.069 |
| `fft_y_Bw_filtered_phase_3` | `RF` | 0.021296 | 0.030342 | 1.584 |
| `fft_y_Bw_filtered_ampl_39` | `RF` | 0.000018 | 0.000023 | 4.069 |
| `fft_y_Bw_filtered_phase_39` | `RF` | 0.211416 | 0.876901 | 7.290 |
| `fft_y_Bw_filtered_ampl_40` | `RF` | 0.000023 | 0.000032 | 7.673 |
| `fft_y_Bw_filtered_phase_40` | `RF` | 0.082224 | 0.110211 | 33.398 |
| `fft_y_Bw_filtered_ampl_78` | `RF` | 0.000035 | 0.000046 | 3.862 |
| `fft_y_Bw_filtered_phase_78` | `RF` | 0.034844 | 0.059512 | 30.550 |
| `fft_y_Bw_filtered_ampl_81` | `RF` | 0.000009 | 0.000013 | 7.801 |
| `fft_y_Bw_filtered_phase_81` | `RF` | 0.081059 | 0.117700 | 39.210 |
| `fft_y_Bw_filtered_ampl_156` | `RF` | 0.000126 | 0.000513 | 7.712 |
| `fft_y_Bw_filtered_phase_156` | `RF` | 0.087012 | 0.356327 | 9.169 |
| `fft_y_Bw_filtered_ampl_162` | `RF` | 0.000062 | 0.000263 | 6.017 |
| `fft_y_Bw_filtered_phase_162` | `RF` | 0.049375 | 0.088517 | 2.675 |
| `fft_y_Bw_filtered_ampl_240` | `RF` | 0.000094 | 0.000269 | 11.148 |
| `fft_y_Bw_filtered_phase_240` | `RF` | 0.186010 | 0.642627 | 11.027 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/rf/2026-04-26_track1_backward_rf_original_dataset_mega_campaign/001_track1_original_dataset_backward_rf_attempt_01.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-52-26__track1_original_dataset_backward_rf_attempt_01_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-52-26__track1_original_dataset_backward_rf_attempt_01_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-52-26__track1_original_dataset_backward_rf_attempt_01_campaign_validation/validation_summary.yaml`
