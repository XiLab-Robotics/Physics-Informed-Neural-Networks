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
- random seed: `23`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `48.362%`
- winning mean component MAE: `0.128654`
- winning mean component RMSE: `0.247435`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 48.362 | 0.128654 | 0.247435 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `SVR` | 0.002803 | 0.003373 | 73.983 |
| `fft_y_Bw_filtered_ampl_1` | `SVR` | 0.000192 | 0.000205 | 1.123 |
| `fft_y_Bw_filtered_phase_1` | `SVR` | 0.002282 | 0.003482 | 113.896 |
| `fft_y_Bw_filtered_ampl_3` | `SVR` | 0.000137 | 0.000162 | 15.203 |
| `fft_y_Bw_filtered_phase_3` | `SVR` | 0.027872 | 0.037977 | 2.088 |
| `fft_y_Bw_filtered_ampl_39` | `SVR` | 0.000097 | 0.000113 | 24.673 |
| `fft_y_Bw_filtered_phase_39` | `SVR` | 0.676083 | 1.079237 | 23.958 |
| `fft_y_Bw_filtered_ampl_40` | `SVR` | 0.000049 | 0.000060 | 16.247 |
| `fft_y_Bw_filtered_phase_40` | `SVR` | 0.184604 | 0.382733 | 57.359 |
| `fft_y_Bw_filtered_ampl_78` | `SVR` | 0.000172 | 0.000208 | 29.699 |
| `fft_y_Bw_filtered_phase_78` | `SVR` | 0.143257 | 0.261254 | 42.222 |
| `fft_y_Bw_filtered_ampl_81` | `SVR` | 0.000041 | 0.000046 | 40.857 |
| `fft_y_Bw_filtered_phase_81` | `SVR` | 0.130535 | 0.175454 | 166.186 |
| `fft_y_Bw_filtered_ampl_156` | `SVR` | 0.000666 | 0.002502 | 57.426 |
| `fft_y_Bw_filtered_phase_156` | `SVR` | 0.347750 | 0.662342 | 39.979 |
| `fft_y_Bw_filtered_ampl_162` | `SVR` | 0.000577 | 0.001648 | 98.237 |
| `fft_y_Bw_filtered_phase_162` | `SVR` | 0.387186 | 0.810568 | 19.362 |
| `fft_y_Bw_filtered_ampl_240` | `SVR` | 0.000309 | 0.000644 | 47.196 |
| `fft_y_Bw_filtered_phase_240` | `SVR` | 0.539813 | 1.279252 | 49.179 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/svr/2026-04-26_track1_backward_svr_original_dataset_mega_campaign/011_track1_original_dataset_backward_svr_attempt_11.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-57-38__track1_original_dataset_backward_svr_attempt_11_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-57-38__track1_original_dataset_backward_svr_attempt_11_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-57-38__track1_original_dataset_backward_svr_attempt_11_campaign_validation/validation_summary.yaml`
