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
- random seed: `23`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `52.186%`
- winning mean component MAE: `0.125739`
- winning mean component RMSE: `0.220456`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 52.186 | 0.125739 | 0.220456 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | 0.002714 | 0.003275 | 5.281 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | 0.000064 | 0.000077 | 0.371 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | 0.002070 | 0.002853 | 38.990 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | 0.000154 | 0.000175 | 21.039 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | 0.031564 | 0.039722 | 1.770 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | 0.000155 | 0.000186 | 15.243 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | 0.023189 | 0.037732 | 2.011 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | 0.000088 | 0.000105 | 11.383 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.054540 | 0.093640 | 90.490 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | 0.000343 | 0.000401 | 43.239 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | 0.190022 | 0.338774 | 161.750 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | 0.000093 | 0.000105 | 33.448 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | 0.108145 | 0.167269 | 15.211 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | 0.000337 | 0.000785 | 244.775 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | 1.182539 | 1.738354 | 54.492 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | 0.000558 | 0.001739 | 112.178 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | 0.398623 | 0.951085 | 19.316 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | 0.000294 | 0.000490 | 71.196 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | 0.393548 | 0.811905 | 49.345 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/svr/2026-04-26_track1_forward_svr_original_dataset_mega_campaign/011_track1_original_dataset_forward_svr_attempt_11.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-02-31__track1_original_dataset_forward_svr_attempt_11_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-02-31__track1_original_dataset_forward_svr_attempt_11_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-02-31__track1_original_dataset_forward_svr_attempt_11_campaign_validation/validation_summary.yaml`
