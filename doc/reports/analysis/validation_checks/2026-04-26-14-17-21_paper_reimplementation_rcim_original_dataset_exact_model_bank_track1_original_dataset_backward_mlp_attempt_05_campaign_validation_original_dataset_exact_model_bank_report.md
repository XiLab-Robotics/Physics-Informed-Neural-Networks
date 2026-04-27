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
- random seed: `11`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `513.300%`
- winning mean component MAE: `0.090399`
- winning mean component RMSE: `0.182476`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 513.300 | 0.090399 | 0.182476 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (100,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `MLP` | 0.005269 | 0.006767 | 183.017 |
| `fft_y_Bw_filtered_ampl_1` | `MLP` | 0.003565 | 0.004550 | 20.789 |
| `fft_y_Bw_filtered_phase_1` | `MLP` | 0.004357 | 0.005853 | 126.672 |
| `fft_y_Bw_filtered_ampl_3` | `MLP` | 0.003773 | 0.004783 | 393.065 |
| `fft_y_Bw_filtered_phase_3` | `MLP` | 0.024118 | 0.032662 | 1.811 |
| `fft_y_Bw_filtered_ampl_39` | `MLP` | 0.003733 | 0.004743 | 815.568 |
| `fft_y_Bw_filtered_phase_39` | `MLP` | 0.594906 | 1.429358 | 21.433 |
| `fft_y_Bw_filtered_ampl_40` | `MLP` | 0.003771 | 0.004782 | 1216.499 |
| `fft_y_Bw_filtered_phase_40` | `MLP` | 0.086572 | 0.117351 | 53.225 |
| `fft_y_Bw_filtered_ampl_78` | `MLP` | 0.003733 | 0.004754 | 492.989 |
| `fft_y_Bw_filtered_phase_78` | `MLP` | 0.067536 | 0.123984 | 25.210 |
| `fft_y_Bw_filtered_ampl_81` | `MLP` | 0.003792 | 0.004805 | 3224.039 |
| `fft_y_Bw_filtered_phase_81` | `MLP` | 0.097620 | 0.133896 | 202.375 |
| `fft_y_Bw_filtered_ampl_156` | `MLP` | 0.004301 | 0.005697 | 703.545 |
| `fft_y_Bw_filtered_phase_156` | `MLP` | 0.272906 | 0.552147 | 24.165 |
| `fft_y_Bw_filtered_ampl_162` | `MLP` | 0.003973 | 0.005252 | 1344.008 |
| `fft_y_Bw_filtered_phase_162` | `MLP` | 0.089751 | 0.178372 | 5.524 |
| `fft_y_Bw_filtered_ampl_240` | `MLP` | 0.003734 | 0.004719 | 871.894 |
| `fft_y_Bw_filtered_phase_240` | `MLP` | 0.440174 | 0.842580 | 26.875 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/mlp/2026-04-26_track1_backward_mlp_original_dataset_mega_campaign/005_track1_original_dataset_backward_mlp_attempt_05.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-15-08__track1_original_dataset_backward_mlp_attempt_05_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-15-08__track1_original_dataset_backward_mlp_attempt_05_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-15-08__track1_original_dataset_backward_mlp_attempt_05_campaign_validation/validation_summary.yaml`
