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

- train rows / files: `678` / `678`
- validation rows / files: `194` / `194`
- test rows / files: `97` / `97`
- validation split: `0.2`
- test split: `0.1`
- random seed: `53`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `505.968%`
- winning mean component MAE: `0.088273`
- winning mean component RMSE: `0.181499`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 505.968 | 0.088273 | 0.181499 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.001, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `MLP` | 0.004656 | 0.006298 | 151.096 |
| `fft_y_Bw_filtered_ampl_1` | `MLP` | 0.003454 | 0.004403 | 20.095 |
| `fft_y_Bw_filtered_phase_1` | `MLP` | 0.004763 | 0.006576 | 98.473 |
| `fft_y_Bw_filtered_ampl_3` | `MLP` | 0.003377 | 0.004284 | 367.668 |
| `fft_y_Bw_filtered_phase_3` | `MLP` | 0.026501 | 0.054045 | 1.973 |
| `fft_y_Bw_filtered_ampl_39` | `MLP` | 0.003393 | 0.004321 | 738.417 |
| `fft_y_Bw_filtered_phase_39` | `MLP` | 0.327831 | 0.842416 | 12.749 |
| `fft_y_Bw_filtered_ampl_40` | `MLP` | 0.003405 | 0.004323 | 1044.845 |
| `fft_y_Bw_filtered_phase_40` | `MLP` | 0.140084 | 0.208710 | 188.377 |
| `fft_y_Bw_filtered_ampl_78` | `MLP` | 0.003366 | 0.004271 | 1051.666 |
| `fft_y_Bw_filtered_phase_78` | `MLP` | 0.096958 | 0.192993 | 47.521 |
| `fft_y_Bw_filtered_ampl_81` | `MLP` | 0.003420 | 0.004349 | 2882.215 |
| `fft_y_Bw_filtered_phase_81` | `MLP` | 0.126297 | 0.194945 | 113.746 |
| `fft_y_Bw_filtered_ampl_156` | `MLP` | 0.003455 | 0.004748 | 763.706 |
| `fft_y_Bw_filtered_phase_156` | `MLP` | 0.223890 | 0.383192 | 29.615 |
| `fft_y_Bw_filtered_ampl_162` | `MLP` | 0.002255 | 0.003333 | 1024.568 |
| `fft_y_Bw_filtered_phase_162` | `MLP` | 0.125435 | 0.351246 | 7.317 |
| `fft_y_Bw_filtered_ampl_240` | `MLP` | 0.003479 | 0.004352 | 1032.487 |
| `fft_y_Bw_filtered_phase_240` | `MLP` | 0.571173 | 1.169666 | 36.858 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/mlp/2026-04-26_track1_backward_mlp_original_dataset_mega_campaign/018_track1_original_dataset_backward_mlp_attempt_18.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-45-34__track1_original_dataset_backward_mlp_attempt_18_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-45-34__track1_original_dataset_backward_mlp_attempt_18_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-45-34__track1_original_dataset_backward_mlp_attempt_18_campaign_validation/validation_summary.yaml`
