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
- random seed: `0`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `489.257%`
- winning mean component MAE: `0.108793`
- winning mean component RMSE: `0.194288`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 489.257 | 0.108793 | 0.194288 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `MLP` | 0.003840 | 0.004679 | 8.189 |
| `fft_y_Fw_filtered_ampl_1` | `MLP` | 0.002887 | 0.003521 | 16.838 |
| `fft_y_Fw_filtered_phase_1` | `MLP` | 0.003628 | 0.004836 | 101.943 |
| `fft_y_Fw_filtered_ampl_3` | `MLP` | 0.002830 | 0.003458 | 361.623 |
| `fft_y_Fw_filtered_phase_3` | `MLP` | 0.027513 | 0.036303 | 1.512 |
| `fft_y_Fw_filtered_ampl_39` | `MLP` | 0.002873 | 0.003537 | 271.751 |
| `fft_y_Fw_filtered_phase_39` | `MLP` | 0.030243 | 0.048743 | 2.404 |
| `fft_y_Fw_filtered_ampl_40` | `MLP` | 0.002826 | 0.003454 | 352.370 |
| `fft_y_Fw_filtered_phase_40` | `MLP` | 0.043928 | 0.067497 | 86.766 |
| `fft_y_Fw_filtered_ampl_78` | `MLP` | 0.002881 | 0.003692 | 1761.642 |
| `fft_y_Fw_filtered_phase_78` | `MLP` | 0.091068 | 0.179568 | 235.692 |
| `fft_y_Fw_filtered_ampl_81` | `MLP` | 0.002844 | 0.003481 | 954.224 |
| `fft_y_Fw_filtered_phase_81` | `MLP` | 0.056381 | 0.085392 | 5.986 |
| `fft_y_Fw_filtered_ampl_156` | `MLP` | 0.002802 | 0.003414 | 2729.608 |
| `fft_y_Fw_filtered_phase_156` | `MLP` | 0.881508 | 1.442223 | 88.016 |
| `fft_y_Fw_filtered_ampl_162` | `MLP` | 0.003127 | 0.004111 | 1492.756 |
| `fft_y_Fw_filtered_phase_162` | `MLP` | 0.354340 | 0.687019 | 17.002 |
| `fft_y_Fw_filtered_ampl_240` | `MLP` | 0.002906 | 0.003593 | 777.659 |
| `fft_y_Fw_filtered_phase_240` | `MLP` | 0.548645 | 1.102955 | 29.910 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/mlp/2026-04-26_track1_forward_mlp_original_dataset_mega_campaign/001_track1_original_dataset_forward_mlp_attempt_01.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-14-47__track1_original_dataset_forward_mlp_attempt_01_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-14-47__track1_original_dataset_forward_mlp_attempt_01_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-14-47__track1_original_dataset_forward_mlp_attempt_01_campaign_validation/validation_summary.yaml`
