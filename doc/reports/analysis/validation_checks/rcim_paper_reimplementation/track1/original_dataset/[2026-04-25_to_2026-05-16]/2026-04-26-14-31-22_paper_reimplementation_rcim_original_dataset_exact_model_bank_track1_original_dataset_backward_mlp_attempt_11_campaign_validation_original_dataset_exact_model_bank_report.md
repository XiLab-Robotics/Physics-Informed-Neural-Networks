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
- random seed: `23`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `443.755%`
- winning mean component MAE: `0.075619`
- winning mean component RMSE: `0.171997`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 443.755 | 0.075619 | 0.171997 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `MLP` | 0.004938 | 0.005942 | 173.382 |
| `fft_y_Bw_filtered_ampl_1` | `MLP` | 0.002810 | 0.003436 | 16.419 |
| `fft_y_Bw_filtered_phase_1` | `MLP` | 0.003590 | 0.004534 | 79.611 |
| `fft_y_Bw_filtered_ampl_3` | `MLP` | 0.002823 | 0.003458 | 299.667 |
| `fft_y_Bw_filtered_phase_3` | `MLP` | 0.025910 | 0.032502 | 1.929 |
| `fft_y_Bw_filtered_ampl_39` | `MLP` | 0.002846 | 0.003480 | 639.867 |
| `fft_y_Bw_filtered_phase_39` | `MLP` | 0.466060 | 1.604132 | 16.434 |
| `fft_y_Bw_filtered_ampl_40` | `MLP` | 0.002862 | 0.003493 | 928.083 |
| `fft_y_Bw_filtered_phase_40` | `MLP` | 0.109960 | 0.177863 | 43.329 |
| `fft_y_Bw_filtered_ampl_78` | `MLP` | 0.002797 | 0.003441 | 496.732 |
| `fft_y_Bw_filtered_phase_78` | `MLP` | 0.061554 | 0.096664 | 21.145 |
| `fft_y_Bw_filtered_ampl_81` | `MLP` | 0.002866 | 0.003490 | 2660.846 |
| `fft_y_Bw_filtered_phase_81` | `MLP` | 0.101109 | 0.135627 | 201.644 |
| `fft_y_Bw_filtered_ampl_156` | `MLP` | 0.002827 | 0.003971 | 684.151 |
| `fft_y_Bw_filtered_phase_156` | `MLP` | 0.157558 | 0.368369 | 19.204 |
| `fft_y_Bw_filtered_ampl_162` | `MLP` | 0.003025 | 0.003852 | 1490.245 |
| `fft_y_Bw_filtered_phase_162` | `MLP` | 0.099843 | 0.181827 | 6.350 |
| `fft_y_Bw_filtered_ampl_240` | `MLP` | 0.002944 | 0.003602 | 631.765 |
| `fft_y_Bw_filtered_phase_240` | `MLP` | 0.380449 | 0.628251 | 20.547 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/mlp/2026-04-26_track1_backward_mlp_original_dataset_mega_campaign/011_track1_original_dataset_backward_mlp_attempt_11.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-29-03__track1_original_dataset_backward_mlp_attempt_11_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-29-03__track1_original_dataset_backward_mlp_attempt_11_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-29-03__track1_original_dataset_backward_mlp_attempt_11_campaign_validation/validation_summary.yaml`
