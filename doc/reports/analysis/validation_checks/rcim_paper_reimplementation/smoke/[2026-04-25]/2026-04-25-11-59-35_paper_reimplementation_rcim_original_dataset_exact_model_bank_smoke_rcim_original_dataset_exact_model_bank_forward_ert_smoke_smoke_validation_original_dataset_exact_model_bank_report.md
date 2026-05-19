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

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `9.254%`
- winning mean component MAE: `0.014325`
- winning mean component RMSE: `0.018010`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 9.254 | 0.014325 | 0.018010 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.002002 | 0.002474 | 2.659 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000033 | 0.000036 | 0.192 |
| `fft_y_Fw_filtered_phase_1` | `ERT` | 0.002581 | 0.003070 | 20.846 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000026 | 0.000036 | 2.578 |
| `fft_y_Fw_filtered_phase_3` | `ERT` | 0.014347 | 0.014750 | 0.754 |
| `fft_y_Fw_filtered_ampl_39` | `ERT` | 0.000007 | 0.000009 | 0.530 |
| `fft_y_Fw_filtered_phase_39` | `ERT` | 0.008350 | 0.009803 | 0.781 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000048 | 0.000066 | 5.483 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.065990 | 0.080551 | 78.076 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000061 | 0.000099 | 3.244 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.009463 | 0.013754 | 30.246 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000001 | 0.000002 | 0.456 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.018253 | 0.027581 | 0.951 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000012 | 0.000013 | 9.294 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.066132 | 0.094412 | 2.287 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000016 | 0.000016 | 6.359 |
| `fft_y_Fw_filtered_phase_162` | `ERT` | 0.033691 | 0.036245 | 1.652 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000033 | 0.000039 | 5.877 |
| `fft_y_Fw_filtered_phase_240` | `ERT` | 0.051130 | 0.059228 | 3.569 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/smoke/forward/ert_smoke.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-59-34__rcim_original_dataset_exact_model_bank_forward_ert_smoke_smoke_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-59-34__rcim_original_dataset_exact_model_bank_forward_ert_smoke_smoke_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-59-34__rcim_original_dataset_exact_model_bank_forward_ert_smoke_smoke_validation/validation_summary.yaml`
