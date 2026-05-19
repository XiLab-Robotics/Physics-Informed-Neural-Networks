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
- random seed: `59`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `28.324%`
- winning mean component MAE: `0.066512`
- winning mean component RMSE: `0.189302`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 28.324 | 0.066512 | 0.189302 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 4}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.003063 | 0.003912 | 77.757 |
| `fft_y_Bw_filtered_ampl_1` | `ET` | 0.000030 | 0.000042 | 0.174 |
| `fft_y_Bw_filtered_phase_1` | `ET` | 0.002580 | 0.004567 | 156.312 |
| `fft_y_Bw_filtered_ampl_3` | `ET` | 0.000030 | 0.000051 | 2.966 |
| `fft_y_Bw_filtered_phase_3` | `ET` | 0.027624 | 0.038475 | 2.084 |
| `fft_y_Bw_filtered_ampl_39` | `ET` | 0.000022 | 0.000036 | 5.097 |
| `fft_y_Bw_filtered_phase_39` | `ET` | 0.279612 | 1.116252 | 9.789 |
| `fft_y_Bw_filtered_ampl_40` | `ET` | 0.000033 | 0.000045 | 10.518 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.143458 | 0.279541 | 79.130 |
| `fft_y_Bw_filtered_ampl_78` | `ET` | 0.000073 | 0.000107 | 8.015 |
| `fft_y_Bw_filtered_phase_78` | `ET` | 0.068278 | 0.176419 | 15.772 |
| `fft_y_Bw_filtered_ampl_81` | `ET` | 0.000013 | 0.000021 | 11.027 |
| `fft_y_Bw_filtered_phase_81` | `ET` | 0.131492 | 0.183456 | 65.737 |
| `fft_y_Bw_filtered_ampl_156` | `ET` | 0.000179 | 0.000528 | 24.555 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.173451 | 0.580386 | 16.712 |
| `fft_y_Bw_filtered_ampl_162` | `ET` | 0.000057 | 0.000137 | 8.018 |
| `fft_y_Bw_filtered_phase_162` | `ET` | 0.147764 | 0.327671 | 8.968 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000108 | 0.000222 | 16.822 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.285868 | 0.884875 | 18.704 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/et/2026-04-26_track1_backward_et_original_dataset_mega_campaign/019_track1_original_dataset_backward_et_attempt_19.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-32-39__track1_original_dataset_backward_et_attempt_19_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-32-39__track1_original_dataset_backward_et_attempt_19_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-32-39__track1_original_dataset_backward_et_attempt_19_campaign_validation/validation_summary.yaml`
