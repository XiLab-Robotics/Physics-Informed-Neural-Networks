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
- random seed: `61`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `55.306%`
- winning mean component MAE: `0.148565`
- winning mean component RMSE: `0.264381`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 55.306 | 0.148565 | 0.264381 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | 0.002512 | 0.003052 | 5.202 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | 0.000062 | 0.000075 | 0.360 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | 0.002324 | 0.002972 | 41.048 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | 0.000164 | 0.000185 | 23.080 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | 0.032611 | 0.042502 | 1.838 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | 0.000206 | 0.000241 | 20.943 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | 0.019900 | 0.030717 | 1.686 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | 0.000087 | 0.000101 | 10.791 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.052550 | 0.084266 | 77.812 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | 0.000249 | 0.000311 | 30.920 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | 0.177284 | 0.281895 | 172.501 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | 0.000089 | 0.000100 | 32.949 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | 0.115317 | 0.178447 | 17.415 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | 0.000407 | 0.000951 | 239.806 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | 1.226108 | 1.751986 | 84.520 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | 0.000460 | 0.001557 | 129.927 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | 0.612750 | 1.400485 | 27.625 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | 0.000320 | 0.000632 | 90.367 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | 0.579334 | 1.242767 | 42.022 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/svr/2026-04-26_track1_forward_svr_original_dataset_mega_campaign/020_track1_original_dataset_forward_svr_attempt_20.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-13-33__track1_original_dataset_forward_svr_attempt_20_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-13-33__track1_original_dataset_forward_svr_attempt_20_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-13-33__track1_original_dataset_forward_svr_attempt_20_campaign_validation/validation_summary.yaml`
