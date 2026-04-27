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

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `8.221%`
- winning mean component MAE: `0.087529`
- winning mean component RMSE: `0.103573`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 8.221 | 0.087529 | 0.103573 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ERT` | 0.002431 | 0.002929 | 5.660 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000022 | 0.000022 | 0.128 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001258 | 0.001463 | 11.381 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000020 | 0.000021 | 1.881 |
| `fft_y_Bw_filtered_phase_3` | `ERT` | 0.018555 | 0.023300 | 1.708 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000034 | 0.000043 | 6.050 |
| `fft_y_Bw_filtered_phase_39` | `ERT` | 1.404338 | 1.697759 | 45.974 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000035 | 0.000037 | 13.677 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.122680 | 0.124089 | 39.419 |
| `fft_y_Bw_filtered_ampl_78` | `ERT` | 0.000065 | 0.000104 | 2.959 |
| `fft_y_Bw_filtered_phase_78` | `ERT` | 0.005784 | 0.007242 | 2.177 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000007 | 0.000007 | 6.410 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.032994 | 0.033316 | 4.617 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000018 | 0.000023 | 2.702 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.016336 | 0.016379 | 1.548 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000013 | 0.000018 | 3.276 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.033398 | 0.034668 | 2.215 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000061 | 0.000097 | 2.952 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.025003 | 0.026368 | 1.459 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/smoke/backward/ert_smoke.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-57-58__rcim_original_dataset_exact_model_bank_backward_ert_smoke_smoke_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-57-58__rcim_original_dataset_exact_model_bank_backward_ert_smoke_smoke_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-57-58__rcim_original_dataset_exact_model_bank_backward_ert_smoke_smoke_validation/validation_summary.yaml`
