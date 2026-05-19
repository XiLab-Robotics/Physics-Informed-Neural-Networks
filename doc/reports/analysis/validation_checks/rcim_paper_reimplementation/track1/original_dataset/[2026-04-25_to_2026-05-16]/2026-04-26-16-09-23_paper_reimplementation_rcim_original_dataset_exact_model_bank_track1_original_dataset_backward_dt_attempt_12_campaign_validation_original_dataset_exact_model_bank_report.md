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
- random seed: `27`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `15.264%`
- winning mean component MAE: `0.050072`
- winning mean component RMSE: `0.149689`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 15.264 | 0.050072 | 0.149689 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 7}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.002818 | 0.003842 | 24.617 |
| `fft_y_Bw_filtered_ampl_1` | `DT` | 0.000029 | 0.000039 | 0.167 |
| `fft_y_Bw_filtered_phase_1` | `DT` | 0.001905 | 0.002862 | 36.432 |
| `fft_y_Bw_filtered_ampl_3` | `DT` | 0.000029 | 0.000042 | 2.863 |
| `fft_y_Bw_filtered_phase_3` | `DT` | 0.027509 | 0.039145 | 2.115 |
| `fft_y_Bw_filtered_ampl_39` | `DT` | 0.000023 | 0.000034 | 5.017 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.174865 | 0.882830 | 6.138 |
| `fft_y_Bw_filtered_ampl_40` | `DT` | 0.000035 | 0.000052 | 12.067 |
| `fft_y_Bw_filtered_phase_40` | `DT` | 0.101033 | 0.185499 | 61.447 |
| `fft_y_Bw_filtered_ampl_78` | `DT` | 0.000070 | 0.000095 | 7.545 |
| `fft_y_Bw_filtered_phase_78` | `DT` | 0.061447 | 0.118046 | 25.004 |
| `fft_y_Bw_filtered_ampl_81` | `DT` | 0.000012 | 0.000019 | 10.039 |
| `fft_y_Bw_filtered_phase_81` | `DT` | 0.111503 | 0.156808 | 31.223 |
| `fft_y_Bw_filtered_ampl_156` | `DT` | 0.000229 | 0.000684 | 9.174 |
| `fft_y_Bw_filtered_phase_156` | `DT` | 0.112059 | 0.416910 | 7.466 |
| `fft_y_Bw_filtered_ampl_162` | `DT` | 0.000062 | 0.000134 | 7.227 |
| `fft_y_Bw_filtered_phase_162` | `DT` | 0.062613 | 0.129981 | 3.567 |
| `fft_y_Bw_filtered_ampl_240` | `DT` | 0.000095 | 0.000198 | 14.335 |
| `fft_y_Bw_filtered_phase_240` | `DT` | 0.295038 | 0.906877 | 23.576 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/dt/2026-04-26_track1_backward_dt_original_dataset_mega_campaign/012_track1_original_dataset_backward_dt_attempt_12.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-08-37__track1_original_dataset_backward_dt_attempt_12_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-08-37__track1_original_dataset_backward_dt_attempt_12_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-08-37__track1_original_dataset_backward_dt_attempt_12_campaign_validation/validation_summary.yaml`
