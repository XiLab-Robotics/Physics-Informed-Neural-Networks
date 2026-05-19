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
- random seed: `21`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `50.714%`
- winning mean component MAE: `0.145092`
- winning mean component RMSE: `0.262477`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 50.714 | 0.145092 | 0.262477 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `SVR` | 0.002448 | 0.002973 | 60.691 |
| `fft_y_Bw_filtered_ampl_1` | `SVR` | 0.000175 | 0.000187 | 1.025 |
| `fft_y_Bw_filtered_phase_1` | `SVR` | 0.002591 | 0.004033 | 211.210 |
| `fft_y_Bw_filtered_ampl_3` | `SVR` | 0.000137 | 0.000158 | 15.229 |
| `fft_y_Bw_filtered_phase_3` | `SVR` | 0.027095 | 0.034521 | 2.039 |
| `fft_y_Bw_filtered_ampl_39` | `SVR` | 0.000108 | 0.000124 | 26.135 |
| `fft_y_Bw_filtered_phase_39` | `SVR` | 0.645103 | 1.034590 | 23.334 |
| `fft_y_Bw_filtered_ampl_40` | `SVR` | 0.000047 | 0.000061 | 15.983 |
| `fft_y_Bw_filtered_phase_40` | `SVR` | 0.143276 | 0.267137 | 74.252 |
| `fft_y_Bw_filtered_ampl_78` | `SVR` | 0.000345 | 0.000416 | 31.878 |
| `fft_y_Bw_filtered_phase_78` | `SVR` | 0.139070 | 0.207635 | 44.934 |
| `fft_y_Bw_filtered_ampl_81` | `SVR` | 0.000043 | 0.000049 | 42.004 |
| `fft_y_Bw_filtered_phase_81` | `SVR` | 0.136910 | 0.185814 | 47.005 |
| `fft_y_Bw_filtered_ampl_156` | `SVR` | 0.000646 | 0.002049 | 52.222 |
| `fft_y_Bw_filtered_phase_156` | `SVR` | 0.556013 | 0.944354 | 52.469 |
| `fft_y_Bw_filtered_ampl_162` | `SVR` | 0.000614 | 0.001525 | 115.049 |
| `fft_y_Bw_filtered_phase_162` | `SVR` | 0.431056 | 0.828070 | 21.416 |
| `fft_y_Bw_filtered_ampl_240` | `SVR` | 0.000421 | 0.001051 | 61.728 |
| `fft_y_Bw_filtered_phase_240` | `SVR` | 0.670644 | 1.472322 | 64.962 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/svr/2026-04-26_track1_backward_svr_original_dataset_mega_campaign/010_track1_original_dataset_backward_svr_attempt_10.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-56-53__track1_original_dataset_backward_svr_attempt_10_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-56-53__track1_original_dataset_backward_svr_attempt_10_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-56-53__track1_original_dataset_backward_svr_attempt_10_campaign_validation/validation_summary.yaml`
