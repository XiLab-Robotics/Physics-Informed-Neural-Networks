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
- random seed: `61`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `18.064%`
- winning mean component MAE: `0.054662`
- winning mean component RMSE: `0.113399`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 18.064 | 0.054662 | 0.113399 | `{'estimator__learning_rate': 0.19, 'estimator__max_depth': 10, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `HGBM` | 0.002542 | 0.003047 | 32.170 |
| `fft_y_Bw_filtered_ampl_1` | `HGBM` | 0.000027 | 0.000040 | 0.158 |
| `fft_y_Bw_filtered_phase_1` | `HGBM` | 0.001567 | 0.002274 | 32.247 |
| `fft_y_Bw_filtered_ampl_3` | `HGBM` | 0.000020 | 0.000031 | 2.145 |
| `fft_y_Bw_filtered_phase_3` | `HGBM` | 0.020538 | 0.028325 | 1.509 |
| `fft_y_Bw_filtered_ampl_39` | `HGBM` | 0.000016 | 0.000021 | 3.540 |
| `fft_y_Bw_filtered_phase_39` | `HGBM` | 0.239677 | 0.707389 | 8.554 |
| `fft_y_Bw_filtered_ampl_40` | `HGBM` | 0.000030 | 0.000048 | 8.970 |
| `fft_y_Bw_filtered_phase_40` | `HGBM` | 0.099632 | 0.157713 | 33.610 |
| `fft_y_Bw_filtered_ampl_78` | `HGBM` | 0.000034 | 0.000048 | 4.602 |
| `fft_y_Bw_filtered_phase_78` | `HGBM` | 0.055580 | 0.086628 | 66.287 |
| `fft_y_Bw_filtered_ampl_81` | `HGBM` | 0.000009 | 0.000013 | 7.760 |
| `fft_y_Bw_filtered_phase_81` | `HGBM` | 0.088569 | 0.116526 | 62.757 |
| `fft_y_Bw_filtered_ampl_156` | `HGBM` | 0.000376 | 0.001272 | 18.759 |
| `fft_y_Bw_filtered_phase_156` | `HGBM` | 0.180008 | 0.468668 | 13.093 |
| `fft_y_Bw_filtered_ampl_162` | `HGBM` | 0.000137 | 0.000366 | 12.984 |
| `fft_y_Bw_filtered_phase_162` | `HGBM` | 0.080012 | 0.134257 | 4.629 |
| `fft_y_Bw_filtered_ampl_240` | `HGBM` | 0.000086 | 0.000146 | 14.031 |
| `fft_y_Bw_filtered_phase_240` | `HGBM` | 0.269709 | 0.447775 | 15.410 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/hgbm/2026-04-26_track1_backward_hgbm_original_dataset_mega_campaign/020_track1_original_dataset_backward_hgbm_attempt_20.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-47-42__track1_original_dataset_backward_hgbm_attempt_20_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-47-42__track1_original_dataset_backward_hgbm_attempt_20_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-47-42__track1_original_dataset_backward_hgbm_attempt_20_campaign_validation/validation_summary.yaml`
