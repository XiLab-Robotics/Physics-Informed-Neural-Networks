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
- random seed: `42`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `16.110%`
- winning mean component MAE: `0.062305`
- winning mean component RMSE: `0.142050`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 16.110 | 0.062305 | 0.142050 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 13, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 50}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `RF` | 0.003079 | 0.003694 | 5.912 |
| `fft_y_Fw_filtered_ampl_1` | `RF` | 0.000025 | 0.000030 | 0.144 |
| `fft_y_Fw_filtered_phase_1` | `RF` | 0.001583 | 0.002117 | 83.774 |
| `fft_y_Fw_filtered_ampl_3` | `RF` | 0.000020 | 0.000026 | 2.284 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.021322 | 0.028357 | 1.176 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000032 | 0.000053 | 2.641 |
| `fft_y_Fw_filtered_phase_39` | `RF` | 0.020569 | 0.027498 | 1.783 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | 0.000027 | 0.000040 | 3.542 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.045721 | 0.068002 | 56.770 |
| `fft_y_Fw_filtered_ampl_78` | `RF` | 0.000045 | 0.000066 | 9.244 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.081939 | 0.217868 | 50.829 |
| `fft_y_Fw_filtered_ampl_81` | `RF` | 0.000010 | 0.000014 | 3.177 |
| `fft_y_Fw_filtered_phase_81` | `RF` | 0.049727 | 0.076980 | 4.703 |
| `fft_y_Fw_filtered_ampl_156` | `RF` | 0.000037 | 0.000123 | 9.281 |
| `fft_y_Fw_filtered_phase_156` | `RF` | 0.333473 | 0.676607 | 14.248 |
| `fft_y_Fw_filtered_ampl_162` | `RF` | 0.000052 | 0.000135 | 9.068 |
| `fft_y_Fw_filtered_phase_162` | `RF` | 0.339996 | 0.869518 | 12.503 |
| `fft_y_Fw_filtered_ampl_240` | `RF` | 0.000041 | 0.000076 | 9.141 |
| `fft_y_Fw_filtered_phase_240` | `RF` | 0.286107 | 0.727753 | 25.863 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/forward_remote_diagnostic/rf/2026-04-25_track1_forward_rf_remote_diagnostic/001_track1_original_dataset_forward_rf_remote_diagnostic.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_diagnostic/2026-04-25-16-19-14__track1_original_dataset_forward_rf_remote_diagnostic_remote_diagnostic`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_diagnostic/2026-04-25-16-19-14__track1_original_dataset_forward_rf_remote_diagnostic_remote_diagnostic/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_diagnostic/2026-04-25-16-19-14__track1_original_dataset_forward_rf_remote_diagnostic_remote_diagnostic/validation_summary.yaml`
