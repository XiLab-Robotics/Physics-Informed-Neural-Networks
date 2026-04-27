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
- random seed: `0`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `24.115%`
- winning mean component MAE: `0.082952`
- winning mean component RMSE: `0.155675`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 24.115 | 0.082952 | 0.155675 | `{'estimator__learning_rate': 0.2, 'estimator__max_depth': 11, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | 0.002471 | 0.003193 | 5.362 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | 0.000029 | 0.000037 | 0.170 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | 0.001819 | 0.002433 | 48.054 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | 0.000014 | 0.000021 | 1.819 |
| `fft_y_Fw_filtered_phase_3` | `HGBM` | 0.020900 | 0.025917 | 1.153 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | 0.000022 | 0.000030 | 2.032 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | 0.022474 | 0.033047 | 1.851 |
| `fft_y_Fw_filtered_ampl_40` | `HGBM` | 0.000024 | 0.000031 | 3.010 |
| `fft_y_Fw_filtered_phase_40` | `HGBM` | 0.037614 | 0.056445 | 69.304 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | 0.000026 | 0.000038 | 11.723 |
| `fft_y_Fw_filtered_phase_78` | `HGBM` | 0.059008 | 0.095097 | 144.381 |
| `fft_y_Fw_filtered_ampl_81` | `HGBM` | 0.000011 | 0.000016 | 3.720 |
| `fft_y_Fw_filtered_phase_81` | `HGBM` | 0.043818 | 0.061870 | 3.782 |
| `fft_y_Fw_filtered_ampl_156` | `HGBM` | 0.000125 | 0.000347 | 30.926 |
| `fft_y_Fw_filtered_phase_156` | `HGBM` | 0.655772 | 1.067963 | 66.233 |
| `fft_y_Fw_filtered_ampl_162` | `HGBM` | 0.000119 | 0.000353 | 17.975 |
| `fft_y_Fw_filtered_phase_162` | `HGBM` | 0.360457 | 0.735244 | 16.142 |
| `fft_y_Fw_filtered_ampl_240` | `HGBM` | 0.000046 | 0.000092 | 12.267 |
| `fft_y_Fw_filtered_phase_240` | `HGBM` | 0.371345 | 0.875644 | 18.283 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/hgbm/2026-04-26_track1_forward_hgbm_original_dataset_mega_campaign/001_track1_original_dataset_forward_hgbm_attempt_01.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-34-27__track1_original_dataset_forward_hgbm_attempt_01_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-34-27__track1_original_dataset_forward_hgbm_attempt_01_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-34-27__track1_original_dataset_forward_hgbm_attempt_01_campaign_validation/validation_summary.yaml`
