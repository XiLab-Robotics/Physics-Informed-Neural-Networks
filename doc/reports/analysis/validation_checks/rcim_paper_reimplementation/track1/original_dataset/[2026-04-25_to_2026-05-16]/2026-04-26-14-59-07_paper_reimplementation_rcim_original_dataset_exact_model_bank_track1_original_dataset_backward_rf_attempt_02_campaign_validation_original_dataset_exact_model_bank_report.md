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
- random seed: `5`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `14.907%`
- winning mean component MAE: `0.045817`
- winning mean component RMSE: `0.113641`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 14.907 | 0.045817 | 0.113641 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 12, 'estimator__min_samples_split': 2, 'estimator__n_estimators': 70}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `RF` | 0.002482 | 0.003348 | 38.630 |
| `fft_y_Bw_filtered_ampl_1` | `RF` | 0.000024 | 0.000032 | 0.140 |
| `fft_y_Bw_filtered_phase_1` | `RF` | 0.001836 | 0.002340 | 50.912 |
| `fft_y_Bw_filtered_ampl_3` | `RF` | 0.000021 | 0.000031 | 2.084 |
| `fft_y_Bw_filtered_phase_3` | `RF` | 0.023939 | 0.032916 | 1.865 |
| `fft_y_Bw_filtered_ampl_39` | `RF` | 0.000019 | 0.000028 | 4.171 |
| `fft_y_Bw_filtered_phase_39` | `RF` | 0.160568 | 0.439565 | 5.771 |
| `fft_y_Bw_filtered_ampl_40` | `RF` | 0.000026 | 0.000037 | 9.046 |
| `fft_y_Bw_filtered_phase_40` | `RF` | 0.092420 | 0.183556 | 42.082 |
| `fft_y_Bw_filtered_ampl_78` | `RF` | 0.000046 | 0.000059 | 6.179 |
| `fft_y_Bw_filtered_phase_78` | `RF` | 0.074591 | 0.159566 | 25.974 |
| `fft_y_Bw_filtered_ampl_81` | `RF` | 0.000009 | 0.000015 | 7.330 |
| `fft_y_Bw_filtered_phase_81` | `RF` | 0.088639 | 0.119931 | 27.462 |
| `fft_y_Bw_filtered_ampl_156` | `RF` | 0.000109 | 0.000456 | 11.875 |
| `fft_y_Bw_filtered_phase_156` | `RF` | 0.148566 | 0.551364 | 17.718 |
| `fft_y_Bw_filtered_ampl_162` | `RF` | 0.000068 | 0.000218 | 8.614 |
| `fft_y_Bw_filtered_phase_162` | `RF` | 0.048660 | 0.082443 | 2.765 |
| `fft_y_Bw_filtered_ampl_240` | `RF` | 0.000069 | 0.000142 | 9.847 |
| `fft_y_Bw_filtered_phase_240` | `RF` | 0.228430 | 0.583140 | 10.762 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/rf/2026-04-26_track1_backward_rf_original_dataset_mega_campaign/002_track1_original_dataset_backward_rf_attempt_02.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-55-50__track1_original_dataset_backward_rf_attempt_02_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-55-50__track1_original_dataset_backward_rf_attempt_02_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-55-50__track1_original_dataset_backward_rf_attempt_02_campaign_validation/validation_summary.yaml`
