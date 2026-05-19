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
- random seed: `19`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `63.845%`
- winning mean component MAE: `0.153824`
- winning mean component RMSE: `0.226042`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 63.845 | 0.153824 | 0.226042 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 11, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `LGBM` | 0.007248 | 0.008884 | 30.954 |
| `fft_y_Fw_filtered_ampl_1` | `LGBM` | 0.000028 | 0.000036 | 0.163 |
| `fft_y_Fw_filtered_phase_1` | `LGBM` | 0.001798 | 0.002610 | 165.301 |
| `fft_y_Fw_filtered_ampl_3` | `LGBM` | 0.000057 | 0.000068 | 7.413 |
| `fft_y_Fw_filtered_phase_3` | `LGBM` | 0.053356 | 0.066444 | 2.982 |
| `fft_y_Fw_filtered_ampl_39` | `LGBM` | 0.000098 | 0.000116 | 9.020 |
| `fft_y_Fw_filtered_phase_39` | `LGBM` | 0.077944 | 0.097278 | 6.728 |
| `fft_y_Fw_filtered_ampl_40` | `LGBM` | 0.000036 | 0.000049 | 4.470 |
| `fft_y_Fw_filtered_phase_40` | `LGBM` | 0.058810 | 0.082881 | 105.360 |
| `fft_y_Fw_filtered_ampl_78` | `LGBM` | 0.000208 | 0.000245 | 64.554 |
| `fft_y_Fw_filtered_phase_78` | `LGBM` | 0.136832 | 0.206742 | 226.097 |
| `fft_y_Fw_filtered_ampl_81` | `LGBM` | 0.000030 | 0.000037 | 10.330 |
| `fft_y_Fw_filtered_phase_81` | `LGBM` | 0.140501 | 0.180039 | 14.530 |
| `fft_y_Fw_filtered_ampl_156` | `LGBM` | 0.000370 | 0.000746 | 200.771 |
| `fft_y_Fw_filtered_phase_156` | `LGBM` | 1.279023 | 1.604509 | 58.587 |
| `fft_y_Fw_filtered_ampl_162` | `LGBM` | 0.000668 | 0.001899 | 140.246 |
| `fft_y_Fw_filtered_phase_162` | `LGBM` | 0.647126 | 1.050394 | 36.254 |
| `fft_y_Fw_filtered_ampl_240` | `LGBM` | 0.000149 | 0.000282 | 88.361 |
| `fft_y_Fw_filtered_phase_240` | `LGBM` | 0.518376 | 0.991539 | 40.927 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/lgbm/2026-04-26_track1_forward_lgbm_original_dataset_mega_campaign/009_track1_original_dataset_forward_lgbm_attempt_09.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-09-24-27__track1_original_dataset_forward_lgbm_attempt_09_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-09-24-27__track1_original_dataset_forward_lgbm_attempt_09_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-09-24-27__track1_original_dataset_forward_lgbm_attempt_09_campaign_validation/validation_summary.yaml`
