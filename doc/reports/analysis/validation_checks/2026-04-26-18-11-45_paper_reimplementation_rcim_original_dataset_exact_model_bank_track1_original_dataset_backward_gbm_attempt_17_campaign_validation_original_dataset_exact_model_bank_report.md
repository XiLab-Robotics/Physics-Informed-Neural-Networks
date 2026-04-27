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
- random seed: `47`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `30.772%`
- winning mean component MAE: `0.073041`
- winning mean component RMSE: `0.138734`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 30.772 | 0.073041 | 0.138734 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 14, 'estimator__min_samples_split': 18, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `GBM` | 0.003403 | 0.004277 | 98.950 |
| `fft_y_Bw_filtered_ampl_1` | `GBM` | 0.000029 | 0.000038 | 0.169 |
| `fft_y_Bw_filtered_phase_1` | `GBM` | 0.002048 | 0.003047 | 124.354 |
| `fft_y_Bw_filtered_ampl_3` | `GBM` | 0.000024 | 0.000032 | 2.462 |
| `fft_y_Bw_filtered_phase_3` | `GBM` | 0.031201 | 0.042665 | 2.360 |
| `fft_y_Bw_filtered_ampl_39` | `GBM` | 0.000023 | 0.000031 | 5.360 |
| `fft_y_Bw_filtered_phase_39` | `GBM` | 0.437835 | 0.859371 | 16.114 |
| `fft_y_Bw_filtered_ampl_40` | `GBM` | 0.000032 | 0.000049 | 9.948 |
| `fft_y_Bw_filtered_phase_40` | `GBM` | 0.112745 | 0.209987 | 41.489 |
| `fft_y_Bw_filtered_ampl_78` | `GBM` | 0.000092 | 0.000112 | 15.028 |
| `fft_y_Bw_filtered_phase_78` | `GBM` | 0.069690 | 0.116034 | 66.790 |
| `fft_y_Bw_filtered_ampl_81` | `GBM` | 0.000013 | 0.000019 | 9.469 |
| `fft_y_Bw_filtered_phase_81` | `GBM` | 0.104437 | 0.148941 | 49.265 |
| `fft_y_Bw_filtered_ampl_156` | `GBM` | 0.000249 | 0.001084 | 31.446 |
| `fft_y_Bw_filtered_phase_156` | `GBM` | 0.189861 | 0.461418 | 26.534 |
| `fft_y_Bw_filtered_ampl_162` | `GBM` | 0.000241 | 0.000778 | 46.750 |
| `fft_y_Bw_filtered_phase_162` | `GBM` | 0.152833 | 0.221722 | 8.188 |
| `fft_y_Bw_filtered_ampl_240` | `GBM` | 0.000117 | 0.000390 | 16.266 |
| `fft_y_Bw_filtered_phase_240` | `GBM` | 0.282901 | 0.565946 | 13.734 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/gbm/2026-04-26_track1_backward_gbm_original_dataset_mega_campaign/017_track1_original_dataset_backward_gbm_attempt_17.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-09-52__track1_original_dataset_backward_gbm_attempt_17_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-09-52__track1_original_dataset_backward_gbm_attempt_17_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-09-52__track1_original_dataset_backward_gbm_attempt_17_campaign_validation/validation_summary.yaml`
