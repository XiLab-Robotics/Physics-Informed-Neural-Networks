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

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `48.725%`
- winning mean component MAE: `0.095190`
- winning mean component RMSE: `0.114199`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 48.725 | 0.095190 | 0.114199 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `GBM` | 0.016593 | 0.019075 | 22.135 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000031 | 0.000031 | 0.178 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.003410 | 0.004333 | 21.554 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000112 | 0.000147 | 11.228 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | 0.115068 | 0.122117 | 5.981 |
| `fft_y_Fw_filtered_ampl_39` | `GBM` | 0.000252 | 0.000327 | 16.379 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.202132 | 0.216161 | 20.323 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000060 | 0.000062 | 7.193 |
| `fft_y_Fw_filtered_phase_40` | `GBM` | 0.088995 | 0.090339 | 64.468 |
| `fft_y_Fw_filtered_ampl_78` | `GBM` | 0.000488 | 0.000588 | 29.696 |
| `fft_y_Fw_filtered_phase_78` | `GBM` | 0.143647 | 0.146153 | 579.828 |
| `fft_y_Fw_filtered_ampl_81` | `GBM` | 0.000014 | 0.000023 | 3.801 |
| `fft_y_Fw_filtered_phase_81` | `GBM` | 0.333156 | 0.355824 | 18.238 |
| `fft_y_Fw_filtered_ampl_156` | `GBM` | 0.000049 | 0.000053 | 42.075 |
| `fft_y_Fw_filtered_phase_156` | `GBM` | 0.475684 | 0.637373 | 16.720 |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000065 | 0.000075 | 23.788 |
| `fft_y_Fw_filtered_phase_162` | `GBM` | 0.079596 | 0.098486 | 4.024 |
| `fft_y_Fw_filtered_ampl_240` | `GBM` | 0.000076 | 0.000114 | 11.926 |
| `fft_y_Fw_filtered_phase_240` | `GBM` | 0.349176 | 0.478509 | 26.245 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/smoke/forward/gbm_smoke.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-59-52__rcim_original_dataset_exact_model_bank_forward_gbm_smoke_smoke_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-59-52__rcim_original_dataset_exact_model_bank_forward_gbm_smoke_smoke_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-59-52__rcim_original_dataset_exact_model_bank_forward_gbm_smoke_smoke_validation/validation_summary.yaml`
