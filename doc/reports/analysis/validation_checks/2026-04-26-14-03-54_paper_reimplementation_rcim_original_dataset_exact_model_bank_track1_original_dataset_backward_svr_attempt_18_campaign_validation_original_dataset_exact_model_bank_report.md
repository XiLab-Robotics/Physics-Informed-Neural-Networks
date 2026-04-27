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
- random seed: `53`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `49.426%`
- winning mean component MAE: `0.163650`
- winning mean component RMSE: `0.292424`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 49.426 | 0.163650 | 0.292424 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `SVR` | 0.002958 | 0.004167 | 28.075 |
| `fft_y_Bw_filtered_ampl_1` | `SVR` | 0.000176 | 0.000198 | 1.025 |
| `fft_y_Bw_filtered_phase_1` | `SVR` | 0.002849 | 0.004296 | 61.166 |
| `fft_y_Bw_filtered_ampl_3` | `SVR` | 0.000162 | 0.000183 | 18.452 |
| `fft_y_Bw_filtered_phase_3` | `SVR` | 0.030542 | 0.061955 | 2.271 |
| `fft_y_Bw_filtered_ampl_39` | `SVR` | 0.000107 | 0.000123 | 26.637 |
| `fft_y_Bw_filtered_phase_39` | `SVR` | 0.563930 | 0.995695 | 21.237 |
| `fft_y_Bw_filtered_ampl_40` | `SVR` | 0.000048 | 0.000062 | 15.246 |
| `fft_y_Bw_filtered_phase_40` | `SVR` | 0.177067 | 0.318872 | 133.668 |
| `fft_y_Bw_filtered_ampl_78` | `SVR` | 0.000150 | 0.000180 | 44.760 |
| `fft_y_Bw_filtered_phase_78` | `SVR` | 0.191996 | 0.400467 | 60.692 |
| `fft_y_Bw_filtered_ampl_81` | `SVR` | 0.000044 | 0.000050 | 43.368 |
| `fft_y_Bw_filtered_phase_81` | `SVR` | 0.163520 | 0.235916 | 138.720 |
| `fft_y_Bw_filtered_ampl_156` | `SVR` | 0.000866 | 0.002947 | 53.282 |
| `fft_y_Bw_filtered_phase_156` | `SVR` | 0.458189 | 0.839687 | 33.500 |
| `fft_y_Bw_filtered_ampl_162` | `SVR` | 0.000653 | 0.001700 | 98.917 |
| `fft_y_Bw_filtered_phase_162` | `SVR` | 0.432081 | 0.736251 | 22.100 |
| `fft_y_Bw_filtered_ampl_240` | `SVR` | 0.000235 | 0.000366 | 70.961 |
| `fft_y_Bw_filtered_phase_240` | `SVR` | 1.083766 | 1.952941 | 65.015 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/svr/2026-04-26_track1_backward_svr_original_dataset_mega_campaign/018_track1_original_dataset_backward_svr_attempt_18.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-03-10__track1_original_dataset_backward_svr_attempt_18_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-03-10__track1_original_dataset_backward_svr_attempt_18_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-03-10__track1_original_dataset_backward_svr_attempt_18_campaign_validation/validation_summary.yaml`
