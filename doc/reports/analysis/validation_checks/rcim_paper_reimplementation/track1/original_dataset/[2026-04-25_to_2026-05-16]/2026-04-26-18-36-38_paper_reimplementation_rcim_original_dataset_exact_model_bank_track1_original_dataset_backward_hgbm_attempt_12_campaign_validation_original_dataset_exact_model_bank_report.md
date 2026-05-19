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

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `16.507%`
- winning mean component MAE: `0.063350`
- winning mean component RMSE: `0.118507`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 16.507 | 0.063350 | 0.118507 | `{'estimator__learning_rate': 0.18, 'estimator__max_depth': 13, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `HGBM` | 0.002209 | 0.002885 | 29.510 |
| `fft_y_Bw_filtered_ampl_1` | `HGBM` | 0.000024 | 0.000034 | 0.141 |
| `fft_y_Bw_filtered_phase_1` | `HGBM` | 0.001905 | 0.002584 | 39.921 |
| `fft_y_Bw_filtered_ampl_3` | `HGBM` | 0.000023 | 0.000035 | 2.262 |
| `fft_y_Bw_filtered_phase_3` | `HGBM` | 0.018789 | 0.024405 | 1.424 |
| `fft_y_Bw_filtered_ampl_39` | `HGBM` | 0.000014 | 0.000021 | 3.287 |
| `fft_y_Bw_filtered_phase_39` | `HGBM` | 0.260678 | 0.657589 | 9.238 |
| `fft_y_Bw_filtered_ampl_40` | `HGBM` | 0.000027 | 0.000038 | 9.249 |
| `fft_y_Bw_filtered_phase_40` | `HGBM` | 0.091991 | 0.139134 | 42.004 |
| `fft_y_Bw_filtered_ampl_78` | `HGBM` | 0.000027 | 0.000036 | 3.742 |
| `fft_y_Bw_filtered_phase_78` | `HGBM` | 0.059494 | 0.097409 | 32.217 |
| `fft_y_Bw_filtered_ampl_81` | `HGBM` | 0.000010 | 0.000013 | 8.049 |
| `fft_y_Bw_filtered_phase_81` | `HGBM` | 0.097512 | 0.129029 | 35.629 |
| `fft_y_Bw_filtered_ampl_156` | `HGBM` | 0.000374 | 0.001151 | 13.573 |
| `fft_y_Bw_filtered_phase_156` | `HGBM` | 0.139870 | 0.324512 | 11.137 |
| `fft_y_Bw_filtered_ampl_162` | `HGBM` | 0.000150 | 0.000285 | 16.569 |
| `fft_y_Bw_filtered_phase_162` | `HGBM` | 0.115259 | 0.208584 | 6.939 |
| `fft_y_Bw_filtered_ampl_240` | `HGBM` | 0.000142 | 0.000252 | 23.057 |
| `fft_y_Bw_filtered_phase_240` | `HGBM` | 0.415154 | 0.663629 | 25.683 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/hgbm/2026-04-26_track1_backward_hgbm_original_dataset_mega_campaign/012_track1_original_dataset_backward_hgbm_attempt_12.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-35-12__track1_original_dataset_backward_hgbm_attempt_12_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-35-12__track1_original_dataset_backward_hgbm_attempt_12_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-35-12__track1_original_dataset_backward_hgbm_attempt_12_campaign_validation/validation_summary.yaml`
