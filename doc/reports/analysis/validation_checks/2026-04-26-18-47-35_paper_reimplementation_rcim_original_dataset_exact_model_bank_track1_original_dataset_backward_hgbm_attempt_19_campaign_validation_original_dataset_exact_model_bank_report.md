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
- random seed: `59`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `20.946%`
- winning mean component MAE: `0.065309`
- winning mean component RMSE: `0.126585`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 20.946 | 0.065309 | 0.126585 | `{'estimator__learning_rate': 0.18, 'estimator__max_depth': 13, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `HGBM` | 0.002501 | 0.003038 | 61.010 |
| `fft_y_Bw_filtered_ampl_1` | `HGBM` | 0.000026 | 0.000039 | 0.154 |
| `fft_y_Bw_filtered_phase_1` | `HGBM` | 0.002068 | 0.003162 | 91.851 |
| `fft_y_Bw_filtered_ampl_3` | `HGBM` | 0.000025 | 0.000040 | 2.466 |
| `fft_y_Bw_filtered_phase_3` | `HGBM` | 0.020102 | 0.025682 | 1.509 |
| `fft_y_Bw_filtered_ampl_39` | `HGBM` | 0.000016 | 0.000023 | 3.485 |
| `fft_y_Bw_filtered_phase_39` | `HGBM` | 0.370252 | 0.875451 | 12.815 |
| `fft_y_Bw_filtered_ampl_40` | `HGBM` | 0.000027 | 0.000039 | 8.796 |
| `fft_y_Bw_filtered_phase_40` | `HGBM` | 0.091157 | 0.125976 | 28.632 |
| `fft_y_Bw_filtered_ampl_78` | `HGBM` | 0.000035 | 0.000049 | 4.171 |
| `fft_y_Bw_filtered_phase_78` | `HGBM` | 0.071912 | 0.127532 | 19.949 |
| `fft_y_Bw_filtered_ampl_81` | `HGBM` | 0.000010 | 0.000015 | 8.622 |
| `fft_y_Bw_filtered_phase_81` | `HGBM` | 0.089090 | 0.118291 | 39.759 |
| `fft_y_Bw_filtered_ampl_156` | `HGBM` | 0.000341 | 0.001028 | 22.511 |
| `fft_y_Bw_filtered_phase_156` | `HGBM` | 0.138258 | 0.264691 | 38.194 |
| `fft_y_Bw_filtered_ampl_162` | `HGBM` | 0.000081 | 0.000191 | 14.636 |
| `fft_y_Bw_filtered_phase_162` | `HGBM` | 0.126917 | 0.258753 | 7.156 |
| `fft_y_Bw_filtered_ampl_240` | `HGBM` | 0.000097 | 0.000174 | 15.436 |
| `fft_y_Bw_filtered_phase_240` | `HGBM` | 0.327953 | 0.600932 | 16.825 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/hgbm/2026-04-26_track1_backward_hgbm_original_dataset_mega_campaign/019_track1_original_dataset_backward_hgbm_attempt_19.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-46-08__track1_original_dataset_backward_hgbm_attempt_19_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-46-08__track1_original_dataset_backward_hgbm_attempt_19_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-46-08__track1_original_dataset_backward_hgbm_attempt_19_campaign_validation/validation_summary.yaml`
