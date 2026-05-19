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

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `10339.690%`
- winning mean component MAE: `0.103566`
- winning mean component RMSE: `0.131042`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 10339.690 | 0.103566 | 0.131042 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `MLP` | 0.057460 | 0.095995 | 92.384 |
| `fft_y_Fw_filtered_ampl_1` | `MLP` | 0.084644 | 0.111818 | 492.062 |
| `fft_y_Fw_filtered_phase_1` | `MLP` | 0.127456 | 0.154965 | 1060.941 |
| `fft_y_Fw_filtered_ampl_3` | `MLP` | 0.087919 | 0.121271 | 10448.985 |
| `fft_y_Fw_filtered_phase_3` | `MLP` | 0.072037 | 0.074222 | 3.778 |
| `fft_y_Fw_filtered_ampl_39` | `MLP` | 0.087749 | 0.121318 | 7225.594 |
| `fft_y_Fw_filtered_phase_39` | `MLP` | 0.097953 | 0.103200 | 9.321 |
| `fft_y_Fw_filtered_ampl_40` | `MLP` | 0.087953 | 0.121403 | 10817.397 |
| `fft_y_Fw_filtered_phase_40` | `MLP` | 0.145683 | 0.183682 | 106.147 |
| `fft_y_Fw_filtered_ampl_78` | `MLP` | 0.087809 | 0.121403 | 7127.284 |
| `fft_y_Fw_filtered_phase_78` | `MLP` | 0.090798 | 0.132747 | 307.640 |
| `fft_y_Fw_filtered_ampl_81` | `MLP` | 0.089132 | 0.121276 | 27603.167 |
| `fft_y_Fw_filtered_phase_81` | `MLP` | 0.185885 | 0.241234 | 11.015 |
| `fft_y_Fw_filtered_ampl_156` | `MLP` | 0.089986 | 0.122583 | 75260.971 |
| `fft_y_Fw_filtered_phase_156` | `MLP` | 0.171133 | 0.180807 | 6.656 |
| `fft_y_Fw_filtered_ampl_162` | `MLP` | 0.089598 | 0.121664 | 37893.460 |
| `fft_y_Fw_filtered_phase_162` | `MLP` | 0.131429 | 0.138530 | 6.514 |
| `fft_y_Fw_filtered_ampl_240` | `MLP` | 0.088356 | 0.121144 | 17974.690 |
| `fft_y_Fw_filtered_phase_240` | `MLP` | 0.094770 | 0.100530 | 6.110 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/smoke/forward/mlp_smoke.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-12-00-25__rcim_original_dataset_exact_model_bank_forward_mlp_smoke_smoke_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-12-00-25__rcim_original_dataset_exact_model_bank_forward_mlp_smoke_smoke_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-12-00-25__rcim_original_dataset_exact_model_bank_forward_mlp_smoke_smoke_validation/validation_summary.yaml`
