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
- random seed: `9`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `776.745%`
- winning mean component MAE: `0.083189`
- winning mean component RMSE: `0.154139`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 776.745 | 0.083189 | 0.154139 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `MLP` | 0.006294 | 0.008249 | 141.631 |
| `fft_y_Bw_filtered_ampl_1` | `MLP` | 0.004471 | 0.006389 | 26.074 |
| `fft_y_Bw_filtered_phase_1` | `MLP` | 0.003238 | 0.004646 | 110.208 |
| `fft_y_Bw_filtered_ampl_3` | `MLP` | 0.004456 | 0.006200 | 474.546 |
| `fft_y_Bw_filtered_phase_3` | `MLP` | 0.025358 | 0.034003 | 1.881 |
| `fft_y_Bw_filtered_ampl_39` | `MLP` | 0.004461 | 0.006133 | 965.694 |
| `fft_y_Bw_filtered_phase_39` | `MLP` | 0.474241 | 1.154214 | 17.040 |
| `fft_y_Bw_filtered_ampl_40` | `MLP` | 0.004464 | 0.006143 | 1473.607 |
| `fft_y_Bw_filtered_phase_40` | `MLP` | 0.122756 | 0.192262 | 26.181 |
| `fft_y_Bw_filtered_ampl_78` | `MLP` | 0.004436 | 0.006175 | 2697.146 |
| `fft_y_Bw_filtered_phase_78` | `MLP` | 0.082357 | 0.226610 | 31.290 |
| `fft_y_Bw_filtered_ampl_81` | `MLP` | 0.004452 | 0.006132 | 3709.498 |
| `fft_y_Bw_filtered_phase_81` | `MLP` | 0.116688 | 0.162062 | 486.446 |
| `fft_y_Bw_filtered_ampl_156` | `MLP` | 0.004922 | 0.006959 | 1062.467 |
| `fft_y_Bw_filtered_phase_156` | `MLP` | 0.206786 | 0.318272 | 23.662 |
| `fft_y_Bw_filtered_ampl_162` | `MLP` | 0.005053 | 0.006913 | 2468.180 |
| `fft_y_Bw_filtered_phase_162` | `MLP` | 0.102878 | 0.151502 | 6.699 |
| `fft_y_Bw_filtered_ampl_240` | `MLP` | 0.004676 | 0.006373 | 1017.311 |
| `fft_y_Bw_filtered_phase_240` | `MLP` | 0.398595 | 0.619414 | 18.601 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/mlp/2026-04-26_track1_backward_mlp_original_dataset_mega_campaign/004_track1_original_dataset_backward_mlp_attempt_04.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-12-55__track1_original_dataset_backward_mlp_attempt_04_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-12-55__track1_original_dataset_backward_mlp_attempt_04_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-12-55__track1_original_dataset_backward_mlp_attempt_04_campaign_validation/validation_summary.yaml`
