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

- train rows / files: `678` / `678`
- validation rows / files: `194` / `194`
- test rows / files: `97` / `97`
- validation split: `0.2`
- test split: `0.1`
- random seed: `15`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `493.289%`
- winning mean component MAE: `0.117703`
- winning mean component RMSE: `0.196275`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 493.289 | 0.117703 | 0.196275 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `MLP` | 0.004629 | 0.006304 | 24.054 |
| `fft_y_Fw_filtered_ampl_1` | `MLP` | 0.002413 | 0.002997 | 14.059 |
| `fft_y_Fw_filtered_phase_1` | `MLP` | 0.004854 | 0.005936 | 72.354 |
| `fft_y_Fw_filtered_ampl_3` | `MLP` | 0.002495 | 0.003062 | 329.791 |
| `fft_y_Fw_filtered_phase_3` | `MLP` | 0.027993 | 0.036553 | 1.570 |
| `fft_y_Fw_filtered_ampl_39` | `MLP` | 0.002494 | 0.003052 | 250.208 |
| `fft_y_Fw_filtered_phase_39` | `MLP` | 0.027987 | 0.045776 | 2.228 |
| `fft_y_Fw_filtered_ampl_40` | `MLP` | 0.002479 | 0.003044 | 301.831 |
| `fft_y_Fw_filtered_phase_40` | `MLP` | 0.048803 | 0.081697 | 54.998 |
| `fft_y_Fw_filtered_ampl_78` | `MLP` | 0.002457 | 0.003015 | 2265.303 |
| `fft_y_Fw_filtered_phase_78` | `MLP` | 0.121645 | 0.234968 | 61.490 |
| `fft_y_Fw_filtered_ampl_81` | `MLP` | 0.002451 | 0.003030 | 821.402 |
| `fft_y_Fw_filtered_phase_81` | `MLP` | 0.065669 | 0.111535 | 6.936 |
| `fft_y_Fw_filtered_ampl_156` | `MLP` | 0.002460 | 0.003070 | 2438.496 |
| `fft_y_Fw_filtered_phase_156` | `MLP` | 0.871565 | 1.331199 | 54.955 |
| `fft_y_Fw_filtered_ampl_162` | `MLP` | 0.002879 | 0.003887 | 1734.556 |
| `fft_y_Fw_filtered_phase_162` | `MLP` | 0.528870 | 0.978061 | 35.393 |
| `fft_y_Fw_filtered_ampl_240` | `MLP` | 0.002557 | 0.003112 | 873.279 |
| `fft_y_Fw_filtered_phase_240` | `MLP` | 0.511665 | 0.868919 | 29.590 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/mlp/2026-04-26_track1_forward_mlp_original_dataset_mega_campaign/007_track1_original_dataset_forward_mlp_attempt_07.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-34-27__track1_original_dataset_forward_mlp_attempt_07_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-34-27__track1_original_dataset_forward_mlp_attempt_07_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-34-27__track1_original_dataset_forward_mlp_attempt_07_campaign_validation/validation_summary.yaml`
