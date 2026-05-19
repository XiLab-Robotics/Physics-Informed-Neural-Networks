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
- random seed: `5`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `528.961%`
- winning mean component MAE: `0.096991`
- winning mean component RMSE: `0.203047`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 528.961 | 0.096991 | 0.203047 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (100,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `MLP` | 0.006271 | 0.008298 | 154.001 |
| `fft_y_Bw_filtered_ampl_1` | `MLP` | 0.003573 | 0.004489 | 20.871 |
| `fft_y_Bw_filtered_phase_1` | `MLP` | 0.005038 | 0.006322 | 172.540 |
| `fft_y_Bw_filtered_ampl_3` | `MLP` | 0.003658 | 0.004526 | 378.997 |
| `fft_y_Bw_filtered_phase_3` | `MLP` | 0.028507 | 0.045836 | 2.195 |
| `fft_y_Bw_filtered_ampl_39` | `MLP` | 0.003597 | 0.004499 | 780.490 |
| `fft_y_Bw_filtered_phase_39` | `MLP` | 0.627940 | 1.578533 | 22.297 |
| `fft_y_Bw_filtered_ampl_40` | `MLP` | 0.003653 | 0.004528 | 1166.543 |
| `fft_y_Bw_filtered_phase_40` | `MLP` | 0.113893 | 0.191627 | 56.578 |
| `fft_y_Bw_filtered_ampl_78` | `MLP` | 0.003621 | 0.004523 | 586.068 |
| `fft_y_Bw_filtered_phase_78` | `MLP` | 0.077340 | 0.125830 | 26.546 |
| `fft_y_Bw_filtered_ampl_81` | `MLP` | 0.003663 | 0.004531 | 3039.247 |
| `fft_y_Bw_filtered_phase_81` | `MLP` | 0.104517 | 0.140097 | 36.430 |
| `fft_y_Bw_filtered_ampl_156` | `MLP` | 0.003918 | 0.004969 | 906.720 |
| `fft_y_Bw_filtered_phase_156` | `MLP` | 0.279601 | 0.645590 | 41.222 |
| `fft_y_Bw_filtered_ampl_162` | `MLP` | 0.003791 | 0.004905 | 1785.897 |
| `fft_y_Bw_filtered_phase_162` | `MLP` | 0.115481 | 0.255515 | 6.233 |
| `fft_y_Bw_filtered_ampl_240` | `MLP` | 0.003744 | 0.004623 | 844.885 |
| `fft_y_Bw_filtered_phase_240` | `MLP` | 0.451024 | 0.818658 | 22.500 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/mlp/2026-04-26_track1_backward_mlp_original_dataset_mega_campaign/002_track1_original_dataset_backward_mlp_attempt_02.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-07-55__track1_original_dataset_backward_mlp_attempt_02_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-07-55__track1_original_dataset_backward_mlp_attempt_02_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-07-55__track1_original_dataset_backward_mlp_attempt_02_campaign_validation/validation_summary.yaml`
