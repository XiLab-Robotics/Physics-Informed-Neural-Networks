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
- random seed: `19`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `41.660%`
- winning mean component MAE: `0.146315`
- winning mean component RMSE: `0.266380`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 41.660 | 0.146315 | 0.266380 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `SVR` | 0.002943 | 0.004195 | 35.990 |
| `fft_y_Bw_filtered_ampl_1` | `SVR` | 0.000189 | 0.000204 | 1.108 |
| `fft_y_Bw_filtered_phase_1` | `SVR` | 0.002335 | 0.003380 | 82.599 |
| `fft_y_Bw_filtered_ampl_3` | `SVR` | 0.000129 | 0.000150 | 14.561 |
| `fft_y_Bw_filtered_phase_3` | `SVR` | 0.028572 | 0.051476 | 2.130 |
| `fft_y_Bw_filtered_ampl_39` | `SVR` | 0.000100 | 0.000114 | 25.023 |
| `fft_y_Bw_filtered_phase_39` | `SVR` | 0.912337 | 1.451966 | 31.355 |
| `fft_y_Bw_filtered_ampl_40` | `SVR` | 0.000037 | 0.000048 | 12.063 |
| `fft_y_Bw_filtered_phase_40` | `SVR` | 0.121770 | 0.221742 | 32.986 |
| `fft_y_Bw_filtered_ampl_78` | `SVR` | 0.000189 | 0.000214 | 29.182 |
| `fft_y_Bw_filtered_phase_78` | `SVR` | 0.106436 | 0.152783 | 53.812 |
| `fft_y_Bw_filtered_ampl_81` | `SVR` | 0.000048 | 0.000052 | 48.408 |
| `fft_y_Bw_filtered_phase_81` | `SVR` | 0.135367 | 0.180951 | 120.578 |
| `fft_y_Bw_filtered_ampl_156` | `SVR` | 0.000605 | 0.002474 | 43.641 |
| `fft_y_Bw_filtered_phase_156` | `SVR` | 0.384645 | 0.809113 | 28.692 |
| `fft_y_Bw_filtered_ampl_162` | `SVR` | 0.000846 | 0.002671 | 99.220 |
| `fft_y_Bw_filtered_phase_162` | `SVR` | 0.435390 | 0.799162 | 22.265 |
| `fft_y_Bw_filtered_ampl_240` | `SVR` | 0.000218 | 0.000308 | 47.119 |
| `fft_y_Bw_filtered_phase_240` | `SVR` | 0.647835 | 1.380221 | 60.806 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/svr/2026-04-26_track1_backward_svr_original_dataset_mega_campaign/009_track1_original_dataset_backward_svr_attempt_09.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-56-04__track1_original_dataset_backward_svr_attempt_09_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-56-04__track1_original_dataset_backward_svr_attempt_09_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-56-04__track1_original_dataset_backward_svr_attempt_09_campaign_validation/validation_summary.yaml`
