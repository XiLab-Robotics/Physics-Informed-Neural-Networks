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
- random seed: `42`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `26.919%`
- winning mean component MAE: `0.065106`
- winning mean component RMSE: `0.118259`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 26.919 | 0.065106 | 0.118259 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 14, 'estimator__min_samples_split': 18, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `GBM` | 0.003538 | 0.004103 | 77.524 |
| `fft_y_Bw_filtered_ampl_1` | `GBM` | 0.000026 | 0.000036 | 0.150 |
| `fft_y_Bw_filtered_phase_1` | `GBM` | 0.001793 | 0.002469 | 41.115 |
| `fft_y_Bw_filtered_ampl_3` | `GBM` | 0.000028 | 0.000042 | 2.694 |
| `fft_y_Bw_filtered_phase_3` | `GBM` | 0.035699 | 0.044483 | 2.722 |
| `fft_y_Bw_filtered_ampl_39` | `GBM` | 0.000024 | 0.000035 | 5.306 |
| `fft_y_Bw_filtered_phase_39` | `GBM` | 0.433829 | 0.817876 | 15.512 |
| `fft_y_Bw_filtered_ampl_40` | `GBM` | 0.000031 | 0.000045 | 10.055 |
| `fft_y_Bw_filtered_phase_40` | `GBM` | 0.098981 | 0.167643 | 48.529 |
| `fft_y_Bw_filtered_ampl_78` | `GBM` | 0.000087 | 0.000108 | 17.519 |
| `fft_y_Bw_filtered_phase_78` | `GBM` | 0.071920 | 0.156570 | 49.199 |
| `fft_y_Bw_filtered_ampl_81` | `GBM` | 0.000011 | 0.000017 | 9.041 |
| `fft_y_Bw_filtered_phase_81` | `GBM` | 0.092831 | 0.122066 | 108.418 |
| `fft_y_Bw_filtered_ampl_156` | `GBM` | 0.000232 | 0.000750 | 30.103 |
| `fft_y_Bw_filtered_phase_156` | `GBM` | 0.129812 | 0.319953 | 10.828 |
| `fft_y_Bw_filtered_ampl_162` | `GBM` | 0.000146 | 0.000317 | 46.170 |
| `fft_y_Bw_filtered_phase_162` | `GBM` | 0.137624 | 0.198162 | 7.338 |
| `fft_y_Bw_filtered_ampl_240` | `GBM` | 0.000122 | 0.000427 | 16.947 |
| `fft_y_Bw_filtered_phase_240` | `GBM` | 0.230272 | 0.411820 | 12.292 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/gbm/2026-04-26_track1_backward_gbm_original_dataset_mega_campaign/016_track1_original_dataset_backward_gbm_attempt_16.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-07-51__track1_original_dataset_backward_gbm_attempt_16_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-07-51__track1_original_dataset_backward_gbm_attempt_16_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-07-51__track1_original_dataset_backward_gbm_attempt_16_campaign_validation/validation_summary.yaml`
