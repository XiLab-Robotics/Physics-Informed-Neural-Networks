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
- random seed: `15`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `25.124%`
- winning mean component MAE: `0.048874`
- winning mean component RMSE: `0.139190`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 25.124 | 0.048874 | 0.139190 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 5}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.003354 | 0.004440 | 37.551 |
| `fft_y_Bw_filtered_ampl_1` | `DT` | 0.000026 | 0.000036 | 0.150 |
| `fft_y_Bw_filtered_phase_1` | `DT` | 0.002063 | 0.003581 | 32.570 |
| `fft_y_Bw_filtered_ampl_3` | `DT` | 0.000024 | 0.000032 | 2.526 |
| `fft_y_Bw_filtered_phase_3` | `DT` | 0.029945 | 0.045645 | 2.255 |
| `fft_y_Bw_filtered_ampl_39` | `DT` | 0.000023 | 0.000031 | 5.408 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.204818 | 0.833807 | 7.293 |
| `fft_y_Bw_filtered_ampl_40` | `DT` | 0.000031 | 0.000047 | 9.996 |
| `fft_y_Bw_filtered_phase_40` | `DT` | 0.100352 | 0.193867 | 35.763 |
| `fft_y_Bw_filtered_ampl_78` | `DT` | 0.000063 | 0.000082 | 7.573 |
| `fft_y_Bw_filtered_phase_78` | `DT` | 0.054796 | 0.095808 | 23.561 |
| `fft_y_Bw_filtered_ampl_81` | `DT` | 0.000012 | 0.000018 | 9.567 |
| `fft_y_Bw_filtered_phase_81` | `DT` | 0.130201 | 0.183370 | 225.728 |
| `fft_y_Bw_filtered_ampl_156` | `DT` | 0.000066 | 0.000131 | 7.024 |
| `fft_y_Bw_filtered_phase_156` | `DT` | 0.093758 | 0.226328 | 37.089 |
| `fft_y_Bw_filtered_ampl_162` | `DT` | 0.000046 | 0.000113 | 6.640 |
| `fft_y_Bw_filtered_phase_162` | `DT` | 0.051266 | 0.080154 | 3.054 |
| `fft_y_Bw_filtered_ampl_240` | `DT` | 0.000090 | 0.000183 | 12.325 |
| `fft_y_Bw_filtered_phase_240` | `DT` | 0.257676 | 0.976934 | 11.286 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/dt/2026-04-26_track1_backward_dt_original_dataset_mega_campaign/007_track1_original_dataset_backward_dt_attempt_07.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-04-08__track1_original_dataset_backward_dt_attempt_07_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-04-08__track1_original_dataset_backward_dt_attempt_07_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-04-08__track1_original_dataset_backward_dt_attempt_07_campaign_validation/validation_summary.yaml`
