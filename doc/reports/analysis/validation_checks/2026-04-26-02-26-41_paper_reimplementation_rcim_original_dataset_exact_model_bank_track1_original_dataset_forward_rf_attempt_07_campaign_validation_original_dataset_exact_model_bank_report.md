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
- random seed: `15`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `15.426%`
- winning mean component MAE: `0.070632`
- winning mean component RMSE: `0.167474`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 15.426 | 0.070632 | 0.167474 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 5, 'estimator__n_estimators': 60}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `RF` | 0.003152 | 0.004741 | 18.756 |
| `fft_y_Fw_filtered_ampl_1` | `RF` | 0.000028 | 0.000038 | 0.162 |
| `fft_y_Fw_filtered_phase_1` | `RF` | 0.002137 | 0.003108 | 30.734 |
| `fft_y_Fw_filtered_ampl_3` | `RF` | 0.000020 | 0.000028 | 2.602 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.023937 | 0.030548 | 1.338 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000034 | 0.000046 | 3.061 |
| `fft_y_Fw_filtered_phase_39` | `RF` | 0.028050 | 0.047810 | 2.231 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | 0.000027 | 0.000041 | 3.580 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.041763 | 0.070602 | 62.699 |
| `fft_y_Fw_filtered_ampl_78` | `RF` | 0.000045 | 0.000062 | 21.800 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.096079 | 0.360807 | 43.198 |
| `fft_y_Fw_filtered_ampl_81` | `RF` | 0.000010 | 0.000014 | 3.296 |
| `fft_y_Fw_filtered_phase_81` | `RF` | 0.059357 | 0.087307 | 6.256 |
| `fft_y_Fw_filtered_ampl_156` | `RF` | 0.000060 | 0.000234 | 14.817 |
| `fft_y_Fw_filtered_phase_156` | `RF` | 0.537697 | 1.002677 | 31.867 |
| `fft_y_Fw_filtered_ampl_162` | `RF` | 0.000071 | 0.000282 | 11.066 |
| `fft_y_Fw_filtered_phase_162` | `RF` | 0.282345 | 0.812628 | 13.040 |
| `fft_y_Fw_filtered_ampl_240` | `RF` | 0.000035 | 0.000053 | 10.509 |
| `fft_y_Fw_filtered_phase_240` | `RF` | 0.267161 | 0.760980 | 12.091 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/rf/2026-04-26_track1_forward_rf_original_dataset_mega_campaign/007_track1_original_dataset_forward_rf_attempt_07.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-23-32__track1_original_dataset_forward_rf_attempt_07_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-23-32__track1_original_dataset_forward_rf_attempt_07_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-02-23-32__track1_original_dataset_forward_rf_attempt_07_campaign_validation/validation_summary.yaml`
