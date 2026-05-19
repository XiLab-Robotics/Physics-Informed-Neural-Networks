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
- random seed: `59`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `32.665%`
- winning mean component MAE: `0.080494`
- winning mean component RMSE: `0.178730`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 32.665 | 0.080494 | 0.178730 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 16, 'estimator__min_samples_split': 4, 'estimator__n_estimators': 90}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `RF` | 0.002963 | 0.003467 | 6.152 |
| `fft_y_Fw_filtered_ampl_1` | `RF` | 0.000027 | 0.000034 | 0.157 |
| `fft_y_Fw_filtered_phase_1` | `RF` | 0.002260 | 0.003387 | 51.331 |
| `fft_y_Fw_filtered_ampl_3` | `RF` | 0.000018 | 0.000027 | 2.191 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.022176 | 0.029846 | 1.228 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000031 | 0.000043 | 2.734 |
| `fft_y_Fw_filtered_phase_39` | `RF` | 0.026852 | 0.044788 | 2.295 |
| `fft_y_Fw_filtered_ampl_40` | `RF` | 0.000026 | 0.000037 | 3.241 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.041341 | 0.063502 | 107.262 |
| `fft_y_Fw_filtered_ampl_78` | `RF` | 0.000048 | 0.000073 | 7.410 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.087104 | 0.218148 | 47.961 |
| `fft_y_Fw_filtered_ampl_81` | `RF` | 0.000010 | 0.000014 | 3.226 |
| `fft_y_Fw_filtered_phase_81` | `RF` | 0.059798 | 0.095844 | 5.668 |
| `fft_y_Fw_filtered_ampl_156` | `RF` | 0.000053 | 0.000140 | 18.184 |
| `fft_y_Fw_filtered_phase_156` | `RF` | 0.486483 | 0.919330 | 39.006 |
| `fft_y_Fw_filtered_ampl_162` | `RF` | 0.000041 | 0.000110 | 8.110 |
| `fft_y_Fw_filtered_phase_162` | `RF` | 0.518562 | 1.296748 | 21.782 |
| `fft_y_Fw_filtered_ampl_240` | `RF` | 0.000035 | 0.000060 | 10.343 |
| `fft_y_Fw_filtered_phase_240` | `RF` | 0.281550 | 0.720278 | 282.360 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/rf/2026-04-26_track1_forward_rf_original_dataset_mega_campaign/019_track1_original_dataset_forward_rf_attempt_19.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-03-30__track1_original_dataset_forward_rf_attempt_19_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-03-30__track1_original_dataset_forward_rf_attempt_19_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-03-30__track1_original_dataset_forward_rf_attempt_19_campaign_validation/validation_summary.yaml`
