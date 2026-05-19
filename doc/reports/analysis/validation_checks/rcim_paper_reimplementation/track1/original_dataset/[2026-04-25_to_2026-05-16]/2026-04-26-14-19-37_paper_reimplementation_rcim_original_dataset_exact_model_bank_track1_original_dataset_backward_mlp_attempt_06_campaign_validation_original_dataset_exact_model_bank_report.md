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
- random seed: `13`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `420.882%`
- winning mean component MAE: `0.078705`
- winning mean component RMSE: `0.165665`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 420.882 | 0.078705 | 0.165665 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (100,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `MLP` | 0.004612 | 0.006509 | 75.120 |
| `fft_y_Bw_filtered_ampl_1` | `MLP` | 0.002958 | 0.003794 | 17.258 |
| `fft_y_Bw_filtered_phase_1` | `MLP` | 0.004077 | 0.005481 | 228.218 |
| `fft_y_Bw_filtered_ampl_3` | `MLP` | 0.003000 | 0.003832 | 321.345 |
| `fft_y_Bw_filtered_phase_3` | `MLP` | 0.024914 | 0.035545 | 1.815 |
| `fft_y_Bw_filtered_ampl_39` | `MLP` | 0.002990 | 0.003829 | 671.354 |
| `fft_y_Bw_filtered_phase_39` | `MLP` | 0.309422 | 0.976001 | 10.986 |
| `fft_y_Bw_filtered_ampl_40` | `MLP` | 0.003020 | 0.003851 | 906.694 |
| `fft_y_Bw_filtered_phase_40` | `MLP` | 0.099333 | 0.159828 | 38.235 |
| `fft_y_Bw_filtered_ampl_78` | `MLP` | 0.002985 | 0.003830 | 426.106 |
| `fft_y_Bw_filtered_phase_78` | `MLP` | 0.055336 | 0.084849 | 22.588 |
| `fft_y_Bw_filtered_ampl_81` | `MLP` | 0.003016 | 0.003853 | 2658.772 |
| `fft_y_Bw_filtered_phase_81` | `MLP` | 0.083053 | 0.111446 | 41.938 |
| `fft_y_Bw_filtered_ampl_156` | `MLP` | 0.003367 | 0.004634 | 661.366 |
| `fft_y_Bw_filtered_phase_156` | `MLP` | 0.296483 | 0.554165 | 29.890 |
| `fft_y_Bw_filtered_ampl_162` | `MLP` | 0.003498 | 0.004827 | 1121.827 |
| `fft_y_Bw_filtered_phase_162` | `MLP` | 0.107457 | 0.184001 | 6.580 |
| `fft_y_Bw_filtered_ampl_240` | `MLP` | 0.002978 | 0.003714 | 735.661 |
| `fft_y_Bw_filtered_phase_240` | `MLP` | 0.482897 | 0.993634 | 21.002 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/mlp/2026-04-26_track1_backward_mlp_original_dataset_mega_campaign/006_track1_original_dataset_backward_mlp_attempt_06.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-17-28__track1_original_dataset_backward_mlp_attempt_06_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-17-28__track1_original_dataset_backward_mlp_attempt_06_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-17-28__track1_original_dataset_backward_mlp_attempt_06_campaign_validation/validation_summary.yaml`
