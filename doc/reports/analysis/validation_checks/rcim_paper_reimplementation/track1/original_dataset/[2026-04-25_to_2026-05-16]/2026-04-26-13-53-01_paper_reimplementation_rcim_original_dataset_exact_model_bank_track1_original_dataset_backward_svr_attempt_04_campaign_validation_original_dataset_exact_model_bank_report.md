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
- random seed: `9`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `59.766%`
- winning mean component MAE: `0.155917`
- winning mean component RMSE: `0.290287`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 59.766 | 0.155917 | 0.290287 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `SVR` | 0.002710 | 0.003314 | 60.439 |
| `fft_y_Bw_filtered_ampl_1` | `SVR` | 0.000164 | 0.000185 | 0.954 |
| `fft_y_Bw_filtered_phase_1` | `SVR` | 0.002354 | 0.003502 | 93.925 |
| `fft_y_Bw_filtered_ampl_3` | `SVR` | 0.000130 | 0.000149 | 14.548 |
| `fft_y_Bw_filtered_phase_3` | `SVR` | 0.026681 | 0.040537 | 1.946 |
| `fft_y_Bw_filtered_ampl_39` | `SVR` | 0.000114 | 0.000127 | 27.192 |
| `fft_y_Bw_filtered_phase_39` | `SVR` | 0.718449 | 1.216973 | 25.342 |
| `fft_y_Bw_filtered_ampl_40` | `SVR` | 0.000045 | 0.000058 | 14.606 |
| `fft_y_Bw_filtered_phase_40` | `SVR` | 0.180334 | 0.367653 | 32.885 |
| `fft_y_Bw_filtered_ampl_78` | `SVR` | 0.000152 | 0.000195 | 32.124 |
| `fft_y_Bw_filtered_phase_78` | `SVR` | 0.162029 | 0.274701 | 41.668 |
| `fft_y_Bw_filtered_ampl_81` | `SVR` | 0.000045 | 0.000049 | 41.258 |
| `fft_y_Bw_filtered_phase_81` | `SVR` | 0.154795 | 0.214212 | 418.601 |
| `fft_y_Bw_filtered_ampl_156` | `SVR` | 0.001067 | 0.003613 | 56.978 |
| `fft_y_Bw_filtered_phase_156` | `SVR` | 0.488200 | 0.828458 | 47.462 |
| `fft_y_Bw_filtered_ampl_162` | `SVR` | 0.000772 | 0.002307 | 114.617 |
| `fft_y_Bw_filtered_phase_162` | `SVR` | 0.389357 | 0.761919 | 20.802 |
| `fft_y_Bw_filtered_ampl_240` | `SVR` | 0.000509 | 0.001456 | 50.011 |
| `fft_y_Bw_filtered_phase_240` | `SVR` | 0.834510 | 1.796045 | 40.201 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/svr/2026-04-26_track1_backward_svr_original_dataset_mega_campaign/004_track1_original_dataset_backward_svr_attempt_04.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-52-22__track1_original_dataset_backward_svr_attempt_04_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-52-22__track1_original_dataset_backward_svr_attempt_04_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-52-22__track1_original_dataset_backward_svr_attempt_04_campaign_validation/validation_summary.yaml`
