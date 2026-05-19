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
- random seed: `31`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `33.432%`
- winning mean component MAE: `0.104584`
- winning mean component RMSE: `0.203147`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 33.432 | 0.104584 | 0.203147 | `{'estimator__learning_rate': 0.18, 'estimator__max_depth': 9, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | 0.002661 | 0.003530 | 6.203 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | 0.000027 | 0.000040 | 0.158 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | 0.002295 | 0.003768 | 40.549 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | 0.000020 | 0.000044 | 2.403 |
| `fft_y_Fw_filtered_phase_3` | `HGBM` | 0.023349 | 0.031606 | 1.280 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | 0.000026 | 0.000043 | 2.510 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | 0.025003 | 0.043474 | 2.032 |
| `fft_y_Fw_filtered_ampl_40` | `HGBM` | 0.000028 | 0.000038 | 3.561 |
| `fft_y_Fw_filtered_phase_40` | `HGBM` | 0.033959 | 0.055147 | 58.804 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | 0.000028 | 0.000043 | 6.892 |
| `fft_y_Fw_filtered_phase_78` | `HGBM` | 0.137012 | 0.379330 | 361.626 |
| `fft_y_Fw_filtered_ampl_81` | `HGBM` | 0.000011 | 0.000022 | 3.364 |
| `fft_y_Fw_filtered_phase_81` | `HGBM` | 0.068695 | 0.111599 | 6.761 |
| `fft_y_Fw_filtered_ampl_156` | `HGBM` | 0.000118 | 0.000374 | 25.200 |
| `fft_y_Fw_filtered_phase_156` | `HGBM` | 0.704369 | 1.127113 | 37.290 |
| `fft_y_Fw_filtered_ampl_162` | `HGBM` | 0.000091 | 0.000286 | 17.638 |
| `fft_y_Fw_filtered_phase_162` | `HGBM` | 0.495083 | 1.077503 | 18.864 |
| `fft_y_Fw_filtered_ampl_240` | `HGBM` | 0.000037 | 0.000053 | 15.405 |
| `fft_y_Fw_filtered_phase_240` | `HGBM` | 0.494276 | 1.025786 | 24.671 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/hgbm/2026-04-26_track1_forward_hgbm_original_dataset_mega_campaign/014_track1_original_dataset_forward_hgbm_attempt_14.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-55-30__track1_original_dataset_forward_hgbm_attempt_14_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-55-30__track1_original_dataset_forward_hgbm_attempt_14_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-55-30__track1_original_dataset_forward_hgbm_attempt_14_campaign_validation/validation_summary.yaml`
