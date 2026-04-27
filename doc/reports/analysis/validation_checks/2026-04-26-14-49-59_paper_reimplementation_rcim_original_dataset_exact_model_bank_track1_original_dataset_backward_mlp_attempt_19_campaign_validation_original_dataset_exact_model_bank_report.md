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
- random seed: `59`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `461.016%`
- winning mean component MAE: `0.081375`
- winning mean component RMSE: `0.152514`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 461.016 | 0.081375 | 0.152514 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `MLP` | 0.004879 | 0.006102 | 166.504 |
| `fft_y_Bw_filtered_ampl_1` | `MLP` | 0.003104 | 0.003815 | 18.123 |
| `fft_y_Bw_filtered_phase_1` | `MLP` | 0.004068 | 0.005594 | 490.449 |
| `fft_y_Bw_filtered_ampl_3` | `MLP` | 0.003039 | 0.003755 | 325.784 |
| `fft_y_Bw_filtered_phase_3` | `MLP` | 0.023281 | 0.031486 | 1.727 |
| `fft_y_Bw_filtered_ampl_39` | `MLP` | 0.003049 | 0.003783 | 688.327 |
| `fft_y_Bw_filtered_phase_39` | `MLP` | 0.470505 | 1.202483 | 17.184 |
| `fft_y_Bw_filtered_ampl_40` | `MLP` | 0.003026 | 0.003744 | 967.899 |
| `fft_y_Bw_filtered_phase_40` | `MLP` | 0.102346 | 0.164105 | 36.194 |
| `fft_y_Bw_filtered_ampl_78` | `MLP` | 0.003032 | 0.003754 | 502.224 |
| `fft_y_Bw_filtered_phase_78` | `MLP` | 0.064315 | 0.097457 | 16.459 |
| `fft_y_Bw_filtered_ampl_81` | `MLP` | 0.003041 | 0.003744 | 2506.648 |
| `fft_y_Bw_filtered_phase_81` | `MLP` | 0.102266 | 0.140206 | 46.576 |
| `fft_y_Bw_filtered_ampl_156` | `MLP` | 0.002956 | 0.003849 | 692.180 |
| `fft_y_Bw_filtered_phase_156` | `MLP` | 0.193004 | 0.330623 | 30.787 |
| `fft_y_Bw_filtered_ampl_162` | `MLP` | 0.003048 | 0.003925 | 1482.551 |
| `fft_y_Bw_filtered_phase_162` | `MLP` | 0.107472 | 0.193008 | 6.261 |
| `fft_y_Bw_filtered_ampl_240` | `MLP` | 0.003215 | 0.003947 | 736.714 |
| `fft_y_Bw_filtered_phase_240` | `MLP` | 0.446479 | 0.692383 | 26.721 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/mlp/2026-04-26_track1_backward_mlp_original_dataset_mega_campaign/019_track1_original_dataset_backward_mlp_attempt_19.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-47-47__track1_original_dataset_backward_mlp_attempt_19_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-47-47__track1_original_dataset_backward_mlp_attempt_19_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-47-47__track1_original_dataset_backward_mlp_attempt_19_campaign_validation/validation_summary.yaml`
