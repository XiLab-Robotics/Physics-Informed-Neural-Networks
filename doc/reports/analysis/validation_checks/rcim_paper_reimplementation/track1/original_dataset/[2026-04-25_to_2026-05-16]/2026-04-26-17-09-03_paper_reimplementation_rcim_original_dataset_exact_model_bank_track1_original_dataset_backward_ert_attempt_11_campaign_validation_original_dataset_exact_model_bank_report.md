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
- random seed: `23`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `19.854%`
- winning mean component MAE: `0.036511`
- winning mean component RMSE: `0.104918`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 19.854 | 0.036511 | 0.104918 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 16, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ERT` | 0.003132 | 0.003788 | 77.946 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000025 | 0.000033 | 0.149 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001624 | 0.002477 | 101.647 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000022 | 0.000032 | 2.208 |
| `fft_y_Bw_filtered_phase_3` | `ERT` | 0.024187 | 0.032702 | 1.842 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000020 | 0.000029 | 4.565 |
| `fft_y_Bw_filtered_phase_39` | `ERT` | 0.136584 | 0.617764 | 5.015 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000028 | 0.000041 | 9.251 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.074356 | 0.105595 | 43.945 |
| `fft_y_Bw_filtered_ampl_78` | `ERT` | 0.000046 | 0.000062 | 5.334 |
| `fft_y_Bw_filtered_phase_78` | `ERT` | 0.047775 | 0.095330 | 17.175 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000008 | 0.000013 | 7.274 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.090689 | 0.125999 | 52.272 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000101 | 0.000351 | 7.965 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.104371 | 0.356028 | 9.232 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000067 | 0.000329 | 6.617 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.068351 | 0.155700 | 4.455 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000069 | 0.000104 | 11.052 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.142260 | 0.497061 | 9.277 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/ert/2026-04-26_track1_backward_ert_original_dataset_mega_campaign/011_track1_original_dataset_backward_ert_attempt_11.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-06-02__track1_original_dataset_backward_ert_attempt_11_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-06-02__track1_original_dataset_backward_ert_attempt_11_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-06-02__track1_original_dataset_backward_ert_attempt_11_campaign_validation/validation_summary.yaml`
