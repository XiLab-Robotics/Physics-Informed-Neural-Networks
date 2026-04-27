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

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `21.137%`
- winning mean component MAE: `0.084942`
- winning mean component RMSE: `0.191470`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 21.137 | 0.084942 | 0.191470 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 6}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ET` | 0.003077 | 0.003702 | 5.991 |
| `fft_y_Fw_filtered_ampl_1` | `ET` | 0.000031 | 0.000039 | 0.178 |
| `fft_y_Fw_filtered_phase_1` | `ET` | 0.002519 | 0.003317 | 28.087 |
| `fft_y_Fw_filtered_ampl_3` | `ET` | 0.000026 | 0.000037 | 3.304 |
| `fft_y_Fw_filtered_phase_3` | `ET` | 0.029594 | 0.040091 | 1.655 |
| `fft_y_Fw_filtered_ampl_39` | `ET` | 0.000041 | 0.000057 | 3.535 |
| `fft_y_Fw_filtered_phase_39` | `ET` | 0.025656 | 0.038620 | 2.311 |
| `fft_y_Fw_filtered_ampl_40` | `ET` | 0.000029 | 0.000049 | 3.633 |
| `fft_y_Fw_filtered_phase_40` | `ET` | 0.054598 | 0.076970 | 69.904 |
| `fft_y_Fw_filtered_ampl_78` | `ET` | 0.000077 | 0.000108 | 13.299 |
| `fft_y_Fw_filtered_phase_78` | `ET` | 0.114345 | 0.343995 | 86.506 |
| `fft_y_Fw_filtered_ampl_81` | `ET` | 0.000016 | 0.000021 | 5.333 |
| `fft_y_Fw_filtered_phase_81` | `ET` | 0.077442 | 0.115113 | 9.294 |
| `fft_y_Fw_filtered_ampl_156` | `ET` | 0.000097 | 0.000331 | 20.362 |
| `fft_y_Fw_filtered_phase_156` | `ET` | 0.615217 | 1.178904 | 73.010 |
| `fft_y_Fw_filtered_ampl_162` | `ET` | 0.000079 | 0.000233 | 11.847 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.419639 | 1.101923 | 16.212 |
| `fft_y_Fw_filtered_ampl_240` | `ET` | 0.000097 | 0.000304 | 15.889 |
| `fft_y_Fw_filtered_phase_240` | `ET` | 0.271309 | 0.734109 | 31.256 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/et/2026-04-26_track1_forward_et_original_dataset_mega_campaign/003_track1_original_dataset_forward_et_attempt_03.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-30-39__track1_original_dataset_forward_et_attempt_03_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-30-39__track1_original_dataset_forward_et_attempt_03_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-30-39__track1_original_dataset_forward_et_attempt_03_campaign_validation/validation_summary.yaml`
