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
- random seed: `59`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `59.274%`
- winning mean component MAE: `0.136758`
- winning mean component RMSE: `0.253200`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 59.274 | 0.136758 | 0.253200 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `SVR` | 0.002846 | 0.003452 | 66.674 |
| `fft_y_Bw_filtered_ampl_1` | `SVR` | 0.000246 | 0.000260 | 1.438 |
| `fft_y_Bw_filtered_phase_1` | `SVR` | 0.002808 | 0.004604 | 449.950 |
| `fft_y_Bw_filtered_ampl_3` | `SVR` | 0.000142 | 0.000166 | 15.532 |
| `fft_y_Bw_filtered_phase_3` | `SVR` | 0.029462 | 0.039692 | 2.156 |
| `fft_y_Bw_filtered_ampl_39` | `SVR` | 0.000098 | 0.000113 | 24.159 |
| `fft_y_Bw_filtered_phase_39` | `SVR` | 0.694519 | 1.136304 | 24.491 |
| `fft_y_Bw_filtered_ampl_40` | `SVR` | 0.000045 | 0.000057 | 14.918 |
| `fft_y_Bw_filtered_phase_40` | `SVR` | 0.151230 | 0.289716 | 40.783 |
| `fft_y_Bw_filtered_ampl_78` | `SVR` | 0.000160 | 0.000206 | 22.207 |
| `fft_y_Bw_filtered_phase_78` | `SVR` | 0.147438 | 0.252968 | 32.073 |
| `fft_y_Bw_filtered_ampl_81` | `SVR` | 0.000040 | 0.000044 | 37.809 |
| `fft_y_Bw_filtered_phase_81` | `SVR` | 0.141187 | 0.198764 | 56.541 |
| `fft_y_Bw_filtered_ampl_156` | `SVR` | 0.000540 | 0.001480 | 56.739 |
| `fft_y_Bw_filtered_phase_156` | `SVR` | 0.354949 | 0.681521 | 42.721 |
| `fft_y_Bw_filtered_ampl_162` | `SVR` | 0.000437 | 0.001036 | 118.614 |
| `fft_y_Bw_filtered_phase_162` | `SVR` | 0.384690 | 0.687353 | 20.715 |
| `fft_y_Bw_filtered_ampl_240` | `SVR` | 0.000305 | 0.000669 | 54.307 |
| `fft_y_Bw_filtered_phase_240` | `SVR` | 0.687256 | 1.512399 | 44.372 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/svr/2026-04-26_track1_backward_svr_original_dataset_mega_campaign/019_track1_original_dataset_backward_svr_attempt_19.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-04-00__track1_original_dataset_backward_svr_attempt_19_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-04-00__track1_original_dataset_backward_svr_attempt_19_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-04-00__track1_original_dataset_backward_svr_attempt_19_campaign_validation/validation_summary.yaml`
