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
- random seed: `21`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `70.104%`
- winning mean component MAE: `0.154871`
- winning mean component RMSE: `0.232452`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 70.104 | 0.154871 | 0.232452 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 10, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `LGBM` | 0.006792 | 0.007923 | 16.129 |
| `fft_y_Fw_filtered_ampl_1` | `LGBM` | 0.000033 | 0.000041 | 0.190 |
| `fft_y_Fw_filtered_phase_1` | `LGBM` | 0.002583 | 0.003775 | 43.957 |
| `fft_y_Fw_filtered_ampl_3` | `LGBM` | 0.000066 | 0.000079 | 8.292 |
| `fft_y_Fw_filtered_phase_3` | `LGBM` | 0.054955 | 0.066866 | 3.056 |
| `fft_y_Fw_filtered_ampl_39` | `LGBM` | 0.000105 | 0.000123 | 9.974 |
| `fft_y_Fw_filtered_phase_39` | `LGBM` | 0.089633 | 0.116712 | 7.493 |
| `fft_y_Fw_filtered_ampl_40` | `LGBM` | 0.000038 | 0.000053 | 5.011 |
| `fft_y_Fw_filtered_phase_40` | `LGBM` | 0.058307 | 0.084884 | 280.067 |
| `fft_y_Fw_filtered_ampl_78` | `LGBM` | 0.000207 | 0.000248 | 52.579 |
| `fft_y_Fw_filtered_phase_78` | `LGBM` | 0.159470 | 0.275908 | 92.574 |
| `fft_y_Fw_filtered_ampl_81` | `LGBM` | 0.000024 | 0.000031 | 8.254 |
| `fft_y_Fw_filtered_phase_81` | `LGBM` | 0.156501 | 0.197230 | 20.653 |
| `fft_y_Fw_filtered_ampl_156` | `LGBM` | 0.000358 | 0.000687 | 193.297 |
| `fft_y_Fw_filtered_phase_156` | `LGBM` | 1.135998 | 1.479311 | 61.334 |
| `fft_y_Fw_filtered_ampl_162` | `LGBM` | 0.000399 | 0.000791 | 160.257 |
| `fft_y_Fw_filtered_phase_162` | `LGBM` | 0.714558 | 1.056643 | 35.332 |
| `fft_y_Fw_filtered_ampl_240` | `LGBM` | 0.000190 | 0.000369 | 47.093 |
| `fft_y_Fw_filtered_phase_240` | `LGBM` | 0.562330 | 1.124911 | 286.435 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/lgbm/2026-04-26_track1_forward_lgbm_original_dataset_mega_campaign/010_track1_original_dataset_forward_lgbm_attempt_10.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-09-46-31__track1_original_dataset_forward_lgbm_attempt_10_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-09-46-31__track1_original_dataset_forward_lgbm_attempt_10_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-09-46-31__track1_original_dataset_forward_lgbm_attempt_10_campaign_validation/validation_summary.yaml`
