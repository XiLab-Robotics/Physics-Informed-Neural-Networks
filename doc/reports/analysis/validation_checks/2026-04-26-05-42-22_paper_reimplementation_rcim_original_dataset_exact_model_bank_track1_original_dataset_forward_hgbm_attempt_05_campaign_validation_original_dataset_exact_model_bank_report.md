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
- random seed: `11`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `56.641%`
- winning mean component MAE: `0.101143`
- winning mean component RMSE: `0.199295`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 56.641 | 0.101143 | 0.199295 | `{'estimator__learning_rate': 0.18, 'estimator__max_depth': 13, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | 0.002598 | 0.003267 | 4.995 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | 0.000028 | 0.000037 | 0.165 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | 0.001967 | 0.002782 | 30.494 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | 0.000016 | 0.000021 | 1.993 |
| `fft_y_Fw_filtered_phase_3` | `HGBM` | 0.019730 | 0.027433 | 1.096 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | 0.000025 | 0.000034 | 2.212 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | 0.021291 | 0.034579 | 1.699 |
| `fft_y_Fw_filtered_ampl_40` | `HGBM` | 0.000029 | 0.000043 | 3.430 |
| `fft_y_Fw_filtered_phase_40` | `HGBM` | 0.040836 | 0.060877 | 59.749 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | 0.000028 | 0.000040 | 9.487 |
| `fft_y_Fw_filtered_phase_78` | `HGBM` | 0.100457 | 0.346919 | 807.500 |
| `fft_y_Fw_filtered_ampl_81` | `HGBM` | 0.000010 | 0.000015 | 3.355 |
| `fft_y_Fw_filtered_phase_81` | `HGBM` | 0.049707 | 0.079531 | 5.126 |
| `fft_y_Fw_filtered_ampl_156` | `HGBM` | 0.000183 | 0.000494 | 22.752 |
| `fft_y_Fw_filtered_phase_156` | `HGBM` | 0.924468 | 1.533424 | 50.891 |
| `fft_y_Fw_filtered_ampl_162` | `HGBM` | 0.000147 | 0.000409 | 25.406 |
| `fft_y_Fw_filtered_phase_162` | `HGBM` | 0.432928 | 0.948251 | 18.845 |
| `fft_y_Fw_filtered_ampl_240` | `HGBM` | 0.000035 | 0.000058 | 9.309 |
| `fft_y_Fw_filtered_phase_240` | `HGBM` | 0.327235 | 0.748388 | 17.679 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/hgbm/2026-04-26_track1_forward_hgbm_original_dataset_mega_campaign/005_track1_original_dataset_forward_hgbm_attempt_05.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-40-52__track1_original_dataset_forward_hgbm_attempt_05_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-40-52__track1_original_dataset_forward_hgbm_attempt_05_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-40-52__track1_original_dataset_forward_hgbm_attempt_05_campaign_validation/validation_summary.yaml`
