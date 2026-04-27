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
- random seed: `7`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `19.948%`
- winning mean component MAE: `0.074401`
- winning mean component RMSE: `0.152369`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 19.948 | 0.074401 | 0.152369 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 15, 'estimator__min_samples_split': 16, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `GBM` | 0.003460 | 0.004308 | 46.488 |
| `fft_y_Bw_filtered_ampl_1` | `GBM` | 0.000026 | 0.000040 | 0.153 |
| `fft_y_Bw_filtered_phase_1` | `GBM` | 0.001533 | 0.002325 | 30.543 |
| `fft_y_Bw_filtered_ampl_3` | `GBM` | 0.000024 | 0.000036 | 2.502 |
| `fft_y_Bw_filtered_phase_3` | `GBM` | 0.028835 | 0.034693 | 2.171 |
| `fft_y_Bw_filtered_ampl_39` | `GBM` | 0.000020 | 0.000026 | 4.506 |
| `fft_y_Bw_filtered_phase_39` | `GBM` | 0.478607 | 1.078748 | 17.087 |
| `fft_y_Bw_filtered_ampl_40` | `GBM` | 0.000029 | 0.000042 | 9.317 |
| `fft_y_Bw_filtered_phase_40` | `GBM` | 0.087081 | 0.134991 | 35.489 |
| `fft_y_Bw_filtered_ampl_78` | `GBM` | 0.000090 | 0.000114 | 18.788 |
| `fft_y_Bw_filtered_phase_78` | `GBM` | 0.060360 | 0.104479 | 16.631 |
| `fft_y_Bw_filtered_ampl_81` | `GBM` | 0.000009 | 0.000011 | 7.148 |
| `fft_y_Bw_filtered_phase_81` | `GBM` | 0.087073 | 0.107968 | 52.208 |
| `fft_y_Bw_filtered_ampl_156` | `GBM` | 0.000343 | 0.001495 | 31.416 |
| `fft_y_Bw_filtered_phase_156` | `GBM` | 0.179149 | 0.493639 | 12.220 |
| `fft_y_Bw_filtered_ampl_162` | `GBM` | 0.000152 | 0.000414 | 40.275 |
| `fft_y_Bw_filtered_phase_162` | `GBM` | 0.143554 | 0.199423 | 7.728 |
| `fft_y_Bw_filtered_ampl_240` | `GBM` | 0.000147 | 0.000389 | 23.043 |
| `fft_y_Bw_filtered_phase_240` | `GBM` | 0.343129 | 0.731875 | 21.291 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/gbm/2026-04-26_track1_backward_gbm_original_dataset_mega_campaign/003_track1_original_dataset_backward_gbm_attempt_03.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-41-33__track1_original_dataset_backward_gbm_attempt_03_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-41-33__track1_original_dataset_backward_gbm_attempt_03_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-17-41-33__track1_original_dataset_backward_gbm_attempt_03_campaign_validation/validation_summary.yaml`
