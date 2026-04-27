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
- random seed: `21`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `17.893%`
- winning mean component MAE: `0.042603`
- winning mean component RMSE: `0.124659`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 17.893 | 0.042603 | 0.124659 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 12, 'estimator__min_samples_split': 2, 'estimator__n_estimators': 60}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `RF` | 0.002728 | 0.003338 | 54.933 |
| `fft_y_Bw_filtered_ampl_1` | `RF` | 0.000023 | 0.000031 | 0.137 |
| `fft_y_Bw_filtered_phase_1` | `RF` | 0.001645 | 0.002362 | 73.661 |
| `fft_y_Bw_filtered_ampl_3` | `RF` | 0.000025 | 0.000036 | 2.560 |
| `fft_y_Bw_filtered_phase_3` | `RF` | 0.022819 | 0.032920 | 1.711 |
| `fft_y_Bw_filtered_ampl_39` | `RF` | 0.000019 | 0.000027 | 4.454 |
| `fft_y_Bw_filtered_phase_39` | `RF` | 0.263800 | 1.064990 | 9.204 |
| `fft_y_Bw_filtered_ampl_40` | `RF` | 0.000030 | 0.000046 | 10.589 |
| `fft_y_Bw_filtered_phase_40` | `RF` | 0.095838 | 0.143190 | 50.872 |
| `fft_y_Bw_filtered_ampl_78` | `RF` | 0.000048 | 0.000066 | 5.913 |
| `fft_y_Bw_filtered_phase_78` | `RF` | 0.052924 | 0.108753 | 25.074 |
| `fft_y_Bw_filtered_ampl_81` | `RF` | 0.000011 | 0.000018 | 8.767 |
| `fft_y_Bw_filtered_phase_81` | `RF` | 0.081461 | 0.103032 | 32.534 |
| `fft_y_Bw_filtered_ampl_156` | `RF` | 0.000274 | 0.001123 | 9.323 |
| `fft_y_Bw_filtered_phase_156` | `RF` | 0.145724 | 0.596376 | 12.678 |
| `fft_y_Bw_filtered_ampl_162` | `RF` | 0.000071 | 0.000188 | 7.038 |
| `fft_y_Bw_filtered_phase_162` | `RF` | 0.050071 | 0.116132 | 2.809 |
| `fft_y_Bw_filtered_ampl_240` | `RF` | 0.000093 | 0.000232 | 13.955 |
| `fft_y_Bw_filtered_phase_240` | `RF` | 0.091852 | 0.195657 | 13.759 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/rf/2026-04-26_track1_backward_rf_original_dataset_mega_campaign/010_track1_original_dataset_backward_rf_attempt_10.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-22-22__track1_original_dataset_backward_rf_attempt_10_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-22-22__track1_original_dataset_backward_rf_attempt_10_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-22-22__track1_original_dataset_backward_rf_attempt_10_campaign_validation/validation_summary.yaml`
