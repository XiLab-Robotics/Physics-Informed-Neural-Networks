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
- random seed: `11`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `50.098%`
- winning mean component MAE: `0.161813`
- winning mean component RMSE: `0.291597`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 50.098 | 0.161813 | 0.291597 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `SVR` | 0.002720 | 0.003329 | 54.585 |
| `fft_y_Bw_filtered_ampl_1` | `SVR` | 0.000175 | 0.000189 | 1.023 |
| `fft_y_Bw_filtered_phase_1` | `SVR` | 0.002438 | 0.003806 | 131.714 |
| `fft_y_Bw_filtered_ampl_3` | `SVR` | 0.000129 | 0.000151 | 14.129 |
| `fft_y_Bw_filtered_phase_3` | `SVR` | 0.028408 | 0.040784 | 2.131 |
| `fft_y_Bw_filtered_ampl_39` | `SVR` | 0.000106 | 0.000122 | 25.351 |
| `fft_y_Bw_filtered_phase_39` | `SVR` | 0.859344 | 1.411758 | 29.904 |
| `fft_y_Bw_filtered_ampl_40` | `SVR` | 0.000047 | 0.000059 | 15.609 |
| `fft_y_Bw_filtered_phase_40` | `SVR` | 0.119861 | 0.173432 | 164.224 |
| `fft_y_Bw_filtered_ampl_78` | `SVR` | 0.000172 | 0.000220 | 16.501 |
| `fft_y_Bw_filtered_phase_78` | `SVR` | 0.155009 | 0.344564 | 42.340 |
| `fft_y_Bw_filtered_ampl_81` | `SVR` | 0.000044 | 0.000049 | 42.218 |
| `fft_y_Bw_filtered_phase_81` | `SVR` | 0.137810 | 0.184361 | 68.522 |
| `fft_y_Bw_filtered_ampl_156` | `SVR` | 0.000642 | 0.001634 | 56.149 |
| `fft_y_Bw_filtered_phase_156` | `SVR` | 0.517534 | 0.885288 | 37.578 |
| `fft_y_Bw_filtered_ampl_162` | `SVR` | 0.000706 | 0.002236 | 116.072 |
| `fft_y_Bw_filtered_phase_162` | `SVR` | 0.355360 | 0.694414 | 19.618 |
| `fft_y_Bw_filtered_ampl_240` | `SVR` | 0.000309 | 0.000853 | 40.361 |
| `fft_y_Bw_filtered_phase_240` | `SVR` | 0.893622 | 1.793101 | 73.835 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/svr/2026-04-26_track1_backward_svr_original_dataset_mega_campaign/005_track1_original_dataset_backward_svr_attempt_05.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-53-07__track1_original_dataset_backward_svr_attempt_05_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-53-07__track1_original_dataset_backward_svr_attempt_05_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-53-07__track1_original_dataset_backward_svr_attempt_05_campaign_validation/validation_summary.yaml`
