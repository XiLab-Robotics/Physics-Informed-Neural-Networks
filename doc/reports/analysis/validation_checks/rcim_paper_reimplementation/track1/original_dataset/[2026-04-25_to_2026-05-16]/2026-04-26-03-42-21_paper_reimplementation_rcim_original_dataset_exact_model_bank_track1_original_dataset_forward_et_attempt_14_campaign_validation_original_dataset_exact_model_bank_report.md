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
- random seed: `31`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `28.945%`
- winning mean component MAE: `0.129323`
- winning mean component RMSE: `0.284482`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 28.945 | 0.129323 | 0.284482 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 6}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ET` | 0.003530 | 0.004710 | 8.061 |
| `fft_y_Fw_filtered_ampl_1` | `ET` | 0.000037 | 0.000051 | 0.216 |
| `fft_y_Fw_filtered_phase_1` | `ET` | 0.002699 | 0.004355 | 48.906 |
| `fft_y_Fw_filtered_ampl_3` | `ET` | 0.000029 | 0.000055 | 3.520 |
| `fft_y_Fw_filtered_phase_3` | `ET` | 0.033074 | 0.058540 | 1.829 |
| `fft_y_Fw_filtered_ampl_39` | `ET` | 0.000043 | 0.000064 | 4.023 |
| `fft_y_Fw_filtered_phase_39` | `ET` | 0.034715 | 0.059348 | 2.858 |
| `fft_y_Fw_filtered_ampl_40` | `ET` | 0.000032 | 0.000042 | 3.910 |
| `fft_y_Fw_filtered_phase_40` | `ET` | 0.053729 | 0.074921 | 95.468 |
| `fft_y_Fw_filtered_ampl_78` | `ET` | 0.000061 | 0.000091 | 9.632 |
| `fft_y_Fw_filtered_phase_78` | `ET` | 0.217003 | 0.587524 | 191.448 |
| `fft_y_Fw_filtered_ampl_81` | `ET` | 0.000018 | 0.000027 | 5.540 |
| `fft_y_Fw_filtered_phase_81` | `ET` | 0.086423 | 0.132642 | 7.981 |
| `fft_y_Fw_filtered_ampl_156` | `ET` | 0.000094 | 0.000452 | 20.361 |
| `fft_y_Fw_filtered_phase_156` | `ET` | 0.809607 | 1.585327 | 42.886 |
| `fft_y_Fw_filtered_ampl_162` | `ET` | 0.000053 | 0.000134 | 13.162 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.510499 | 1.368763 | 18.790 |
| `fft_y_Fw_filtered_ampl_240` | `ET` | 0.000048 | 0.000070 | 19.829 |
| `fft_y_Fw_filtered_phase_240` | `ET` | 0.705447 | 1.528050 | 51.526 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/et/2026-04-26_track1_forward_et_original_dataset_mega_campaign/014_track1_original_dataset_forward_et_attempt_14.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-41-29__track1_original_dataset_forward_et_attempt_14_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-41-29__track1_original_dataset_forward_et_attempt_14_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-41-29__track1_original_dataset_forward_et_attempt_14_campaign_validation/validation_summary.yaml`
