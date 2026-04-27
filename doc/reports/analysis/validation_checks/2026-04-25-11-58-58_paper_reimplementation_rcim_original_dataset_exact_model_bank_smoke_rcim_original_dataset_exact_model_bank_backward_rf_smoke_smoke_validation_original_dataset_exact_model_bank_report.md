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

- train rows / files: `10` / `10`
- validation rows / files: `3` / `3`
- test rows / files: `3` / `3`
- validation split: `0.2`
- test split: `0.1`
- random seed: `42`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `8.548%`
- winning mean component MAE: `0.063703`
- winning mean component RMSE: `0.076310`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 8.548 | 0.063703 | 0.076310 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `RF` | 0.004986 | 0.005449 | 12.010 |
| `fft_y_Bw_filtered_ampl_1` | `RF` | 0.000020 | 0.000021 | 0.115 |
| `fft_y_Bw_filtered_phase_1` | `RF` | 0.001081 | 0.001206 | 10.464 |
| `fft_y_Bw_filtered_ampl_3` | `RF` | 0.000036 | 0.000038 | 3.355 |
| `fft_y_Bw_filtered_phase_3` | `RF` | 0.037455 | 0.041206 | 3.380 |
| `fft_y_Bw_filtered_ampl_39` | `RF` | 0.000041 | 0.000065 | 6.431 |
| `fft_y_Bw_filtered_phase_39` | `RF` | 0.941925 | 1.163625 | 30.922 |
| `fft_y_Bw_filtered_ampl_40` | `RF` | 0.000018 | 0.000023 | 6.244 |
| `fft_y_Bw_filtered_phase_40` | `RF` | 0.129151 | 0.129544 | 40.714 |
| `fft_y_Bw_filtered_ampl_78` | `RF` | 0.000166 | 0.000197 | 8.821 |
| `fft_y_Bw_filtered_phase_78` | `RF` | 0.006917 | 0.007411 | 2.579 |
| `fft_y_Bw_filtered_ampl_81` | `RF` | 0.000009 | 0.000010 | 8.166 |
| `fft_y_Bw_filtered_phase_81` | `RF` | 0.016612 | 0.019504 | 2.245 |
| `fft_y_Bw_filtered_ampl_156` | `RF` | 0.000031 | 0.000037 | 4.737 |
| `fft_y_Bw_filtered_phase_156` | `RF` | 0.022167 | 0.022749 | 2.104 |
| `fft_y_Bw_filtered_ampl_162` | `RF` | 0.000028 | 0.000031 | 7.524 |
| `fft_y_Bw_filtered_phase_162` | `RF` | 0.023548 | 0.028732 | 1.551 |
| `fft_y_Bw_filtered_ampl_240` | `RF` | 0.000165 | 0.000188 | 9.531 |
| `fft_y_Bw_filtered_phase_240` | `RF` | 0.026003 | 0.029855 | 1.508 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/smoke/backward/rf_smoke.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-58-57__rcim_original_dataset_exact_model_bank_backward_rf_smoke_smoke_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-58-57__rcim_original_dataset_exact_model_bank_backward_rf_smoke_smoke_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-58-57__rcim_original_dataset_exact_model_bank_backward_rf_smoke_smoke_validation/validation_summary.yaml`
