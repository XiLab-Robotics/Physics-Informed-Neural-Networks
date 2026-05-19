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
- random seed: `19`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `69.640%`
- winning mean component MAE: `0.138045`
- winning mean component RMSE: `0.251185`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 69.640 | 0.138045 | 0.251185 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | 0.003003 | 0.004627 | 18.360 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | 0.000050 | 0.000065 | 0.290 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | 0.002063 | 0.002885 | 101.188 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | 0.000153 | 0.000177 | 21.386 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | 0.034124 | 0.044637 | 1.884 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | 0.000083 | 0.000105 | 7.969 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | 0.022488 | 0.040636 | 1.920 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | 0.000087 | 0.000098 | 10.277 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.054610 | 0.086214 | 90.130 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | 0.000274 | 0.000339 | 36.670 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | 0.132166 | 0.189910 | 433.165 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | 0.000107 | 0.000117 | 40.510 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | 0.097120 | 0.157212 | 11.003 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | 0.000366 | 0.000802 | 184.636 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | 1.179911 | 1.697030 | 58.142 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | 0.000879 | 0.002850 | 148.467 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | 0.595671 | 1.412888 | 31.257 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | 0.000242 | 0.000426 | 78.711 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | 0.499465 | 1.131497 | 47.203 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/svr/2026-04-26_track1_forward_svr_original_dataset_mega_campaign/009_track1_original_dataset_forward_svr_attempt_09.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-00-06__track1_original_dataset_forward_svr_attempt_09_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-00-06__track1_original_dataset_forward_svr_attempt_09_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-00-06__track1_original_dataset_forward_svr_attempt_09_campaign_validation/validation_summary.yaml`
