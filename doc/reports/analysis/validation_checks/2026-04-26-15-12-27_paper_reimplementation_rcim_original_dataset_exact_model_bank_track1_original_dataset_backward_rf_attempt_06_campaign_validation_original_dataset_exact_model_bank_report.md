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
- random seed: `13`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `15.114%`
- winning mean component MAE: `0.055173`
- winning mean component RMSE: `0.140751`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 15.114 | 0.055173 | 0.140751 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 12, 'estimator__min_samples_split': 6, 'estimator__n_estimators': 70}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `RF` | 0.002763 | 0.003506 | 45.616 |
| `fft_y_Bw_filtered_ampl_1` | `RF` | 0.000026 | 0.000037 | 0.154 |
| `fft_y_Bw_filtered_phase_1` | `RF` | 0.001518 | 0.002302 | 35.393 |
| `fft_y_Bw_filtered_ampl_3` | `RF` | 0.000018 | 0.000026 | 1.830 |
| `fft_y_Bw_filtered_phase_3` | `RF` | 0.022061 | 0.030772 | 1.666 |
| `fft_y_Bw_filtered_ampl_39` | `RF` | 0.000019 | 0.000027 | 4.268 |
| `fft_y_Bw_filtered_phase_39` | `RF` | 0.153195 | 0.596752 | 5.343 |
| `fft_y_Bw_filtered_ampl_40` | `RF` | 0.000029 | 0.000042 | 9.250 |
| `fft_y_Bw_filtered_phase_40` | `RF` | 0.089245 | 0.121515 | 31.442 |
| `fft_y_Bw_filtered_ampl_78` | `RF` | 0.000049 | 0.000068 | 6.333 |
| `fft_y_Bw_filtered_phase_78` | `RF` | 0.065356 | 0.129346 | 22.313 |
| `fft_y_Bw_filtered_ampl_81` | `RF` | 0.000010 | 0.000015 | 7.650 |
| `fft_y_Bw_filtered_phase_81` | `RF` | 0.095115 | 0.128131 | 57.998 |
| `fft_y_Bw_filtered_ampl_156` | `RF` | 0.000174 | 0.000653 | 10.370 |
| `fft_y_Bw_filtered_phase_156` | `RF` | 0.125778 | 0.431991 | 9.862 |
| `fft_y_Bw_filtered_ampl_162` | `RF` | 0.000068 | 0.000155 | 7.154 |
| `fft_y_Bw_filtered_phase_162` | `RF` | 0.060355 | 0.127166 | 3.200 |
| `fft_y_Bw_filtered_ampl_240` | `RF` | 0.000087 | 0.000279 | 10.840 |
| `fft_y_Bw_filtered_phase_240` | `RF` | 0.432427 | 1.101487 | 16.487 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/rf/2026-04-26_track1_backward_rf_original_dataset_mega_campaign/006_track1_original_dataset_backward_rf_attempt_06.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-09-14__track1_original_dataset_backward_rf_attempt_06_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-09-14__track1_original_dataset_backward_rf_attempt_06_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-09-14__track1_original_dataset_backward_rf_attempt_06_campaign_validation/validation_summary.yaml`
