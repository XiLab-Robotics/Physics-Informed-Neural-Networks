# Original-Dataset Exact RCIM Model Bank Validation Report

## Overview

This report covers the direction-specific exact-model-bank branch trained from the repository dataset under `data/datasets`.

- direction label: `forward`
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
- random seed: `27`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `60.239%`
- winning mean component MAE: `0.153543`
- winning mean component RMSE: `0.247007`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 60.239 | 0.153543 | 0.247007 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | 0.002715 | 0.003450 | 5.142 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | 0.000059 | 0.000074 | 0.343 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | 0.002629 | 0.003610 | 37.581 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | 0.000154 | 0.000174 | 20.203 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | 0.029223 | 0.037115 | 1.606 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | 0.000123 | 0.000145 | 11.971 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | 0.023143 | 0.037465 | 1.990 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | 0.000084 | 0.000100 | 10.752 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.060899 | 0.095147 | 87.318 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | 0.000250 | 0.000296 | 26.033 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | 0.137196 | 0.227839 | 357.476 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | 0.000079 | 0.000092 | 28.699 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | 0.115352 | 0.175532 | 14.028 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | 0.000365 | 0.000781 | 141.933 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | 1.592902 | 2.065980 | 133.791 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | 0.000427 | 0.001158 | 110.332 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | 0.621288 | 1.348420 | 28.696 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | 0.000292 | 0.000555 | 55.932 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | 0.330132 | 0.695203 | 70.715 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/svr/2026-04-26_track1_forward_svr_original_dataset_mega_campaign/012_track1_original_dataset_forward_svr_attempt_12.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-03-44__track1_original_dataset_forward_svr_attempt_12_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-03-44__track1_original_dataset_forward_svr_attempt_12_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-03-44__track1_original_dataset_forward_svr_attempt_12_campaign_validation/validation_summary.yaml`
