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
- random seed: `27`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `30.268%`
- winning mean component MAE: `0.055461`
- winning mean component RMSE: `0.150305`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 30.268 | 0.055461 | 0.150305 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 5}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.002984 | 0.003732 | 5.909 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000032 | 0.000044 | 0.184 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.002456 | 0.003451 | 37.326 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000025 | 0.000035 | 3.089 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.026082 | 0.034343 | 1.426 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000041 | 0.000055 | 3.396 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.033598 | 0.054264 | 2.803 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000033 | 0.000051 | 4.141 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.045593 | 0.066968 | 111.219 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000063 | 0.000087 | 8.579 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.052529 | 0.089049 | 246.426 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000013 | 0.000020 | 4.617 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.057849 | 0.086440 | 5.056 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000077 | 0.000233 | 18.328 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.451476 | 1.141714 | 35.894 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000053 | 0.000160 | 10.271 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.213505 | 0.908563 | 8.134 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000041 | 0.000061 | 10.102 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.167310 | 0.466521 | 58.188 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/dt/2026-04-26_track1_forward_dt_original_dataset_mega_campaign/012_track1_original_dataset_forward_dt_attempt_12.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-20-16__track1_original_dataset_forward_dt_attempt_12_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-20-16__track1_original_dataset_forward_dt_attempt_12_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-20-16__track1_original_dataset_forward_dt_attempt_12_campaign_validation/validation_summary.yaml`
