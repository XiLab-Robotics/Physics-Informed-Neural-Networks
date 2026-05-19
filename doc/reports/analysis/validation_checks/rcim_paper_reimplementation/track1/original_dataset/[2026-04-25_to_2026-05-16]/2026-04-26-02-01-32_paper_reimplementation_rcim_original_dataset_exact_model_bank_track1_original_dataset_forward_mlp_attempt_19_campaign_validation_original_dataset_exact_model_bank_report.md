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
- random seed: `59`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `486.532%`
- winning mean component MAE: `0.126790`
- winning mean component RMSE: `0.224541`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 486.532 | 0.126790 | 0.224541 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `MLP` | 0.004185 | 0.005116 | 9.347 |
| `fft_y_Fw_filtered_ampl_1` | `MLP` | 0.003102 | 0.003805 | 18.074 |
| `fft_y_Fw_filtered_phase_1` | `MLP` | 0.004298 | 0.005573 | 96.637 |
| `fft_y_Fw_filtered_ampl_3` | `MLP` | 0.003037 | 0.003758 | 396.879 |
| `fft_y_Fw_filtered_phase_3` | `MLP` | 0.028117 | 0.036774 | 1.574 |
| `fft_y_Fw_filtered_ampl_39` | `MLP` | 0.003067 | 0.003790 | 303.959 |
| `fft_y_Fw_filtered_phase_39` | `MLP` | 0.030966 | 0.047055 | 2.671 |
| `fft_y_Fw_filtered_ampl_40` | `MLP` | 0.003049 | 0.003779 | 374.623 |
| `fft_y_Fw_filtered_phase_40` | `MLP` | 0.047969 | 0.068883 | 100.194 |
| `fft_y_Fw_filtered_ampl_78` | `MLP` | 0.002983 | 0.003734 | 614.799 |
| `fft_y_Fw_filtered_phase_78` | `MLP` | 0.127120 | 0.234433 | 106.577 |
| `fft_y_Fw_filtered_ampl_81` | `MLP` | 0.003020 | 0.003734 | 990.917 |
| `fft_y_Fw_filtered_phase_81` | `MLP` | 0.064890 | 0.102837 | 8.054 |
| `fft_y_Fw_filtered_ampl_156` | `MLP` | 0.002912 | 0.003708 | 3669.975 |
| `fft_y_Fw_filtered_phase_156` | `MLP` | 0.786874 | 1.288726 | 65.130 |
| `fft_y_Fw_filtered_ampl_162` | `MLP` | 0.002117 | 0.002765 | 1192.990 |
| `fft_y_Fw_filtered_phase_162` | `MLP` | 0.742364 | 1.519421 | 31.552 |
| `fft_y_Fw_filtered_ampl_240` | `MLP` | 0.003147 | 0.003867 | 1187.102 |
| `fft_y_Fw_filtered_phase_240` | `MLP` | 0.545789 | 0.924522 | 73.054 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/mlp/2026-04-26_track1_forward_mlp_original_dataset_mega_campaign/019_track1_original_dataset_forward_mlp_attempt_19.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-59-30__track1_original_dataset_forward_mlp_attempt_19_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-59-30__track1_original_dataset_forward_mlp_attempt_19_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-59-30__track1_original_dataset_forward_mlp_attempt_19_campaign_validation/validation_summary.yaml`
