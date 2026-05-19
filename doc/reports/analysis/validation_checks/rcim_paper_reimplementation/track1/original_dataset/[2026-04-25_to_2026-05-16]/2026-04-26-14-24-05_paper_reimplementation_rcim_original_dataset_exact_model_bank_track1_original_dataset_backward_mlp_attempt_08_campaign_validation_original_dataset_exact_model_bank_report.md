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
- random seed: `17`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `449.354%`
- winning mean component MAE: `0.080944`
- winning mean component RMSE: `0.144804`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 449.354 | 0.080944 | 0.144804 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (50,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `MLP` | 0.003937 | 0.005003 | 43.515 |
| `fft_y_Bw_filtered_ampl_1` | `MLP` | 0.001825 | 0.002176 | 10.642 |
| `fft_y_Bw_filtered_phase_1` | `MLP` | 0.003180 | 0.003949 | 80.838 |
| `fft_y_Bw_filtered_ampl_3` | `MLP` | 0.003109 | 0.003800 | 334.087 |
| `fft_y_Bw_filtered_phase_3` | `MLP` | 0.020018 | 0.025118 | 1.552 |
| `fft_y_Bw_filtered_ampl_39` | `MLP` | 0.003111 | 0.003799 | 686.122 |
| `fft_y_Bw_filtered_phase_39` | `MLP` | 0.441214 | 0.892796 | 16.319 |
| `fft_y_Bw_filtered_ampl_40` | `MLP` | 0.003061 | 0.003745 | 926.110 |
| `fft_y_Bw_filtered_phase_40` | `MLP` | 0.114056 | 0.162227 | 43.471 |
| `fft_y_Bw_filtered_ampl_78` | `MLP` | 0.003090 | 0.003773 | 597.559 |
| `fft_y_Bw_filtered_phase_78` | `MLP` | 0.070089 | 0.104389 | 32.234 |
| `fft_y_Bw_filtered_ampl_81` | `MLP` | 0.003072 | 0.003725 | 2716.366 |
| `fft_y_Bw_filtered_phase_81` | `MLP` | 0.102903 | 0.149074 | 79.275 |
| `fft_y_Bw_filtered_ampl_156` | `MLP` | 0.003303 | 0.004318 | 778.109 |
| `fft_y_Bw_filtered_phase_156` | `MLP` | 0.204255 | 0.390164 | 21.012 |
| `fft_y_Bw_filtered_ampl_162` | `MLP` | 0.003157 | 0.004001 | 1450.180 |
| `fft_y_Bw_filtered_phase_162` | `MLP` | 0.095269 | 0.178490 | 5.330 |
| `fft_y_Bw_filtered_ampl_240` | `MLP` | 0.003190 | 0.003882 | 693.713 |
| `fft_y_Bw_filtered_phase_240` | `MLP` | 0.456100 | 0.806841 | 21.288 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/mlp/2026-04-26_track1_backward_mlp_original_dataset_mega_campaign/008_track1_original_dataset_backward_mlp_attempt_08.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-22-02__track1_original_dataset_backward_mlp_attempt_08_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-22-02__track1_original_dataset_backward_mlp_attempt_08_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-22-02__track1_original_dataset_backward_mlp_attempt_08_campaign_validation/validation_summary.yaml`
