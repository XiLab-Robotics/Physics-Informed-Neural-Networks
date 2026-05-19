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
- random seed: `31`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `592.015%`
- winning mean component MAE: `0.078071`
- winning mean component RMSE: `0.132811`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 592.015 | 0.078071 | 0.132811 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `MLP` | 0.006590 | 0.008180 | 88.182 |
| `fft_y_Bw_filtered_ampl_1` | `MLP` | 0.004778 | 0.006533 | 27.943 |
| `fft_y_Bw_filtered_phase_1` | `MLP` | 0.004449 | 0.006706 | 73.221 |
| `fft_y_Bw_filtered_ampl_3` | `MLP` | 0.002998 | 0.003737 | 318.604 |
| `fft_y_Bw_filtered_phase_3` | `MLP` | 0.024539 | 0.032770 | 1.756 |
| `fft_y_Bw_filtered_ampl_39` | `MLP` | 0.002997 | 0.003733 | 686.060 |
| `fft_y_Bw_filtered_phase_39` | `MLP` | 0.436445 | 0.731254 | 18.282 |
| `fft_y_Bw_filtered_ampl_40` | `MLP` | 0.002901 | 0.003632 | 966.521 |
| `fft_y_Bw_filtered_phase_40` | `MLP` | 0.093736 | 0.182428 | 30.119 |
| `fft_y_Bw_filtered_ampl_78` | `MLP` | 0.002129 | 0.002742 | 542.543 |
| `fft_y_Bw_filtered_phase_78` | `MLP` | 0.071219 | 0.136926 | 38.905 |
| `fft_y_Bw_filtered_ampl_81` | `MLP` | 0.004694 | 0.006213 | 3827.874 |
| `fft_y_Bw_filtered_phase_81` | `MLP` | 0.126717 | 0.177525 | 51.065 |
| `fft_y_Bw_filtered_ampl_156` | `MLP` | 0.004617 | 0.006291 | 1137.539 |
| `fft_y_Bw_filtered_phase_156` | `MLP` | 0.199768 | 0.296411 | 26.825 |
| `fft_y_Bw_filtered_ampl_162` | `MLP` | 0.004958 | 0.006682 | 2280.126 |
| `fft_y_Bw_filtered_phase_162` | `MLP` | 0.114670 | 0.252490 | 6.078 |
| `fft_y_Bw_filtered_ampl_240` | `MLP` | 0.004711 | 0.006212 | 1107.569 |
| `fft_y_Bw_filtered_phase_240` | `MLP` | 0.370431 | 0.652945 | 19.069 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/mlp/2026-04-26_track1_backward_mlp_original_dataset_mega_campaign/014_track1_original_dataset_backward_mlp_attempt_14.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-36-03__track1_original_dataset_backward_mlp_attempt_14_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-36-03__track1_original_dataset_backward_mlp_attempt_14_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-36-03__track1_original_dataset_backward_mlp_attempt_14_campaign_validation/validation_summary.yaml`
