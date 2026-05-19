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
- random seed: `47`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `61.744%`
- winning mean component MAE: `0.159971`
- winning mean component RMSE: `0.282136`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 61.744 | 0.159971 | 0.282136 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | 0.003230 | 0.004807 | 19.200 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | 0.000051 | 0.000066 | 0.299 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | 0.002672 | 0.003752 | 128.445 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | 0.000163 | 0.000182 | 21.928 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | 0.033780 | 0.044229 | 1.895 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | 0.000609 | 0.000692 | 68.193 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | 0.027989 | 0.053253 | 2.291 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | 0.000078 | 0.000094 | 9.872 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.065259 | 0.107596 | 155.370 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | 0.000249 | 0.000299 | 27.004 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | 0.157153 | 0.250414 | 89.323 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | 0.000083 | 0.000093 | 29.570 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | 0.129361 | 0.203758 | 16.566 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | 0.000428 | 0.000963 | 192.242 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | 1.341866 | 1.900892 | 103.001 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | 0.000679 | 0.002066 | 115.154 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | 0.677813 | 1.493940 | 31.628 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | 0.000260 | 0.000465 | 66.997 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | 0.597718 | 1.293031 | 94.163 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/svr/2026-04-26_track1_forward_svr_original_dataset_mega_campaign/017_track1_original_dataset_forward_svr_attempt_17.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-09-52__track1_original_dataset_forward_svr_attempt_17_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-09-52__track1_original_dataset_forward_svr_attempt_17_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-09-52__track1_original_dataset_forward_svr_attempt_17_campaign_validation/validation_summary.yaml`
