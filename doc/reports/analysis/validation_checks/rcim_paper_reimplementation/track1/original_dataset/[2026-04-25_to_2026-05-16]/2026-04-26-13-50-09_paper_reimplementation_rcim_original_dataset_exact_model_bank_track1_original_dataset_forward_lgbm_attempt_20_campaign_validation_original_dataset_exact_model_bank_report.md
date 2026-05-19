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
- random seed: `61`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `65.964%`
- winning mean component MAE: `0.157623`
- winning mean component RMSE: `0.230744`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 65.964 | 0.157623 | 0.230744 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 10, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `LGBM` | 0.006457 | 0.007624 | 15.240 |
| `fft_y_Fw_filtered_ampl_1` | `LGBM` | 0.000031 | 0.000040 | 0.179 |
| `fft_y_Fw_filtered_phase_1` | `LGBM` | 0.002283 | 0.002948 | 64.489 |
| `fft_y_Fw_filtered_ampl_3` | `LGBM` | 0.000058 | 0.000070 | 7.672 |
| `fft_y_Fw_filtered_phase_3` | `LGBM` | 0.052384 | 0.065733 | 2.989 |
| `fft_y_Fw_filtered_ampl_39` | `LGBM` | 0.000100 | 0.000118 | 9.958 |
| `fft_y_Fw_filtered_phase_39` | `LGBM` | 0.078466 | 0.098740 | 6.385 |
| `fft_y_Fw_filtered_ampl_40` | `LGBM` | 0.000039 | 0.000055 | 5.221 |
| `fft_y_Fw_filtered_phase_40` | `LGBM` | 0.056464 | 0.076543 | 180.227 |
| `fft_y_Fw_filtered_ampl_78` | `LGBM` | 0.000190 | 0.000237 | 55.572 |
| `fft_y_Fw_filtered_phase_78` | `LGBM` | 0.188939 | 0.304778 | 140.583 |
| `fft_y_Fw_filtered_ampl_81` | `LGBM` | 0.000024 | 0.000032 | 8.373 |
| `fft_y_Fw_filtered_phase_81` | `LGBM` | 0.130158 | 0.177617 | 18.556 |
| `fft_y_Fw_filtered_ampl_156` | `LGBM` | 0.000393 | 0.000923 | 365.541 |
| `fft_y_Fw_filtered_phase_156` | `LGBM` | 1.244387 | 1.634853 | 75.682 |
| `fft_y_Fw_filtered_ampl_162` | `LGBM` | 0.000370 | 0.000727 | 161.974 |
| `fft_y_Fw_filtered_phase_162` | `LGBM` | 0.705480 | 1.090639 | 31.506 |
| `fft_y_Fw_filtered_ampl_240` | `LGBM` | 0.000212 | 0.000475 | 70.238 |
| `fft_y_Fw_filtered_phase_240` | `LGBM` | 0.528401 | 0.921995 | 32.941 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/lgbm/2026-04-26_track1_forward_lgbm_original_dataset_mega_campaign/020_track1_original_dataset_forward_lgbm_attempt_20.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-28-13__track1_original_dataset_forward_lgbm_attempt_20_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-28-13__track1_original_dataset_forward_lgbm_attempt_20_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-28-13__track1_original_dataset_forward_lgbm_attempt_20_campaign_validation/validation_summary.yaml`
