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
- random seed: `15`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `44.045%`
- winning mean component MAE: `0.152457`
- winning mean component RMSE: `0.284941`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 44.045 | 0.152457 | 0.284941 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `SVR` | 0.003129 | 0.004294 | 32.118 |
| `fft_y_Bw_filtered_ampl_1` | `SVR` | 0.000187 | 0.000199 | 1.090 |
| `fft_y_Bw_filtered_phase_1` | `SVR` | 0.002629 | 0.004092 | 141.997 |
| `fft_y_Bw_filtered_ampl_3` | `SVR` | 0.000127 | 0.000148 | 14.364 |
| `fft_y_Bw_filtered_phase_3` | `SVR` | 0.033577 | 0.056053 | 2.461 |
| `fft_y_Bw_filtered_ampl_39` | `SVR` | 0.000122 | 0.000137 | 31.236 |
| `fft_y_Bw_filtered_phase_39` | `SVR` | 0.791853 | 1.240854 | 28.094 |
| `fft_y_Bw_filtered_ampl_40` | `SVR` | 0.000044 | 0.000058 | 12.996 |
| `fft_y_Bw_filtered_phase_40` | `SVR` | 0.140144 | 0.287887 | 43.347 |
| `fft_y_Bw_filtered_ampl_78` | `SVR` | 0.000172 | 0.000200 | 29.918 |
| `fft_y_Bw_filtered_phase_78` | `SVR` | 0.166424 | 0.346731 | 33.648 |
| `fft_y_Bw_filtered_ampl_81` | `SVR` | 0.000037 | 0.000041 | 34.406 |
| `fft_y_Bw_filtered_phase_81` | `SVR` | 0.158251 | 0.228053 | 117.983 |
| `fft_y_Bw_filtered_ampl_156` | `SVR` | 0.000589 | 0.002750 | 55.202 |
| `fft_y_Bw_filtered_phase_156` | `SVR` | 0.496615 | 0.967550 | 50.138 |
| `fft_y_Bw_filtered_ampl_162` | `SVR` | 0.000750 | 0.002231 | 113.860 |
| `fft_y_Bw_filtered_phase_162` | `SVR` | 0.392668 | 0.752260 | 21.800 |
| `fft_y_Bw_filtered_ampl_240` | `SVR` | 0.000229 | 0.000406 | 35.127 |
| `fft_y_Bw_filtered_phase_240` | `SVR` | 0.709130 | 1.519941 | 37.067 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/svr/2026-04-26_track1_backward_svr_original_dataset_mega_campaign/007_track1_original_dataset_backward_svr_attempt_07.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-54-37__track1_original_dataset_backward_svr_attempt_07_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-54-37__track1_original_dataset_backward_svr_attempt_07_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-54-37__track1_original_dataset_backward_svr_attempt_07_campaign_validation/validation_summary.yaml`
