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
- random seed: `27`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `35.381%`
- winning mean component MAE: `0.146533`
- winning mean component RMSE: `0.262838`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 35.381 | 0.146533 | 0.262838 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `SVR` | 0.002654 | 0.003405 | 32.093 |
| `fft_y_Bw_filtered_ampl_1` | `SVR` | 0.000177 | 0.000189 | 1.036 |
| `fft_y_Bw_filtered_phase_1` | `SVR` | 0.002456 | 0.003814 | 61.910 |
| `fft_y_Bw_filtered_ampl_3` | `SVR` | 0.000127 | 0.000149 | 14.197 |
| `fft_y_Bw_filtered_phase_3` | `SVR` | 0.030238 | 0.041763 | 2.263 |
| `fft_y_Bw_filtered_ampl_39` | `SVR` | 0.000103 | 0.000117 | 24.893 |
| `fft_y_Bw_filtered_phase_39` | `SVR` | 0.610646 | 1.032919 | 21.937 |
| `fft_y_Bw_filtered_ampl_40` | `SVR` | 0.000046 | 0.000057 | 15.601 |
| `fft_y_Bw_filtered_phase_40` | `SVR` | 0.147898 | 0.306091 | 54.084 |
| `fft_y_Bw_filtered_ampl_78` | `SVR` | 0.000157 | 0.000182 | 27.145 |
| `fft_y_Bw_filtered_phase_78` | `SVR` | 0.108527 | 0.155910 | 42.400 |
| `fft_y_Bw_filtered_ampl_81` | `SVR` | 0.000045 | 0.000051 | 44.528 |
| `fft_y_Bw_filtered_phase_81` | `SVR` | 0.142131 | 0.179173 | 38.820 |
| `fft_y_Bw_filtered_ampl_156` | `SVR` | 0.000743 | 0.002698 | 45.519 |
| `fft_y_Bw_filtered_phase_156` | `SVR` | 0.552658 | 0.965170 | 42.050 |
| `fft_y_Bw_filtered_ampl_162` | `SVR` | 0.000427 | 0.001126 | 78.705 |
| `fft_y_Bw_filtered_phase_162` | `SVR` | 0.363456 | 0.645842 | 20.013 |
| `fft_y_Bw_filtered_ampl_240` | `SVR` | 0.000322 | 0.000985 | 39.339 |
| `fft_y_Bw_filtered_phase_240` | `SVR` | 0.821319 | 1.654279 | 65.705 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/svr/2026-04-26_track1_backward_svr_original_dataset_mega_campaign/012_track1_original_dataset_backward_svr_attempt_12.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-58-26__track1_original_dataset_backward_svr_attempt_12_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-58-26__track1_original_dataset_backward_svr_attempt_12_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-58-26__track1_original_dataset_backward_svr_attempt_12_campaign_validation/validation_summary.yaml`
