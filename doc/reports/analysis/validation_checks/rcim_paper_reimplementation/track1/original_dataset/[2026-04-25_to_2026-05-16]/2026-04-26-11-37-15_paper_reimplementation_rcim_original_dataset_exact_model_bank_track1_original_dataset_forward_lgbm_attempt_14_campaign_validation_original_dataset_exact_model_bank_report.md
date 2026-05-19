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
- random seed: `31`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `67.634%`
- winning mean component MAE: `0.166773`
- winning mean component RMSE: `0.250877`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 67.634 | 0.166773 | 0.250877 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 12, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `LGBM` | 0.006730 | 0.008392 | 16.725 |
| `fft_y_Fw_filtered_ampl_1` | `LGBM` | 0.000036 | 0.000048 | 0.212 |
| `fft_y_Fw_filtered_phase_1` | `LGBM` | 0.002863 | 0.004230 | 54.013 |
| `fft_y_Fw_filtered_ampl_3` | `LGBM` | 0.000055 | 0.000067 | 7.214 |
| `fft_y_Fw_filtered_phase_3` | `LGBM` | 0.051233 | 0.064318 | 2.804 |
| `fft_y_Fw_filtered_ampl_39` | `LGBM` | 0.000105 | 0.000124 | 10.285 |
| `fft_y_Fw_filtered_phase_39` | `LGBM` | 0.084302 | 0.104220 | 7.149 |
| `fft_y_Fw_filtered_ampl_40` | `LGBM` | 0.000041 | 0.000055 | 5.214 |
| `fft_y_Fw_filtered_phase_40` | `LGBM` | 0.057158 | 0.074020 | 110.852 |
| `fft_y_Fw_filtered_ampl_78` | `LGBM` | 0.000217 | 0.000261 | 75.142 |
| `fft_y_Fw_filtered_phase_78` | `LGBM` | 0.215241 | 0.402377 | 320.630 |
| `fft_y_Fw_filtered_ampl_81` | `LGBM` | 0.000027 | 0.000040 | 7.663 |
| `fft_y_Fw_filtered_phase_81` | `LGBM` | 0.152541 | 0.193985 | 21.500 |
| `fft_y_Fw_filtered_ampl_156` | `LGBM` | 0.000271 | 0.000349 | 272.671 |
| `fft_y_Fw_filtered_phase_156` | `LGBM` | 1.145289 | 1.423200 | 55.119 |
| `fft_y_Fw_filtered_ampl_162` | `LGBM` | 0.000441 | 0.001222 | 168.007 |
| `fft_y_Fw_filtered_phase_162` | `LGBM` | 0.782546 | 1.221094 | 33.491 |
| `fft_y_Fw_filtered_ampl_240` | `LGBM` | 0.000133 | 0.000199 | 71.955 |
| `fft_y_Fw_filtered_phase_240` | `LGBM` | 0.669456 | 1.268466 | 44.405 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/lgbm/2026-04-26_track1_forward_lgbm_original_dataset_mega_campaign/014_track1_original_dataset_forward_lgbm_attempt_14.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-11-15-18__track1_original_dataset_forward_lgbm_attempt_14_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-11-15-18__track1_original_dataset_forward_lgbm_attempt_14_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-11-15-18__track1_original_dataset_forward_lgbm_attempt_14_campaign_validation/validation_summary.yaml`
