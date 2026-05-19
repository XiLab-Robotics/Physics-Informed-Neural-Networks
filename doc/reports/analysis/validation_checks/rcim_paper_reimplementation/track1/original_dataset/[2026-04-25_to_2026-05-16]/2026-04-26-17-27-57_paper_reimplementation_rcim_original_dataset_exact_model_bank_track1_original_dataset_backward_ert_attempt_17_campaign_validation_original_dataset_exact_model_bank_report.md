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
- random seed: `47`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `19.113%`
- winning mean component MAE: `0.044993`
- winning mean component RMSE: `0.117344`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 19.113 | 0.044993 | 0.117344 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 80}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ERT` | 0.003262 | 0.003960 | 54.921 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000029 | 0.000038 | 0.169 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001961 | 0.002606 | 96.242 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000024 | 0.000039 | 2.409 |
| `fft_y_Bw_filtered_phase_3` | `ERT` | 0.023354 | 0.037143 | 1.737 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000018 | 0.000024 | 3.980 |
| `fft_y_Bw_filtered_phase_39` | `ERT` | 0.204351 | 0.708617 | 7.282 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000030 | 0.000046 | 9.438 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.093695 | 0.190718 | 29.806 |
| `fft_y_Bw_filtered_ampl_78` | `ERT` | 0.000049 | 0.000067 | 6.125 |
| `fft_y_Bw_filtered_phase_78` | `ERT` | 0.047589 | 0.097640 | 42.165 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000010 | 0.000018 | 7.465 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.089900 | 0.127987 | 43.442 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000100 | 0.000438 | 5.282 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.128101 | 0.486621 | 19.505 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000127 | 0.000591 | 8.163 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.069857 | 0.134716 | 3.678 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000067 | 0.000171 | 11.206 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.192351 | 0.438101 | 10.133 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/ert/2026-04-26_track1_backward_ert_original_dataset_mega_campaign/017_track1_original_dataset_backward_ert_attempt_17.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-24-48__track1_original_dataset_backward_ert_attempt_17_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-24-48__track1_original_dataset_backward_ert_attempt_17_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-24-48__track1_original_dataset_backward_ert_attempt_17_campaign_validation/validation_summary.yaml`
