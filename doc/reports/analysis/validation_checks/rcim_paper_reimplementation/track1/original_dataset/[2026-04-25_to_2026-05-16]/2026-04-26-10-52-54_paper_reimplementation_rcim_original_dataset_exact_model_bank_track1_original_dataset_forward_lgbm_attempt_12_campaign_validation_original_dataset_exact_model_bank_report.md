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
- random seed: `27`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `79.448%`
- winning mean component MAE: `0.149876`
- winning mean component RMSE: `0.211188`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 79.448 | 0.149876 | 0.211188 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 10, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `LGBM` | 0.007021 | 0.008293 | 14.627 |
| `fft_y_Fw_filtered_ampl_1` | `LGBM` | 0.000035 | 0.000045 | 0.207 |
| `fft_y_Fw_filtered_phase_1` | `LGBM` | 0.002893 | 0.004005 | 57.996 |
| `fft_y_Fw_filtered_ampl_3` | `LGBM` | 0.000056 | 0.000068 | 6.824 |
| `fft_y_Fw_filtered_phase_3` | `LGBM` | 0.051454 | 0.061569 | 2.815 |
| `fft_y_Fw_filtered_ampl_39` | `LGBM` | 0.000117 | 0.000138 | 10.353 |
| `fft_y_Fw_filtered_phase_39` | `LGBM` | 0.083692 | 0.103066 | 7.497 |
| `fft_y_Fw_filtered_ampl_40` | `LGBM` | 0.000042 | 0.000059 | 5.644 |
| `fft_y_Fw_filtered_phase_40` | `LGBM` | 0.068040 | 0.087844 | 164.497 |
| `fft_y_Fw_filtered_ampl_78` | `LGBM` | 0.000224 | 0.000258 | 36.687 |
| `fft_y_Fw_filtered_phase_78` | `LGBM` | 0.141579 | 0.228145 | 610.908 |
| `fft_y_Fw_filtered_ampl_81` | `LGBM` | 0.000025 | 0.000031 | 8.163 |
| `fft_y_Fw_filtered_phase_81` | `LGBM` | 0.156419 | 0.196403 | 16.697 |
| `fft_y_Fw_filtered_ampl_156` | `LGBM` | 0.000411 | 0.000739 | 218.761 |
| `fft_y_Fw_filtered_phase_156` | `LGBM` | 1.286845 | 1.601919 | 77.570 |
| `fft_y_Fw_filtered_ampl_162` | `LGBM` | 0.000363 | 0.000690 | 120.474 |
| `fft_y_Fw_filtered_phase_162` | `LGBM` | 0.714937 | 1.111718 | 40.984 |
| `fft_y_Fw_filtered_ampl_240` | `LGBM` | 0.000168 | 0.000316 | 49.983 |
| `fft_y_Fw_filtered_phase_240` | `LGBM` | 0.333324 | 0.607257 | 58.834 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/lgbm/2026-04-26_track1_forward_lgbm_original_dataset_mega_campaign/012_track1_original_dataset_forward_lgbm_attempt_12.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-10-30-50__track1_original_dataset_forward_lgbm_attempt_12_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-10-30-50__track1_original_dataset_forward_lgbm_attempt_12_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-10-30-50__track1_original_dataset_forward_lgbm_attempt_12_campaign_validation/validation_summary.yaml`
