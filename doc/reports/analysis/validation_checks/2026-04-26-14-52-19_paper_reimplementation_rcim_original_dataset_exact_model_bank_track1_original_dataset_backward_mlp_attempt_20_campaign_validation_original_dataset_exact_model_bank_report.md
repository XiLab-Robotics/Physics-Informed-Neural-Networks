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
- random seed: `61`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `403.736%`
- winning mean component MAE: `0.069400`
- winning mean component RMSE: `0.146391`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 403.736 | 0.069400 | 0.146391 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `MLP` | 0.005304 | 0.006294 | 92.676 |
| `fft_y_Bw_filtered_ampl_1` | `MLP` | 0.002691 | 0.003443 | 15.704 |
| `fft_y_Bw_filtered_phase_1` | `MLP` | 0.003874 | 0.005332 | 83.060 |
| `fft_y_Bw_filtered_ampl_3` | `MLP` | 0.002720 | 0.003456 | 298.024 |
| `fft_y_Bw_filtered_phase_3` | `MLP` | 0.023926 | 0.036281 | 1.760 |
| `fft_y_Bw_filtered_ampl_39` | `MLP` | 0.002688 | 0.003436 | 587.556 |
| `fft_y_Bw_filtered_phase_39` | `MLP` | 0.392661 | 1.007947 | 15.349 |
| `fft_y_Bw_filtered_ampl_40` | `MLP` | 0.002720 | 0.003457 | 820.799 |
| `fft_y_Bw_filtered_phase_40` | `MLP` | 0.105926 | 0.154957 | 58.691 |
| `fft_y_Bw_filtered_ampl_78` | `MLP` | 0.002681 | 0.003439 | 451.486 |
| `fft_y_Bw_filtered_phase_78` | `MLP` | 0.074004 | 0.128153 | 77.097 |
| `fft_y_Bw_filtered_ampl_81` | `MLP` | 0.002695 | 0.003411 | 2321.527 |
| `fft_y_Bw_filtered_phase_81` | `MLP` | 0.081189 | 0.104923 | 83.021 |
| `fft_y_Bw_filtered_ampl_156` | `MLP` | 0.002674 | 0.004004 | 678.196 |
| `fft_y_Bw_filtered_phase_156` | `MLP` | 0.230937 | 0.680512 | 18.239 |
| `fft_y_Bw_filtered_ampl_162` | `MLP` | 0.002741 | 0.003773 | 1426.196 |
| `fft_y_Bw_filtered_phase_162` | `MLP` | 0.076790 | 0.152055 | 4.744 |
| `fft_y_Bw_filtered_ampl_240` | `MLP` | 0.002686 | 0.003447 | 618.865 |
| `fft_y_Bw_filtered_phase_240` | `MLP` | 0.299699 | 0.473102 | 17.995 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/mlp/2026-04-26_track1_backward_mlp_original_dataset_mega_campaign/020_track1_original_dataset_backward_mlp_attempt_20.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-50-07__track1_original_dataset_backward_mlp_attempt_20_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-50-07__track1_original_dataset_backward_mlp_attempt_20_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-50-07__track1_original_dataset_backward_mlp_attempt_20_campaign_validation/validation_summary.yaml`
