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
- random seed: `17`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `20.274%`
- winning mean component MAE: `0.074761`
- winning mean component RMSE: `0.134949`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 20.274 | 0.074761 | 0.134949 | `{'estimator__learning_rate': 0.18, 'estimator__max_depth': 12, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | 0.002512 | 0.003191 | 4.962 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | 0.000024 | 0.000033 | 0.142 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | 0.001928 | 0.002494 | 33.188 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | 0.000016 | 0.000023 | 2.046 |
| `fft_y_Fw_filtered_phase_3` | `HGBM` | 0.021946 | 0.027083 | 1.206 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | 0.000023 | 0.000032 | 2.023 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | 0.020713 | 0.028553 | 1.839 |
| `fft_y_Fw_filtered_ampl_40` | `HGBM` | 0.000022 | 0.000029 | 2.689 |
| `fft_y_Fw_filtered_phase_40` | `HGBM` | 0.038516 | 0.060224 | 77.208 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | 0.000036 | 0.000049 | 10.897 |
| `fft_y_Fw_filtered_phase_78` | `HGBM` | 0.066994 | 0.104413 | 136.820 |
| `fft_y_Fw_filtered_ampl_81` | `HGBM` | 0.000010 | 0.000014 | 3.304 |
| `fft_y_Fw_filtered_phase_81` | `HGBM` | 0.054107 | 0.075656 | 4.833 |
| `fft_y_Fw_filtered_ampl_156` | `HGBM` | 0.000105 | 0.000235 | 15.527 |
| `fft_y_Fw_filtered_phase_156` | `HGBM` | 0.643027 | 1.092138 | 29.969 |
| `fft_y_Fw_filtered_ampl_162` | `HGBM` | 0.000122 | 0.000293 | 19.883 |
| `fft_y_Fw_filtered_phase_162` | `HGBM` | 0.309134 | 0.593354 | 14.912 |
| `fft_y_Fw_filtered_ampl_240` | `HGBM` | 0.000040 | 0.000071 | 8.753 |
| `fft_y_Fw_filtered_phase_240` | `HGBM` | 0.261186 | 0.576148 | 15.007 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/hgbm/2026-04-26_track1_forward_hgbm_original_dataset_mega_campaign/008_track1_original_dataset_forward_hgbm_attempt_08.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-45-40__track1_original_dataset_forward_hgbm_attempt_08_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-45-40__track1_original_dataset_forward_hgbm_attempt_08_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-45-40__track1_original_dataset_forward_hgbm_attempt_08_campaign_validation/validation_summary.yaml`
