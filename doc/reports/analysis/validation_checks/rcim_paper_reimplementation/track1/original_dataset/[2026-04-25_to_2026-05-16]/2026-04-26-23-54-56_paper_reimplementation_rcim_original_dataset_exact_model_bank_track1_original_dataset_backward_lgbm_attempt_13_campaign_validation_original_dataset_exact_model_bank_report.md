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
- random seed: `29`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `31.994%`
- winning mean component MAE: `0.072999`
- winning mean component RMSE: `0.151511`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 31.994 | 0.072999 | 0.151511 | `{'estimator__learning_rate': 0.2, 'estimator__max_depth': 10, 'estimator__num_leaves': 10, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `LGBM` | 0.002968 | 0.004259 | 80.058 |
| `fft_y_Bw_filtered_ampl_1` | `LGBM` | 0.000026 | 0.000037 | 0.152 |
| `fft_y_Bw_filtered_phase_1` | `LGBM` | 0.001697 | 0.002297 | 64.028 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000021 | 0.000034 | 2.302 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.023046 | 0.039225 | 1.694 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000018 | 0.000027 | 4.441 |
| `fft_y_Bw_filtered_phase_39` | `LGBM` | 0.335457 | 0.863963 | 12.085 |
| `fft_y_Bw_filtered_ampl_40` | `LGBM` | 0.000025 | 0.000039 | 8.317 |
| `fft_y_Bw_filtered_phase_40` | `LGBM` | 0.130258 | 0.241055 | 51.282 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000034 | 0.000056 | 4.363 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.075816 | 0.123900 | 26.512 |
| `fft_y_Bw_filtered_ampl_81` | `LGBM` | 0.000011 | 0.000018 | 8.321 |
| `fft_y_Bw_filtered_phase_81` | `LGBM` | 0.102774 | 0.162177 | 216.842 |
| `fft_y_Bw_filtered_ampl_156` | `LGBM` | 0.000376 | 0.001143 | 17.098 |
| `fft_y_Bw_filtered_phase_156` | `LGBM` | 0.194626 | 0.442563 | 21.111 |
| `fft_y_Bw_filtered_ampl_162` | `LGBM` | 0.000101 | 0.000182 | 19.423 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.117017 | 0.205837 | 7.328 |
| `fft_y_Bw_filtered_ampl_240` | `LGBM` | 0.000118 | 0.000220 | 32.958 |
| `fft_y_Bw_filtered_phase_240` | `LGBM` | 0.402591 | 0.791670 | 29.575 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/lgbm/2026-04-26_track1_backward_lgbm_original_dataset_mega_campaign/013_track1_original_dataset_backward_lgbm_attempt_13.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-23-33-03__track1_original_dataset_backward_lgbm_attempt_13_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-23-33-03__track1_original_dataset_backward_lgbm_attempt_13_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-23-33-03__track1_original_dataset_backward_lgbm_attempt_13_campaign_validation/validation_summary.yaml`
