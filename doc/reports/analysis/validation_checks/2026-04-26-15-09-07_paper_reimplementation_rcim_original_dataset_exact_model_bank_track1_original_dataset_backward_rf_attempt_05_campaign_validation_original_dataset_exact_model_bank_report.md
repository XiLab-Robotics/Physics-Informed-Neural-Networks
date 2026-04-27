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
- random seed: `11`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `29.918%`
- winning mean component MAE: `0.045150`
- winning mean component RMSE: `0.123625`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 29.918 | 0.045150 | 0.123625 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 70}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `RF` | 0.003092 | 0.003672 | 71.619 |
| `fft_y_Bw_filtered_ampl_1` | `RF` | 0.000027 | 0.000036 | 0.158 |
| `fft_y_Bw_filtered_phase_1` | `RF` | 0.001633 | 0.002200 | 74.498 |
| `fft_y_Bw_filtered_ampl_3` | `RF` | 0.000020 | 0.000029 | 1.968 |
| `fft_y_Bw_filtered_phase_3` | `RF` | 0.024223 | 0.035899 | 1.815 |
| `fft_y_Bw_filtered_ampl_39` | `RF` | 0.000017 | 0.000024 | 3.877 |
| `fft_y_Bw_filtered_phase_39` | `RF` | 0.211779 | 0.753799 | 7.396 |
| `fft_y_Bw_filtered_ampl_40` | `RF` | 0.000034 | 0.000051 | 10.872 |
| `fft_y_Bw_filtered_phase_40` | `RF` | 0.077646 | 0.117302 | 120.377 |
| `fft_y_Bw_filtered_ampl_78` | `RF` | 0.000040 | 0.000055 | 4.649 |
| `fft_y_Bw_filtered_phase_78` | `RF` | 0.042213 | 0.082843 | 18.693 |
| `fft_y_Bw_filtered_ampl_81` | `RF` | 0.000008 | 0.000014 | 6.668 |
| `fft_y_Bw_filtered_phase_81` | `RF` | 0.087570 | 0.122613 | 191.964 |
| `fft_y_Bw_filtered_ampl_156` | `RF` | 0.000128 | 0.000388 | 9.248 |
| `fft_y_Bw_filtered_phase_156` | `RF` | 0.138112 | 0.397849 | 8.715 |
| `fft_y_Bw_filtered_ampl_162` | `RF` | 0.000061 | 0.000191 | 6.594 |
| `fft_y_Bw_filtered_phase_162` | `RF` | 0.076270 | 0.200064 | 5.500 |
| `fft_y_Bw_filtered_ampl_240` | `RF` | 0.000073 | 0.000166 | 10.546 |
| `fft_y_Bw_filtered_phase_240` | `RF` | 0.194901 | 0.631686 | 13.277 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/rf/2026-04-26_track1_backward_rf_original_dataset_mega_campaign/005_track1_original_dataset_backward_rf_attempt_05.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-05-54__track1_original_dataset_backward_rf_attempt_05_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-05-54__track1_original_dataset_backward_rf_attempt_05_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-05-54__track1_original_dataset_backward_rf_attempt_05_campaign_validation/validation_summary.yaml`
