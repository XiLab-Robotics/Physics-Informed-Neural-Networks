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
- random seed: `15`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `390.574%`
- winning mean component MAE: `0.091309`
- winning mean component RMSE: `0.183377`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 390.574 | 0.091309 | 0.183377 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.001, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `MLP` | 0.004654 | 0.006054 | 74.954 |
| `fft_y_Bw_filtered_ampl_1` | `MLP` | 0.002592 | 0.003181 | 15.109 |
| `fft_y_Bw_filtered_phase_1` | `MLP` | 0.003488 | 0.004644 | 100.246 |
| `fft_y_Bw_filtered_ampl_3` | `MLP` | 0.002470 | 0.003060 | 266.709 |
| `fft_y_Bw_filtered_phase_3` | `MLP` | 0.025241 | 0.041735 | 1.856 |
| `fft_y_Bw_filtered_ampl_39` | `MLP` | 0.002478 | 0.003062 | 563.736 |
| `fft_y_Bw_filtered_phase_39` | `MLP` | 0.606415 | 1.426407 | 21.693 |
| `fft_y_Bw_filtered_ampl_40` | `MLP` | 0.002487 | 0.003062 | 773.177 |
| `fft_y_Bw_filtered_phase_40` | `MLP` | 0.102045 | 0.170665 | 32.284 |
| `fft_y_Bw_filtered_ampl_78` | `MLP` | 0.002507 | 0.003068 | 527.012 |
| `fft_y_Bw_filtered_phase_78` | `MLP` | 0.065463 | 0.102981 | 20.797 |
| `fft_y_Bw_filtered_ampl_81` | `MLP` | 0.002466 | 0.003048 | 2147.681 |
| `fft_y_Bw_filtered_phase_81` | `MLP` | 0.108285 | 0.160070 | 114.585 |
| `fft_y_Bw_filtered_ampl_156` | `MLP` | 0.002325 | 0.003597 | 581.264 |
| `fft_y_Bw_filtered_phase_156` | `MLP` | 0.200666 | 0.573954 | 60.670 |
| `fft_y_Bw_filtered_ampl_162` | `MLP` | 0.002919 | 0.003861 | 1411.127 |
| `fft_y_Bw_filtered_phase_162` | `MLP` | 0.091552 | 0.148633 | 6.130 |
| `fft_y_Bw_filtered_ampl_240` | `MLP` | 0.002598 | 0.003108 | 677.527 |
| `fft_y_Bw_filtered_phase_240` | `MLP` | 0.504213 | 0.819972 | 24.346 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/mlp/2026-04-26_track1_backward_mlp_original_dataset_mega_campaign/007_track1_original_dataset_backward_mlp_attempt_07.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-19-44__track1_original_dataset_backward_mlp_attempt_07_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-19-44__track1_original_dataset_backward_mlp_attempt_07_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-19-44__track1_original_dataset_backward_mlp_attempt_07_campaign_validation/validation_summary.yaml`
