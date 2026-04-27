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
- random seed: `42`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `493.088%`
- winning mean component MAE: `0.075321`
- winning mean component RMSE: `0.131441`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 493.088 | 0.075321 | 0.131441 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.001, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `MLP` | 0.005292 | 0.006418 | 106.255 |
| `fft_y_Bw_filtered_ampl_1` | `MLP` | 0.003213 | 0.003979 | 18.739 |
| `fft_y_Bw_filtered_phase_1` | `MLP` | 0.004348 | 0.005688 | 199.891 |
| `fft_y_Bw_filtered_ampl_3` | `MLP` | 0.003193 | 0.003991 | 337.662 |
| `fft_y_Bw_filtered_phase_3` | `MLP` | 0.022258 | 0.031923 | 1.655 |
| `fft_y_Bw_filtered_ampl_39` | `MLP` | 0.003258 | 0.004003 | 693.181 |
| `fft_y_Bw_filtered_phase_39` | `MLP` | 0.437716 | 0.909345 | 16.163 |
| `fft_y_Bw_filtered_ampl_40` | `MLP` | 0.003236 | 0.003991 | 1005.603 |
| `fft_y_Bw_filtered_phase_40` | `MLP` | 0.107813 | 0.191208 | 59.287 |
| `fft_y_Bw_filtered_ampl_78` | `MLP` | 0.003213 | 0.003967 | 563.983 |
| `fft_y_Bw_filtered_phase_78` | `MLP` | 0.056047 | 0.079384 | 50.479 |
| `fft_y_Bw_filtered_ampl_81` | `MLP` | 0.003231 | 0.003983 | 2742.279 |
| `fft_y_Bw_filtered_phase_81` | `MLP` | 0.102921 | 0.137058 | 219.808 |
| `fft_y_Bw_filtered_ampl_156` | `MLP` | 0.003421 | 0.004496 | 831.614 |
| `fft_y_Bw_filtered_phase_156` | `MLP` | 0.169216 | 0.295473 | 15.826 |
| `fft_y_Bw_filtered_ampl_162` | `MLP` | 0.003269 | 0.004157 | 1729.367 |
| `fft_y_Bw_filtered_phase_162` | `MLP` | 0.085385 | 0.142293 | 5.005 |
| `fft_y_Bw_filtered_ampl_240` | `MLP` | 0.003319 | 0.004075 | 750.340 |
| `fft_y_Bw_filtered_phase_240` | `MLP` | 0.410746 | 0.661955 | 21.540 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/mlp/2026-04-26_track1_backward_mlp_original_dataset_mega_campaign/016_track1_original_dataset_backward_mlp_attempt_16.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-40-48__track1_original_dataset_backward_mlp_attempt_16_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-40-48__track1_original_dataset_backward_mlp_attempt_16_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-40-48__track1_original_dataset_backward_mlp_attempt_16_campaign_validation/validation_summary.yaml`
