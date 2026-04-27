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
- random seed: `31`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `695.830%`
- winning mean component MAE: `0.139587`
- winning mean component RMSE: `0.243527`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 695.830 | 0.139587 | 0.243527 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `MLP` | 0.005330 | 0.007197 | 11.312 |
| `fft_y_Fw_filtered_ampl_1` | `MLP` | 0.004756 | 0.006521 | 27.730 |
| `fft_y_Fw_filtered_phase_1` | `MLP` | 0.004108 | 0.005897 | 67.368 |
| `fft_y_Fw_filtered_ampl_3` | `MLP` | 0.002104 | 0.002748 | 284.794 |
| `fft_y_Fw_filtered_phase_3` | `MLP` | 0.031879 | 0.044950 | 1.745 |
| `fft_y_Fw_filtered_ampl_39` | `MLP` | 0.002045 | 0.002663 | 208.061 |
| `fft_y_Fw_filtered_phase_39` | `MLP` | 0.028988 | 0.051025 | 2.392 |
| `fft_y_Fw_filtered_ampl_40` | `MLP` | 0.003048 | 0.003778 | 378.163 |
| `fft_y_Fw_filtered_phase_40` | `MLP` | 0.039138 | 0.062705 | 81.956 |
| `fft_y_Fw_filtered_ampl_78` | `MLP` | 0.002060 | 0.002699 | 741.657 |
| `fft_y_Fw_filtered_phase_78` | `MLP` | 0.142802 | 0.484171 | 510.026 |
| `fft_y_Fw_filtered_ampl_81` | `MLP` | 0.004696 | 0.006216 | 1418.968 |
| `fft_y_Fw_filtered_phase_81` | `MLP` | 0.067858 | 0.113828 | 6.248 |
| `fft_y_Fw_filtered_ampl_156` | `MLP` | 0.004699 | 0.006249 | 5165.880 |
| `fft_y_Fw_filtered_phase_156` | `MLP` | 0.920897 | 1.371088 | 49.970 |
| `fft_y_Fw_filtered_ampl_162` | `MLP` | 0.004967 | 0.006702 | 2977.329 |
| `fft_y_Fw_filtered_phase_162` | `MLP` | 0.522947 | 0.887014 | 24.447 |
| `fft_y_Fw_filtered_ampl_240` | `MLP` | 0.003102 | 0.003811 | 1220.680 |
| `fft_y_Fw_filtered_phase_240` | `MLP` | 0.856729 | 1.557758 | 42.041 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/mlp/2026-04-26_track1_forward_mlp_original_dataset_mega_campaign/014_track1_original_dataset_forward_mlp_attempt_14.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-48-57__track1_original_dataset_forward_mlp_attempt_14_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-48-57__track1_original_dataset_forward_mlp_attempt_14_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-48-57__track1_original_dataset_forward_mlp_attempt_14_campaign_validation/validation_summary.yaml`
