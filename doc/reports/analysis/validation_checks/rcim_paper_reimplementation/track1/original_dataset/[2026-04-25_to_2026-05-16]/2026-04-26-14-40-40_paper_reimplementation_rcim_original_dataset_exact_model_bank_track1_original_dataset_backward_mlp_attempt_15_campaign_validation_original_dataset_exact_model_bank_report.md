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
- random seed: `37`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `499.254%`
- winning mean component MAE: `0.068415`
- winning mean component RMSE: `0.135357`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 499.254 | 0.068415 | 0.135357 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (100,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `MLP` | 0.005400 | 0.007104 | 76.097 |
| `fft_y_Bw_filtered_ampl_1` | `MLP` | 0.003411 | 0.004304 | 19.922 |
| `fft_y_Bw_filtered_phase_1` | `MLP` | 0.004621 | 0.005832 | 186.753 |
| `fft_y_Bw_filtered_ampl_3` | `MLP` | 0.003231 | 0.004024 | 350.974 |
| `fft_y_Bw_filtered_phase_3` | `MLP` | 0.021769 | 0.028821 | 1.573 |
| `fft_y_Bw_filtered_ampl_39` | `MLP` | 0.003308 | 0.004099 | 759.256 |
| `fft_y_Bw_filtered_phase_39` | `MLP` | 0.281941 | 0.752583 | 10.499 |
| `fft_y_Bw_filtered_ampl_40` | `MLP` | 0.003313 | 0.004151 | 1093.593 |
| `fft_y_Bw_filtered_phase_40` | `MLP` | 0.097919 | 0.157723 | 64.332 |
| `fft_y_Bw_filtered_ampl_78` | `MLP` | 0.003203 | 0.003999 | 501.529 |
| `fft_y_Bw_filtered_phase_78` | `MLP` | 0.060484 | 0.101680 | 19.649 |
| `fft_y_Bw_filtered_ampl_81` | `MLP` | 0.003328 | 0.004172 | 2982.638 |
| `fft_y_Bw_filtered_phase_81` | `MLP` | 0.078653 | 0.100999 | 332.619 |
| `fft_y_Bw_filtered_ampl_156` | `MLP` | 0.003945 | 0.005528 | 756.352 |
| `fft_y_Bw_filtered_phase_156` | `MLP` | 0.180235 | 0.401465 | 16.257 |
| `fft_y_Bw_filtered_ampl_162` | `MLP` | 0.003060 | 0.003982 | 1518.285 |
| `fft_y_Bw_filtered_phase_162` | `MLP` | 0.093275 | 0.207180 | 4.994 |
| `fft_y_Bw_filtered_ampl_240` | `MLP` | 0.003454 | 0.004243 | 767.976 |
| `fft_y_Bw_filtered_phase_240` | `MLP` | 0.445334 | 0.769899 | 22.532 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/mlp/2026-04-26_track1_backward_mlp_original_dataset_mega_campaign/015_track1_original_dataset_backward_mlp_attempt_15.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-38-18__track1_original_dataset_backward_mlp_attempt_15_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-38-18__track1_original_dataset_backward_mlp_attempt_15_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-38-18__track1_original_dataset_backward_mlp_attempt_15_campaign_validation/validation_summary.yaml`
