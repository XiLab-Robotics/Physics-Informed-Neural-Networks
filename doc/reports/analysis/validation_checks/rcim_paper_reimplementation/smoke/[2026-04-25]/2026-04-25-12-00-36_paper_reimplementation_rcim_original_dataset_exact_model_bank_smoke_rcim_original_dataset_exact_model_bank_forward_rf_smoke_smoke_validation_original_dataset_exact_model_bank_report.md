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

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `10.256%`
- winning mean component MAE: `0.021516`
- winning mean component RMSE: `0.025856`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 10.256 | 0.021516 | 0.025856 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `RF` | 0.002722 | 0.004002 | 3.431 |
| `fft_y_Fw_filtered_ampl_1` | `RF` | 0.000030 | 0.000033 | 0.175 |
| `fft_y_Fw_filtered_phase_1` | `RF` | 0.001969 | 0.002708 | 17.341 |
| `fft_y_Fw_filtered_ampl_3` | `RF` | 0.000039 | 0.000049 | 3.928 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.021072 | 0.026366 | 1.118 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000060 | 0.000066 | 4.203 |
| `fft_y_Fw_filtered_phase_39` | `RF` | 0.027618 | 0.033416 | 2.706 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | 0.000052 | 0.000070 | 5.929 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.046228 | 0.051212 | 49.118 |
| `fft_y_Fw_filtered_ampl_78` | `RF` | 0.000137 | 0.000167 | 8.421 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.011202 | 0.012610 | 54.672 |
| `fft_y_Fw_filtered_ampl_81` | `RF` | 0.000005 | 0.000007 | 1.587 |
| `fft_y_Fw_filtered_phase_81` | `RF` | 0.042886 | 0.048729 | 2.388 |
| `fft_y_Fw_filtered_ampl_156` | `RF` | 0.000013 | 0.000015 | 10.296 |
| `fft_y_Fw_filtered_phase_156` | `RF` | 0.135476 | 0.164454 | 4.990 |
| `fft_y_Fw_filtered_ampl_162` | `RF` | 0.000025 | 0.000025 | 9.595 |
| `fft_y_Fw_filtered_phase_162` | `RF` | 0.037107 | 0.038612 | 1.824 |
| `fft_y_Fw_filtered_ampl_240` | `RF` | 0.000041 | 0.000049 | 7.123 |
| `fft_y_Fw_filtered_phase_240` | `RF` | 0.082117 | 0.108673 | 6.013 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/smoke/forward/rf_smoke.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-12-00-35__rcim_original_dataset_exact_model_bank_forward_rf_smoke_smoke_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-12-00-35__rcim_original_dataset_exact_model_bank_forward_rf_smoke_smoke_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-12-00-35__rcim_original_dataset_exact_model_bank_forward_rf_smoke_smoke_validation/validation_summary.yaml`
