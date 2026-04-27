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
- random seed: `7`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `MLP`
- winning estimator: `MLPRegressor`
- winning mean component MAPE: `534.372%`
- winning mean component MAE: `0.078765`
- winning mean component RMSE: `0.158521`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `MLP` | `MLPRegressor` | 534.372 | 0.078765 | 0.158521 | `{'estimator__mlp__activation': 'tanh', 'estimator__mlp__alpha': 0.01, 'estimator__mlp__hidden_layer_sizes': (100,), 'estimator__mlp__max_iter': 2000, 'estimator__mlp__solver': 'lbfgs'}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `MLP` | 0.005546 | 0.006873 | 66.972 |
| `fft_y_Bw_filtered_ampl_1` | `MLP` | 0.003686 | 0.004422 | 21.508 |
| `fft_y_Bw_filtered_phase_1` | `MLP` | 0.004408 | 0.005624 | 107.488 |
| `fft_y_Bw_filtered_ampl_3` | `MLP` | 0.003727 | 0.004455 | 394.413 |
| `fft_y_Bw_filtered_phase_3` | `MLP` | 0.021792 | 0.030909 | 1.590 |
| `fft_y_Bw_filtered_ampl_39` | `MLP` | 0.003716 | 0.004437 | 853.586 |
| `fft_y_Bw_filtered_phase_39` | `MLP` | 0.566876 | 1.375012 | 19.530 |
| `fft_y_Bw_filtered_ampl_40` | `MLP` | 0.003748 | 0.004468 | 1184.928 |
| `fft_y_Bw_filtered_phase_40` | `MLP` | 0.088403 | 0.127686 | 27.559 |
| `fft_y_Bw_filtered_ampl_78` | `MLP` | 0.003706 | 0.004434 | 635.321 |
| `fft_y_Bw_filtered_phase_78` | `MLP` | 0.066997 | 0.142030 | 17.566 |
| `fft_y_Bw_filtered_ampl_81` | `MLP` | 0.003744 | 0.004466 | 3286.719 |
| `fft_y_Bw_filtered_phase_81` | `MLP` | 0.077030 | 0.106173 | 48.651 |
| `fft_y_Bw_filtered_ampl_156` | `MLP` | 0.004026 | 0.005058 | 867.647 |
| `fft_y_Bw_filtered_phase_156` | `MLP` | 0.186134 | 0.405995 | 16.700 |
| `fft_y_Bw_filtered_ampl_162` | `MLP` | 0.003949 | 0.004903 | 1675.954 |
| `fft_y_Bw_filtered_phase_162` | `MLP` | 0.086345 | 0.147142 | 4.867 |
| `fft_y_Bw_filtered_ampl_240` | `MLP` | 0.003606 | 0.004331 | 892.423 |
| `fft_y_Bw_filtered_phase_240` | `MLP` | 0.359096 | 0.623477 | 29.637 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/mlp/2026-04-26_track1_backward_mlp_original_dataset_mega_campaign/003_track1_original_dataset_backward_mlp_attempt_03.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-10-26__track1_original_dataset_backward_mlp_attempt_03_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-10-26__track1_original_dataset_backward_mlp_attempt_03_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-10-26__track1_original_dataset_backward_mlp_attempt_03_campaign_validation/validation_summary.yaml`
