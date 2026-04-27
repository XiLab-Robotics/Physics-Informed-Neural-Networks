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
- random seed: `7`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `51.110%`
- winning mean component MAE: `0.144015`
- winning mean component RMSE: `0.213416`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 51.110 | 0.144015 | 0.213416 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 10, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `LGBM` | 0.006264 | 0.007717 | 14.076 |
| `fft_y_Fw_filtered_ampl_1` | `LGBM` | 0.000030 | 0.000040 | 0.174 |
| `fft_y_Fw_filtered_phase_1` | `LGBM` | 0.002311 | 0.003062 | 30.243 |
| `fft_y_Fw_filtered_ampl_3` | `LGBM` | 0.000052 | 0.000067 | 6.641 |
| `fft_y_Fw_filtered_phase_3` | `LGBM` | 0.050871 | 0.066018 | 2.865 |
| `fft_y_Fw_filtered_ampl_39` | `LGBM` | 0.000102 | 0.000122 | 9.407 |
| `fft_y_Fw_filtered_phase_39` | `LGBM` | 0.072273 | 0.094012 | 6.423 |
| `fft_y_Fw_filtered_ampl_40` | `LGBM` | 0.000045 | 0.000061 | 5.640 |
| `fft_y_Fw_filtered_phase_40` | `LGBM` | 0.052841 | 0.066654 | 147.539 |
| `fft_y_Fw_filtered_ampl_78` | `LGBM` | 0.000186 | 0.000231 | 57.882 |
| `fft_y_Fw_filtered_phase_78` | `LGBM` | 0.179233 | 0.369183 | 90.778 |
| `fft_y_Fw_filtered_ampl_81` | `LGBM` | 0.000024 | 0.000032 | 8.525 |
| `fft_y_Fw_filtered_phase_81` | `LGBM` | 0.156994 | 0.210262 | 31.759 |
| `fft_y_Fw_filtered_ampl_156` | `LGBM` | 0.000412 | 0.000978 | 234.616 |
| `fft_y_Fw_filtered_phase_156` | `LGBM` | 1.081093 | 1.380108 | 57.058 |
| `fft_y_Fw_filtered_ampl_162` | `LGBM` | 0.000495 | 0.001478 | 123.949 |
| `fft_y_Fw_filtered_phase_162` | `LGBM` | 0.834856 | 1.384667 | 40.032 |
| `fft_y_Fw_filtered_ampl_240` | `LGBM` | 0.000140 | 0.000258 | 51.547 |
| `fft_y_Fw_filtered_phase_240` | `LGBM` | 0.298069 | 0.469953 | 51.933 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/lgbm/2026-04-26_track1_forward_lgbm_original_dataset_mega_campaign/003_track1_original_dataset_forward_lgbm_attempt_03.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-07-11-20__track1_original_dataset_forward_lgbm_attempt_03_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-07-11-20__track1_original_dataset_forward_lgbm_attempt_03_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-07-11-20__track1_original_dataset_forward_lgbm_attempt_03_campaign_validation/validation_summary.yaml`
