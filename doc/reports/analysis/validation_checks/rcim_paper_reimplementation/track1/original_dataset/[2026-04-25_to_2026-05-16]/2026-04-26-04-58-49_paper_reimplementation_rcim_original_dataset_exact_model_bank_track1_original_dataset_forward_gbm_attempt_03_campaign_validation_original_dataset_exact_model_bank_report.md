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

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `53.161%`
- winning mean component MAE: `0.141883`
- winning mean component RMSE: `0.205451`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 53.161 | 0.141883 | 0.205451 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.01, 'estimator__max_depth': 14, 'estimator__min_samples_split': 18, 'estimator__n_estimators': 84}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `GBM` | 0.007328 | 0.008908 | 16.471 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000031 | 0.000040 | 0.180 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.002311 | 0.002990 | 31.160 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000059 | 0.000075 | 7.427 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | 0.053309 | 0.068173 | 2.992 |
| `fft_y_Fw_filtered_ampl_39` | `GBM` | 0.000111 | 0.000134 | 10.247 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.084640 | 0.106394 | 7.454 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000045 | 0.000061 | 5.706 |
| `fft_y_Fw_filtered_phase_40` | `GBM` | 0.050921 | 0.063544 | 138.212 |
| `fft_y_Fw_filtered_ampl_78` | `GBM` | 0.000214 | 0.000263 | 66.151 |
| `fft_y_Fw_filtered_phase_78` | `GBM` | 0.184857 | 0.357668 | 96.767 |
| `fft_y_Fw_filtered_ampl_81` | `GBM` | 0.000023 | 0.000030 | 8.254 |
| `fft_y_Fw_filtered_phase_81` | `GBM` | 0.163426 | 0.217863 | 31.086 |
| `fft_y_Fw_filtered_ampl_156` | `GBM` | 0.000427 | 0.000911 | 255.963 |
| `fft_y_Fw_filtered_phase_156` | `GBM` | 1.049411 | 1.320424 | 60.767 |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000399 | 0.001106 | 133.693 |
| `fft_y_Fw_filtered_phase_162` | `GBM` | 0.809434 | 1.292132 | 37.310 |
| `fft_y_Fw_filtered_ampl_240` | `GBM` | 0.000154 | 0.000265 | 54.854 |
| `fft_y_Fw_filtered_phase_240` | `GBM` | 0.288683 | 0.462585 | 45.363 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/gbm/2026-04-26_track1_forward_gbm_original_dataset_mega_campaign/003_track1_original_dataset_forward_gbm_attempt_03.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-56-47__track1_original_dataset_forward_gbm_attempt_03_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-56-47__track1_original_dataset_forward_gbm_attempt_03_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-56-47__track1_original_dataset_forward_gbm_attempt_03_campaign_validation/validation_summary.yaml`
