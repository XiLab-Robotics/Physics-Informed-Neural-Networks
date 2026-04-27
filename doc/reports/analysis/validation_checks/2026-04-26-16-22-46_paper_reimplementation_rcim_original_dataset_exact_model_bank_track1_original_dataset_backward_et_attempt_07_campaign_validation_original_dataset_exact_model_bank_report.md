# Original-Dataset Exact RCIM Model Bank Validation Report

## Overview

This report covers the direction-specific exact-model-bank branch trained from the repository dataset under `data/datasets`.

- direction label: `backward`
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
- random seed: `15`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `23.756%`
- winning mean component MAE: `0.056658`
- winning mean component RMSE: `0.156515`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 23.756 | 0.056658 | 0.156515 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 5}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.003369 | 0.004544 | 36.640 |
| `fft_y_Bw_filtered_ampl_1` | `ET` | 0.000025 | 0.000034 | 0.145 |
| `fft_y_Bw_filtered_phase_1` | `ET` | 0.002166 | 0.003543 | 39.185 |
| `fft_y_Bw_filtered_ampl_3` | `ET` | 0.000034 | 0.000048 | 3.472 |
| `fft_y_Bw_filtered_phase_3` | `ET` | 0.030914 | 0.048161 | 2.323 |
| `fft_y_Bw_filtered_ampl_39` | `ET` | 0.000023 | 0.000031 | 5.378 |
| `fft_y_Bw_filtered_phase_39` | `ET` | 0.208237 | 0.785911 | 7.461 |
| `fft_y_Bw_filtered_ampl_40` | `ET` | 0.000025 | 0.000040 | 7.883 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.109067 | 0.194098 | 39.953 |
| `fft_y_Bw_filtered_ampl_78` | `ET` | 0.000064 | 0.000086 | 8.294 |
| `fft_y_Bw_filtered_phase_78` | `ET` | 0.077181 | 0.144953 | 20.137 |
| `fft_y_Bw_filtered_ampl_81` | `ET` | 0.000013 | 0.000019 | 10.008 |
| `fft_y_Bw_filtered_phase_81` | `ET` | 0.121973 | 0.169873 | 176.140 |
| `fft_y_Bw_filtered_ampl_156` | `ET` | 0.000079 | 0.000198 | 7.462 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.144714 | 0.632587 | 40.610 |
| `fft_y_Bw_filtered_ampl_162` | `ET` | 0.000155 | 0.000651 | 13.891 |
| `fft_y_Bw_filtered_phase_162` | `ET` | 0.091366 | 0.197617 | 5.767 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000101 | 0.000256 | 12.276 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.286996 | 0.791130 | 14.333 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/et/2026-04-26_track1_backward_et_original_dataset_mega_campaign/007_track1_original_dataset_backward_et_attempt_07.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-21-57__track1_original_dataset_backward_et_attempt_07_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-21-57__track1_original_dataset_backward_et_attempt_07_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-21-57__track1_original_dataset_backward_et_attempt_07_campaign_validation/validation_summary.yaml`
