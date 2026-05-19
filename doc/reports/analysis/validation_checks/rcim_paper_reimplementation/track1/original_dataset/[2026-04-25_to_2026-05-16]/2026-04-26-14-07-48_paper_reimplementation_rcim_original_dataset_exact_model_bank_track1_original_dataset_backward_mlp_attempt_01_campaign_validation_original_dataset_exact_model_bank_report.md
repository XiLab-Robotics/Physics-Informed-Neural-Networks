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
- random seed: `0`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `423.669%`
- winning mean component MAE: `0.078244`
- winning mean component RMSE: `0.149154`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 423.669 | 0.078244 | 0.149154 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `MLP` | 0.005342 | 0.006565 | 225.157 |
| `fft_y_Bw_filtered_ampl_1` | `MLP` | 0.002914 | 0.003555 | 17.007 |
| `fft_y_Bw_filtered_phase_1` | `MLP` | 0.003588 | 0.005129 | 45.759 |
| `fft_y_Bw_filtered_ampl_3` | `MLP` | 0.002812 | 0.003481 | 297.053 |
| `fft_y_Bw_filtered_phase_3` | `MLP` | 0.026210 | 0.034639 | 1.871 |
| `fft_y_Bw_filtered_ampl_39` | `MLP` | 0.002830 | 0.003537 | 681.678 |
| `fft_y_Bw_filtered_phase_39` | `MLP` | 0.484149 | 0.850850 | 17.791 |
| `fft_y_Bw_filtered_ampl_40` | `MLP` | 0.002846 | 0.003463 | 908.057 |
| `fft_y_Bw_filtered_phase_40` | `MLP` | 0.102074 | 0.143648 | 37.605 |
| `fft_y_Bw_filtered_ampl_78` | `MLP` | 0.002822 | 0.003440 | 436.406 |
| `fft_y_Bw_filtered_phase_78` | `MLP` | 0.056048 | 0.096342 | 42.870 |
| `fft_y_Bw_filtered_ampl_81` | `MLP` | 0.002851 | 0.003492 | 2622.484 |
| `fft_y_Bw_filtered_phase_81` | `MLP` | 0.084723 | 0.106972 | 29.817 |
| `fft_y_Bw_filtered_ampl_156` | `MLP` | 0.002833 | 0.003591 | 644.891 |
| `fft_y_Bw_filtered_phase_156` | `MLP` | 0.224206 | 0.611828 | 25.663 |
| `fft_y_Bw_filtered_ampl_162` | `MLP` | 0.003116 | 0.004119 | 1243.960 |
| `fft_y_Bw_filtered_phase_162` | `MLP` | 0.100990 | 0.168262 | 5.984 |
| `fft_y_Bw_filtered_ampl_240` | `MLP` | 0.003034 | 0.003809 | 741.334 |
| `fft_y_Bw_filtered_phase_240` | `MLP` | 0.373241 | 0.777209 | 24.316 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/mlp/2026-04-26_track1_backward_mlp_original_dataset_mega_campaign/001_track1_original_dataset_backward_mlp_attempt_01.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-05-36__track1_original_dataset_backward_mlp_attempt_01_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-05-36__track1_original_dataset_backward_mlp_attempt_01_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-05-36__track1_original_dataset_backward_mlp_attempt_01_campaign_validation/validation_summary.yaml`
