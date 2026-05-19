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
- random seed: `0`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `20.120%`
- winning mean component MAE: `0.049671`
- winning mean component RMSE: `0.129551`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 20.120 | 0.049671 | 0.129551 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 5, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ERT` | 0.003469 | 0.004146 | 127.955 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000021 | 0.000029 | 0.120 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001580 | 0.002130 | 21.064 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000026 | 0.000035 | 2.716 |
| `fft_y_Bw_filtered_phase_3` | `ERT` | 0.023643 | 0.035600 | 1.761 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000018 | 0.000024 | 4.086 |
| `fft_y_Bw_filtered_phase_39` | `ERT` | 0.243882 | 0.849285 | 8.386 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000024 | 0.000032 | 8.162 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.079012 | 0.107083 | 29.427 |
| `fft_y_Bw_filtered_ampl_78` | `ERT` | 0.000036 | 0.000052 | 3.581 |
| `fft_y_Bw_filtered_phase_78` | `ERT` | 0.055378 | 0.124823 | 66.270 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000009 | 0.000013 | 7.486 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.080424 | 0.125367 | 38.917 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000109 | 0.000432 | 9.326 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.106373 | 0.334748 | 11.191 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000085 | 0.000370 | 7.048 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.062612 | 0.133295 | 3.539 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000135 | 0.000486 | 15.763 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.286918 | 0.743524 | 15.484 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/ert/2026-04-26_track1_backward_ert_original_dataset_mega_campaign/001_track1_original_dataset_backward_ert_attempt_01.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-34-28__track1_original_dataset_backward_ert_attempt_01_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-34-28__track1_original_dataset_backward_ert_attempt_01_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-34-28__track1_original_dataset_backward_ert_attempt_01_campaign_validation/validation_summary.yaml`
