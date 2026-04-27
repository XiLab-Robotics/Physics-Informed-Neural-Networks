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
- random seed: `61`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `14.734%`
- winning mean component MAE: `0.037705`
- winning mean component RMSE: `0.100180`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 14.734 | 0.037705 | 0.100180 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 12, 'estimator__min_samples_split': 2, 'estimator__n_estimators': 60}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `RF` | 0.002858 | 0.003423 | 35.333 |
| `fft_y_Bw_filtered_ampl_1` | `RF` | 0.000027 | 0.000039 | 0.156 |
| `fft_y_Bw_filtered_phase_1` | `RF` | 0.001700 | 0.002693 | 36.634 |
| `fft_y_Bw_filtered_ampl_3` | `RF` | 0.000020 | 0.000032 | 2.172 |
| `fft_y_Bw_filtered_phase_3` | `RF` | 0.021599 | 0.029551 | 1.587 |
| `fft_y_Bw_filtered_ampl_39` | `RF` | 0.000016 | 0.000023 | 3.612 |
| `fft_y_Bw_filtered_phase_39` | `RF` | 0.182081 | 0.737260 | 6.281 |
| `fft_y_Bw_filtered_ampl_40` | `RF` | 0.000029 | 0.000048 | 8.679 |
| `fft_y_Bw_filtered_phase_40` | `RF` | 0.093916 | 0.163242 | 35.648 |
| `fft_y_Bw_filtered_ampl_78` | `RF` | 0.000047 | 0.000063 | 5.603 |
| `fft_y_Bw_filtered_phase_78` | `RF` | 0.041551 | 0.072802 | 53.853 |
| `fft_y_Bw_filtered_ampl_81` | `RF` | 0.000009 | 0.000015 | 7.447 |
| `fft_y_Bw_filtered_phase_81` | `RF` | 0.080080 | 0.109336 | 36.106 |
| `fft_y_Bw_filtered_ampl_156` | `RF` | 0.000146 | 0.000490 | 10.783 |
| `fft_y_Bw_filtered_phase_156` | `RF` | 0.077096 | 0.235992 | 5.049 |
| `fft_y_Bw_filtered_ampl_162` | `RF` | 0.000070 | 0.000165 | 9.773 |
| `fft_y_Bw_filtered_phase_162` | `RF` | 0.074194 | 0.155634 | 4.564 |
| `fft_y_Bw_filtered_ampl_240` | `RF` | 0.000054 | 0.000144 | 7.743 |
| `fft_y_Bw_filtered_phase_240` | `RF` | 0.140905 | 0.392471 | 8.928 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/rf/2026-04-26_track1_backward_rf_original_dataset_mega_campaign/020_track1_original_dataset_backward_rf_attempt_20.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-55-07__track1_original_dataset_backward_rf_attempt_20_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-55-07__track1_original_dataset_backward_rf_attempt_20_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-55-07__track1_original_dataset_backward_rf_attempt_20_campaign_validation/validation_summary.yaml`
