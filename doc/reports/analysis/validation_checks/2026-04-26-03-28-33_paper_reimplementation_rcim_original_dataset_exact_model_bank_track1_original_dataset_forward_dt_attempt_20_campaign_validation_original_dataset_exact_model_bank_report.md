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
- random seed: `61`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `25.497%`
- winning mean component MAE: `0.074024`
- winning mean component RMSE: `0.196698`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 25.497 | 0.074024 | 0.196698 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.003160 | 0.004009 | 6.618 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000034 | 0.000044 | 0.195 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.002169 | 0.002772 | 44.492 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000022 | 0.000033 | 2.834 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.026447 | 0.035506 | 1.473 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000035 | 0.000050 | 3.167 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.024787 | 0.034581 | 2.042 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000031 | 0.000046 | 3.912 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.036572 | 0.053229 | 61.200 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000053 | 0.000073 | 8.977 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.100176 | 0.229338 | 200.010 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000014 | 0.000021 | 4.941 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.062135 | 0.087316 | 5.158 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000118 | 0.000391 | 45.624 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.535529 | 1.399892 | 38.553 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000066 | 0.000188 | 11.843 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.211133 | 0.632148 | 8.174 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000063 | 0.000238 | 14.630 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.403905 | 1.257386 | 20.608 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/dt/2026-04-26_track1_forward_dt_original_dataset_mega_campaign/020_track1_original_dataset_forward_dt_attempt_20.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-27-44__track1_original_dataset_forward_dt_attempt_20_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-27-44__track1_original_dataset_forward_dt_attempt_20_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-27-44__track1_original_dataset_forward_dt_attempt_20_campaign_validation/validation_summary.yaml`
