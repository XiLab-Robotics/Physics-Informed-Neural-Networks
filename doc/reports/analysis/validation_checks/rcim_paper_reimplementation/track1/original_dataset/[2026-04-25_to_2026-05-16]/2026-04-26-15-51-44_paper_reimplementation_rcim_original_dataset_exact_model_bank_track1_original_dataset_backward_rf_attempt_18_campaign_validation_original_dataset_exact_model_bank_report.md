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
- random seed: `53`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `28.718%`
- winning mean component MAE: `0.047504`
- winning mean component RMSE: `0.126752`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 28.718 | 0.047504 | 0.126752 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 12, 'estimator__min_samples_split': 2, 'estimator__n_estimators': 50}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `RF` | 0.002644 | 0.003401 | 39.341 |
| `fft_y_Bw_filtered_ampl_1` | `RF` | 0.000028 | 0.000042 | 0.165 |
| `fft_y_Bw_filtered_phase_1` | `RF` | 0.001918 | 0.002688 | 34.735 |
| `fft_y_Bw_filtered_ampl_3` | `RF` | 0.000023 | 0.000037 | 2.425 |
| `fft_y_Bw_filtered_phase_3` | `RF` | 0.022017 | 0.038829 | 1.631 |
| `fft_y_Bw_filtered_ampl_39` | `RF` | 0.000017 | 0.000025 | 3.727 |
| `fft_y_Bw_filtered_phase_39` | `RF` | 0.170408 | 0.742921 | 6.231 |
| `fft_y_Bw_filtered_ampl_40` | `RF` | 0.000029 | 0.000044 | 10.006 |
| `fft_y_Bw_filtered_phase_40` | `RF` | 0.110000 | 0.177326 | 230.688 |
| `fft_y_Bw_filtered_ampl_78` | `RF` | 0.000045 | 0.000056 | 8.158 |
| `fft_y_Bw_filtered_phase_78` | `RF` | 0.074558 | 0.153944 | 34.345 |
| `fft_y_Bw_filtered_ampl_81` | `RF` | 0.000007 | 0.000011 | 6.347 |
| `fft_y_Bw_filtered_phase_81` | `RF` | 0.105886 | 0.194554 | 97.480 |
| `fft_y_Bw_filtered_ampl_156` | `RF` | 0.000135 | 0.000386 | 7.804 |
| `fft_y_Bw_filtered_phase_156` | `RF` | 0.093292 | 0.241527 | 22.254 |
| `fft_y_Bw_filtered_ampl_162` | `RF` | 0.000071 | 0.000181 | 7.290 |
| `fft_y_Bw_filtered_phase_162` | `RF` | 0.081383 | 0.201850 | 4.570 |
| `fft_y_Bw_filtered_ampl_240` | `RF` | 0.000056 | 0.000105 | 14.577 |
| `fft_y_Bw_filtered_phase_240` | `RF` | 0.240054 | 0.650364 | 13.863 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/rf/2026-04-26_track1_backward_rf_original_dataset_mega_campaign/018_track1_original_dataset_backward_rf_attempt_18.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-48-34__track1_original_dataset_backward_rf_attempt_18_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-48-34__track1_original_dataset_backward_rf_attempt_18_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-48-34__track1_original_dataset_backward_rf_attempt_18_campaign_validation/validation_summary.yaml`
