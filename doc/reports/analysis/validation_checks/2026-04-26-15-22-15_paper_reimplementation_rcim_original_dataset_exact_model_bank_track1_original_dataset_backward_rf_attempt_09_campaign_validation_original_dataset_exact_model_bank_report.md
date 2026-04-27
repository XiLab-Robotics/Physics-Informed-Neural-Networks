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
- random seed: `19`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `RF`
- winning estimator: `RandomForestRegressor`
- winning mean component MAPE: `16.936%`
- winning mean component MAE: `0.048060`
- winning mean component RMSE: `0.113606`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `RF` | `RandomForestRegressor` | 16.936 | 0.048060 | 0.113606 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 12, 'estimator__min_samples_split': 6, 'estimator__n_estimators': 50}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `RF` | 0.002990 | 0.004058 | 40.925 |
| `fft_y_Bw_filtered_ampl_1` | `RF` | 0.000023 | 0.000034 | 0.133 |
| `fft_y_Bw_filtered_phase_1` | `RF` | 0.001588 | 0.002186 | 49.483 |
| `fft_y_Bw_filtered_ampl_3` | `RF` | 0.000017 | 0.000023 | 1.738 |
| `fft_y_Bw_filtered_phase_3` | `RF` | 0.022829 | 0.035059 | 1.724 |
| `fft_y_Bw_filtered_ampl_39` | `RF` | 0.000018 | 0.000027 | 4.002 |
| `fft_y_Bw_filtered_phase_39` | `RF` | 0.318833 | 0.928829 | 10.797 |
| `fft_y_Bw_filtered_ampl_40` | `RF` | 0.000022 | 0.000031 | 7.420 |
| `fft_y_Bw_filtered_phase_40` | `RF` | 0.076186 | 0.141308 | 23.729 |
| `fft_y_Bw_filtered_ampl_78` | `RF` | 0.000049 | 0.000063 | 6.464 |
| `fft_y_Bw_filtered_phase_78` | `RF` | 0.046406 | 0.076069 | 40.506 |
| `fft_y_Bw_filtered_ampl_81` | `RF` | 0.000009 | 0.000014 | 8.330 |
| `fft_y_Bw_filtered_phase_81` | `RF` | 0.084855 | 0.129606 | 58.048 |
| `fft_y_Bw_filtered_ampl_156` | `RF` | 0.000146 | 0.000515 | 10.584 |
| `fft_y_Bw_filtered_phase_156` | `RF` | 0.095383 | 0.275789 | 18.611 |
| `fft_y_Bw_filtered_ampl_162` | `RF` | 0.000077 | 0.000221 | 8.447 |
| `fft_y_Bw_filtered_phase_162` | `RF` | 0.071051 | 0.150341 | 3.794 |
| `fft_y_Bw_filtered_ampl_240` | `RF` | 0.000057 | 0.000086 | 11.323 |
| `fft_y_Bw_filtered_phase_240` | `RF` | 0.192609 | 0.414259 | 15.720 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/rf/2026-04-26_track1_backward_rf_original_dataset_mega_campaign/009_track1_original_dataset_backward_rf_attempt_09.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-19-08__track1_original_dataset_backward_rf_attempt_09_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-19-08__track1_original_dataset_backward_rf_attempt_09_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-15-19-08__track1_original_dataset_backward_rf_attempt_09_campaign_validation/validation_summary.yaml`
