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
- random seed: `29`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `59.021%`
- winning mean component MAE: `0.152869`
- winning mean component RMSE: `0.274015`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 59.021 | 0.152869 | 0.274015 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | 0.003018 | 0.005026 | 19.749 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | 0.000057 | 0.000073 | 0.333 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | 0.002233 | 0.002930 | 26.657 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | 0.000164 | 0.000182 | 22.973 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | 0.031485 | 0.039920 | 1.737 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | 0.000332 | 0.000367 | 34.920 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | 0.023664 | 0.035585 | 1.997 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | 0.000101 | 0.000115 | 12.440 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.057959 | 0.094946 | 147.927 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | 0.000246 | 0.000320 | 29.852 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | 0.177490 | 0.327587 | 200.405 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | 0.000086 | 0.000097 | 30.187 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | 0.113461 | 0.168226 | 13.298 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | 0.000441 | 0.000950 | 166.815 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | 1.277042 | 1.828277 | 93.661 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | 0.000428 | 0.001441 | 109.830 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | 0.721515 | 1.502536 | 31.298 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | 0.000330 | 0.000515 | 132.522 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | 0.494455 | 1.197197 | 44.802 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/svr/2026-04-26_track1_forward_svr_original_dataset_mega_campaign/013_track1_original_dataset_forward_svr_attempt_13.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-04-57__track1_original_dataset_forward_svr_attempt_13_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-04-57__track1_original_dataset_forward_svr_attempt_13_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-04-57__track1_original_dataset_forward_svr_attempt_13_campaign_validation/validation_summary.yaml`
