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
- random seed: `19`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `460.602%`
- winning mean component MAE: `0.087767`
- winning mean component RMSE: `0.185894`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 460.602 | 0.087767 | 0.185894 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (100,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `MLP` | 0.005134 | 0.006851 | 104.837 |
| `fft_y_Bw_filtered_ampl_1` | `MLP` | 0.003019 | 0.003885 | 17.648 |
| `fft_y_Bw_filtered_phase_1` | `MLP` | 0.004126 | 0.005239 | 101.247 |
| `fft_y_Bw_filtered_ampl_3` | `MLP` | 0.003047 | 0.003954 | 323.411 |
| `fft_y_Bw_filtered_phase_3` | `MLP` | 0.023799 | 0.040731 | 1.789 |
| `fft_y_Bw_filtered_ampl_39` | `MLP` | 0.003033 | 0.003945 | 696.249 |
| `fft_y_Bw_filtered_phase_39` | `MLP` | 0.647417 | 1.322866 | 23.272 |
| `fft_y_Bw_filtered_ampl_40` | `MLP` | 0.003056 | 0.003963 | 976.893 |
| `fft_y_Bw_filtered_phase_40` | `MLP` | 0.098395 | 0.166814 | 31.097 |
| `fft_y_Bw_filtered_ampl_78` | `MLP` | 0.003011 | 0.003927 | 360.830 |
| `fft_y_Bw_filtered_phase_78` | `MLP` | 0.057332 | 0.099436 | 28.941 |
| `fft_y_Bw_filtered_ampl_81` | `MLP` | 0.003089 | 0.003895 | 2875.913 |
| `fft_y_Bw_filtered_phase_81` | `MLP` | 0.099231 | 0.148602 | 125.364 |
| `fft_y_Bw_filtered_ampl_156` | `MLP` | 0.003421 | 0.004738 | 746.242 |
| `fft_y_Bw_filtered_phase_156` | `MLP` | 0.233126 | 0.614563 | 28.623 |
| `fft_y_Bw_filtered_ampl_162` | `MLP` | 0.003347 | 0.004566 | 1566.564 |
| `fft_y_Bw_filtered_phase_162` | `MLP` | 0.105614 | 0.261385 | 6.484 |
| `fft_y_Bw_filtered_ampl_240` | `MLP` | 0.003091 | 0.004010 | 690.807 |
| `fft_y_Bw_filtered_phase_240` | `MLP` | 0.365289 | 0.828620 | 45.233 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/mlp/2026-04-26_track1_backward_mlp_original_dataset_mega_campaign/009_track1_original_dataset_backward_mlp_attempt_09.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-24-12__track1_original_dataset_backward_mlp_attempt_09_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-24-12__track1_original_dataset_backward_mlp_attempt_09_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-24-12__track1_original_dataset_backward_mlp_attempt_09_campaign_validation/validation_summary.yaml`
