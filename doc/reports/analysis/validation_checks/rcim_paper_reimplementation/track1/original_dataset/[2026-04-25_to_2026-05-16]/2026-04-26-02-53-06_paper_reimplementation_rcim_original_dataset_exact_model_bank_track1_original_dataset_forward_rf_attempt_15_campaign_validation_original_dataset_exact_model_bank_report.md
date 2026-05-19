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
- random seed: `37`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `27.425%`
- winning mean component MAE: `0.074327`
- winning mean component RMSE: `0.163370`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 27.425 | 0.074327 | 0.163370 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 5, 'estimator__n_estimators': 80}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `RF` | 0.002939 | 0.003528 | 6.015 |
| `fft_y_Fw_filtered_ampl_1` | `RF` | 0.000022 | 0.000029 | 0.126 |
| `fft_y_Fw_filtered_phase_1` | `RF` | 0.001900 | 0.002492 | 33.915 |
| `fft_y_Fw_filtered_ampl_3` | `RF` | 0.000018 | 0.000023 | 2.299 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.021952 | 0.029356 | 1.225 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000029 | 0.000038 | 2.696 |
| `fft_y_Fw_filtered_phase_39` | `RF` | 0.021360 | 0.031973 | 1.714 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | 0.000024 | 0.000037 | 2.998 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.034184 | 0.049503 | 52.791 |
| `fft_y_Fw_filtered_ampl_78` | `RF` | 0.000045 | 0.000061 | 8.887 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.084543 | 0.197396 | 166.084 |
| `fft_y_Fw_filtered_ampl_81` | `RF` | 0.000010 | 0.000014 | 3.268 |
| `fft_y_Fw_filtered_phase_81` | `RF` | 0.056307 | 0.081628 | 7.000 |
| `fft_y_Fw_filtered_ampl_156` | `RF` | 0.000124 | 0.000365 | 19.225 |
| `fft_y_Fw_filtered_phase_156` | `RF` | 0.580800 | 1.131982 | 34.478 |
| `fft_y_Fw_filtered_ampl_162` | `RF` | 0.000046 | 0.000143 | 9.058 |
| `fft_y_Fw_filtered_phase_162` | `RF` | 0.359779 | 0.943729 | 13.532 |
| `fft_y_Fw_filtered_ampl_240` | `RF` | 0.000034 | 0.000047 | 11.455 |
| `fft_y_Fw_filtered_phase_240` | `RF` | 0.248096 | 0.631681 | 144.313 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/rf/2026-04-26_track1_forward_rf_original_dataset_mega_campaign/015_track1_original_dataset_forward_rf_attempt_15.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-49-58__track1_original_dataset_forward_rf_attempt_15_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-49-58__track1_original_dataset_forward_rf_attempt_15_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-49-58__track1_original_dataset_forward_rf_attempt_15_campaign_validation/validation_summary.yaml`
