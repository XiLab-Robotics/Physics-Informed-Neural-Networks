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
- random seed: `17`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `43.397%`
- winning mean component MAE: `0.161362`
- winning mean component RMSE: `0.285776`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 43.397 | 0.161362 | 0.285776 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `SVR` | 0.002857 | 0.003416 | 46.184 |
| `fft_y_Bw_filtered_ampl_1` | `SVR` | 0.000237 | 0.000249 | 1.385 |
| `fft_y_Bw_filtered_phase_1` | `SVR` | 0.002564 | 0.003900 | 105.060 |
| `fft_y_Bw_filtered_ampl_3` | `SVR` | 0.000122 | 0.000145 | 13.638 |
| `fft_y_Bw_filtered_phase_3` | `SVR` | 0.028313 | 0.036778 | 2.131 |
| `fft_y_Bw_filtered_ampl_39` | `SVR` | 0.000106 | 0.000121 | 25.256 |
| `fft_y_Bw_filtered_phase_39` | `SVR` | 0.866862 | 1.290539 | 30.400 |
| `fft_y_Bw_filtered_ampl_40` | `SVR` | 0.000043 | 0.000056 | 13.168 |
| `fft_y_Bw_filtered_phase_40` | `SVR` | 0.143139 | 0.261683 | 61.614 |
| `fft_y_Bw_filtered_ampl_78` | `SVR` | 0.000135 | 0.000174 | 20.256 |
| `fft_y_Bw_filtered_phase_78` | `SVR` | 0.129705 | 0.230166 | 44.756 |
| `fft_y_Bw_filtered_ampl_81` | `SVR` | 0.000041 | 0.000046 | 41.881 |
| `fft_y_Bw_filtered_phase_81` | `SVR` | 0.150901 | 0.199894 | 122.190 |
| `fft_y_Bw_filtered_ampl_156` | `SVR` | 0.000752 | 0.002455 | 45.279 |
| `fft_y_Bw_filtered_phase_156` | `SVR` | 0.506594 | 0.904195 | 42.033 |
| `fft_y_Bw_filtered_ampl_162` | `SVR` | 0.000696 | 0.002067 | 96.209 |
| `fft_y_Bw_filtered_phase_162` | `SVR` | 0.489024 | 0.917368 | 23.984 |
| `fft_y_Bw_filtered_ampl_240` | `SVR` | 0.000389 | 0.000882 | 53.363 |
| `fft_y_Bw_filtered_phase_240` | `SVR` | 0.743396 | 1.575602 | 35.752 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/svr/2026-04-26_track1_backward_svr_original_dataset_mega_campaign/008_track1_original_dataset_backward_svr_attempt_08.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-55-21__track1_original_dataset_backward_svr_attempt_08_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-55-21__track1_original_dataset_backward_svr_attempt_08_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-55-21__track1_original_dataset_backward_svr_attempt_08_campaign_validation/validation_summary.yaml`
