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
- random seed: `37`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `571.791%`
- winning mean component MAE: `0.116075`
- winning mean component RMSE: `0.207442`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 571.791 | 0.116075 | 0.207442 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (100,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `MLP` | 0.003737 | 0.004825 | 8.073 |
| `fft_y_Fw_filtered_ampl_1` | `MLP` | 0.003420 | 0.004306 | 19.933 |
| `fft_y_Fw_filtered_phase_1` | `MLP` | 0.004117 | 0.005265 | 96.583 |
| `fft_y_Fw_filtered_ampl_3` | `MLP` | 0.003258 | 0.004078 | 419.751 |
| `fft_y_Fw_filtered_phase_3` | `MLP` | 0.030457 | 0.039737 | 1.715 |
| `fft_y_Fw_filtered_ampl_39` | `MLP` | 0.003224 | 0.004022 | 297.829 |
| `fft_y_Fw_filtered_phase_39` | `MLP` | 0.024304 | 0.036572 | 2.055 |
| `fft_y_Fw_filtered_ampl_40` | `MLP` | 0.002156 | 0.002941 | 264.096 |
| `fft_y_Fw_filtered_phase_40` | `MLP` | 0.041032 | 0.059483 | 71.388 |
| `fft_y_Fw_filtered_ampl_78` | `MLP` | 0.003218 | 0.004018 | 628.183 |
| `fft_y_Fw_filtered_phase_78` | `MLP` | 0.135713 | 0.354620 | 343.484 |
| `fft_y_Fw_filtered_ampl_81` | `MLP` | 0.003319 | 0.004166 | 1131.049 |
| `fft_y_Fw_filtered_phase_81` | `MLP` | 0.058438 | 0.091133 | 8.735 |
| `fft_y_Fw_filtered_ampl_156` | `MLP` | 0.003413 | 0.004357 | 4472.393 |
| `fft_y_Fw_filtered_phase_156` | `MLP` | 0.804619 | 1.296405 | 56.018 |
| `fft_y_Fw_filtered_ampl_162` | `MLP` | 0.003122 | 0.004035 | 1833.602 |
| `fft_y_Fw_filtered_phase_162` | `MLP` | 0.610109 | 1.225618 | 24.444 |
| `fft_y_Fw_filtered_ampl_240` | `MLP` | 0.003341 | 0.004125 | 1112.632 |
| `fft_y_Fw_filtered_phase_240` | `MLP` | 0.464437 | 0.791685 | 72.069 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/mlp/2026-04-26_track1_forward_mlp_original_dataset_mega_campaign/015_track1_original_dataset_forward_mlp_attempt_15.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-51-10__track1_original_dataset_forward_mlp_attempt_15_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-51-10__track1_original_dataset_forward_mlp_attempt_15_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-51-10__track1_original_dataset_forward_mlp_attempt_15_campaign_validation/validation_summary.yaml`
