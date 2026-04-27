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
- random seed: `13`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `447.389%`
- winning mean component MAE: `0.113336`
- winning mean component RMSE: `0.184203`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 447.389 | 0.113336 | 0.184203 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (100,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `MLP` | 0.003457 | 0.004420 | 6.804 |
| `fft_y_Fw_filtered_ampl_1` | `MLP` | 0.002992 | 0.003815 | 17.434 |
| `fft_y_Fw_filtered_phase_1` | `MLP` | 0.003616 | 0.004948 | 101.250 |
| `fft_y_Fw_filtered_ampl_3` | `MLP` | 0.002988 | 0.003831 | 380.516 |
| `fft_y_Fw_filtered_phase_3` | `MLP` | 0.025767 | 0.035815 | 1.448 |
| `fft_y_Fw_filtered_ampl_39` | `MLP` | 0.003012 | 0.003843 | 289.650 |
| `fft_y_Fw_filtered_phase_39` | `MLP` | 0.023209 | 0.033152 | 2.059 |
| `fft_y_Fw_filtered_ampl_40` | `MLP` | 0.003036 | 0.003859 | 371.230 |
| `fft_y_Fw_filtered_phase_40` | `MLP` | 0.037611 | 0.054861 | 47.998 |
| `fft_y_Fw_filtered_ampl_78` | `MLP` | 0.002994 | 0.003843 | 608.648 |
| `fft_y_Fw_filtered_phase_78` | `MLP` | 0.081893 | 0.155087 | 64.593 |
| `fft_y_Fw_filtered_ampl_81` | `MLP` | 0.003015 | 0.003856 | 1020.601 |
| `fft_y_Fw_filtered_phase_81` | `MLP` | 0.058819 | 0.078204 | 7.344 |
| `fft_y_Fw_filtered_ampl_156` | `MLP` | 0.003111 | 0.004030 | 3017.398 |
| `fft_y_Fw_filtered_phase_156` | `MLP` | 0.859446 | 1.444929 | 42.489 |
| `fft_y_Fw_filtered_ampl_162` | `MLP` | 0.003506 | 0.004853 | 1360.879 |
| `fft_y_Fw_filtered_phase_162` | `MLP` | 0.484959 | 0.770962 | 25.511 |
| `fft_y_Fw_filtered_ampl_240` | `MLP` | 0.003006 | 0.003820 | 999.213 |
| `fft_y_Fw_filtered_phase_240` | `MLP` | 0.546937 | 0.881736 | 135.333 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/mlp/2026-04-26_track1_forward_mlp_original_dataset_mega_campaign/006_track1_original_dataset_forward_mlp_attempt_06.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-32-15__track1_original_dataset_forward_mlp_attempt_06_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-32-15__track1_original_dataset_forward_mlp_attempt_06_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-32-15__track1_original_dataset_forward_mlp_attempt_06_campaign_validation/validation_summary.yaml`
