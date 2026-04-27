# Original-Dataset Exact RCIM Model Bank Validation Report

## Overview

This report covers the direction-specific exact-model-bank branch trained from the repository dataset under `data/datasets`.

- direction label: `forward`
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
- random seed: `7`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `612.434%`
- winning mean component MAE: `0.117056`
- winning mean component RMSE: `0.199217`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 612.434 | 0.117056 | 0.199217 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (100,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `MLP` | 0.003893 | 0.005281 | 7.746 |
| `fft_y_Fw_filtered_ampl_1` | `MLP` | 0.003692 | 0.004430 | 21.531 |
| `fft_y_Fw_filtered_phase_1` | `MLP` | 0.003980 | 0.005349 | 43.419 |
| `fft_y_Fw_filtered_ampl_3` | `MLP` | 0.003742 | 0.004463 | 464.387 |
| `fft_y_Fw_filtered_phase_3` | `MLP` | 0.031137 | 0.043259 | 1.730 |
| `fft_y_Fw_filtered_ampl_39` | `MLP` | 0.003735 | 0.004453 | 336.299 |
| `fft_y_Fw_filtered_phase_39` | `MLP` | 0.022975 | 0.031420 | 2.052 |
| `fft_y_Fw_filtered_ampl_40` | `MLP` | 0.003752 | 0.004471 | 466.324 |
| `fft_y_Fw_filtered_phase_40` | `MLP` | 0.043844 | 0.057929 | 94.586 |
| `fft_y_Fw_filtered_ampl_78` | `MLP` | 0.003722 | 0.004449 | 867.807 |
| `fft_y_Fw_filtered_phase_78` | `MLP` | 0.105536 | 0.311761 | 329.886 |
| `fft_y_Fw_filtered_ampl_81` | `MLP` | 0.003747 | 0.004471 | 1215.795 |
| `fft_y_Fw_filtered_phase_81` | `MLP` | 0.056298 | 0.078395 | 6.755 |
| `fft_y_Fw_filtered_ampl_156` | `MLP` | 0.003687 | 0.004436 | 4426.437 |
| `fft_y_Fw_filtered_phase_156` | `MLP` | 0.859110 | 1.325326 | 69.454 |
| `fft_y_Fw_filtered_ampl_162` | `MLP` | 0.003943 | 0.004903 | 2037.038 |
| `fft_y_Fw_filtered_phase_162` | `MLP` | 0.599979 | 1.146225 | 27.879 |
| `fft_y_Fw_filtered_ampl_240` | `MLP` | 0.003691 | 0.004400 | 1164.953 |
| `fft_y_Fw_filtered_phase_240` | `MLP` | 0.463599 | 0.739707 | 52.173 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/mlp/2026-04-26_track1_forward_mlp_original_dataset_mega_campaign/003_track1_original_dataset_forward_mlp_attempt_03.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-26-02__track1_original_dataset_forward_mlp_attempt_03_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-26-02__track1_original_dataset_forward_mlp_attempt_03_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-26-02__track1_original_dataset_forward_mlp_attempt_03_campaign_validation/validation_summary.yaml`
