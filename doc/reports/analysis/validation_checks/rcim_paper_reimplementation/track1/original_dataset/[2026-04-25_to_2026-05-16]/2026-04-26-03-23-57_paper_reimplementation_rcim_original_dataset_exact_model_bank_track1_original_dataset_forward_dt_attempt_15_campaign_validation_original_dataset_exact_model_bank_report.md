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
- random seed: `37`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `23.312%`
- winning mean component MAE: `0.073713`
- winning mean component RMSE: `0.185240`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 23.312 | 0.073713 | 0.185240 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 16, 'estimator__min_samples_split': 7}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.003153 | 0.003986 | 6.614 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000027 | 0.000035 | 0.155 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.001974 | 0.002481 | 65.392 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000020 | 0.000027 | 2.521 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.024896 | 0.033104 | 1.389 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000036 | 0.000046 | 3.252 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.026610 | 0.040329 | 2.143 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000030 | 0.000045 | 3.686 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.043049 | 0.065099 | 55.453 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000056 | 0.000078 | 10.179 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.088324 | 0.209028 | 164.695 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000012 | 0.000016 | 3.969 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.064364 | 0.092546 | 7.891 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000114 | 0.000338 | 21.440 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.573361 | 1.305713 | 37.477 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000052 | 0.000148 | 9.958 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.372600 | 1.136178 | 14.280 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000048 | 0.000097 | 13.733 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.201821 | 0.630258 | 18.706 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/dt/2026-04-26_track1_forward_dt_original_dataset_mega_campaign/015_track1_original_dataset_forward_dt_attempt_15.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-23-08__track1_original_dataset_forward_dt_attempt_15_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-23-08__track1_original_dataset_forward_dt_attempt_15_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-23-08__track1_original_dataset_forward_dt_attempt_15_campaign_validation/validation_summary.yaml`
