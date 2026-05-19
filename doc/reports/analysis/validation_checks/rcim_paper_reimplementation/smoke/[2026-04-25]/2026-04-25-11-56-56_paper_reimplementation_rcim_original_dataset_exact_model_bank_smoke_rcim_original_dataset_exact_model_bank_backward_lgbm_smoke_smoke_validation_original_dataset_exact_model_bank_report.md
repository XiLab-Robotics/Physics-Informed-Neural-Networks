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

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `23.494%`
- winning mean component MAE: `0.212386`
- winning mean component RMSE: `0.214855`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 23.494 | 0.212386 | 0.214855 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `LGBM` | 0.015143 | 0.017930 | 33.728 |
| `fft_y_Bw_filtered_ampl_1` | `LGBM` | 0.000056 | 0.000057 | 0.329 |
| `fft_y_Bw_filtered_phase_1` | `LGBM` | 0.001643 | 0.002280 | 12.793 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000098 | 0.000118 | 9.004 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.202197 | 0.222175 | 18.256 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000108 | 0.000135 | 19.676 |
| `fft_y_Bw_filtered_phase_39` | `LGBM` | 2.971687 | 2.974728 | 100.704 |
| `fft_y_Bw_filtered_ampl_40` | `LGBM` | 0.000058 | 0.000067 | 23.567 |
| `fft_y_Bw_filtered_phase_40` | `LGBM` | 0.075028 | 0.081820 | 22.194 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000584 | 0.000707 | 30.119 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.082310 | 0.083840 | 30.425 |
| `fft_y_Bw_filtered_ampl_81` | `LGBM` | 0.000006 | 0.000010 | 5.891 |
| `fft_y_Bw_filtered_phase_81` | `LGBM` | 0.261719 | 0.265515 | 36.051 |
| `fft_y_Bw_filtered_ampl_156` | `LGBM` | 0.000148 | 0.000151 | 21.880 |
| `fft_y_Bw_filtered_phase_156` | `LGBM` | 0.087643 | 0.091693 | 8.356 |
| `fft_y_Bw_filtered_ampl_162` | `LGBM` | 0.000091 | 0.000102 | 23.527 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.108913 | 0.111755 | 7.273 |
| `fft_y_Bw_filtered_ampl_240` | `LGBM` | 0.000539 | 0.000662 | 29.354 |
| `fft_y_Bw_filtered_phase_240` | `LGBM` | 0.227357 | 0.228501 | 13.262 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/smoke/backward/lgbm_smoke.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-56-53__rcim_original_dataset_exact_model_bank_backward_lgbm_smoke_smoke_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-56-53__rcim_original_dataset_exact_model_bank_backward_lgbm_smoke_smoke_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-56-53__rcim_original_dataset_exact_model_bank_backward_lgbm_smoke_smoke_validation/validation_summary.yaml`
