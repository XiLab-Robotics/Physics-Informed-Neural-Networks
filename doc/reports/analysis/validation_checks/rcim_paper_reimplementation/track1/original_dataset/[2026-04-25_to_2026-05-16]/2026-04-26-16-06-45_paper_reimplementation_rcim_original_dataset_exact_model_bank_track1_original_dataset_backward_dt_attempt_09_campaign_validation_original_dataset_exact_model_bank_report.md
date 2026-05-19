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
- random seed: `19`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `21.512%`
- winning mean component MAE: `0.055689`
- winning mean component RMSE: `0.151344`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 21.512 | 0.055689 | 0.151344 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 8}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.003111 | 0.004538 | 41.996 |
| `fft_y_Bw_filtered_ampl_1` | `DT` | 0.000028 | 0.000041 | 0.165 |
| `fft_y_Bw_filtered_phase_1` | `DT` | 0.001945 | 0.003319 | 72.412 |
| `fft_y_Bw_filtered_ampl_3` | `DT` | 0.000022 | 0.000031 | 2.317 |
| `fft_y_Bw_filtered_phase_3` | `DT` | 0.026016 | 0.036885 | 1.979 |
| `fft_y_Bw_filtered_ampl_39` | `DT` | 0.000020 | 0.000031 | 4.764 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.366744 | 1.405443 | 12.438 |
| `fft_y_Bw_filtered_ampl_40` | `DT` | 0.000029 | 0.000044 | 9.862 |
| `fft_y_Bw_filtered_phase_40` | `DT` | 0.108413 | 0.169615 | 36.699 |
| `fft_y_Bw_filtered_ampl_78` | `DT` | 0.000062 | 0.000081 | 8.027 |
| `fft_y_Bw_filtered_phase_78` | `DT` | 0.071845 | 0.138779 | 51.137 |
| `fft_y_Bw_filtered_ampl_81` | `DT` | 0.000012 | 0.000021 | 10.360 |
| `fft_y_Bw_filtered_phase_81` | `DT` | 0.100252 | 0.153189 | 71.838 |
| `fft_y_Bw_filtered_ampl_156` | `DT` | 0.000225 | 0.000718 | 12.553 |
| `fft_y_Bw_filtered_phase_156` | `DT` | 0.069783 | 0.162913 | 20.673 |
| `fft_y_Bw_filtered_ampl_162` | `DT` | 0.000132 | 0.000460 | 7.686 |
| `fft_y_Bw_filtered_phase_162` | `DT` | 0.060446 | 0.107749 | 3.377 |
| `fft_y_Bw_filtered_ampl_240` | `DT` | 0.000072 | 0.000128 | 13.946 |
| `fft_y_Bw_filtered_phase_240` | `DT` | 0.248934 | 0.691559 | 26.508 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/dt/2026-04-26_track1_backward_dt_original_dataset_mega_campaign/009_track1_original_dataset_backward_dt_attempt_09.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-05-58__track1_original_dataset_backward_dt_attempt_09_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-05-58__track1_original_dataset_backward_dt_attempt_09_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-05-58__track1_original_dataset_backward_dt_attempt_09_campaign_validation/validation_summary.yaml`
