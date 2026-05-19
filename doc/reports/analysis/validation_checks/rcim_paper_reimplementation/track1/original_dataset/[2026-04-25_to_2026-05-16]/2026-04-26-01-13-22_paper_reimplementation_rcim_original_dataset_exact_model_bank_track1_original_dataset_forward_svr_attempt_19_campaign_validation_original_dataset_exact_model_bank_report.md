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
- random seed: `59`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `83.481%`
- winning mean component MAE: `0.153618`
- winning mean component RMSE: `0.268801`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 83.481 | 0.153618 | 0.268801 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | 0.002652 | 0.003290 | 5.623 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | 0.000051 | 0.000065 | 0.295 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | 0.002540 | 0.003742 | 112.990 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | 0.000156 | 0.000179 | 21.222 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | 0.034083 | 0.042765 | 1.881 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | 0.000160 | 0.000189 | 14.659 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | 0.028850 | 0.047805 | 2.598 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | 0.000086 | 0.000100 | 10.477 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.062620 | 0.098066 | 142.137 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | 0.000233 | 0.000290 | 25.913 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | 0.200082 | 0.344281 | 212.666 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | 0.000091 | 0.000101 | 32.592 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | 0.123192 | 0.207529 | 16.057 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | 0.000336 | 0.000599 | 166.339 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | 1.293243 | 1.762833 | 94.526 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | 0.000371 | 0.001028 | 101.252 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | 0.656289 | 1.466444 | 28.518 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | 0.000276 | 0.000381 | 81.569 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | 0.513422 | 1.127542 | 514.831 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/svr/2026-04-26_track1_forward_svr_original_dataset_mega_campaign/019_track1_original_dataset_forward_svr_attempt_19.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-12-20__track1_original_dataset_forward_svr_attempt_19_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-12-20__track1_original_dataset_forward_svr_attempt_19_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-12-20__track1_original_dataset_forward_svr_attempt_19_campaign_validation/validation_summary.yaml`
