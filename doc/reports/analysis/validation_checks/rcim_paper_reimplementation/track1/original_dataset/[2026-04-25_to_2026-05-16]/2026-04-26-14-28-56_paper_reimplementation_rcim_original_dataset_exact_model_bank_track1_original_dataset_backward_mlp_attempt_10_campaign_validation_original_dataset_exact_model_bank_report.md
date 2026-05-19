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
- random seed: `21`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `510.489%`
- winning mean component MAE: `0.085625`
- winning mean component RMSE: `0.159039`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 510.489 | 0.085625 | 0.159039 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.001, 'estimator__mlp__hidden_layer_sizes': (100,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `MLP` | 0.005366 | 0.006645 | 153.344 |
| `fft_y_Bw_filtered_ampl_1` | `MLP` | 0.003687 | 0.004852 | 21.516 |
| `fft_y_Bw_filtered_phase_1` | `MLP` | 0.004713 | 0.006259 | 205.912 |
| `fft_y_Bw_filtered_ampl_3` | `MLP` | 0.003746 | 0.004932 | 395.642 |
| `fft_y_Bw_filtered_phase_3` | `MLP` | 0.027219 | 0.035624 | 2.029 |
| `fft_y_Bw_filtered_ampl_39` | `MLP` | 0.003731 | 0.004918 | 826.224 |
| `fft_y_Bw_filtered_phase_39` | `MLP` | 0.393993 | 0.731926 | 14.966 |
| `fft_y_Bw_filtered_ampl_40` | `MLP` | 0.003766 | 0.004963 | 1181.171 |
| `fft_y_Bw_filtered_phase_40` | `MLP` | 0.106614 | 0.172894 | 38.148 |
| `fft_y_Bw_filtered_ampl_78` | `MLP` | 0.003718 | 0.004911 | 413.223 |
| `fft_y_Bw_filtered_phase_78` | `MLP` | 0.062284 | 0.113764 | 28.888 |
| `fft_y_Bw_filtered_ampl_81` | `MLP` | 0.003767 | 0.004963 | 3270.597 |
| `fft_y_Bw_filtered_phase_81` | `MLP` | 0.113126 | 0.152623 | 36.046 |
| `fft_y_Bw_filtered_ampl_156` | `MLP` | 0.004289 | 0.005838 | 729.302 |
| `fft_y_Bw_filtered_phase_156` | `MLP` | 0.322864 | 0.728084 | 33.467 |
| `fft_y_Bw_filtered_ampl_162` | `MLP` | 0.004150 | 0.005765 | 1382.201 |
| `fft_y_Bw_filtered_phase_162` | `MLP` | 0.140366 | 0.261827 | 8.755 |
| `fft_y_Bw_filtered_ampl_240` | `MLP` | 0.003837 | 0.005017 | 929.368 |
| `fft_y_Bw_filtered_phase_240` | `MLP` | 0.415639 | 0.765935 | 28.485 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/mlp/2026-04-26_track1_backward_mlp_original_dataset_mega_campaign/010_track1_original_dataset_backward_mlp_attempt_10.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-26-36__track1_original_dataset_backward_mlp_attempt_10_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-26-36__track1_original_dataset_backward_mlp_attempt_10_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-26-36__track1_original_dataset_backward_mlp_attempt_10_campaign_validation/validation_summary.yaml`
