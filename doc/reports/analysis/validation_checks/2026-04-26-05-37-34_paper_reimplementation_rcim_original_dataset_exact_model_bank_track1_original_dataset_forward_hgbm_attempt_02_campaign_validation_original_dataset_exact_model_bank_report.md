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
- random seed: `5`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `32.251%`
- winning mean component MAE: `0.098399`
- winning mean component RMSE: `0.177795`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 32.251 | 0.098399 | 0.177795 | `{'estimator__learning_rate': 0.2, 'estimator__max_depth': 10, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | 0.002303 | 0.003579 | 14.337 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | 0.000025 | 0.000035 | 0.147 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | 0.002131 | 0.002878 | 31.724 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | 0.000019 | 0.000027 | 2.354 |
| `fft_y_Fw_filtered_phase_3` | `HGBM` | 0.026067 | 0.036275 | 1.430 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | 0.000025 | 0.000033 | 2.238 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | 0.020893 | 0.030519 | 1.801 |
| `fft_y_Fw_filtered_ampl_40` | `HGBM` | 0.000030 | 0.000044 | 3.754 |
| `fft_y_Fw_filtered_phase_40` | `HGBM` | 0.044635 | 0.067486 | 111.520 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | 0.000030 | 0.000043 | 5.009 |
| `fft_y_Fw_filtered_phase_78` | `HGBM` | 0.105500 | 0.230627 | 120.861 |
| `fft_y_Fw_filtered_ampl_81` | `HGBM` | 0.000013 | 0.000019 | 3.962 |
| `fft_y_Fw_filtered_phase_81` | `HGBM` | 0.053284 | 0.083773 | 6.833 |
| `fft_y_Fw_filtered_ampl_156` | `HGBM` | 0.000098 | 0.000263 | 19.132 |
| `fft_y_Fw_filtered_phase_156` | `HGBM` | 0.669892 | 1.024442 | 41.955 |
| `fft_y_Fw_filtered_ampl_162` | `HGBM` | 0.000110 | 0.000277 | 23.162 |
| `fft_y_Fw_filtered_phase_162` | `HGBM` | 0.538257 | 1.010797 | 25.673 |
| `fft_y_Fw_filtered_ampl_240` | `HGBM` | 0.000042 | 0.000069 | 11.198 |
| `fft_y_Fw_filtered_phase_240` | `HGBM` | 0.406220 | 0.886922 | 185.684 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/hgbm/2026-04-26_track1_forward_hgbm_original_dataset_mega_campaign/002_track1_original_dataset_forward_hgbm_attempt_02.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-36-04__track1_original_dataset_forward_hgbm_attempt_02_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-36-04__track1_original_dataset_forward_hgbm_attempt_02_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-36-04__track1_original_dataset_forward_hgbm_attempt_02_campaign_validation/validation_summary.yaml`
