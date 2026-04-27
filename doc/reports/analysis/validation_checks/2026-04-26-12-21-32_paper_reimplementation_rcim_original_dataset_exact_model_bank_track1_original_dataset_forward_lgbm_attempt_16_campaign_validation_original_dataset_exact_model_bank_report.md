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
- random seed: `42`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `61.771%`
- winning mean component MAE: `0.150914`
- winning mean component RMSE: `0.225755`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 61.771 | 0.150914 | 0.225755 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 11, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `LGBM` | 0.006732 | 0.007933 | 14.250 |
| `fft_y_Fw_filtered_ampl_1` | `LGBM` | 0.000032 | 0.000041 | 0.189 |
| `fft_y_Fw_filtered_phase_1` | `LGBM` | 0.002348 | 0.003029 | 192.051 |
| `fft_y_Fw_filtered_ampl_3` | `LGBM` | 0.000055 | 0.000067 | 6.549 |
| `fft_y_Fw_filtered_phase_3` | `LGBM` | 0.052640 | 0.065780 | 2.926 |
| `fft_y_Fw_filtered_ampl_39` | `LGBM` | 0.000100 | 0.000119 | 9.030 |
| `fft_y_Fw_filtered_phase_39` | `LGBM` | 0.079444 | 0.100502 | 7.134 |
| `fft_y_Fw_filtered_ampl_40` | `LGBM` | 0.000044 | 0.000062 | 6.055 |
| `fft_y_Fw_filtered_phase_40` | `LGBM` | 0.061053 | 0.081971 | 67.445 |
| `fft_y_Fw_filtered_ampl_78` | `LGBM` | 0.000214 | 0.000251 | 57.267 |
| `fft_y_Fw_filtered_phase_78` | `LGBM` | 0.186120 | 0.376964 | 92.590 |
| `fft_y_Fw_filtered_ampl_81` | `LGBM` | 0.000025 | 0.000033 | 8.271 |
| `fft_y_Fw_filtered_phase_81` | `LGBM` | 0.150071 | 0.192903 | 17.781 |
| `fft_y_Fw_filtered_ampl_156` | `LGBM` | 0.000326 | 0.000673 | 166.105 |
| `fft_y_Fw_filtered_phase_156` | `LGBM` | 1.096784 | 1.324593 | 47.538 |
| `fft_y_Fw_filtered_ampl_162` | `LGBM` | 0.000367 | 0.000957 | 148.161 |
| `fft_y_Fw_filtered_phase_162` | `LGBM` | 0.729756 | 1.253654 | 34.726 |
| `fft_y_Fw_filtered_ampl_240` | `LGBM` | 0.000114 | 0.000203 | 33.989 |
| `fft_y_Fw_filtered_phase_240` | `LGBM` | 0.501136 | 0.879606 | 261.584 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/lgbm/2026-04-26_track1_forward_lgbm_original_dataset_mega_campaign/016_track1_original_dataset_forward_lgbm_attempt_16.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-11-59-33__track1_original_dataset_forward_lgbm_attempt_16_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-11-59-33__track1_original_dataset_forward_lgbm_attempt_16_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-11-59-33__track1_original_dataset_forward_lgbm_attempt_16_campaign_validation/validation_summary.yaml`
