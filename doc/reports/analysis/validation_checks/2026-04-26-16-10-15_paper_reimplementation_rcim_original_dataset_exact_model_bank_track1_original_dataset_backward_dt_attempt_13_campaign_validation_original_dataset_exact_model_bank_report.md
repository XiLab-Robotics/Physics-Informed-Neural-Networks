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
- random seed: `29`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `40.925%`
- winning mean component MAE: `0.061671`
- winning mean component RMSE: `0.174846`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 40.925 | 0.061671 | 0.174846 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 8}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.003691 | 0.004896 | 76.135 |
| `fft_y_Bw_filtered_ampl_1` | `DT` | 0.000030 | 0.000044 | 0.178 |
| `fft_y_Bw_filtered_phase_1` | `DT` | 0.001747 | 0.002342 | 132.729 |
| `fft_y_Bw_filtered_ampl_3` | `DT` | 0.000031 | 0.000051 | 3.374 |
| `fft_y_Bw_filtered_phase_3` | `DT` | 0.023216 | 0.036289 | 1.738 |
| `fft_y_Bw_filtered_ampl_39` | `DT` | 0.000026 | 0.000038 | 6.070 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.247791 | 0.929569 | 8.814 |
| `fft_y_Bw_filtered_ampl_40` | `DT` | 0.000029 | 0.000043 | 9.245 |
| `fft_y_Bw_filtered_phase_40` | `DT` | 0.127518 | 0.256509 | 31.897 |
| `fft_y_Bw_filtered_ampl_78` | `DT` | 0.000081 | 0.000109 | 9.076 |
| `fft_y_Bw_filtered_phase_78` | `DT` | 0.098868 | 0.183855 | 30.673 |
| `fft_y_Bw_filtered_ampl_81` | `DT` | 0.000011 | 0.000018 | 8.480 |
| `fft_y_Bw_filtered_phase_81` | `DT` | 0.128623 | 0.191512 | 378.092 |
| `fft_y_Bw_filtered_ampl_156` | `DT` | 0.000264 | 0.000928 | 10.849 |
| `fft_y_Bw_filtered_phase_156` | `DT` | 0.170025 | 0.662886 | 19.549 |
| `fft_y_Bw_filtered_ampl_162` | `DT` | 0.000059 | 0.000120 | 9.347 |
| `fft_y_Bw_filtered_phase_162` | `DT` | 0.056344 | 0.076302 | 3.134 |
| `fft_y_Bw_filtered_ampl_240` | `DT` | 0.000070 | 0.000128 | 14.280 |
| `fft_y_Bw_filtered_phase_240` | `DT` | 0.313321 | 0.976442 | 23.912 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/dt/2026-04-26_track1_backward_dt_original_dataset_mega_campaign/013_track1_original_dataset_backward_dt_attempt_13.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-09-30__track1_original_dataset_backward_dt_attempt_13_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-09-30__track1_original_dataset_backward_dt_attempt_13_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-09-30__track1_original_dataset_backward_dt_attempt_13_campaign_validation/validation_summary.yaml`
