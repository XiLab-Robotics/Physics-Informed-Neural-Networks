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
- random seed: `31`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `26.447%`
- winning mean component MAE: `0.056545`
- winning mean component RMSE: `0.162243`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 26.447 | 0.056545 | 0.162243 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__min_samples_split': 3}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.003669 | 0.005084 | 44.344 |
| `fft_y_Bw_filtered_ampl_1` | `ET` | 0.000033 | 0.000047 | 0.195 |
| `fft_y_Bw_filtered_phase_1` | `ET` | 0.002101 | 0.003270 | 132.620 |
| `fft_y_Bw_filtered_ampl_3` | `ET` | 0.000035 | 0.000057 | 3.514 |
| `fft_y_Bw_filtered_phase_3` | `ET` | 0.028063 | 0.038028 | 2.055 |
| `fft_y_Bw_filtered_ampl_39` | `ET` | 0.000024 | 0.000035 | 5.733 |
| `fft_y_Bw_filtered_phase_39` | `ET` | 0.144537 | 0.697442 | 5.337 |
| `fft_y_Bw_filtered_ampl_40` | `ET` | 0.000030 | 0.000040 | 10.455 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.130297 | 0.228515 | 57.042 |
| `fft_y_Bw_filtered_ampl_78` | `ET` | 0.000075 | 0.000107 | 9.028 |
| `fft_y_Bw_filtered_phase_78` | `ET` | 0.089378 | 0.172516 | 39.060 |
| `fft_y_Bw_filtered_ampl_81` | `ET` | 0.000016 | 0.000027 | 13.117 |
| `fft_y_Bw_filtered_phase_81` | `ET` | 0.131000 | 0.195332 | 91.958 |
| `fft_y_Bw_filtered_ampl_156` | `ET` | 0.000150 | 0.000551 | 9.502 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.128390 | 0.444697 | 18.669 |
| `fft_y_Bw_filtered_ampl_162` | `ET` | 0.000062 | 0.000152 | 7.896 |
| `fft_y_Bw_filtered_phase_162` | `ET` | 0.123152 | 0.330219 | 5.739 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000146 | 0.000309 | 30.514 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.293204 | 0.966189 | 15.708 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/et/2026-04-26_track1_backward_et_original_dataset_mega_campaign/014_track1_original_dataset_backward_et_attempt_14.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-28-14__track1_original_dataset_backward_et_attempt_14_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-28-14__track1_original_dataset_backward_et_attempt_14_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-28-14__track1_original_dataset_backward_et_attempt_14_campaign_validation/validation_summary.yaml`
