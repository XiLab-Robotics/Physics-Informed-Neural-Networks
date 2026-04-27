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
- random seed: `21`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `534.076%`
- winning mean component MAE: `0.142294`
- winning mean component RMSE: `0.244298`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 534.076 | 0.142294 | 0.244298 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.001, 'estimator__mlp__hidden_layer_sizes': (100,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `MLP` | 0.004250 | 0.005525 | 9.023 |
| `fft_y_Fw_filtered_ampl_1` | `MLP` | 0.003686 | 0.004866 | 21.509 |
| `fft_y_Fw_filtered_phase_1` | `MLP` | 0.004287 | 0.005677 | 57.882 |
| `fft_y_Fw_filtered_ampl_3` | `MLP` | 0.003742 | 0.004925 | 459.944 |
| `fft_y_Fw_filtered_phase_3` | `MLP` | 0.027542 | 0.035582 | 1.526 |
| `fft_y_Fw_filtered_ampl_39` | `MLP` | 0.003750 | 0.004942 | 350.540 |
| `fft_y_Fw_filtered_phase_39` | `MLP` | 0.032161 | 0.050997 | 2.593 |
| `fft_y_Fw_filtered_ampl_40` | `MLP` | 0.003767 | 0.004947 | 465.159 |
| `fft_y_Fw_filtered_phase_40` | `MLP` | 0.050524 | 0.073716 | 170.426 |
| `fft_y_Fw_filtered_ampl_78` | `MLP` | 0.003719 | 0.004911 | 518.634 |
| `fft_y_Fw_filtered_phase_78` | `MLP` | 0.118189 | 0.218566 | 163.233 |
| `fft_y_Fw_filtered_ampl_81` | `MLP` | 0.003773 | 0.004972 | 1246.807 |
| `fft_y_Fw_filtered_phase_81` | `MLP` | 0.066959 | 0.104450 | 10.062 |
| `fft_y_Fw_filtered_ampl_156` | `MLP` | 0.003913 | 0.005189 | 3420.284 |
| `fft_y_Fw_filtered_phase_156` | `MLP` | 1.300560 | 2.149784 | 155.679 |
| `fft_y_Fw_filtered_ampl_162` | `MLP` | 0.004142 | 0.005742 | 1768.396 |
| `fft_y_Fw_filtered_phase_162` | `MLP` | 0.497579 | 0.843098 | 25.968 |
| `fft_y_Fw_filtered_ampl_240` | `MLP` | 0.003852 | 0.004965 | 1074.979 |
| `fft_y_Fw_filtered_phase_240` | `MLP` | 0.567191 | 1.108806 | 224.791 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/mlp/2026-04-26_track1_forward_mlp_original_dataset_mega_campaign/010_track1_original_dataset_forward_mlp_attempt_10.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-40-36__track1_original_dataset_forward_mlp_attempt_10_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-40-36__track1_original_dataset_forward_mlp_attempt_10_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-40-36__track1_original_dataset_forward_mlp_attempt_10_campaign_validation/validation_summary.yaml`
