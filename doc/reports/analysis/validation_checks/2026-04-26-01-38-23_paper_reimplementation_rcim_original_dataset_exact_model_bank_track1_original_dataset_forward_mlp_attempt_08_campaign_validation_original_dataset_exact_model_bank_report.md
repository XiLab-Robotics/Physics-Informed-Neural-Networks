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
- random seed: `17`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `497.061%`
- winning mean component MAE: `0.106406`
- winning mean component RMSE: `0.173532`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 497.061 | 0.106406 | 0.173532 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `MLP` | 0.005263 | 0.006424 | 10.236 |
| `fft_y_Fw_filtered_ampl_1` | `MLP` | 0.001710 | 0.002118 | 9.960 |
| `fft_y_Fw_filtered_phase_1` | `MLP` | 0.003175 | 0.003870 | 45.960 |
| `fft_y_Fw_filtered_ampl_3` | `MLP` | 0.003114 | 0.003804 | 404.008 |
| `fft_y_Fw_filtered_phase_3` | `MLP` | 0.024362 | 0.031064 | 1.349 |
| `fft_y_Fw_filtered_ampl_39` | `MLP` | 0.003118 | 0.003803 | 304.995 |
| `fft_y_Fw_filtered_phase_39` | `MLP` | 0.022695 | 0.034283 | 2.042 |
| `fft_y_Fw_filtered_ampl_40` | `MLP` | 0.003111 | 0.003801 | 376.395 |
| `fft_y_Fw_filtered_phase_40` | `MLP` | 0.050715 | 0.075047 | 86.883 |
| `fft_y_Fw_filtered_ampl_78` | `MLP` | 0.003082 | 0.003769 | 863.323 |
| `fft_y_Fw_filtered_phase_78` | `MLP` | 0.075101 | 0.105906 | 121.866 |
| `fft_y_Fw_filtered_ampl_81` | `MLP` | 0.001797 | 0.002167 | 620.997 |
| `fft_y_Fw_filtered_phase_81` | `MLP` | 0.062737 | 0.088589 | 5.925 |
| `fft_y_Fw_filtered_ampl_156` | `MLP` | 0.004607 | 0.006011 | 3685.994 |
| `fft_y_Fw_filtered_phase_156` | `MLP` | 0.866976 | 1.530581 | 46.262 |
| `fft_y_Fw_filtered_ampl_162` | `MLP` | 0.003189 | 0.004067 | 1715.268 |
| `fft_y_Fw_filtered_phase_162` | `MLP` | 0.407975 | 0.609692 | 19.385 |
| `fft_y_Fw_filtered_ampl_240` | `MLP` | 0.003177 | 0.003843 | 1092.297 |
| `fft_y_Fw_filtered_phase_240` | `MLP` | 0.475811 | 0.778267 | 31.016 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/mlp/2026-04-26_track1_forward_mlp_original_dataset_mega_campaign/008_track1_original_dataset_forward_mlp_attempt_08.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-36-28__track1_original_dataset_forward_mlp_attempt_08_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-36-28__track1_original_dataset_forward_mlp_attempt_08_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-36-28__track1_original_dataset_forward_mlp_attempt_08_campaign_validation/validation_summary.yaml`
