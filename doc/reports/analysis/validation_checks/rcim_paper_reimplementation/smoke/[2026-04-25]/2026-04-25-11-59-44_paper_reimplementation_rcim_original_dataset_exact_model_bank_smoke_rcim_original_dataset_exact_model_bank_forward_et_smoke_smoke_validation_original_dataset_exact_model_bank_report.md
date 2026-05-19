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

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `25.359%`
- winning mean component MAE: `0.068893`
- winning mean component RMSE: `0.072899`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 25.359 | 0.068893 | 0.072899 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ET` | 0.010006 | 0.010266 | 14.610 |
| `fft_y_Fw_filtered_ampl_1` | `ET` | 0.000028 | 0.000030 | 0.165 |
| `fft_y_Fw_filtered_phase_1` | `ET` | 0.002821 | 0.003437 | 24.144 |
| `fft_y_Fw_filtered_ampl_3` | `ET` | 0.000102 | 0.000104 | 11.308 |
| `fft_y_Fw_filtered_phase_3` | `ET` | 0.044436 | 0.049311 | 2.349 |
| `fft_y_Fw_filtered_ampl_39` | `ET` | 0.000234 | 0.000244 | 17.867 |
| `fft_y_Fw_filtered_phase_39` | `ET` | 0.088984 | 0.094721 | 8.460 |
| `fft_y_Fw_filtered_ampl_40` | `ET` | 0.000047 | 0.000071 | 5.284 |
| `fft_y_Fw_filtered_phase_40` | `ET` | 0.088873 | 0.090165 | 64.553 |
| `fft_y_Fw_filtered_ampl_78` | `ET` | 0.000348 | 0.000352 | 24.726 |
| `fft_y_Fw_filtered_phase_78` | `ET` | 0.027627 | 0.032671 | 205.677 |
| `fft_y_Fw_filtered_ampl_81` | `ET` | 0.000018 | 0.000018 | 5.408 |
| `fft_y_Fw_filtered_phase_81` | `ET` | 0.145171 | 0.158239 | 8.386 |
| `fft_y_Fw_filtered_ampl_156` | `ET` | 0.000017 | 0.000021 | 13.162 |
| `fft_y_Fw_filtered_phase_156` | `ET` | 0.465614 | 0.478920 | 19.559 |
| `fft_y_Fw_filtered_ampl_162` | `ET` | 0.000039 | 0.000039 | 15.296 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.068905 | 0.080894 | 3.453 |
| `fft_y_Fw_filtered_ampl_240` | `ET` | 0.000087 | 0.000090 | 15.977 |
| `fft_y_Fw_filtered_phase_240` | `ET` | 0.365608 | 0.385496 | 21.433 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/smoke/forward/et_smoke.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-59-43__rcim_original_dataset_exact_model_bank_forward_et_smoke_smoke_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-59-43__rcim_original_dataset_exact_model_bank_forward_et_smoke_smoke_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-59-43__rcim_original_dataset_exact_model_bank_forward_et_smoke_smoke_validation/validation_summary.yaml`
