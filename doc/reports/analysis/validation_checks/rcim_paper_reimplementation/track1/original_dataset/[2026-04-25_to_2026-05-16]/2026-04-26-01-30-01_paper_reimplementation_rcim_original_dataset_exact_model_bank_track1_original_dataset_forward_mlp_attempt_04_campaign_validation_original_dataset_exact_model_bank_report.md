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
- random seed: `9`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `727.188%`
- winning mean component MAE: `0.116247`
- winning mean component RMSE: `0.187364`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 727.188 | 0.116247 | 0.187364 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `MLP` | 0.005288 | 0.007472 | 10.719 |
| `fft_y_Fw_filtered_ampl_1` | `MLP` | 0.004445 | 0.006350 | 25.909 |
| `fft_y_Fw_filtered_phase_1` | `MLP` | 0.004926 | 0.007134 | 49.996 |
| `fft_y_Fw_filtered_ampl_3` | `MLP` | 0.004461 | 0.006212 | 555.006 |
| `fft_y_Fw_filtered_phase_3` | `MLP` | 0.030768 | 0.039360 | 1.717 |
| `fft_y_Fw_filtered_ampl_39` | `MLP` | 0.004461 | 0.006190 | 408.796 |
| `fft_y_Fw_filtered_phase_39` | `MLP` | 0.023224 | 0.033199 | 2.047 |
| `fft_y_Fw_filtered_ampl_40` | `MLP` | 0.004446 | 0.006196 | 549.045 |
| `fft_y_Fw_filtered_phase_40` | `MLP` | 0.052564 | 0.082508 | 58.219 |
| `fft_y_Fw_filtered_ampl_78` | `MLP` | 0.004435 | 0.006185 | 1957.473 |
| `fft_y_Fw_filtered_phase_78` | `MLP` | 0.124535 | 0.255781 | 135.331 |
| `fft_y_Fw_filtered_ampl_81` | `MLP` | 0.004457 | 0.006132 | 1377.924 |
| `fft_y_Fw_filtered_phase_81` | `MLP` | 0.058723 | 0.076820 | 6.720 |
| `fft_y_Fw_filtered_ampl_156` | `MLP` | 0.004535 | 0.006291 | 4016.471 |
| `fft_y_Fw_filtered_phase_156` | `MLP` | 0.658122 | 1.008425 | 47.876 |
| `fft_y_Fw_filtered_ampl_162` | `MLP` | 0.005029 | 0.006872 | 2843.589 |
| `fft_y_Fw_filtered_phase_162` | `MLP` | 0.596392 | 1.028175 | 26.270 |
| `fft_y_Fw_filtered_ampl_240` | `MLP` | 0.004483 | 0.006208 | 1705.199 |
| `fft_y_Fw_filtered_phase_240` | `MLP` | 0.613405 | 0.964398 | 38.258 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/mlp/2026-04-26_track1_forward_mlp_original_dataset_mega_campaign/004_track1_original_dataset_forward_mlp_attempt_04.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-28-07__track1_original_dataset_forward_mlp_attempt_04_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-28-07__track1_original_dataset_forward_mlp_attempt_04_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-28-07__track1_original_dataset_forward_mlp_attempt_04_campaign_validation/validation_summary.yaml`
