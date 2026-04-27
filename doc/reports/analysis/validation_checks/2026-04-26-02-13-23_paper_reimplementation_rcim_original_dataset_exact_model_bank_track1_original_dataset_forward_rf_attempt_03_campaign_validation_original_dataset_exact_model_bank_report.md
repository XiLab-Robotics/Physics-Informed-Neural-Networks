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
- random seed: `7`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `17.376%`
- winning mean component MAE: `0.060119`
- winning mean component RMSE: `0.138490`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 17.376 | 0.060119 | 0.138490 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 12, 'estimator__min_samples_split': 4, 'estimator__n_estimators': 70}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `RF` | 0.003027 | 0.003587 | 5.799 |
| `fft_y_Fw_filtered_ampl_1` | `RF` | 0.000026 | 0.000035 | 0.151 |
| `fft_y_Fw_filtered_phase_1` | `RF` | 0.001933 | 0.002584 | 23.138 |
| `fft_y_Fw_filtered_ampl_3` | `RF` | 0.000020 | 0.000028 | 2.568 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.022266 | 0.030224 | 1.238 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000033 | 0.000043 | 2.803 |
| `fft_y_Fw_filtered_phase_39` | `RF` | 0.021399 | 0.029269 | 1.876 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | 0.000028 | 0.000044 | 3.440 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.036716 | 0.051726 | 56.535 |
| `fft_y_Fw_filtered_ampl_78` | `RF` | 0.000044 | 0.000066 | 9.060 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.077417 | 0.236561 | 101.480 |
| `fft_y_Fw_filtered_ampl_81` | `RF` | 0.000012 | 0.000016 | 4.189 |
| `fft_y_Fw_filtered_phase_81` | `RF` | 0.049194 | 0.065304 | 6.011 |
| `fft_y_Fw_filtered_ampl_156` | `RF` | 0.000097 | 0.000388 | 18.337 |
| `fft_y_Fw_filtered_phase_156` | `RF` | 0.465672 | 0.978222 | 52.730 |
| `fft_y_Fw_filtered_ampl_162` | `RF` | 0.000055 | 0.000164 | 8.323 |
| `fft_y_Fw_filtered_phase_162` | `RF` | 0.314751 | 0.807095 | 11.657 |
| `fft_y_Fw_filtered_ampl_240` | `RF` | 0.000030 | 0.000048 | 7.301 |
| `fft_y_Fw_filtered_phase_240` | `RF` | 0.149540 | 0.425903 | 13.503 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/rf/2026-04-26_track1_forward_rf_original_dataset_mega_campaign/003_track1_original_dataset_forward_rf_attempt_03.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-10-12__track1_original_dataset_forward_rf_attempt_03_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-10-12__track1_original_dataset_forward_rf_attempt_03_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-10-12__track1_original_dataset_forward_rf_attempt_03_campaign_validation/validation_summary.yaml`
