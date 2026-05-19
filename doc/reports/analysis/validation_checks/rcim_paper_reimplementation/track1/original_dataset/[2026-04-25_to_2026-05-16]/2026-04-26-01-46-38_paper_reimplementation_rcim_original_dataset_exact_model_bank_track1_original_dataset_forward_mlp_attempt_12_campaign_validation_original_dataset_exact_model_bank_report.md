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
- random seed: `27`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `471.388%`
- winning mean component MAE: `0.121644`
- winning mean component RMSE: `0.192756`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 471.388 | 0.121644 | 0.192756 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `MLP` | 0.004787 | 0.005790 | 9.769 |
| `fft_y_Fw_filtered_ampl_1` | `MLP` | 0.003529 | 0.004121 | 20.567 |
| `fft_y_Fw_filtered_phase_1` | `MLP` | 0.004484 | 0.005770 | 58.559 |
| `fft_y_Fw_filtered_ampl_3` | `MLP` | 0.003618 | 0.004233 | 456.848 |
| `fft_y_Fw_filtered_phase_3` | `MLP` | 0.026388 | 0.033068 | 1.452 |
| `fft_y_Fw_filtered_ampl_39` | `MLP` | 0.001946 | 0.002470 | 185.666 |
| `fft_y_Fw_filtered_phase_39` | `MLP` | 0.032748 | 0.046067 | 2.916 |
| `fft_y_Fw_filtered_ampl_40` | `MLP` | 0.003474 | 0.004032 | 435.152 |
| `fft_y_Fw_filtered_phase_40` | `MLP` | 0.053630 | 0.075434 | 102.614 |
| `fft_y_Fw_filtered_ampl_78` | `MLP` | 0.003642 | 0.004267 | 693.987 |
| `fft_y_Fw_filtered_phase_78` | `MLP` | 0.074375 | 0.106545 | 601.383 |
| `fft_y_Fw_filtered_ampl_81` | `MLP` | 0.003649 | 0.004275 | 1178.956 |
| `fft_y_Fw_filtered_phase_81` | `MLP` | 0.058568 | 0.086711 | 6.294 |
| `fft_y_Fw_filtered_ampl_156` | `MLP` | 0.003553 | 0.004197 | 3027.646 |
| `fft_y_Fw_filtered_phase_156` | `MLP` | 1.005647 | 1.456885 | 82.303 |
| `fft_y_Fw_filtered_ampl_162` | `MLP` | 0.002222 | 0.003256 | 968.822 |
| `fft_y_Fw_filtered_phase_162` | `MLP` | 0.549777 | 1.054847 | 27.303 |
| `fft_y_Fw_filtered_ampl_240` | `MLP` | 0.003581 | 0.004159 | 1051.756 |
| `fft_y_Fw_filtered_phase_240` | `MLP` | 0.471619 | 0.756229 | 44.374 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/mlp/2026-04-26_track1_forward_mlp_original_dataset_mega_campaign/012_track1_original_dataset_forward_mlp_attempt_12.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-44-42__track1_original_dataset_forward_mlp_attempt_12_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-44-42__track1_original_dataset_forward_mlp_attempt_12_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-44-42__track1_original_dataset_forward_mlp_attempt_12_campaign_validation/validation_summary.yaml`
