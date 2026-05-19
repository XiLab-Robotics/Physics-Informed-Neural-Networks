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
- random seed: `37`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `32.317%`
- winning mean component MAE: `0.086916`
- winning mean component RMSE: `0.165510`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 32.317 | 0.086916 | 0.165510 | `{'estimator__learning_rate': 0.2, 'estimator__max_depth': 12, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | 0.002346 | 0.003034 | 4.887 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | 0.000022 | 0.000028 | 0.126 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | 0.001857 | 0.002372 | 49.953 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | 0.000016 | 0.000021 | 2.014 |
| `fft_y_Fw_filtered_phase_3` | `HGBM` | 0.021091 | 0.026610 | 1.175 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | 0.000023 | 0.000031 | 2.142 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | 0.016798 | 0.021991 | 1.373 |
| `fft_y_Fw_filtered_ampl_40` | `HGBM` | 0.000023 | 0.000036 | 2.780 |
| `fft_y_Fw_filtered_phase_40` | `HGBM` | 0.034376 | 0.048850 | 46.127 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | 0.000032 | 0.000044 | 6.700 |
| `fft_y_Fw_filtered_phase_78` | `HGBM` | 0.096261 | 0.180446 | 308.827 |
| `fft_y_Fw_filtered_ampl_81` | `HGBM` | 0.000011 | 0.000014 | 3.619 |
| `fft_y_Fw_filtered_phase_81` | `HGBM` | 0.052301 | 0.076909 | 7.438 |
| `fft_y_Fw_filtered_ampl_156` | `HGBM` | 0.000115 | 0.000292 | 23.568 |
| `fft_y_Fw_filtered_phase_156` | `HGBM` | 0.606314 | 1.052167 | 32.087 |
| `fft_y_Fw_filtered_ampl_162` | `HGBM` | 0.000101 | 0.000301 | 15.331 |
| `fft_y_Fw_filtered_phase_162` | `HGBM` | 0.497955 | 1.055601 | 19.697 |
| `fft_y_Fw_filtered_ampl_240` | `HGBM` | 0.000032 | 0.000055 | 9.887 |
| `fft_y_Fw_filtered_phase_240` | `HGBM` | 0.321731 | 0.675883 | 76.286 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/hgbm/2026-04-26_track1_forward_hgbm_original_dataset_mega_campaign/015_track1_original_dataset_forward_hgbm_attempt_15.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-57-10__track1_original_dataset_forward_hgbm_attempt_15_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-57-10__track1_original_dataset_forward_hgbm_attempt_15_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-57-10__track1_original_dataset_forward_hgbm_attempt_15_campaign_validation/validation_summary.yaml`
