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
- random seed: `47`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `71.599%`
- winning mean component MAE: `0.166486`
- winning mean component RMSE: `0.251883`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 71.599 | 0.166486 | 0.251883 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 10, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `LGBM` | 0.007536 | 0.009386 | 32.623 |
| `fft_y_Fw_filtered_ampl_1` | `LGBM` | 0.000034 | 0.000042 | 0.198 |
| `fft_y_Fw_filtered_phase_1` | `LGBM` | 0.002943 | 0.004060 | 200.161 |
| `fft_y_Fw_filtered_ampl_3` | `LGBM` | 0.000060 | 0.000074 | 7.726 |
| `fft_y_Fw_filtered_phase_3` | `LGBM` | 0.060756 | 0.073055 | 3.405 |
| `fft_y_Fw_filtered_ampl_39` | `LGBM` | 0.000121 | 0.000142 | 11.494 |
| `fft_y_Fw_filtered_phase_39` | `LGBM` | 0.084180 | 0.107894 | 6.890 |
| `fft_y_Fw_filtered_ampl_40` | `LGBM` | 0.000042 | 0.000057 | 5.614 |
| `fft_y_Fw_filtered_phase_40` | `LGBM` | 0.071684 | 0.105650 | 284.530 |
| `fft_y_Fw_filtered_ampl_78` | `LGBM` | 0.000207 | 0.000245 | 41.199 |
| `fft_y_Fw_filtered_phase_78` | `LGBM` | 0.179800 | 0.280251 | 80.628 |
| `fft_y_Fw_filtered_ampl_81` | `LGBM` | 0.000024 | 0.000033 | 7.775 |
| `fft_y_Fw_filtered_phase_81` | `LGBM` | 0.164160 | 0.217815 | 20.271 |
| `fft_y_Fw_filtered_ampl_156` | `LGBM` | 0.000361 | 0.000910 | 194.515 |
| `fft_y_Fw_filtered_phase_156` | `LGBM` | 1.220801 | 1.555983 | 106.717 |
| `fft_y_Fw_filtered_ampl_162` | `LGBM` | 0.000468 | 0.001202 | 135.980 |
| `fft_y_Fw_filtered_phase_162` | `LGBM` | 0.767712 | 1.280841 | 38.556 |
| `fft_y_Fw_filtered_ampl_240` | `LGBM` | 0.000151 | 0.000290 | 102.031 |
| `fft_y_Fw_filtered_phase_240` | `LGBM` | 0.602187 | 1.147841 | 80.072 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/lgbm/2026-04-26_track1_forward_lgbm_original_dataset_mega_campaign/017_track1_original_dataset_forward_lgbm_attempt_17.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-12-21-40__track1_original_dataset_forward_lgbm_attempt_17_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-12-21-40__track1_original_dataset_forward_lgbm_attempt_17_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-12-21-40__track1_original_dataset_forward_lgbm_attempt_17_campaign_validation/validation_summary.yaml`
