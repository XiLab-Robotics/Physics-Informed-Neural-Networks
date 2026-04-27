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
- random seed: `11`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `33.130%`
- winning mean component MAE: `0.063351`
- winning mean component RMSE: `0.212391`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 33.130 | 0.063351 | 0.212391 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 18, 'estimator__min_samples_split': 5}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.003862 | 0.005957 | 82.598 |
| `fft_y_Bw_filtered_ampl_1` | `DT` | 0.000032 | 0.000044 | 0.184 |
| `fft_y_Bw_filtered_phase_1` | `DT` | 0.002373 | 0.004055 | 160.847 |
| `fft_y_Bw_filtered_ampl_3` | `DT` | 0.000027 | 0.000042 | 2.722 |
| `fft_y_Bw_filtered_phase_3` | `DT` | 0.028498 | 0.053623 | 2.097 |
| `fft_y_Bw_filtered_ampl_39` | `DT` | 0.000022 | 0.000032 | 4.801 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.360498 | 1.389020 | 12.418 |
| `fft_y_Bw_filtered_ampl_40` | `DT` | 0.000037 | 0.000058 | 12.126 |
| `fft_y_Bw_filtered_phase_40` | `DT` | 0.098531 | 0.132990 | 164.714 |
| `fft_y_Bw_filtered_ampl_78` | `DT` | 0.000051 | 0.000072 | 5.125 |
| `fft_y_Bw_filtered_phase_78` | `DT` | 0.045850 | 0.078587 | 19.414 |
| `fft_y_Bw_filtered_ampl_81` | `DT` | 0.000011 | 0.000017 | 8.929 |
| `fft_y_Bw_filtered_phase_81` | `DT` | 0.124000 | 0.183083 | 77.028 |
| `fft_y_Bw_filtered_ampl_156` | `DT` | 0.000206 | 0.000771 | 14.010 |
| `fft_y_Bw_filtered_phase_156` | `DT` | 0.184008 | 0.699618 | 10.787 |
| `fft_y_Bw_filtered_ampl_162` | `DT` | 0.000058 | 0.000151 | 6.684 |
| `fft_y_Bw_filtered_phase_162` | `DT` | 0.140320 | 0.589437 | 8.257 |
| `fft_y_Bw_filtered_ampl_240` | `DT` | 0.000115 | 0.000311 | 15.997 |
| `fft_y_Bw_filtered_phase_240` | `DT` | 0.215177 | 0.897568 | 20.741 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/dt/2026-04-26_track1_backward_dt_original_dataset_mega_campaign/005_track1_original_dataset_backward_dt_attempt_05.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-02-06__track1_original_dataset_backward_dt_attempt_05_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-02-06__track1_original_dataset_backward_dt_attempt_05_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-16-02-06__track1_original_dataset_backward_dt_attempt_05_campaign_validation/validation_summary.yaml`
