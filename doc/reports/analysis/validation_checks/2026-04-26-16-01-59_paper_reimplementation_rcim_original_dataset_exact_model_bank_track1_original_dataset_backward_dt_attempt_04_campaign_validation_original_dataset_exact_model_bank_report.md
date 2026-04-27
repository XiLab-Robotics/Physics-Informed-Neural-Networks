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
- random seed: `9`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `26.128%`
- winning mean component MAE: `0.041683`
- winning mean component RMSE: `0.111486`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 26.128 | 0.041683 | 0.111486 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 17, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.003104 | 0.004082 | 96.202 |
| `fft_y_Bw_filtered_ampl_1` | `DT` | 0.000033 | 0.000046 | 0.190 |
| `fft_y_Bw_filtered_phase_1` | `DT` | 0.001942 | 0.002657 | 36.191 |
| `fft_y_Bw_filtered_ampl_3` | `DT` | 0.000025 | 0.000036 | 2.607 |
| `fft_y_Bw_filtered_phase_3` | `DT` | 0.026582 | 0.035700 | 2.032 |
| `fft_y_Bw_filtered_ampl_39` | `DT` | 0.000023 | 0.000031 | 4.917 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.221990 | 0.968058 | 7.666 |
| `fft_y_Bw_filtered_ampl_40` | `DT` | 0.000035 | 0.000049 | 11.382 |
| `fft_y_Bw_filtered_phase_40` | `DT` | 0.131114 | 0.226285 | 30.581 |
| `fft_y_Bw_filtered_ampl_78` | `DT` | 0.000057 | 0.000074 | 11.775 |
| `fft_y_Bw_filtered_phase_78` | `DT` | 0.079499 | 0.249101 | 20.586 |
| `fft_y_Bw_filtered_ampl_81` | `DT` | 0.000012 | 0.000019 | 9.100 |
| `fft_y_Bw_filtered_phase_81` | `DT` | 0.100719 | 0.145815 | 222.126 |
| `fft_y_Bw_filtered_ampl_156` | `DT` | 0.000230 | 0.000774 | 8.203 |
| `fft_y_Bw_filtered_phase_156` | `DT` | 0.070388 | 0.116446 | 8.077 |
| `fft_y_Bw_filtered_ampl_162` | `DT` | 0.000082 | 0.000308 | 6.725 |
| `fft_y_Bw_filtered_phase_162` | `DT` | 0.055089 | 0.078278 | 3.174 |
| `fft_y_Bw_filtered_ampl_240` | `DT` | 0.000084 | 0.000226 | 8.951 |
| `fft_y_Bw_filtered_phase_240` | `DT` | 0.100961 | 0.290239 | 5.947 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/dt/2026-04-26_track1_backward_dt_original_dataset_mega_campaign/004_track1_original_dataset_backward_dt_attempt_04.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-01-13__track1_original_dataset_backward_dt_attempt_04_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-01-13__track1_original_dataset_backward_dt_attempt_04_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-01-13__track1_original_dataset_backward_dt_attempt_04_campaign_validation/validation_summary.yaml`
