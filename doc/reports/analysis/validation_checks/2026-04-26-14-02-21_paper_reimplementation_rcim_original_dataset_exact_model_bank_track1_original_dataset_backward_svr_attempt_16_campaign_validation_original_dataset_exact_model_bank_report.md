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
- random seed: `42`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `49.181%`
- winning mean component MAE: `0.143685`
- winning mean component RMSE: `0.263964`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 49.181 | 0.143685 | 0.263964 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `SVR` | 0.003093 | 0.003633 | 49.027 |
| `fft_y_Bw_filtered_ampl_1` | `SVR` | 0.000177 | 0.000189 | 1.034 |
| `fft_y_Bw_filtered_phase_1` | `SVR` | 0.002253 | 0.003381 | 127.465 |
| `fft_y_Bw_filtered_ampl_3` | `SVR` | 0.000133 | 0.000156 | 14.042 |
| `fft_y_Bw_filtered_phase_3` | `SVR` | 0.027370 | 0.038563 | 2.022 |
| `fft_y_Bw_filtered_ampl_39` | `SVR` | 0.000092 | 0.000107 | 21.937 |
| `fft_y_Bw_filtered_phase_39` | `SVR` | 0.831744 | 1.306017 | 28.753 |
| `fft_y_Bw_filtered_ampl_40` | `SVR` | 0.000047 | 0.000058 | 15.574 |
| `fft_y_Bw_filtered_phase_40` | `SVR` | 0.172796 | 0.326678 | 62.317 |
| `fft_y_Bw_filtered_ampl_78` | `SVR` | 0.000226 | 0.000261 | 36.281 |
| `fft_y_Bw_filtered_phase_78` | `SVR` | 0.135615 | 0.243569 | 64.326 |
| `fft_y_Bw_filtered_ampl_81` | `SVR` | 0.000042 | 0.000047 | 40.319 |
| `fft_y_Bw_filtered_phase_81` | `SVR` | 0.153208 | 0.197579 | 168.421 |
| `fft_y_Bw_filtered_ampl_156` | `SVR` | 0.000563 | 0.002141 | 50.923 |
| `fft_y_Bw_filtered_phase_156` | `SVR` | 0.350763 | 0.723826 | 31.948 |
| `fft_y_Bw_filtered_ampl_162` | `SVR` | 0.000467 | 0.001458 | 103.863 |
| `fft_y_Bw_filtered_phase_162` | `SVR` | 0.329799 | 0.618167 | 17.286 |
| `fft_y_Bw_filtered_ampl_240` | `SVR` | 0.000384 | 0.001000 | 53.626 |
| `fft_y_Bw_filtered_phase_240` | `SVR` | 0.721239 | 1.548495 | 45.277 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/svr/2026-04-26_track1_backward_svr_original_dataset_mega_campaign/016_track1_original_dataset_backward_svr_attempt_16.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-01-39__track1_original_dataset_backward_svr_attempt_16_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-01-39__track1_original_dataset_backward_svr_attempt_16_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-01-39__track1_original_dataset_backward_svr_attempt_16_campaign_validation/validation_summary.yaml`
