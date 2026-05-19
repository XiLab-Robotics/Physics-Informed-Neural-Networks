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
- random seed: `19`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `486.197%`
- winning mean component MAE: `0.116516`
- winning mean component RMSE: `0.211506`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 486.197 | 0.116516 | 0.211506 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (100,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `MLP` | 0.003781 | 0.006047 | 22.457 |
| `fft_y_Fw_filtered_ampl_1` | `MLP` | 0.003016 | 0.003874 | 17.572 |
| `fft_y_Fw_filtered_phase_1` | `MLP` | 0.003694 | 0.004786 | 72.210 |
| `fft_y_Fw_filtered_ampl_3` | `MLP` | 0.003044 | 0.003961 | 394.771 |
| `fft_y_Fw_filtered_phase_3` | `MLP` | 0.027913 | 0.036957 | 1.546 |
| `fft_y_Fw_filtered_ampl_39` | `MLP` | 0.003046 | 0.003954 | 277.578 |
| `fft_y_Fw_filtered_phase_39` | `MLP` | 0.024738 | 0.040244 | 2.109 |
| `fft_y_Fw_filtered_ampl_40` | `MLP` | 0.003047 | 0.003951 | 373.593 |
| `fft_y_Fw_filtered_phase_40` | `MLP` | 0.051879 | 0.077104 | 90.738 |
| `fft_y_Fw_filtered_ampl_78` | `MLP` | 0.003024 | 0.003940 | 519.833 |
| `fft_y_Fw_filtered_phase_78` | `MLP` | 0.095385 | 0.150067 | 421.718 |
| `fft_y_Fw_filtered_ampl_81` | `MLP` | 0.003056 | 0.003971 | 1078.467 |
| `fft_y_Fw_filtered_phase_81` | `MLP` | 0.064897 | 0.102670 | 5.936 |
| `fft_y_Fw_filtered_ampl_156` | `MLP` | 0.003080 | 0.004021 | 2927.186 |
| `fft_y_Fw_filtered_phase_156` | `MLP` | 0.710655 | 1.242637 | 37.915 |
| `fft_y_Fw_filtered_ampl_162` | `MLP` | 0.003392 | 0.004603 | 1779.781 |
| `fft_y_Fw_filtered_phase_162` | `MLP` | 0.510677 | 0.980304 | 25.447 |
| `fft_y_Fw_filtered_ampl_240` | `MLP` | 0.003069 | 0.003988 | 1149.259 |
| `fft_y_Fw_filtered_phase_240` | `MLP` | 0.692413 | 1.341528 | 39.622 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/mlp/2026-04-26_track1_forward_mlp_original_dataset_mega_campaign/009_track1_original_dataset_forward_mlp_attempt_09.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-38-30__track1_original_dataset_forward_mlp_attempt_09_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-38-30__track1_original_dataset_forward_mlp_attempt_09_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-38-30__track1_original_dataset_forward_mlp_attempt_09_campaign_validation/validation_summary.yaml`
