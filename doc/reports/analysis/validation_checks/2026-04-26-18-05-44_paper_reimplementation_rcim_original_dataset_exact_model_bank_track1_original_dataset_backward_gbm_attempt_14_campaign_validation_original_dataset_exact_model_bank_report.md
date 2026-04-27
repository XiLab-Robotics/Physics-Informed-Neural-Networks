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
- random seed: `31`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `28.496%`
- winning mean component MAE: `0.070061`
- winning mean component RMSE: `0.144328`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 28.496 | 0.070061 | 0.144328 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 15, 'estimator__min_samples_split': 10, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `GBM` | 0.003504 | 0.004467 | 63.129 |
| `fft_y_Bw_filtered_ampl_1` | `GBM` | 0.000028 | 0.000039 | 0.164 |
| `fft_y_Bw_filtered_phase_1` | `GBM` | 0.001890 | 0.003422 | 134.101 |
| `fft_y_Bw_filtered_ampl_3` | `GBM` | 0.000023 | 0.000040 | 2.484 |
| `fft_y_Bw_filtered_phase_3` | `GBM` | 0.037049 | 0.057097 | 2.627 |
| `fft_y_Bw_filtered_ampl_39` | `GBM` | 0.000019 | 0.000027 | 4.754 |
| `fft_y_Bw_filtered_phase_39` | `GBM` | 0.372600 | 0.674494 | 13.952 |
| `fft_y_Bw_filtered_ampl_40` | `GBM` | 0.000025 | 0.000034 | 8.991 |
| `fft_y_Bw_filtered_phase_40` | `GBM` | 0.096105 | 0.184949 | 32.070 |
| `fft_y_Bw_filtered_ampl_78` | `GBM` | 0.000094 | 0.000118 | 21.201 |
| `fft_y_Bw_filtered_phase_78` | `GBM` | 0.076813 | 0.144311 | 33.707 |
| `fft_y_Bw_filtered_ampl_81` | `GBM` | 0.000011 | 0.000019 | 8.060 |
| `fft_y_Bw_filtered_phase_81` | `GBM` | 0.114081 | 0.174405 | 56.800 |
| `fft_y_Bw_filtered_ampl_156` | `GBM` | 0.000190 | 0.000316 | 37.611 |
| `fft_y_Bw_filtered_phase_156` | `GBM` | 0.138919 | 0.394558 | 22.772 |
| `fft_y_Bw_filtered_ampl_162` | `GBM` | 0.000169 | 0.000423 | 52.994 |
| `fft_y_Bw_filtered_phase_162` | `GBM` | 0.164278 | 0.281985 | 8.248 |
| `fft_y_Bw_filtered_ampl_240` | `GBM` | 0.000070 | 0.000099 | 21.863 |
| `fft_y_Bw_filtered_phase_240` | `GBM` | 0.325285 | 0.821422 | 15.891 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/gbm/2026-04-26_track1_backward_gbm_original_dataset_mega_campaign/014_track1_original_dataset_backward_gbm_attempt_14.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-03-51__track1_original_dataset_backward_gbm_attempt_14_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-03-51__track1_original_dataset_backward_gbm_attempt_14_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-03-51__track1_original_dataset_backward_gbm_attempt_14_campaign_validation/validation_summary.yaml`
