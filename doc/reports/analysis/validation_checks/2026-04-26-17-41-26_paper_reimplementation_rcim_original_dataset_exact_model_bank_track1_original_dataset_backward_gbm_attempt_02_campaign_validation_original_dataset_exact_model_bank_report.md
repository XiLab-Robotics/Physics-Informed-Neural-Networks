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
- random seed: `5`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `21.887%`
- winning mean component MAE: `0.073378`
- winning mean component RMSE: `0.139324`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 21.887 | 0.073378 | 0.139324 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 15, 'estimator__min_samples_split': 12, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `GBM` | 0.003062 | 0.004173 | 60.993 |
| `fft_y_Bw_filtered_ampl_1` | `GBM` | 0.000028 | 0.000035 | 0.164 |
| `fft_y_Bw_filtered_phase_1` | `GBM` | 0.001804 | 0.002382 | 42.152 |
| `fft_y_Bw_filtered_ampl_3` | `GBM` | 0.000024 | 0.000034 | 2.371 |
| `fft_y_Bw_filtered_phase_3` | `GBM` | 0.035832 | 0.046777 | 2.875 |
| `fft_y_Bw_filtered_ampl_39` | `GBM` | 0.000023 | 0.000031 | 5.048 |
| `fft_y_Bw_filtered_phase_39` | `GBM` | 0.399908 | 0.697878 | 14.632 |
| `fft_y_Bw_filtered_ampl_40` | `GBM` | 0.000026 | 0.000037 | 8.640 |
| `fft_y_Bw_filtered_phase_40` | `GBM` | 0.099631 | 0.175328 | 40.335 |
| `fft_y_Bw_filtered_ampl_78` | `GBM` | 0.000105 | 0.000127 | 19.368 |
| `fft_y_Bw_filtered_phase_78` | `GBM` | 0.097718 | 0.206923 | 27.016 |
| `fft_y_Bw_filtered_ampl_81` | `GBM` | 0.000011 | 0.000016 | 8.770 |
| `fft_y_Bw_filtered_phase_81` | `GBM` | 0.098786 | 0.136101 | 31.574 |
| `fft_y_Bw_filtered_ampl_156` | `GBM` | 0.000179 | 0.000415 | 37.253 |
| `fft_y_Bw_filtered_phase_156` | `GBM` | 0.186634 | 0.542955 | 24.030 |
| `fft_y_Bw_filtered_ampl_162` | `GBM` | 0.000176 | 0.000397 | 50.338 |
| `fft_y_Bw_filtered_phase_162` | `GBM` | 0.150745 | 0.221780 | 8.162 |
| `fft_y_Bw_filtered_ampl_240` | `GBM` | 0.000087 | 0.000151 | 17.376 |
| `fft_y_Bw_filtered_phase_240` | `GBM` | 0.319395 | 0.611612 | 14.752 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/gbm/2026-04-26_track1_backward_gbm_original_dataset_mega_campaign/002_track1_original_dataset_backward_gbm_attempt_02.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-39-33__track1_original_dataset_backward_gbm_attempt_02_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-39-33__track1_original_dataset_backward_gbm_attempt_02_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-39-33__track1_original_dataset_backward_gbm_attempt_02_campaign_validation/validation_summary.yaml`
