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
- random seed: `59`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `18.054%`
- winning mean component MAE: `0.053561`
- winning mean component RMSE: `0.130104`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 18.054 | 0.053561 | 0.130104 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 16, 'estimator__min_samples_split': 4, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ERT` | 0.002952 | 0.003603 | 68.634 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000024 | 0.000035 | 0.139 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.002138 | 0.003413 | 79.874 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000027 | 0.000044 | 2.588 |
| `fft_y_Bw_filtered_phase_3` | `ERT` | 0.024651 | 0.034855 | 1.891 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000018 | 0.000028 | 4.237 |
| `fft_y_Bw_filtered_phase_39` | `ERT` | 0.308795 | 1.031575 | 10.413 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000027 | 0.000040 | 8.532 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.088748 | 0.123517 | 27.297 |
| `fft_y_Bw_filtered_ampl_78` | `ERT` | 0.000050 | 0.000077 | 4.874 |
| `fft_y_Bw_filtered_phase_78` | `ERT` | 0.065289 | 0.120663 | 14.839 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000010 | 0.000015 | 8.384 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.102909 | 0.140940 | 49.077 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000061 | 0.000153 | 6.275 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.093643 | 0.221675 | 22.769 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000046 | 0.000172 | 5.443 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.102695 | 0.233085 | 6.005 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000061 | 0.000151 | 9.631 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.225518 | 0.557938 | 12.120 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/ert/2026-04-26_track1_backward_ert_original_dataset_mega_campaign/019_track1_original_dataset_backward_ert_attempt_19.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-31-13__track1_original_dataset_backward_ert_attempt_19_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-31-13__track1_original_dataset_backward_ert_attempt_19_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-31-13__track1_original_dataset_backward_ert_attempt_19_campaign_validation/validation_summary.yaml`
