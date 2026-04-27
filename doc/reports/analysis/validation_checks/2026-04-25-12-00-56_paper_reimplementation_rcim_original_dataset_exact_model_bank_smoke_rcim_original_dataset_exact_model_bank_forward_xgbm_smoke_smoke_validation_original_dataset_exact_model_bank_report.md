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
- winning mean component MAPE: `21.337%`
- winning mean component MAE: `0.042661`
- winning mean component RMSE: `0.046649`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 21.337 | 0.042661 | 0.046649 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `XGBM` | 0.006281 | 0.007641 | 8.255 |
| `fft_y_Fw_filtered_ampl_1` | `XGBM` | 0.000031 | 0.000031 | 0.178 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.002558 | 0.002823 | 18.531 |
| `fft_y_Fw_filtered_ampl_3` | `XGBM` | 0.000112 | 0.000147 | 11.228 |
| `fft_y_Fw_filtered_phase_3` | `XGBM` | 0.050671 | 0.055078 | 2.660 |
| `fft_y_Fw_filtered_ampl_39` | `XGBM` | 0.000252 | 0.000327 | 16.379 |
| `fft_y_Fw_filtered_phase_39` | `XGBM` | 0.064142 | 0.066557 | 6.252 |
| `fft_y_Fw_filtered_ampl_40` | `XGBM` | 0.000060 | 0.000062 | 7.193 |
| `fft_y_Fw_filtered_phase_40` | `XGBM` | 0.052440 | 0.067465 | 64.756 |
| `fft_y_Fw_filtered_ampl_78` | `XGBM` | 0.000488 | 0.000588 | 29.696 |
| `fft_y_Fw_filtered_phase_78` | `XGBM` | 0.040170 | 0.043027 | 128.281 |
| `fft_y_Fw_filtered_ampl_81` | `XGBM` | 0.000014 | 0.000023 | 3.801 |
| `fft_y_Fw_filtered_phase_81` | `XGBM` | 0.123357 | 0.129410 | 6.939 |
| `fft_y_Fw_filtered_ampl_156` | `XGBM` | 0.000049 | 0.000053 | 42.075 |
| `fft_y_Fw_filtered_phase_156` | `XGBM` | 0.236675 | 0.256749 | 9.197 |
| `fft_y_Fw_filtered_ampl_162` | `XGBM` | 0.000065 | 0.000075 | 23.788 |
| `fft_y_Fw_filtered_phase_162` | `XGBM` | 0.041976 | 0.046551 | 2.068 |
| `fft_y_Fw_filtered_ampl_240` | `XGBM` | 0.000076 | 0.000114 | 11.926 |
| `fft_y_Fw_filtered_phase_240` | `XGBM` | 0.191143 | 0.209611 | 12.201 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/smoke/forward/xgbm_smoke.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-12-00-54__rcim_original_dataset_exact_model_bank_forward_xgbm_smoke_smoke_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-12-00-54__rcim_original_dataset_exact_model_bank_forward_xgbm_smoke_smoke_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-12-00-54__rcim_original_dataset_exact_model_bank_forward_xgbm_smoke_smoke_validation/validation_summary.yaml`
