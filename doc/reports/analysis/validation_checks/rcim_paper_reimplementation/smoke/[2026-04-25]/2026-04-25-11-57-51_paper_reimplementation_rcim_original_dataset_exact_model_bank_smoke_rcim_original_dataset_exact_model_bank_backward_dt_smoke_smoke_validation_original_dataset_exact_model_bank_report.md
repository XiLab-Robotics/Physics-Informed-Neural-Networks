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

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `10.214%`
- winning mean component MAE: `0.027277`
- winning mean component RMSE: `0.028512`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 10.214 | 0.027277 | 0.028512 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.009299 | 0.009652 | 22.804 |
| `fft_y_Bw_filtered_ampl_1` | `DT` | 0.000021 | 0.000023 | 0.126 |
| `fft_y_Bw_filtered_phase_1` | `DT` | 0.001715 | 0.001897 | 15.077 |
| `fft_y_Bw_filtered_ampl_3` | `DT` | 0.000061 | 0.000062 | 5.757 |
| `fft_y_Bw_filtered_phase_3` | `DT` | 0.075186 | 0.078918 | 6.558 |
| `fft_y_Bw_filtered_ampl_39` | `DT` | 0.000050 | 0.000060 | 8.981 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.164888 | 0.164917 | 5.602 |
| `fft_y_Bw_filtered_ampl_40` | `DT` | 0.000024 | 0.000024 | 8.845 |
| `fft_y_Bw_filtered_phase_40` | `DT` | 0.146197 | 0.147675 | 45.565 |
| `fft_y_Bw_filtered_ampl_78` | `DT` | 0.000316 | 0.000327 | 18.120 |
| `fft_y_Bw_filtered_phase_78` | `DT` | 0.008445 | 0.010793 | 3.120 |
| `fft_y_Bw_filtered_ampl_81` | `DT` | 0.000008 | 0.000008 | 7.057 |
| `fft_y_Bw_filtered_phase_81` | `DT` | 0.050531 | 0.050572 | 7.049 |
| `fft_y_Bw_filtered_ampl_156` | `DT` | 0.000031 | 0.000042 | 4.797 |
| `fft_y_Bw_filtered_phase_156` | `DT` | 0.014557 | 0.016571 | 1.369 |
| `fft_y_Bw_filtered_ampl_162` | `DT` | 0.000043 | 0.000048 | 11.558 |
| `fft_y_Bw_filtered_phase_162` | `DT` | 0.023293 | 0.027069 | 1.545 |
| `fft_y_Bw_filtered_ampl_240` | `DT` | 0.000306 | 0.000314 | 18.782 |
| `fft_y_Bw_filtered_phase_240` | `DT` | 0.023295 | 0.032755 | 1.343 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/smoke/backward/dt_smoke.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-57-50__rcim_original_dataset_exact_model_bank_backward_dt_smoke_smoke_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-57-50__rcim_original_dataset_exact_model_bank_backward_dt_smoke_smoke_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-57-50__rcim_original_dataset_exact_model_bank_backward_dt_smoke_smoke_validation/validation_summary.yaml`
