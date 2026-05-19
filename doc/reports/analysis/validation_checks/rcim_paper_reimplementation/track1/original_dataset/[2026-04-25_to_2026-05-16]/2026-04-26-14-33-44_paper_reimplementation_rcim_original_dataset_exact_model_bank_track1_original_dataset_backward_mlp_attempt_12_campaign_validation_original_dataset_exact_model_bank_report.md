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
- random seed: `27`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `522.369%`
- winning mean component MAE: `0.087470`
- winning mean component RMSE: `0.140377`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 522.369 | 0.087470 | 0.140377 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `MLP` | 0.005191 | 0.006518 | 88.887 |
| `fft_y_Bw_filtered_ampl_1` | `MLP` | 0.003479 | 0.004076 | 20.289 |
| `fft_y_Bw_filtered_phase_1` | `MLP` | 0.004432 | 0.005656 | 83.903 |
| `fft_y_Bw_filtered_ampl_3` | `MLP` | 0.005165 | 0.006398 | 539.713 |
| `fft_y_Bw_filtered_phase_3` | `MLP` | 0.022299 | 0.029313 | 1.726 |
| `fft_y_Bw_filtered_ampl_39` | `MLP` | 0.003659 | 0.004282 | 808.860 |
| `fft_y_Bw_filtered_phase_39` | `MLP` | 0.367844 | 0.680761 | 13.668 |
| `fft_y_Bw_filtered_ampl_40` | `MLP` | 0.003676 | 0.004271 | 1163.074 |
| `fft_y_Bw_filtered_phase_40` | `MLP` | 0.110103 | 0.165998 | 50.484 |
| `fft_y_Bw_filtered_ampl_78` | `MLP` | 0.003629 | 0.004238 | 617.748 |
| `fft_y_Bw_filtered_phase_78` | `MLP` | 0.064829 | 0.097368 | 21.747 |
| `fft_y_Bw_filtered_ampl_81` | `MLP` | 0.003633 | 0.004247 | 3109.009 |
| `fft_y_Bw_filtered_phase_81` | `MLP` | 0.100068 | 0.134996 | 34.819 |
| `fft_y_Bw_filtered_ampl_156` | `MLP` | 0.005280 | 0.006578 | 982.664 |
| `fft_y_Bw_filtered_phase_156` | `MLP` | 0.229650 | 0.349867 | 21.605 |
| `fft_y_Bw_filtered_ampl_162` | `MLP` | 0.003842 | 0.004615 | 1445.869 |
| `fft_y_Bw_filtered_phase_162` | `MLP` | 0.114801 | 0.177507 | 7.132 |
| `fft_y_Bw_filtered_ampl_240` | `MLP` | 0.003819 | 0.004435 | 875.874 |
| `fft_y_Bw_filtered_phase_240` | `MLP` | 0.606525 | 0.976030 | 37.939 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/mlp/2026-04-26_track1_backward_mlp_original_dataset_mega_campaign/012_track1_original_dataset_backward_mlp_attempt_12.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-31-29__track1_original_dataset_backward_mlp_attempt_12_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-31-29__track1_original_dataset_backward_mlp_attempt_12_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-31-29__track1_original_dataset_backward_mlp_attempt_12_campaign_validation/validation_summary.yaml`
