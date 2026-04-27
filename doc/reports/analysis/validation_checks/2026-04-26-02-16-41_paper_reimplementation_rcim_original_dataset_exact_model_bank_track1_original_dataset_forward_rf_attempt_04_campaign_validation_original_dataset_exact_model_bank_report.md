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
- random seed: `9`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `15.782%`
- winning mean component MAE: `0.061703`
- winning mean component RMSE: `0.158390`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 15.782 | 0.061703 | 0.158390 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 13, 'estimator__min_samples_split': 2, 'estimator__n_estimators': 70}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `RF` | 0.002865 | 0.003520 | 5.876 |
| `fft_y_Fw_filtered_ampl_1` | `RF` | 0.000026 | 0.000035 | 0.153 |
| `fft_y_Fw_filtered_phase_1` | `RF` | 0.002008 | 0.002775 | 26.250 |
| `fft_y_Fw_filtered_ampl_3` | `RF` | 0.000020 | 0.000029 | 2.549 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.021446 | 0.029074 | 1.174 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000028 | 0.000039 | 2.467 |
| `fft_y_Fw_filtered_phase_39` | `RF` | 0.020196 | 0.027763 | 1.699 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | 0.000025 | 0.000041 | 3.340 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.036065 | 0.064443 | 56.105 |
| `fft_y_Fw_filtered_ampl_78` | `RF` | 0.000037 | 0.000050 | 20.859 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.110136 | 0.396604 | 88.095 |
| `fft_y_Fw_filtered_ampl_81` | `RF` | 0.000012 | 0.000017 | 3.838 |
| `fft_y_Fw_filtered_phase_81` | `RF` | 0.046356 | 0.060343 | 5.871 |
| `fft_y_Fw_filtered_ampl_156` | `RF` | 0.000067 | 0.000225 | 15.326 |
| `fft_y_Fw_filtered_phase_156` | `RF` | 0.388718 | 0.901870 | 24.017 |
| `fft_y_Fw_filtered_ampl_162` | `RF` | 0.000060 | 0.000240 | 7.751 |
| `fft_y_Fw_filtered_phase_162` | `RF` | 0.312192 | 0.873585 | 12.111 |
| `fft_y_Fw_filtered_ampl_240` | `RF` | 0.000038 | 0.000067 | 11.515 |
| `fft_y_Fw_filtered_phase_240` | `RF` | 0.232072 | 0.648684 | 10.866 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/rf/2026-04-26_track1_forward_rf_original_dataset_mega_campaign/004_track1_original_dataset_forward_rf_attempt_04.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-13-30__track1_original_dataset_forward_rf_attempt_04_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-13-30__track1_original_dataset_forward_rf_attempt_04_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-13-30__track1_original_dataset_forward_rf_attempt_04_campaign_validation/validation_summary.yaml`
