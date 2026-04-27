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
- random seed: `27`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `19.493%`
- winning mean component MAE: `0.065520`
- winning mean component RMSE: `0.118679`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 19.493 | 0.065520 | 0.118679 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 14, 'estimator__min_samples_split': 14, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `GBM` | 0.003492 | 0.004057 | 51.766 |
| `fft_y_Bw_filtered_ampl_1` | `GBM` | 0.000024 | 0.000035 | 0.142 |
| `fft_y_Bw_filtered_phase_1` | `GBM` | 0.001705 | 0.002382 | 27.761 |
| `fft_y_Bw_filtered_ampl_3` | `GBM` | 0.000032 | 0.000048 | 3.176 |
| `fft_y_Bw_filtered_phase_3` | `GBM` | 0.036743 | 0.045896 | 2.790 |
| `fft_y_Bw_filtered_ampl_39` | `GBM` | 0.000020 | 0.000027 | 4.480 |
| `fft_y_Bw_filtered_phase_39` | `GBM` | 0.377598 | 0.743388 | 13.812 |
| `fft_y_Bw_filtered_ampl_40` | `GBM` | 0.000028 | 0.000039 | 9.717 |
| `fft_y_Bw_filtered_phase_40` | `GBM` | 0.097029 | 0.136315 | 53.864 |
| `fft_y_Bw_filtered_ampl_78` | `GBM` | 0.000089 | 0.000107 | 13.983 |
| `fft_y_Bw_filtered_phase_78` | `GBM` | 0.057474 | 0.105414 | 23.475 |
| `fft_y_Bw_filtered_ampl_81` | `GBM` | 0.000010 | 0.000014 | 8.187 |
| `fft_y_Bw_filtered_phase_81` | `GBM` | 0.106574 | 0.141093 | 34.458 |
| `fft_y_Bw_filtered_ampl_156` | `GBM` | 0.000337 | 0.000879 | 27.521 |
| `fft_y_Bw_filtered_phase_156` | `GBM` | 0.134223 | 0.285889 | 9.682 |
| `fft_y_Bw_filtered_ampl_162` | `GBM` | 0.000143 | 0.000291 | 37.660 |
| `fft_y_Bw_filtered_phase_162` | `GBM` | 0.144736 | 0.219421 | 8.185 |
| `fft_y_Bw_filtered_ampl_240` | `GBM` | 0.000113 | 0.000293 | 17.293 |
| `fft_y_Bw_filtered_phase_240` | `GBM` | 0.284508 | 0.569318 | 22.417 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/gbm/2026-04-26_track1_backward_gbm_original_dataset_mega_campaign/012_track1_original_dataset_backward_gbm_attempt_12.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-59-43__track1_original_dataset_backward_gbm_attempt_12_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-59-43__track1_original_dataset_backward_gbm_attempt_12_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-59-43__track1_original_dataset_backward_gbm_attempt_12_campaign_validation/validation_summary.yaml`
