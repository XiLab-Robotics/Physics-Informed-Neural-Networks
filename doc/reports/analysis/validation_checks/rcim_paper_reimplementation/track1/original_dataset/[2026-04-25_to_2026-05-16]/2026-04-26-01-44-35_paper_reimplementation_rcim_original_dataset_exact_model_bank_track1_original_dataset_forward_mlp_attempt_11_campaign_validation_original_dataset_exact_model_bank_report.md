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
- random seed: `23`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `495.903%`
- winning mean component MAE: `0.115912`
- winning mean component RMSE: `0.219343`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 495.903 | 0.115912 | 0.219343 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `MLP` | 0.003735 | 0.004374 | 7.458 |
| `fft_y_Fw_filtered_ampl_1` | `MLP` | 0.002797 | 0.003422 | 16.300 |
| `fft_y_Fw_filtered_phase_1` | `MLP` | 0.003523 | 0.004638 | 54.517 |
| `fft_y_Fw_filtered_ampl_3` | `MLP` | 0.002841 | 0.003476 | 369.318 |
| `fft_y_Fw_filtered_phase_3` | `MLP` | 0.023393 | 0.032097 | 1.315 |
| `fft_y_Fw_filtered_ampl_39` | `MLP` | 0.002846 | 0.003484 | 269.524 |
| `fft_y_Fw_filtered_phase_39` | `MLP` | 0.026329 | 0.039289 | 2.280 |
| `fft_y_Fw_filtered_ampl_40` | `MLP` | 0.002825 | 0.003467 | 356.250 |
| `fft_y_Fw_filtered_phase_40` | `MLP` | 0.042131 | 0.059923 | 186.118 |
| `fft_y_Fw_filtered_ampl_78` | `MLP` | 0.002819 | 0.003446 | 706.416 |
| `fft_y_Fw_filtered_phase_78` | `MLP` | 0.085210 | 0.137114 | 106.095 |
| `fft_y_Fw_filtered_ampl_81` | `MLP` | 0.002850 | 0.003482 | 953.197 |
| `fft_y_Fw_filtered_phase_81` | `MLP` | 0.060615 | 0.089420 | 6.074 |
| `fft_y_Fw_filtered_ampl_156` | `MLP` | 0.002749 | 0.003452 | 3393.222 |
| `fft_y_Fw_filtered_phase_156` | `MLP` | 0.800770 | 1.412392 | 41.872 |
| `fft_y_Fw_filtered_ampl_162` | `MLP` | 0.003000 | 0.003838 | 1941.173 |
| `fft_y_Fw_filtered_phase_162` | `MLP` | 0.657037 | 1.461012 | 26.476 |
| `fft_y_Fw_filtered_ampl_240` | `MLP` | 0.002930 | 0.003562 | 940.896 |
| `fft_y_Fw_filtered_phase_240` | `MLP` | 0.473933 | 0.895635 | 43.649 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/mlp/2026-04-26_track1_forward_mlp_original_dataset_mega_campaign/011_track1_original_dataset_forward_mlp_attempt_11.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-42-44__track1_original_dataset_forward_mlp_attempt_11_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-42-44__track1_original_dataset_forward_mlp_attempt_11_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-42-44__track1_original_dataset_forward_mlp_attempt_11_campaign_validation/validation_summary.yaml`
