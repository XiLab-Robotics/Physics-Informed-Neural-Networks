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

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `66.612%`
- winning mean component MAE: `0.158411`
- winning mean component RMSE: `0.235048`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 66.612 | 0.158411 | 0.235048 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 10, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `LGBM` | 0.006583 | 0.007697 | 14.094 |
| `fft_y_Fw_filtered_ampl_1` | `LGBM` | 0.000036 | 0.000044 | 0.210 |
| `fft_y_Fw_filtered_phase_1` | `LGBM` | 0.002268 | 0.003229 | 41.342 |
| `fft_y_Fw_filtered_ampl_3` | `LGBM` | 0.000054 | 0.000064 | 6.834 |
| `fft_y_Fw_filtered_phase_3` | `LGBM` | 0.056156 | 0.067332 | 3.106 |
| `fft_y_Fw_filtered_ampl_39` | `LGBM` | 0.000113 | 0.000128 | 10.614 |
| `fft_y_Fw_filtered_phase_39` | `LGBM` | 0.080598 | 0.099595 | 6.802 |
| `fft_y_Fw_filtered_ampl_40` | `LGBM` | 0.000043 | 0.000055 | 5.103 |
| `fft_y_Fw_filtered_phase_40` | `LGBM` | 0.060284 | 0.081458 | 125.560 |
| `fft_y_Fw_filtered_ampl_78` | `LGBM` | 0.000206 | 0.000242 | 90.896 |
| `fft_y_Fw_filtered_phase_78` | `LGBM` | 0.166777 | 0.333748 | 464.366 |
| `fft_y_Fw_filtered_ampl_81` | `LGBM` | 0.000024 | 0.000030 | 8.003 |
| `fft_y_Fw_filtered_phase_81` | `LGBM` | 0.167154 | 0.210240 | 26.092 |
| `fft_y_Fw_filtered_ampl_156` | `LGBM` | 0.000327 | 0.000606 | 173.784 |
| `fft_y_Fw_filtered_phase_156` | `LGBM` | 1.340378 | 1.759795 | 64.970 |
| `fft_y_Fw_filtered_ampl_162` | `LGBM` | 0.000499 | 0.001672 | 120.360 |
| `fft_y_Fw_filtered_phase_162` | `LGBM` | 0.673565 | 0.988742 | 32.765 |
| `fft_y_Fw_filtered_ampl_240` | `LGBM` | 0.000168 | 0.000365 | 46.216 |
| `fft_y_Fw_filtered_phase_240` | `LGBM` | 0.454570 | 0.910872 | 24.521 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/lgbm/2026-04-26_track1_forward_lgbm_original_dataset_mega_campaign/005_track1_original_dataset_forward_lgbm_attempt_05.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-07-55-42__track1_original_dataset_forward_lgbm_attempt_05_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-07-55-42__track1_original_dataset_forward_lgbm_attempt_05_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-07-55-42__track1_original_dataset_forward_lgbm_attempt_05_campaign_validation/validation_summary.yaml`
