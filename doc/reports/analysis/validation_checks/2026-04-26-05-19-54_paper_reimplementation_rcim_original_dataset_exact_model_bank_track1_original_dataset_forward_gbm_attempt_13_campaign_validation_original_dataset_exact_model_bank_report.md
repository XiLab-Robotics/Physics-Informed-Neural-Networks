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
- random seed: `29`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `61.716%`
- winning mean component MAE: `0.153831`
- winning mean component RMSE: `0.235125`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 61.716 | 0.153831 | 0.235125 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.01, 'estimator__max_depth': 14, 'estimator__min_samples_split': 10, 'estimator__n_estimators': 84}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `GBM` | 0.008685 | 0.010748 | 35.532 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000033 | 0.000043 | 0.194 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.002318 | 0.002998 | 33.700 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000064 | 0.000077 | 8.525 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | 0.061893 | 0.073592 | 3.454 |
| `fft_y_Fw_filtered_ampl_39` | `GBM` | 0.000131 | 0.000154 | 12.848 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.091255 | 0.108278 | 7.674 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000044 | 0.000062 | 5.750 |
| `fft_y_Fw_filtered_phase_40` | `GBM` | 0.053449 | 0.085192 | 241.859 |
| `fft_y_Fw_filtered_ampl_78` | `GBM` | 0.000234 | 0.000273 | 61.780 |
| `fft_y_Fw_filtered_phase_78` | `GBM` | 0.203030 | 0.358601 | 120.136 |
| `fft_y_Fw_filtered_ampl_81` | `GBM` | 0.000023 | 0.000030 | 7.275 |
| `fft_y_Fw_filtered_phase_81` | `GBM` | 0.161118 | 0.204061 | 18.527 |
| `fft_y_Fw_filtered_ampl_156` | `GBM` | 0.000435 | 0.000787 | 222.785 |
| `fft_y_Fw_filtered_phase_156` | `GBM` | 1.051841 | 1.428758 | 50.464 |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000318 | 0.000665 | 157.757 |
| `fft_y_Fw_filtered_phase_162` | `GBM` | 0.866653 | 1.350096 | 37.796 |
| `fft_y_Fw_filtered_ampl_240` | `GBM` | 0.000169 | 0.000302 | 116.226 |
| `fft_y_Fw_filtered_phase_240` | `GBM` | 0.421105 | 0.842666 | 30.332 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/gbm/2026-04-26_track1_forward_gbm_original_dataset_mega_campaign/013_track1_original_dataset_forward_gbm_attempt_13.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-17-54__track1_original_dataset_forward_gbm_attempt_13_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-17-54__track1_original_dataset_forward_gbm_attempt_13_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-17-54__track1_original_dataset_forward_gbm_attempt_13_campaign_validation/validation_summary.yaml`
