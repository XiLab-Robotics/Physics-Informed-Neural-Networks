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

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `23.570%`
- winning mean component MAE: `0.054376`
- winning mean component RMSE: `0.169941`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 23.570 | 0.054376 | 0.169941 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 16, 'estimator__min_samples_split': 6}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.003084 | 0.004114 | 53.070 |
| `fft_y_Bw_filtered_ampl_1` | `DT` | 0.000030 | 0.000042 | 0.174 |
| `fft_y_Bw_filtered_phase_1` | `DT` | 0.002076 | 0.003409 | 165.501 |
| `fft_y_Bw_filtered_ampl_3` | `DT` | 0.000024 | 0.000033 | 2.421 |
| `fft_y_Bw_filtered_phase_3` | `DT` | 0.023358 | 0.032018 | 1.761 |
| `fft_y_Bw_filtered_ampl_39` | `DT` | 0.000022 | 0.000031 | 4.767 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.108630 | 0.621849 | 3.895 |
| `fft_y_Bw_filtered_ampl_40` | `DT` | 0.000029 | 0.000043 | 9.364 |
| `fft_y_Bw_filtered_phase_40` | `DT` | 0.125602 | 0.242547 | 51.708 |
| `fft_y_Bw_filtered_ampl_78` | `DT` | 0.000054 | 0.000072 | 6.771 |
| `fft_y_Bw_filtered_phase_78` | `DT` | 0.064407 | 0.129607 | 21.336 |
| `fft_y_Bw_filtered_ampl_81` | `DT` | 0.000013 | 0.000020 | 10.443 |
| `fft_y_Bw_filtered_phase_81` | `DT` | 0.100652 | 0.137112 | 60.440 |
| `fft_y_Bw_filtered_ampl_156` | `DT` | 0.000138 | 0.000434 | 8.596 |
| `fft_y_Bw_filtered_phase_156` | `DT` | 0.117530 | 0.629027 | 7.760 |
| `fft_y_Bw_filtered_ampl_162` | `DT` | 0.000084 | 0.000234 | 6.888 |
| `fft_y_Bw_filtered_phase_162` | `DT` | 0.056469 | 0.138172 | 3.014 |
| `fft_y_Bw_filtered_ampl_240` | `DT` | 0.000093 | 0.000197 | 13.291 |
| `fft_y_Bw_filtered_phase_240` | `DT` | 0.430852 | 1.289922 | 16.631 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/dt/2026-04-26_track1_backward_dt_original_dataset_mega_campaign/006_track1_original_dataset_backward_dt_attempt_06.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-03-01__track1_original_dataset_backward_dt_attempt_06_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-03-01__track1_original_dataset_backward_dt_attempt_06_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-03-01__track1_original_dataset_backward_dt_attempt_06_campaign_validation/validation_summary.yaml`
