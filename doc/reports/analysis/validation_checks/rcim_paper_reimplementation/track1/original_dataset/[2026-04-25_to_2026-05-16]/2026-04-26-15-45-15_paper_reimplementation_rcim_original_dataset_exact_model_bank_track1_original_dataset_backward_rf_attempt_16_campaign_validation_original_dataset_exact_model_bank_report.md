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
- random seed: `42`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `18.994%`
- winning mean component MAE: `0.034930`
- winning mean component RMSE: `0.086777`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 18.994 | 0.034930 | 0.086777 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 12, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 90}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `RF` | 0.002888 | 0.003441 | 42.985 |
| `fft_y_Bw_filtered_ampl_1` | `RF` | 0.000024 | 0.000033 | 0.138 |
| `fft_y_Bw_filtered_phase_1` | `RF` | 0.001522 | 0.002026 | 50.947 |
| `fft_y_Bw_filtered_ampl_3` | `RF` | 0.000022 | 0.000032 | 2.129 |
| `fft_y_Bw_filtered_phase_3` | `RF` | 0.023951 | 0.031275 | 1.830 |
| `fft_y_Bw_filtered_ampl_39` | `RF` | 0.000019 | 0.000027 | 4.120 |
| `fft_y_Bw_filtered_phase_39` | `RF` | 0.200462 | 0.688546 | 6.940 |
| `fft_y_Bw_filtered_ampl_40` | `RF` | 0.000030 | 0.000044 | 9.816 |
| `fft_y_Bw_filtered_phase_40` | `RF` | 0.080088 | 0.157445 | 35.126 |
| `fft_y_Bw_filtered_ampl_78` | `RF` | 0.000043 | 0.000056 | 6.295 |
| `fft_y_Bw_filtered_phase_78` | `RF` | 0.058082 | 0.133320 | 44.336 |
| `fft_y_Bw_filtered_ampl_81` | `RF` | 0.000009 | 0.000014 | 7.123 |
| `fft_y_Bw_filtered_phase_81` | `RF` | 0.082119 | 0.111865 | 114.682 |
| `fft_y_Bw_filtered_ampl_156` | `RF` | 0.000079 | 0.000270 | 6.061 |
| `fft_y_Bw_filtered_phase_156` | `RF` | 0.059770 | 0.216907 | 5.611 |
| `fft_y_Bw_filtered_ampl_162` | `RF` | 0.000053 | 0.000163 | 6.607 |
| `fft_y_Bw_filtered_phase_162` | `RF` | 0.052436 | 0.099062 | 2.777 |
| `fft_y_Bw_filtered_ampl_240` | `RF` | 0.000062 | 0.000176 | 7.629 |
| `fft_y_Bw_filtered_phase_240` | `RF` | 0.102019 | 0.204064 | 5.737 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/rf/2026-04-26_track1_backward_rf_original_dataset_mega_campaign/016_track1_original_dataset_backward_rf_attempt_16.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-42-05__track1_original_dataset_backward_rf_attempt_16_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-42-05__track1_original_dataset_backward_rf_attempt_16_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-42-05__track1_original_dataset_backward_rf_attempt_16_campaign_validation/validation_summary.yaml`
