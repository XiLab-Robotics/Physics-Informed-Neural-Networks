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
- random seed: `42`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `63.025%`
- winning mean component MAE: `0.152480`
- winning mean component RMSE: `0.270712`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 63.025 | 0.152480 | 0.270712 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | 0.002715 | 0.003357 | 5.197 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | 0.000054 | 0.000070 | 0.315 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | 0.002111 | 0.002774 | 49.959 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | 0.000146 | 0.000167 | 18.964 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | 0.034044 | 0.043034 | 1.872 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | 0.000173 | 0.000202 | 16.802 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | 0.023709 | 0.034542 | 2.199 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | 0.000084 | 0.000099 | 10.792 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.058448 | 0.088345 | 53.196 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | 0.000152 | 0.000184 | 52.589 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | 0.194164 | 0.323668 | 135.261 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | 0.000090 | 0.000102 | 32.436 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | 0.115982 | 0.184940 | 13.584 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | 0.000350 | 0.000759 | 150.538 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | 1.228748 | 1.743525 | 54.848 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | 0.000480 | 0.001531 | 172.144 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | 0.703711 | 1.560137 | 30.535 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | 0.000262 | 0.000455 | 59.218 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | 0.531697 | 1.155634 | 337.016 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/forward_remote_micro/svr/2026-04-25_track1_forward_svr_remote_micro/001_track1_original_dataset_forward_svr_remote_micro.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_micro/2026-04-25-23-07-57__track1_original_dataset_forward_svr_remote_micro_campaign_run`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_micro/2026-04-25-23-07-57__track1_original_dataset_forward_svr_remote_micro_campaign_run/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_micro/2026-04-25-23-07-57__track1_original_dataset_forward_svr_remote_micro_campaign_run/validation_summary.yaml`
