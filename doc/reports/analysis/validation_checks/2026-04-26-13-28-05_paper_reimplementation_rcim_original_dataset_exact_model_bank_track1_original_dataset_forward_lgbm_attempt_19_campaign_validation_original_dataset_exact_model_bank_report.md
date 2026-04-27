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
- random seed: `59`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `92.762%`
- winning mean component MAE: `0.159549`
- winning mean component RMSE: `0.233605`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 92.762 | 0.159549 | 0.233605 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 10, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `LGBM` | 0.006816 | 0.007986 | 15.364 |
| `fft_y_Fw_filtered_ampl_1` | `LGBM` | 0.000029 | 0.000037 | 0.167 |
| `fft_y_Fw_filtered_phase_1` | `LGBM` | 0.003121 | 0.004409 | 211.616 |
| `fft_y_Fw_filtered_ampl_3` | `LGBM` | 0.000059 | 0.000073 | 7.388 |
| `fft_y_Fw_filtered_phase_3` | `LGBM` | 0.049964 | 0.062342 | 2.783 |
| `fft_y_Fw_filtered_ampl_39` | `LGBM` | 0.000108 | 0.000131 | 10.101 |
| `fft_y_Fw_filtered_phase_39` | `LGBM` | 0.083367 | 0.103493 | 7.336 |
| `fft_y_Fw_filtered_ampl_40` | `LGBM` | 0.000039 | 0.000055 | 5.124 |
| `fft_y_Fw_filtered_phase_40` | `LGBM` | 0.066791 | 0.090320 | 212.503 |
| `fft_y_Fw_filtered_ampl_78` | `LGBM` | 0.000212 | 0.000260 | 49.181 |
| `fft_y_Fw_filtered_phase_78` | `LGBM` | 0.183974 | 0.307176 | 148.803 |
| `fft_y_Fw_filtered_ampl_81` | `LGBM` | 0.000026 | 0.000037 | 8.212 |
| `fft_y_Fw_filtered_phase_81` | `LGBM` | 0.148154 | 0.184213 | 17.150 |
| `fft_y_Fw_filtered_ampl_156` | `LGBM` | 0.000292 | 0.000464 | 280.160 |
| `fft_y_Fw_filtered_phase_156` | `LGBM` | 1.144637 | 1.398570 | 70.820 |
| `fft_y_Fw_filtered_ampl_162` | `LGBM` | 0.000294 | 0.000564 | 148.891 |
| `fft_y_Fw_filtered_phase_162` | `LGBM` | 0.855293 | 1.375681 | 38.947 |
| `fft_y_Fw_filtered_ampl_240` | `LGBM` | 0.000115 | 0.000181 | 62.379 |
| `fft_y_Fw_filtered_phase_240` | `LGBM` | 0.488147 | 0.902501 | 465.551 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/lgbm/2026-04-26_track1_forward_lgbm_original_dataset_mega_campaign/019_track1_original_dataset_forward_lgbm_attempt_19.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-05-59__track1_original_dataset_forward_lgbm_attempt_19_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-05-59__track1_original_dataset_forward_lgbm_attempt_19_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-05-59__track1_original_dataset_forward_lgbm_attempt_19_campaign_validation/validation_summary.yaml`
