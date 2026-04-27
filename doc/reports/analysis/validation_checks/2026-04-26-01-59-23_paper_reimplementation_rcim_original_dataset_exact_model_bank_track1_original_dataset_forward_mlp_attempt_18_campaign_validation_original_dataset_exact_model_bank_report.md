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
- random seed: `53`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `592.578%`
- winning mean component MAE: `0.136857`
- winning mean component RMSE: `0.237952`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 592.578 | 0.136857 | 0.237952 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `MLP` | 0.004398 | 0.006197 | 14.488 |
| `fft_y_Fw_filtered_ampl_1` | `MLP` | 0.003368 | 0.004268 | 19.629 |
| `fft_y_Fw_filtered_phase_1` | `MLP` | 0.004472 | 0.006134 | 1590.806 |
| `fft_y_Fw_filtered_ampl_3` | `MLP` | 0.003359 | 0.004268 | 435.843 |
| `fft_y_Fw_filtered_phase_3` | `MLP` | 0.034585 | 0.069358 | 1.884 |
| `fft_y_Fw_filtered_ampl_39` | `MLP` | 0.003366 | 0.004278 | 357.039 |
| `fft_y_Fw_filtered_phase_39` | `MLP` | 0.034415 | 0.060882 | 2.584 |
| `fft_y_Fw_filtered_ampl_40` | `MLP` | 0.003359 | 0.004275 | 404.858 |
| `fft_y_Fw_filtered_phase_40` | `MLP` | 0.053326 | 0.080095 | 59.833 |
| `fft_y_Fw_filtered_ampl_78` | `MLP` | 0.003341 | 0.004253 | 1223.168 |
| `fft_y_Fw_filtered_phase_78` | `MLP` | 0.178582 | 0.403260 | 265.778 |
| `fft_y_Fw_filtered_ampl_81` | `MLP` | 0.003335 | 0.004239 | 1089.704 |
| `fft_y_Fw_filtered_phase_81` | `MLP` | 0.086143 | 0.135689 | 10.714 |
| `fft_y_Fw_filtered_ampl_156` | `MLP` | 0.003219 | 0.004206 | 2259.522 |
| `fft_y_Fw_filtered_phase_156` | `MLP` | 0.876176 | 1.290103 | 109.059 |
| `fft_y_Fw_filtered_ampl_162` | `MLP` | 0.003580 | 0.004622 | 2098.751 |
| `fft_y_Fw_filtered_phase_162` | `MLP` | 0.590040 | 1.063478 | 28.495 |
| `fft_y_Fw_filtered_ampl_240` | `MLP` | 0.003405 | 0.004321 | 1246.711 |
| `fft_y_Fw_filtered_phase_240` | `MLP` | 0.707823 | 1.367162 | 40.125 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/mlp/2026-04-26_track1_forward_mlp_original_dataset_mega_campaign/018_track1_original_dataset_forward_mlp_attempt_18.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-57-29__track1_original_dataset_forward_mlp_attempt_18_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-57-29__track1_original_dataset_forward_mlp_attempt_18_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-57-29__track1_original_dataset_forward_mlp_attempt_18_campaign_validation/validation_summary.yaml`
