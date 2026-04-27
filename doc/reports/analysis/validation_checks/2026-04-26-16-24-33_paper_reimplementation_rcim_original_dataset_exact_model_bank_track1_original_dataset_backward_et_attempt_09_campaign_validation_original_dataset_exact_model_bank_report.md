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

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `21.485%`
- winning mean component MAE: `0.058283`
- winning mean component RMSE: `0.147040`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 21.485 | 0.058283 | 0.147040 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 6}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.003218 | 0.004198 | 47.615 |
| `fft_y_Bw_filtered_ampl_1` | `ET` | 0.000026 | 0.000037 | 0.150 |
| `fft_y_Bw_filtered_phase_1` | `ET` | 0.002104 | 0.003258 | 54.912 |
| `fft_y_Bw_filtered_ampl_3` | `ET` | 0.000027 | 0.000043 | 2.771 |
| `fft_y_Bw_filtered_phase_3` | `ET` | 0.024513 | 0.037064 | 1.849 |
| `fft_y_Bw_filtered_ampl_39` | `ET` | 0.000022 | 0.000033 | 5.069 |
| `fft_y_Bw_filtered_phase_39` | `ET` | 0.307467 | 0.961648 | 10.668 |
| `fft_y_Bw_filtered_ampl_40` | `ET` | 0.000028 | 0.000037 | 9.140 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.095608 | 0.182875 | 29.597 |
| `fft_y_Bw_filtered_ampl_78` | `ET` | 0.000076 | 0.000103 | 10.896 |
| `fft_y_Bw_filtered_phase_78` | `ET` | 0.091734 | 0.190764 | 46.026 |
| `fft_y_Bw_filtered_ampl_81` | `ET` | 0.000012 | 0.000021 | 10.128 |
| `fft_y_Bw_filtered_phase_81` | `ET` | 0.142359 | 0.216522 | 110.637 |
| `fft_y_Bw_filtered_ampl_156` | `ET` | 0.000173 | 0.000697 | 9.014 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.117055 | 0.404169 | 10.263 |
| `fft_y_Bw_filtered_ampl_162` | `ET` | 0.000130 | 0.000347 | 11.918 |
| `fft_y_Bw_filtered_phase_162` | `ET` | 0.093379 | 0.281037 | 5.360 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000089 | 0.000150 | 16.760 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.229348 | 0.510765 | 15.437 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/et/2026-04-26_track1_backward_et_original_dataset_mega_campaign/009_track1_original_dataset_backward_et_attempt_09.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-23-46__track1_original_dataset_backward_et_attempt_09_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-23-46__track1_original_dataset_backward_et_attempt_09_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-23-46__track1_original_dataset_backward_et_attempt_09_campaign_validation/validation_summary.yaml`
