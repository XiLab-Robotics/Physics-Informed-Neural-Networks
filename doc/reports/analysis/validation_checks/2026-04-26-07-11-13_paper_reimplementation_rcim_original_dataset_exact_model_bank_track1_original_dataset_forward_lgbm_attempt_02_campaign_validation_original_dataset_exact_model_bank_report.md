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

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `82.415%`
- winning mean component MAE: `0.166185`
- winning mean component RMSE: `0.249480`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 82.415 | 0.166185 | 0.249480 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 11, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `LGBM` | 0.007714 | 0.009209 | 31.244 |
| `fft_y_Fw_filtered_ampl_1` | `LGBM` | 0.000030 | 0.000040 | 0.176 |
| `fft_y_Fw_filtered_phase_1` | `LGBM` | 0.002977 | 0.004172 | 107.180 |
| `fft_y_Fw_filtered_ampl_3` | `LGBM` | 0.000066 | 0.000081 | 7.940 |
| `fft_y_Fw_filtered_phase_3` | `LGBM` | 0.060511 | 0.072101 | 3.295 |
| `fft_y_Fw_filtered_ampl_39` | `LGBM` | 0.000119 | 0.000141 | 10.828 |
| `fft_y_Fw_filtered_phase_39` | `LGBM` | 0.096967 | 0.120394 | 8.613 |
| `fft_y_Fw_filtered_ampl_40` | `LGBM` | 0.000046 | 0.000066 | 5.821 |
| `fft_y_Fw_filtered_phase_40` | `LGBM` | 0.075334 | 0.106277 | 241.153 |
| `fft_y_Fw_filtered_ampl_78` | `LGBM` | 0.000233 | 0.000279 | 53.011 |
| `fft_y_Fw_filtered_phase_78` | `LGBM` | 0.208383 | 0.318999 | 134.898 |
| `fft_y_Fw_filtered_ampl_81` | `LGBM` | 0.000031 | 0.000041 | 9.704 |
| `fft_y_Fw_filtered_phase_81` | `LGBM` | 0.178249 | 0.225480 | 29.851 |
| `fft_y_Fw_filtered_ampl_156` | `LGBM` | 0.000297 | 0.000455 | 192.751 |
| `fft_y_Fw_filtered_phase_156` | `LGBM` | 1.064613 | 1.399904 | 54.419 |
| `fft_y_Fw_filtered_ampl_162` | `LGBM` | 0.000407 | 0.000866 | 149.764 |
| `fft_y_Fw_filtered_phase_162` | `LGBM` | 0.830481 | 1.301103 | 43.527 |
| `fft_y_Fw_filtered_ampl_240` | `LGBM` | 0.000128 | 0.000205 | 36.528 |
| `fft_y_Fw_filtered_phase_240` | `LGBM` | 0.630935 | 1.180308 | 445.178 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/lgbm/2026-04-26_track1_forward_lgbm_original_dataset_mega_campaign/002_track1_original_dataset_forward_lgbm_attempt_02.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-49-14__track1_original_dataset_forward_lgbm_attempt_02_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-49-14__track1_original_dataset_forward_lgbm_attempt_02_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-49-14__track1_original_dataset_forward_lgbm_attempt_02_campaign_validation/validation_summary.yaml`
