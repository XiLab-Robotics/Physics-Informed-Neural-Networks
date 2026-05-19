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
- random seed: `29`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `33.789%`
- winning mean component MAE: `0.080281`
- winning mean component RMSE: `0.172875`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 33.789 | 0.080281 | 0.172875 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 16, 'estimator__min_samples_split': 18, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `GBM` | 0.003947 | 0.005072 | 128.111 |
| `fft_y_Bw_filtered_ampl_1` | `GBM` | 0.000025 | 0.000038 | 0.147 |
| `fft_y_Bw_filtered_phase_1` | `GBM` | 0.001749 | 0.002458 | 78.215 |
| `fft_y_Bw_filtered_ampl_3` | `GBM` | 0.000029 | 0.000045 | 3.090 |
| `fft_y_Bw_filtered_phase_3` | `GBM` | 0.034516 | 0.048856 | 2.544 |
| `fft_y_Bw_filtered_ampl_39` | `GBM` | 0.000024 | 0.000038 | 5.537 |
| `fft_y_Bw_filtered_phase_39` | `GBM` | 0.420366 | 0.903318 | 15.535 |
| `fft_y_Bw_filtered_ampl_40` | `GBM` | 0.000027 | 0.000040 | 8.754 |
| `fft_y_Bw_filtered_phase_40` | `GBM` | 0.127933 | 0.247764 | 30.293 |
| `fft_y_Bw_filtered_ampl_78` | `GBM` | 0.000100 | 0.000122 | 17.849 |
| `fft_y_Bw_filtered_phase_78` | `GBM` | 0.080847 | 0.148357 | 24.783 |
| `fft_y_Bw_filtered_ampl_81` | `GBM` | 0.000011 | 0.000018 | 8.367 |
| `fft_y_Bw_filtered_phase_81` | `GBM` | 0.104239 | 0.166097 | 166.295 |
| `fft_y_Bw_filtered_ampl_156` | `GBM` | 0.000358 | 0.001286 | 31.625 |
| `fft_y_Bw_filtered_phase_156` | `GBM` | 0.222592 | 0.642949 | 19.271 |
| `fft_y_Bw_filtered_ampl_162` | `GBM` | 0.000138 | 0.000279 | 44.906 |
| `fft_y_Bw_filtered_phase_162` | `GBM` | 0.159938 | 0.205738 | 8.618 |
| `fft_y_Bw_filtered_ampl_240` | `GBM` | 0.000086 | 0.000137 | 20.203 |
| `fft_y_Bw_filtered_phase_240` | `GBM` | 0.368418 | 0.912018 | 27.839 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/gbm/2026-04-26_track1_backward_gbm_original_dataset_mega_campaign/013_track1_original_dataset_backward_gbm_attempt_13.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-01-47__track1_original_dataset_backward_gbm_attempt_13_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-01-47__track1_original_dataset_backward_gbm_attempt_13_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-01-47__track1_original_dataset_backward_gbm_attempt_13_campaign_validation/validation_summary.yaml`
