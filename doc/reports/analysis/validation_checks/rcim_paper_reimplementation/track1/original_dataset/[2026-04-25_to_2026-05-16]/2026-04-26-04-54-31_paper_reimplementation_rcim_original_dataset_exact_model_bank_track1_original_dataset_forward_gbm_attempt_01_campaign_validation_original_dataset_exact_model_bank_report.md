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
- random seed: `0`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `26.976%`
- winning mean component MAE: `0.079069`
- winning mean component RMSE: `0.159335`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 26.976 | 0.079069 | 0.159335 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 14, 'estimator__min_samples_split': 14, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `GBM` | 0.003583 | 0.004366 | 7.858 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000032 | 0.000042 | 0.189 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.002137 | 0.002939 | 70.536 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000025 | 0.000034 | 3.275 |
| `fft_y_Fw_filtered_phase_3` | `GBM` | 0.022754 | 0.030332 | 1.251 |
| `fft_y_Fw_filtered_ampl_39` | `GBM` | 0.000041 | 0.000051 | 3.707 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.029935 | 0.046981 | 2.524 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000026 | 0.000034 | 3.414 |
| `fft_y_Fw_filtered_phase_40` | `GBM` | 0.042307 | 0.059302 | 53.237 |
| `fft_y_Fw_filtered_ampl_78` | `GBM` | 0.000067 | 0.000084 | 37.152 |
| `fft_y_Fw_filtered_phase_78` | `GBM` | 0.063682 | 0.098851 | 78.776 |
| `fft_y_Fw_filtered_ampl_81` | `GBM` | 0.000012 | 0.000016 | 4.201 |
| `fft_y_Fw_filtered_phase_81` | `GBM` | 0.074370 | 0.098150 | 7.722 |
| `fft_y_Fw_filtered_ampl_156` | `GBM` | 0.000146 | 0.000308 | 79.805 |
| `fft_y_Fw_filtered_phase_156` | `GBM` | 0.655901 | 1.115839 | 71.916 |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000168 | 0.000500 | 40.542 |
| `fft_y_Fw_filtered_phase_162` | `GBM` | 0.303925 | 0.757314 | 13.609 |
| `fft_y_Fw_filtered_ampl_240` | `GBM` | 0.000054 | 0.000104 | 18.061 |
| `fft_y_Fw_filtered_phase_240` | `GBM` | 0.303145 | 0.812120 | 14.772 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/gbm/2026-04-26_track1_forward_gbm_original_dataset_mega_campaign/001_track1_original_dataset_forward_gbm_attempt_01.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-52-32__track1_original_dataset_forward_gbm_attempt_01_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-52-32__track1_original_dataset_forward_gbm_attempt_01_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-04-52-32__track1_original_dataset_forward_gbm_attempt_01_campaign_validation/validation_summary.yaml`
