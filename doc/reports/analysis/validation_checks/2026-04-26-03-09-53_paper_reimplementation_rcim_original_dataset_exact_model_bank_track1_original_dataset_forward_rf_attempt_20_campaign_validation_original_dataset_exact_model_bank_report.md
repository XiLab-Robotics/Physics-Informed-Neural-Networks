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
- random seed: `61`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `21.704%`
- winning mean component MAE: `0.076723`
- winning mean component RMSE: `0.167798`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 21.704 | 0.076723 | 0.167798 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 3, 'estimator__n_estimators': 50}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `RF` | 0.002911 | 0.003485 | 6.247 |
| `fft_y_Fw_filtered_ampl_1` | `RF` | 0.000029 | 0.000037 | 0.166 |
| `fft_y_Fw_filtered_phase_1` | `RF` | 0.002119 | 0.002756 | 38.830 |
| `fft_y_Fw_filtered_ampl_3` | `RF` | 0.000019 | 0.000027 | 2.385 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.020864 | 0.028110 | 1.169 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000025 | 0.000035 | 2.272 |
| `fft_y_Fw_filtered_phase_39` | `RF` | 0.021257 | 0.028739 | 1.753 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | 0.000026 | 0.000038 | 3.368 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.029974 | 0.048220 | 49.603 |
| `fft_y_Fw_filtered_ampl_78` | `RF` | 0.000049 | 0.000064 | 9.074 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.082751 | 0.202955 | 154.308 |
| `fft_y_Fw_filtered_ampl_81` | `RF` | 0.000010 | 0.000014 | 3.571 |
| `fft_y_Fw_filtered_phase_81` | `RF` | 0.053954 | 0.085865 | 5.469 |
| `fft_y_Fw_filtered_ampl_156` | `RF` | 0.000093 | 0.000285 | 31.394 |
| `fft_y_Fw_filtered_phase_156` | `RF` | 0.621034 | 1.241034 | 49.157 |
| `fft_y_Fw_filtered_ampl_162` | `RF` | 0.000073 | 0.000180 | 11.918 |
| `fft_y_Fw_filtered_phase_162` | `RF` | 0.324313 | 0.828505 | 12.201 |
| `fft_y_Fw_filtered_ampl_240` | `RF` | 0.000067 | 0.000193 | 13.952 |
| `fft_y_Fw_filtered_phase_240` | `RF` | 0.298176 | 0.717611 | 15.537 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/rf/2026-04-26_track1_forward_rf_original_dataset_mega_campaign/020_track1_original_dataset_forward_rf_attempt_20.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-06-44__track1_original_dataset_forward_rf_attempt_20_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-06-44__track1_original_dataset_forward_rf_attempt_20_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-06-44__track1_original_dataset_forward_rf_attempt_20_campaign_validation/validation_summary.yaml`
