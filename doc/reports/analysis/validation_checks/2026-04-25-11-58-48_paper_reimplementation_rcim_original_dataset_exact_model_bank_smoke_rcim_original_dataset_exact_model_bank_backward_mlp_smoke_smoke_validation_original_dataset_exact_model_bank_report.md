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

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `10054.512%`
- winning mean component MAE: `0.116018`
- winning mean component RMSE: `0.145249`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 10054.512 | 0.116018 | 0.145249 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `MLP` | 0.094663 | 0.120478 | 274.435 |
| `fft_y_Bw_filtered_ampl_1` | `MLP` | 0.083457 | 0.111178 | 488.042 |
| `fft_y_Bw_filtered_phase_1` | `MLP` | 0.082736 | 0.121324 | 774.882 |
| `fft_y_Bw_filtered_ampl_3` | `MLP` | 0.088028 | 0.121494 | 8752.849 |
| `fft_y_Bw_filtered_phase_3` | `MLP` | 0.050273 | 0.056623 | 4.445 |
| `fft_y_Bw_filtered_ampl_39` | `MLP` | 0.088959 | 0.121189 | 22409.288 |
| `fft_y_Bw_filtered_phase_39` | `MLP` | 0.582861 | 0.640208 | 19.324 |
| `fft_y_Bw_filtered_ampl_40` | `MLP` | 0.088837 | 0.121419 | 29851.784 |
| `fft_y_Bw_filtered_phase_40` | `MLP` | 0.178547 | 0.183804 | 55.501 |
| `fft_y_Bw_filtered_ampl_78` | `MLP` | 0.087795 | 0.121401 | 6136.853 |
| `fft_y_Bw_filtered_phase_78` | `MLP` | 0.129161 | 0.165797 | 50.574 |
| `fft_y_Bw_filtered_ampl_81` | `MLP` | 0.089986 | 0.122599 | 74535.624 |
| `fft_y_Bw_filtered_phase_81` | `MLP` | 0.053710 | 0.076923 | 7.780 |
| `fft_y_Bw_filtered_ampl_156` | `MLP` | 0.088285 | 0.121033 | 13770.672 |
| `fft_y_Bw_filtered_phase_156` | `MLP` | 0.076654 | 0.094215 | 7.117 |
| `fft_y_Bw_filtered_ampl_162` | `MLP` | 0.089346 | 0.121324 | 27290.118 |
| `fft_y_Bw_filtered_phase_162` | `MLP` | 0.090713 | 0.129319 | 5.952 |
| `fft_y_Bw_filtered_ampl_240` | `MLP` | 0.087943 | 0.121503 | 6596.303 |
| `fft_y_Bw_filtered_phase_240` | `MLP` | 0.072378 | 0.087891 | 4.189 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/smoke/backward/mlp_smoke.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-58-47__rcim_original_dataset_exact_model_bank_backward_mlp_smoke_smoke_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-58-47__rcim_original_dataset_exact_model_bank_backward_mlp_smoke_smoke_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_smoke/2026-04-25-11-58-47__rcim_original_dataset_exact_model_bank_backward_mlp_smoke_smoke_validation/validation_summary.yaml`
