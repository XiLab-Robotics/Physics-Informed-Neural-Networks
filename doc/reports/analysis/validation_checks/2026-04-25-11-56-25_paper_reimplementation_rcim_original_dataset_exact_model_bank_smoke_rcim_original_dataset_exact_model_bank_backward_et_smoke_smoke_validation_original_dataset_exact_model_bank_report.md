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

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `15.414%`
- winning mean component MAE: `0.127603`
- winning mean component RMSE: `0.199844`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 15.414 | 0.127603 | 0.199844 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.010428 | 0.010557 | 27.323 |
| `fft_y_Bw_filtered_ampl_1` | `ET` | 0.000021 | 0.000022 | 0.125 |
| `fft_y_Bw_filtered_phase_1` | `ET` | 0.002165 | 0.002343 | 20.787 |
| `fft_y_Bw_filtered_ampl_3` | `ET` | 0.000069 | 0.000069 | 6.523 |
| `fft_y_Bw_filtered_phase_3` | `ET` | 0.104087 | 0.106660 | 8.896 |
| `fft_y_Bw_filtered_ampl_39` | `ET` | 0.000125 | 0.000131 | 25.255 |
| `fft_y_Bw_filtered_phase_39` | `ET` | 2.094928 | 3.442425 | 68.814 |
| `fft_y_Bw_filtered_ampl_40` | `ET` | 0.000034 | 0.000037 | 13.237 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.081400 | 0.084068 | 25.329 |
| `fft_y_Bw_filtered_ampl_78` | `ET` | 0.000429 | 0.000435 | 26.210 |
| `fft_y_Bw_filtered_phase_78` | `ET` | 0.016384 | 0.017868 | 6.245 |
| `fft_y_Bw_filtered_ampl_81` | `ET` | 0.000007 | 0.000009 | 6.664 |
| `fft_y_Bw_filtered_phase_81` | `ET` | 0.048022 | 0.048262 | 6.705 |
| `fft_y_Bw_filtered_ampl_156` | `ET` | 0.000032 | 0.000044 | 4.948 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.022488 | 0.027503 | 2.154 |
| `fft_y_Bw_filtered_ampl_162` | `ET` | 0.000049 | 0.000051 | 13.866 |
| `fft_y_Bw_filtered_phase_162` | `ET` | 0.021081 | 0.025057 | 1.406 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000413 | 0.000421 | 27.100 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.022300 | 0.031080 | 1.286 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/smoke/backward/et_smoke.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-56-24__rcim_original_dataset_exact_model_bank_backward_et_smoke_smoke_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-56-24__rcim_original_dataset_exact_model_bank_backward_et_smoke_smoke_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-56-24__rcim_original_dataset_exact_model_bank_backward_et_smoke_smoke_validation/validation_summary.yaml`
