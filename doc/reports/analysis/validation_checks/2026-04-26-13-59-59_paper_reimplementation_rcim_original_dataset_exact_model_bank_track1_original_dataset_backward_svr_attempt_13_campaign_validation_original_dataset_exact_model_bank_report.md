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
- random seed: `29`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `65.567%`
- winning mean component MAE: `0.141663`
- winning mean component RMSE: `0.266430`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 65.567 | 0.141663 | 0.266430 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `SVR` | 0.003271 | 0.005029 | 73.611 |
| `fft_y_Bw_filtered_ampl_1` | `SVR` | 0.000122 | 0.000136 | 0.714 |
| `fft_y_Bw_filtered_phase_1` | `SVR` | 0.002445 | 0.003545 | 213.940 |
| `fft_y_Bw_filtered_ampl_3` | `SVR` | 0.000147 | 0.000168 | 16.658 |
| `fft_y_Bw_filtered_phase_3` | `SVR` | 0.027216 | 0.051836 | 1.981 |
| `fft_y_Bw_filtered_ampl_39` | `SVR` | 0.000132 | 0.000147 | 34.107 |
| `fft_y_Bw_filtered_phase_39` | `SVR` | 0.596226 | 1.058448 | 21.542 |
| `fft_y_Bw_filtered_ampl_40` | `SVR` | 0.000047 | 0.000065 | 15.365 |
| `fft_y_Bw_filtered_phase_40` | `SVR` | 0.183610 | 0.347808 | 46.827 |
| `fft_y_Bw_filtered_ampl_78` | `SVR` | 0.000194 | 0.000223 | 37.114 |
| `fft_y_Bw_filtered_phase_78` | `SVR` | 0.111765 | 0.185815 | 26.833 |
| `fft_y_Bw_filtered_ampl_81` | `SVR` | 0.000037 | 0.000043 | 34.547 |
| `fft_y_Bw_filtered_phase_81` | `SVR` | 0.133056 | 0.180298 | 410.220 |
| `fft_y_Bw_filtered_ampl_156` | `SVR` | 0.000820 | 0.002889 | 46.733 |
| `fft_y_Bw_filtered_phase_156` | `SVR` | 0.398797 | 0.732328 | 39.027 |
| `fft_y_Bw_filtered_ampl_162` | `SVR` | 0.000458 | 0.001425 | 85.138 |
| `fft_y_Bw_filtered_phase_162` | `SVR` | 0.393626 | 0.732699 | 20.480 |
| `fft_y_Bw_filtered_ampl_240` | `SVR` | 0.000227 | 0.000271 | 52.185 |
| `fft_y_Bw_filtered_phase_240` | `SVR` | 0.839397 | 1.758999 | 68.758 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/svr/2026-04-26_track1_backward_svr_original_dataset_mega_campaign/013_track1_original_dataset_backward_svr_attempt_13.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-59-13__track1_original_dataset_backward_svr_attempt_13_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-59-13__track1_original_dataset_backward_svr_attempt_13_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-59-13__track1_original_dataset_backward_svr_attempt_13_campaign_validation/validation_summary.yaml`
