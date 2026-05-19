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
- random seed: `9`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `26.199%`
- winning mean component MAE: `0.094022`
- winning mean component RMSE: `0.184129`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 26.199 | 0.094022 | 0.184129 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 14, 'estimator__min_samples_split': 18, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `GBM` | 0.003066 | 0.003555 | 6.626 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000025 | 0.000033 | 0.144 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.001947 | 0.002734 | 27.169 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000025 | 0.000032 | 3.269 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | 0.026709 | 0.035596 | 1.470 |
| `fft_y_Fw_filtered_ampl_39` | `GBM` | 0.000047 | 0.000059 | 4.281 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.029536 | 0.037133 | 2.574 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000027 | 0.000037 | 3.724 |
| `fft_y_Fw_filtered_phase_40` | `GBM` | 0.042946 | 0.066490 | 78.970 |
| `fft_y_Fw_filtered_ampl_78` | `GBM` | 0.000082 | 0.000106 | 50.153 |
| `fft_y_Fw_filtered_phase_78` | `GBM` | 0.124962 | 0.344927 | 73.727 |
| `fft_y_Fw_filtered_ampl_81` | `GBM` | 0.000013 | 0.000020 | 4.341 |
| `fft_y_Fw_filtered_phase_81` | `GBM` | 0.069057 | 0.090601 | 14.091 |
| `fft_y_Fw_filtered_ampl_156` | `GBM` | 0.000218 | 0.000548 | 80.037 |
| `fft_y_Fw_filtered_phase_156` | `GBM` | 0.571810 | 1.042473 | 31.116 |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000185 | 0.000581 | 47.888 |
| `fft_y_Fw_filtered_phase_162` | `GBM` | 0.576188 | 1.125488 | 24.521 |
| `fft_y_Fw_filtered_ampl_240` | `GBM` | 0.000072 | 0.000128 | 27.470 |
| `fft_y_Fw_filtered_phase_240` | `GBM` | 0.339509 | 0.747917 | 16.217 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/gbm/2026-04-26_track1_forward_gbm_original_dataset_mega_campaign/004_track1_original_dataset_forward_gbm_attempt_04.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-58-57__track1_original_dataset_forward_gbm_attempt_04_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-58-57__track1_original_dataset_forward_gbm_attempt_04_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-58-57__track1_original_dataset_forward_gbm_attempt_04_campaign_validation/validation_summary.yaml`
