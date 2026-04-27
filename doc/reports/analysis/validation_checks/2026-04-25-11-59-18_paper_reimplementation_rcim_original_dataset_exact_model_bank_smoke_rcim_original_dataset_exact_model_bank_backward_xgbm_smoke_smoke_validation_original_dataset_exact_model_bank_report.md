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

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `17.566%`
- winning mean component MAE: `0.128172`
- winning mean component RMSE: `0.191797`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 17.566 | 0.128172 | 0.191797 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `XGBM` | 0.007793 | 0.008445 | 18.267 |
| `fft_y_Bw_filtered_ampl_1` | `XGBM` | 0.000056 | 0.000057 | 0.329 |
| `fft_y_Bw_filtered_phase_1` | `XGBM` | 0.001643 | 0.002280 | 12.793 |
| `fft_y_Bw_filtered_ampl_3` | `XGBM` | 0.000098 | 0.000118 | 9.004 |
| `fft_y_Bw_filtered_phase_3` | `XGBM` | 0.051529 | 0.056480 | 4.636 |
| `fft_y_Bw_filtered_ampl_39` | `XGBM` | 0.000108 | 0.000135 | 19.676 |
| `fft_y_Bw_filtered_phase_39` | `XGBM` | 2.049957 | 3.219680 | 66.941 |
| `fft_y_Bw_filtered_ampl_40` | `XGBM` | 0.000058 | 0.000067 | 23.567 |
| `fft_y_Bw_filtered_phase_40` | `XGBM` | 0.139880 | 0.143667 | 45.782 |
| `fft_y_Bw_filtered_ampl_78` | `XGBM` | 0.000584 | 0.000707 | 30.119 |
| `fft_y_Bw_filtered_phase_78` | `XGBM` | 0.019355 | 0.021963 | 7.014 |
| `fft_y_Bw_filtered_ampl_81` | `XGBM` | 0.000006 | 0.000010 | 5.891 |
| `fft_y_Bw_filtered_phase_81` | `XGBM` | 0.057702 | 0.070673 | 7.711 |
| `fft_y_Bw_filtered_ampl_156` | `XGBM` | 0.000148 | 0.000151 | 21.880 |
| `fft_y_Bw_filtered_phase_156` | `XGBM` | 0.021528 | 0.028387 | 2.071 |
| `fft_y_Bw_filtered_ampl_162` | `XGBM` | 0.000091 | 0.000102 | 23.527 |
| `fft_y_Bw_filtered_phase_162` | `XGBM` | 0.032318 | 0.034050 | 2.156 |
| `fft_y_Bw_filtered_ampl_240` | `XGBM` | 0.000539 | 0.000662 | 29.354 |
| `fft_y_Bw_filtered_phase_240` | `XGBM` | 0.051872 | 0.056518 | 3.030 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/smoke/backward/xgbm_smoke.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-59-15__rcim_original_dataset_exact_model_bank_backward_xgbm_smoke_smoke_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-59-15__rcim_original_dataset_exact_model_bank_backward_xgbm_smoke_smoke_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-59-15__rcim_original_dataset_exact_model_bank_backward_xgbm_smoke_smoke_validation/validation_summary.yaml`
