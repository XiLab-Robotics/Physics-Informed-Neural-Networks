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
- random seed: `0`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `42.334%`
- winning mean component MAE: `0.146622`
- winning mean component RMSE: `0.258359`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 42.334 | 0.146622 | 0.258359 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `SVR` | 0.003004 | 0.003566 | 70.410 |
| `fft_y_Bw_filtered_ampl_1` | `SVR` | 0.000160 | 0.000175 | 0.933 |
| `fft_y_Bw_filtered_phase_1` | `SVR` | 0.001958 | 0.003021 | 36.838 |
| `fft_y_Bw_filtered_ampl_3` | `SVR` | 0.000125 | 0.000148 | 14.236 |
| `fft_y_Bw_filtered_phase_3` | `SVR` | 0.026642 | 0.036701 | 1.927 |
| `fft_y_Bw_filtered_ampl_39` | `SVR` | 0.000106 | 0.000121 | 27.510 |
| `fft_y_Bw_filtered_phase_39` | `SVR` | 0.871002 | 1.288625 | 30.767 |
| `fft_y_Bw_filtered_ampl_40` | `SVR` | 0.000040 | 0.000050 | 13.116 |
| `fft_y_Bw_filtered_phase_40` | `SVR` | 0.136013 | 0.257395 | 70.170 |
| `fft_y_Bw_filtered_ampl_78` | `SVR` | 0.000194 | 0.000213 | 26.281 |
| `fft_y_Bw_filtered_phase_78` | `SVR` | 0.145227 | 0.294639 | 71.103 |
| `fft_y_Bw_filtered_ampl_81` | `SVR` | 0.000046 | 0.000052 | 46.781 |
| `fft_y_Bw_filtered_phase_81` | `SVR` | 0.124313 | 0.169213 | 44.136 |
| `fft_y_Bw_filtered_ampl_156` | `SVR` | 0.000468 | 0.001076 | 53.858 |
| `fft_y_Bw_filtered_phase_156` | `SVR` | 0.452321 | 0.823076 | 50.877 |
| `fft_y_Bw_filtered_ampl_162` | `SVR` | 0.000659 | 0.002088 | 93.853 |
| `fft_y_Bw_filtered_phase_162` | `SVR` | 0.403123 | 0.720591 | 22.076 |
| `fft_y_Bw_filtered_ampl_240` | `SVR` | 0.000450 | 0.001250 | 60.448 |
| `fft_y_Bw_filtered_phase_240` | `SVR` | 0.619973 | 1.306816 | 69.028 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/svr/2026-04-26_track1_backward_svr_original_dataset_mega_campaign/001_track1_original_dataset_backward_svr_attempt_01.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-50-17__track1_original_dataset_backward_svr_attempt_01_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-50-17__track1_original_dataset_backward_svr_attempt_01_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-50-17__track1_original_dataset_backward_svr_attempt_01_campaign_validation/validation_summary.yaml`
