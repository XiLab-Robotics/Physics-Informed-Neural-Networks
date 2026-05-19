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
- random seed: `23`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `26.891%`
- winning mean component MAE: `0.093177`
- winning mean component RMSE: `0.221374`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 26.891 | 0.093177 | 0.221374 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 8}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.003853 | 0.004587 | 7.580 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000034 | 0.000045 | 0.197 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.002438 | 0.003478 | 57.715 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000023 | 0.000031 | 2.823 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.023184 | 0.030571 | 1.276 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000045 | 0.000057 | 4.009 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.031511 | 0.045016 | 2.626 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000029 | 0.000043 | 3.812 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.048216 | 0.070306 | 172.658 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000062 | 0.000088 | 10.458 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.096433 | 0.184224 | 105.577 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000014 | 0.000019 | 4.404 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.067973 | 0.096791 | 7.682 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000099 | 0.000340 | 29.146 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.802126 | 1.654499 | 37.589 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000130 | 0.000811 | 11.203 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.355759 | 1.128797 | 14.995 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000052 | 0.000082 | 13.516 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.338389 | 0.986328 | 23.654 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/dt/2026-04-26_track1_forward_dt_original_dataset_mega_campaign/011_track1_original_dataset_forward_dt_attempt_11.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-19-21__track1_original_dataset_forward_dt_attempt_11_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-19-21__track1_original_dataset_forward_dt_attempt_11_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-19-21__track1_original_dataset_forward_dt_attempt_11_campaign_validation/validation_summary.yaml`
