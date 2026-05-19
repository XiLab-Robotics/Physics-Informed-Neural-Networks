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

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `67.066%`
- winning mean component MAE: `0.148358`
- winning mean component RMSE: `0.216630`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 67.066 | 0.148358 | 0.216630 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.01, 'estimator__max_depth': 15, 'estimator__min_samples_split': 10, 'estimator__n_estimators': 84}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `GBM` | 0.007595 | 0.008877 | 17.816 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000033 | 0.000042 | 0.193 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.002458 | 0.003205 | 68.444 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000065 | 0.000077 | 8.643 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | 0.054489 | 0.065922 | 3.099 |
| `fft_y_Fw_filtered_ampl_39` | `GBM` | 0.000110 | 0.000129 | 11.022 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.090388 | 0.111255 | 7.341 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000038 | 0.000053 | 5.087 |
| `fft_y_Fw_filtered_phase_40` | `GBM` | 0.053501 | 0.074982 | 130.440 |
| `fft_y_Fw_filtered_ampl_78` | `GBM` | 0.000217 | 0.000265 | 63.691 |
| `fft_y_Fw_filtered_phase_78` | `GBM` | 0.185342 | 0.292119 | 152.934 |
| `fft_y_Fw_filtered_ampl_81` | `GBM` | 0.000023 | 0.000029 | 7.824 |
| `fft_y_Fw_filtered_phase_81` | `GBM` | 0.145838 | 0.187739 | 19.769 |
| `fft_y_Fw_filtered_ampl_156` | `GBM` | 0.000397 | 0.000782 | 414.343 |
| `fft_y_Fw_filtered_phase_156` | `GBM` | 1.161432 | 1.522257 | 62.354 |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000363 | 0.000674 | 181.521 |
| `fft_y_Fw_filtered_phase_162` | `GBM` | 0.692818 | 1.124557 | 29.957 |
| `fft_y_Fw_filtered_ampl_240` | `GBM` | 0.000161 | 0.000298 | 60.994 |
| `fft_y_Fw_filtered_phase_240` | `GBM` | 0.423534 | 0.722699 | 28.782 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/gbm/2026-04-26_track1_forward_gbm_original_dataset_mega_campaign/020_track1_original_dataset_forward_gbm_attempt_20.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-32-21__track1_original_dataset_forward_gbm_attempt_20_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-32-21__track1_original_dataset_forward_gbm_attempt_20_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-32-21__track1_original_dataset_forward_gbm_attempt_20_campaign_validation/validation_summary.yaml`
