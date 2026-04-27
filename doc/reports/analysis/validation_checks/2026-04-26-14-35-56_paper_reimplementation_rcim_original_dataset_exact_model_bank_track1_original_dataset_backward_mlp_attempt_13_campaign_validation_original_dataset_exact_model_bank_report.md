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
- random seed: `29`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `496.559%`
- winning mean component MAE: `0.081226`
- winning mean component RMSE: `0.160381`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 496.559 | 0.081226 | 0.160381 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `MLP` | 0.005899 | 0.007278 | 215.125 |
| `fft_y_Bw_filtered_ampl_1` | `MLP` | 0.002981 | 0.003643 | 17.401 |
| `fft_y_Bw_filtered_phase_1` | `MLP` | 0.003810 | 0.005269 | 672.074 |
| `fft_y_Bw_filtered_ampl_3` | `MLP` | 0.003030 | 0.003702 | 325.898 |
| `fft_y_Bw_filtered_phase_3` | `MLP` | 0.023941 | 0.040439 | 1.763 |
| `fft_y_Bw_filtered_ampl_39` | `MLP` | 0.003038 | 0.003701 | 690.023 |
| `fft_y_Bw_filtered_phase_39` | `MLP` | 0.355145 | 0.754649 | 13.728 |
| `fft_y_Bw_filtered_ampl_40` | `MLP` | 0.003031 | 0.003690 | 932.570 |
| `fft_y_Bw_filtered_phase_40` | `MLP` | 0.137605 | 0.250623 | 38.790 |
| `fft_y_Bw_filtered_ampl_78` | `MLP` | 0.003026 | 0.003693 | 535.088 |
| `fft_y_Bw_filtered_phase_78` | `MLP` | 0.065662 | 0.130567 | 20.109 |
| `fft_y_Bw_filtered_ampl_81` | `MLP` | 0.003034 | 0.003711 | 2501.617 |
| `fft_y_Bw_filtered_phase_81` | `MLP` | 0.097880 | 0.152043 | 671.282 |
| `fft_y_Bw_filtered_ampl_156` | `MLP` | 0.002450 | 0.003622 | 546.000 |
| `fft_y_Bw_filtered_phase_156` | `MLP` | 0.286273 | 0.549007 | 30.511 |
| `fft_y_Bw_filtered_ampl_162` | `MLP` | 0.003195 | 0.004067 | 1438.034 |
| `fft_y_Bw_filtered_phase_162` | `MLP` | 0.105194 | 0.184473 | 5.819 |
| `fft_y_Bw_filtered_ampl_240` | `MLP` | 0.003077 | 0.003758 | 753.935 |
| `fft_y_Bw_filtered_phase_240` | `MLP` | 0.435022 | 0.939306 | 24.843 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/mlp/2026-04-26_track1_backward_mlp_original_dataset_mega_campaign/013_track1_original_dataset_backward_mlp_attempt_13.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-33-51__track1_original_dataset_backward_mlp_attempt_13_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-33-51__track1_original_dataset_backward_mlp_attempt_13_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-33-51__track1_original_dataset_backward_mlp_attempt_13_campaign_validation/validation_summary.yaml`
