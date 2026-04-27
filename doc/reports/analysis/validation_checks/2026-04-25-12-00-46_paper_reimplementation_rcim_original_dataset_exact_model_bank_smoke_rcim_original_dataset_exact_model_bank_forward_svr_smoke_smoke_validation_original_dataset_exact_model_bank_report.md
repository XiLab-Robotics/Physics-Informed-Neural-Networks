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

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `17.775%`
- winning mean component MAE: `0.017365`
- winning mean component RMSE: `0.019769`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 17.775 | 0.017365 | 0.019769 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | 0.000693 | 0.000977 | 1.020 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | 0.000055 | 0.000063 | 0.320 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | 0.003767 | 0.004616 | 27.662 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | 0.000121 | 0.000155 | 12.303 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | 0.018534 | 0.020037 | 0.963 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | 0.000192 | 0.000273 | 12.165 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | 0.013297 | 0.013409 | 1.309 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | 0.000059 | 0.000062 | 7.023 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.040706 | 0.048645 | 47.059 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | 0.000165 | 0.000176 | 10.791 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | 0.011485 | 0.015081 | 24.080 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | 0.000018 | 0.000018 | 5.161 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | 0.035889 | 0.038732 | 2.002 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | 0.000161 | 0.000163 | 131.771 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | 0.101967 | 0.110675 | 3.971 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | 0.000061 | 0.000072 | 22.293 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | 0.028197 | 0.036273 | 1.401 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | 0.000131 | 0.000158 | 22.250 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | 0.074435 | 0.086028 | 4.181 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/smoke/forward/svr_smoke.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-12-00-45__rcim_original_dataset_exact_model_bank_forward_svr_smoke_smoke_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-12-00-45__rcim_original_dataset_exact_model_bank_forward_svr_smoke_smoke_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-12-00-45__rcim_original_dataset_exact_model_bank_forward_svr_smoke_smoke_validation/validation_summary.yaml`
