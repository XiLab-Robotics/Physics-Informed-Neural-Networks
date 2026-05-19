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
- random seed: `11`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `526.387%`
- winning mean component MAE: `0.126892`
- winning mean component RMSE: `0.223494`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 526.387 | 0.126892 | 0.223494 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (100,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `MLP` | 0.004435 | 0.005534 | 8.710 |
| `fft_y_Fw_filtered_ampl_1` | `MLP` | 0.003583 | 0.004572 | 20.877 |
| `fft_y_Fw_filtered_phase_1` | `MLP` | 0.004752 | 0.006067 | 56.247 |
| `fft_y_Fw_filtered_ampl_3` | `MLP` | 0.003756 | 0.004769 | 456.354 |
| `fft_y_Fw_filtered_phase_3` | `MLP` | 0.031301 | 0.042252 | 1.726 |
| `fft_y_Fw_filtered_ampl_39` | `MLP` | 0.003745 | 0.004756 | 345.790 |
| `fft_y_Fw_filtered_phase_39` | `MLP` | 0.025494 | 0.045953 | 2.042 |
| `fft_y_Fw_filtered_ampl_40` | `MLP` | 0.003781 | 0.004793 | 463.191 |
| `fft_y_Fw_filtered_phase_40` | `MLP` | 0.051088 | 0.074790 | 80.964 |
| `fft_y_Fw_filtered_ampl_78` | `MLP` | 0.003771 | 0.004785 | 1023.210 |
| `fft_y_Fw_filtered_phase_78` | `MLP` | 0.134175 | 0.391251 | 729.587 |
| `fft_y_Fw_filtered_ampl_81` | `MLP` | 0.003777 | 0.004795 | 1230.079 |
| `fft_y_Fw_filtered_phase_81` | `MLP` | 0.062654 | 0.090384 | 6.177 |
| `fft_y_Fw_filtered_ampl_156` | `MLP` | 0.003951 | 0.005099 | 2441.013 |
| `fft_y_Fw_filtered_phase_156` | `MLP` | 0.994681 | 1.688525 | 122.917 |
| `fft_y_Fw_filtered_ampl_162` | `MLP` | 0.003992 | 0.005256 | 1876.228 |
| `fft_y_Fw_filtered_phase_162` | `MLP` | 0.578841 | 1.019622 | 26.672 |
| `fft_y_Fw_filtered_ampl_240` | `MLP` | 0.003820 | 0.004783 | 1076.921 |
| `fft_y_Fw_filtered_phase_240` | `MLP` | 0.489347 | 0.838392 | 32.639 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/mlp/2026-04-26_track1_forward_mlp_original_dataset_mega_campaign/005_track1_original_dataset_forward_mlp_attempt_05.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-30-08__track1_original_dataset_forward_mlp_attempt_05_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-30-08__track1_original_dataset_forward_mlp_attempt_05_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-30-08__track1_original_dataset_forward_mlp_attempt_05_campaign_validation/validation_summary.yaml`
