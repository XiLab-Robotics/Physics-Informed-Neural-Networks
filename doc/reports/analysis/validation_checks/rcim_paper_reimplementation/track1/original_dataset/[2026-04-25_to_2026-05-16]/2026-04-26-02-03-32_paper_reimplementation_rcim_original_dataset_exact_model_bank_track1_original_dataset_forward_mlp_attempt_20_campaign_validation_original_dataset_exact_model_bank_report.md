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
- random seed: `61`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `450.927%`
- winning mean component MAE: `0.132590`
- winning mean component RMSE: `0.247592`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 450.927 | 0.132590 | 0.247592 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `MLP` | 0.003693 | 0.004549 | 8.292 |
| `fft_y_Fw_filtered_ampl_1` | `MLP` | 0.002674 | 0.003434 | 15.568 |
| `fft_y_Fw_filtered_phase_1` | `MLP` | 0.003750 | 0.004623 | 59.025 |
| `fft_y_Fw_filtered_ampl_3` | `MLP` | 0.002695 | 0.003430 | 358.205 |
| `fft_y_Fw_filtered_phase_3` | `MLP` | 0.027792 | 0.037050 | 1.574 |
| `fft_y_Fw_filtered_ampl_39` | `MLP` | 0.002708 | 0.003465 | 268.888 |
| `fft_y_Fw_filtered_phase_39` | `MLP` | 0.021633 | 0.031367 | 1.799 |
| `fft_y_Fw_filtered_ampl_40` | `MLP` | 0.002706 | 0.003447 | 329.508 |
| `fft_y_Fw_filtered_phase_40` | `MLP` | 0.043152 | 0.061265 | 95.306 |
| `fft_y_Fw_filtered_ampl_78` | `MLP` | 0.002696 | 0.003450 | 591.405 |
| `fft_y_Fw_filtered_phase_78` | `MLP` | 0.179111 | 0.448778 | 248.347 |
| `fft_y_Fw_filtered_ampl_81` | `MLP` | 0.002691 | 0.003401 | 948.966 |
| `fft_y_Fw_filtered_phase_81` | `MLP` | 0.059989 | 0.086553 | 7.541 |
| `fft_y_Fw_filtered_ampl_156` | `MLP` | 0.002629 | 0.003409 | 2817.231 |
| `fft_y_Fw_filtered_phase_156` | `MLP` | 0.855433 | 1.435170 | 92.306 |
| `fft_y_Fw_filtered_ampl_162` | `MLP` | 0.002747 | 0.003778 | 1721.196 |
| `fft_y_Fw_filtered_phase_162` | `MLP` | 0.604514 | 1.364639 | 26.029 |
| `fft_y_Fw_filtered_ampl_240` | `MLP` | 0.002684 | 0.003435 | 934.236 |
| `fft_y_Fw_filtered_phase_240` | `MLP` | 0.695923 | 1.198997 | 42.197 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/mlp/2026-04-26_track1_forward_mlp_original_dataset_mega_campaign/020_track1_original_dataset_forward_mlp_attempt_20.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-01-39__track1_original_dataset_forward_mlp_attempt_20_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-01-39__track1_original_dataset_forward_mlp_attempt_20_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-01-39__track1_original_dataset_forward_mlp_attempt_20_campaign_validation/validation_summary.yaml`
