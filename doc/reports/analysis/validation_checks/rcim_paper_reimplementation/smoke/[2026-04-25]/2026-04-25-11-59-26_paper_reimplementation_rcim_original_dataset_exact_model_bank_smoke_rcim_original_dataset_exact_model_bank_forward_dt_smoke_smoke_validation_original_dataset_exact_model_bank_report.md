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

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `17.967%`
- winning mean component MAE: `0.044443`
- winning mean component RMSE: `0.047214`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 17.967 | 0.044443 | 0.047214 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.004001 | 0.004528 | 5.365 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000035 | 0.000039 | 0.206 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.002467 | 0.002790 | 18.358 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000070 | 0.000075 | 7.426 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.038385 | 0.040528 | 2.024 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000156 | 0.000164 | 11.306 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.067774 | 0.069519 | 6.538 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000049 | 0.000068 | 5.568 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.030947 | 0.034367 | 32.106 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000258 | 0.000270 | 17.201 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.024207 | 0.027300 | 168.947 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000003 | 0.000003 | 0.837 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.099253 | 0.103081 | 5.619 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000011 | 0.000012 | 9.074 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.310641 | 0.329569 | 12.246 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000039 | 0.000039 | 15.422 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.042737 | 0.044086 | 2.118 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000038 | 0.000045 | 6.685 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.223353 | 0.240579 | 14.330 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/smoke/forward/dt_smoke.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-59-26__rcim_original_dataset_exact_model_bank_forward_dt_smoke_smoke_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-59-26__rcim_original_dataset_exact_model_bank_forward_dt_smoke_smoke_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-59-26__rcim_original_dataset_exact_model_bank_forward_dt_smoke_smoke_validation/validation_summary.yaml`
