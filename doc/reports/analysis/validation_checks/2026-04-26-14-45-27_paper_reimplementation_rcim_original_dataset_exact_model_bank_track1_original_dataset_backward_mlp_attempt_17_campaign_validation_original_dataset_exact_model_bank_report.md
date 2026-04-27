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
- random seed: `47`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `515.970%`
- winning mean component MAE: `0.090385`
- winning mean component RMSE: `0.184443`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 515.970 | 0.090385 | 0.184443 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.0001, 'estimator__mlp__hidden_layer_sizes': (100,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `MLP` | 0.006128 | 0.007570 | 203.132 |
| `fft_y_Bw_filtered_ampl_1` | `MLP` | 0.003821 | 0.004789 | 22.291 |
| `fft_y_Bw_filtered_phase_1` | `MLP` | 0.005032 | 0.006453 | 190.759 |
| `fft_y_Bw_filtered_ampl_3` | `MLP` | 0.003820 | 0.004840 | 397.348 |
| `fft_y_Bw_filtered_phase_3` | `MLP` | 0.025111 | 0.044461 | 1.882 |
| `fft_y_Bw_filtered_ampl_39` | `MLP` | 0.003794 | 0.004809 | 808.568 |
| `fft_y_Bw_filtered_phase_39` | `MLP` | 0.546516 | 1.440403 | 20.268 |
| `fft_y_Bw_filtered_ampl_40` | `MLP` | 0.003798 | 0.004821 | 1160.114 |
| `fft_y_Bw_filtered_phase_40` | `MLP` | 0.112388 | 0.186670 | 42.701 |
| `fft_y_Bw_filtered_ampl_78` | `MLP` | 0.003812 | 0.004826 | 480.018 |
| `fft_y_Bw_filtered_phase_78` | `MLP` | 0.066466 | 0.113219 | 43.115 |
| `fft_y_Bw_filtered_ampl_81` | `MLP` | 0.003807 | 0.004837 | 3311.622 |
| `fft_y_Bw_filtered_phase_81` | `MLP` | 0.123609 | 0.164588 | 61.233 |
| `fft_y_Bw_filtered_ampl_156` | `MLP` | 0.004327 | 0.005862 | 812.255 |
| `fft_y_Bw_filtered_phase_156` | `MLP` | 0.313987 | 0.635735 | 44.562 |
| `fft_y_Bw_filtered_ampl_162` | `MLP` | 0.004134 | 0.005406 | 1430.668 |
| `fft_y_Bw_filtered_phase_162` | `MLP` | 0.103591 | 0.179613 | 6.218 |
| `fft_y_Bw_filtered_ampl_240` | `MLP` | 0.003725 | 0.004749 | 743.549 |
| `fft_y_Bw_filtered_phase_240` | `MLP` | 0.379453 | 0.680759 | 23.135 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/mlp/2026-04-26_track1_backward_mlp_original_dataset_mega_campaign/017_track1_original_dataset_backward_mlp_attempt_17.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-43-07__track1_original_dataset_backward_mlp_attempt_17_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-43-07__track1_original_dataset_backward_mlp_attempt_17_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-43-07__track1_original_dataset_backward_mlp_attempt_17_campaign_validation/validation_summary.yaml`
