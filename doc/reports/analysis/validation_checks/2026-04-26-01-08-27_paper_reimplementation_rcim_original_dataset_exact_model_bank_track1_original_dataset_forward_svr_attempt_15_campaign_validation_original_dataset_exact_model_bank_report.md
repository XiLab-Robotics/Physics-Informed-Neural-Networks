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
- random seed: `37`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `71.816%`
- winning mean component MAE: `0.132242`
- winning mean component RMSE: `0.236224`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 71.816 | 0.132242 | 0.236224 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | 0.002703 | 0.003421 | 5.494 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | 0.000047 | 0.000060 | 0.277 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | 0.002269 | 0.003057 | 116.903 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | 0.000155 | 0.000178 | 22.125 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | 0.031274 | 0.042220 | 1.749 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | 0.000147 | 0.000170 | 14.819 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | 0.022203 | 0.035756 | 1.849 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | 0.000110 | 0.000124 | 13.070 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.047537 | 0.068659 | 74.594 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | 0.000233 | 0.000300 | 27.258 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | 0.168506 | 0.299936 | 175.751 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | 0.000088 | 0.000099 | 32.727 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | 0.106668 | 0.163927 | 17.655 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | 0.000437 | 0.001094 | 147.478 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | 1.080526 | 1.562470 | 72.463 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | 0.000375 | 0.001589 | 119.681 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | 0.588861 | 1.297630 | 25.242 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | 0.000311 | 0.000472 | 94.504 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | 0.460142 | 1.007095 | 400.873 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/svr/2026-04-26_track1_forward_svr_original_dataset_mega_campaign/015_track1_original_dataset_forward_svr_attempt_15.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-07-24__track1_original_dataset_forward_svr_attempt_15_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-07-24__track1_original_dataset_forward_svr_attempt_15_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-07-24__track1_original_dataset_forward_svr_attempt_15_campaign_validation/validation_summary.yaml`
