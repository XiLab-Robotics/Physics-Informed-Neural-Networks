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

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `19.089%`
- winning mean component MAE: `0.096292`
- winning mean component RMSE: `0.220374`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 19.089 | 0.096292 | 0.220374 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 17, 'estimator__min_samples_split': 5}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ET` | 0.003140 | 0.003721 | 6.561 |
| `fft_y_Fw_filtered_ampl_1` | `ET` | 0.000028 | 0.000036 | 0.164 |
| `fft_y_Fw_filtered_phase_1` | `ET` | 0.002471 | 0.003406 | 28.789 |
| `fft_y_Fw_filtered_ampl_3` | `ET` | 0.000023 | 0.000032 | 2.886 |
| `fft_y_Fw_filtered_phase_3` | `ET` | 0.028718 | 0.039375 | 1.581 |
| `fft_y_Fw_filtered_ampl_39` | `ET` | 0.000038 | 0.000055 | 3.355 |
| `fft_y_Fw_filtered_phase_39` | `ET` | 0.034777 | 0.048798 | 2.947 |
| `fft_y_Fw_filtered_ampl_40` | `ET` | 0.000037 | 0.000062 | 4.769 |
| `fft_y_Fw_filtered_phase_40` | `ET` | 0.048040 | 0.080119 | 74.776 |
| `fft_y_Fw_filtered_ampl_78` | `ET` | 0.000060 | 0.000081 | 29.012 |
| `fft_y_Fw_filtered_phase_78` | `ET` | 0.120959 | 0.397758 | 54.277 |
| `fft_y_Fw_filtered_ampl_81` | `ET` | 0.000018 | 0.000026 | 5.993 |
| `fft_y_Fw_filtered_phase_81` | `ET` | 0.061169 | 0.081941 | 7.084 |
| `fft_y_Fw_filtered_ampl_156` | `ET` | 0.000086 | 0.000264 | 18.438 |
| `fft_y_Fw_filtered_phase_156` | `ET` | 0.927701 | 1.710069 | 63.531 |
| `fft_y_Fw_filtered_ampl_162` | `ET` | 0.000075 | 0.000227 | 9.339 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.350884 | 1.123438 | 12.891 |
| `fft_y_Fw_filtered_ampl_240` | `ET` | 0.000072 | 0.000118 | 22.930 |
| `fft_y_Fw_filtered_phase_240` | `ET` | 0.251260 | 0.697589 | 13.371 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/et/2026-04-26_track1_forward_et_original_dataset_mega_campaign/004_track1_original_dataset_forward_et_attempt_04.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-31-39__track1_original_dataset_forward_et_attempt_04_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-31-39__track1_original_dataset_forward_et_attempt_04_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-31-39__track1_original_dataset_forward_et_attempt_04_campaign_validation/validation_summary.yaml`
