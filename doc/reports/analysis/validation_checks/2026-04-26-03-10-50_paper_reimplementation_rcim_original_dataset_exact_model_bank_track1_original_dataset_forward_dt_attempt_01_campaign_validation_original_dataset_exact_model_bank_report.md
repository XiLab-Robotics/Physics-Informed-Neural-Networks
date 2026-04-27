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
- random seed: `0`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `20.288%`
- winning mean component MAE: `0.070122`
- winning mean component RMSE: `0.190089`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 20.288 | 0.070122 | 0.190089 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 6}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.003711 | 0.004906 | 7.521 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000037 | 0.000048 | 0.214 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.002394 | 0.003363 | 46.192 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000020 | 0.000028 | 2.518 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.025861 | 0.032416 | 1.421 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000037 | 0.000052 | 3.177 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.028812 | 0.045843 | 2.338 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000029 | 0.000045 | 3.709 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.041790 | 0.066380 | 70.130 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000053 | 0.000074 | 11.860 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.064524 | 0.135045 | 98.291 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000012 | 0.000017 | 4.076 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.065342 | 0.107003 | 5.842 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000109 | 0.000374 | 21.416 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.595276 | 1.396122 | 61.562 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000107 | 0.000548 | 8.236 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.241048 | 0.948770 | 10.000 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000054 | 0.000099 | 12.557 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.263092 | 0.870567 | 14.402 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/dt/2026-04-26_track1_forward_dt_original_dataset_mega_campaign/001_track1_original_dataset_forward_dt_attempt_01.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-10-01__track1_original_dataset_forward_dt_attempt_01_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-10-01__track1_original_dataset_forward_dt_attempt_01_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-03-10-01__track1_original_dataset_forward_dt_attempt_01_campaign_validation/validation_summary.yaml`
