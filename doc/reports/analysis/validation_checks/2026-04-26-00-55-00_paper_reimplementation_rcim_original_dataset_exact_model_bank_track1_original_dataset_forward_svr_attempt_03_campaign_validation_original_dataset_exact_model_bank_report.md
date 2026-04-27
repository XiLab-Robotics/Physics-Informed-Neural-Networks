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
- random seed: `7`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `56.383%`
- winning mean component MAE: `0.143375`
- winning mean component RMSE: `0.244211`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 56.383 | 0.143375 | 0.244211 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | 0.002402 | 0.002961 | 4.377 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | 0.000053 | 0.000067 | 0.310 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | 0.002206 | 0.003018 | 25.041 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | 0.000146 | 0.000169 | 19.644 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | 0.036544 | 0.046229 | 2.042 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | 0.000174 | 0.000206 | 15.888 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | 0.022015 | 0.034281 | 2.056 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | 0.000078 | 0.000097 | 9.431 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.051397 | 0.068775 | 65.235 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | 0.000302 | 0.000364 | 37.710 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | 0.183835 | 0.367142 | 266.041 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | 0.000091 | 0.000105 | 33.751 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | 0.123091 | 0.187332 | 23.460 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | 0.000434 | 0.001068 | 161.651 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | 1.193739 | 1.679336 | 100.611 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | 0.000651 | 0.002168 | 135.241 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | 0.784533 | 1.741682 | 34.888 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | 0.000286 | 0.000528 | 64.275 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | 0.322142 | 0.504478 | 69.631 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/svr/2026-04-26_track1_forward_svr_original_dataset_mega_campaign/003_track1_original_dataset_forward_svr_attempt_03.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-00-54-06__track1_original_dataset_forward_svr_attempt_03_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-00-54-06__track1_original_dataset_forward_svr_attempt_03_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-00-54-06__track1_original_dataset_forward_svr_attempt_03_campaign_validation/validation_summary.yaml`
