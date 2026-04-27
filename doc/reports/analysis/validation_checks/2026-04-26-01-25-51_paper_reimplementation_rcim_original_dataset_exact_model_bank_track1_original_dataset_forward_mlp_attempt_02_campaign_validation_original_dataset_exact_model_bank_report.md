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
- random seed: `5`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `427.965%`
- winning mean component MAE: `0.132000`
- winning mean component RMSE: `0.239270`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 427.965 | 0.132000 | 0.239270 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `MLP` | 0.005166 | 0.007090 | 23.764 |
| `fft_y_Fw_filtered_ampl_1` | `MLP` | 0.002866 | 0.003653 | 16.703 |
| `fft_y_Fw_filtered_phase_1` | `MLP` | 0.003969 | 0.005647 | 60.635 |
| `fft_y_Fw_filtered_ampl_3` | `MLP` | 0.002835 | 0.003605 | 361.472 |
| `fft_y_Fw_filtered_phase_3` | `MLP` | 0.030448 | 0.041071 | 1.670 |
| `fft_y_Fw_filtered_ampl_39` | `MLP` | 0.002845 | 0.003609 | 284.194 |
| `fft_y_Fw_filtered_phase_39` | `MLP` | 0.031839 | 0.048972 | 2.701 |
| `fft_y_Fw_filtered_ampl_40` | `MLP` | 0.002830 | 0.003605 | 346.060 |
| `fft_y_Fw_filtered_phase_40` | `MLP` | 0.054270 | 0.082601 | 148.464 |
| `fft_y_Fw_filtered_ampl_78` | `MLP` | 0.002808 | 0.003584 | 665.832 |
| `fft_y_Fw_filtered_phase_78` | `MLP` | 0.132433 | 0.380674 | 92.364 |
| `fft_y_Fw_filtered_ampl_81` | `MLP` | 0.002829 | 0.003618 | 932.953 |
| `fft_y_Fw_filtered_phase_81` | `MLP` | 0.068427 | 0.101945 | 10.426 |
| `fft_y_Fw_filtered_ampl_156` | `MLP` | 0.002858 | 0.003656 | 2230.586 |
| `fft_y_Fw_filtered_phase_156` | `MLP` | 0.823309 | 1.335341 | 64.090 |
| `fft_y_Fw_filtered_ampl_162` | `MLP` | 0.002998 | 0.003823 | 1831.762 |
| `fft_y_Fw_filtered_phase_162` | `MLP` | 0.693030 | 1.286943 | 35.208 |
| `fft_y_Fw_filtered_ampl_240` | `MLP` | 0.002953 | 0.003722 | 924.915 |
| `fft_y_Fw_filtered_phase_240` | `MLP` | 0.639279 | 1.222972 | 97.541 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/mlp/2026-04-26_track1_forward_mlp_original_dataset_mega_campaign/002_track1_original_dataset_forward_mlp_attempt_02.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-20-30__track1_original_dataset_forward_mlp_attempt_02_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-20-30__track1_original_dataset_forward_mlp_attempt_02_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-20-30__track1_original_dataset_forward_mlp_attempt_02_campaign_validation/validation_summary.yaml`
