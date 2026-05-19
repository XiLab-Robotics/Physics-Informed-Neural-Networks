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
- random seed: `11`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `66.747%`
- winning mean component MAE: `0.148944`
- winning mean component RMSE: `0.257975`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 66.747 | 0.148944 | 0.257975 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | 0.002637 | 0.003214 | 4.982 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | 0.000055 | 0.000071 | 0.321 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | 0.002220 | 0.003160 | 34.807 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | 0.000144 | 0.000170 | 19.534 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | 0.033914 | 0.043015 | 1.879 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | 0.000118 | 0.000139 | 11.530 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | 0.023282 | 0.045729 | 1.880 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | 0.000088 | 0.000102 | 10.247 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.050209 | 0.074124 | 103.649 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | 0.000265 | 0.000321 | 43.731 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | 0.185305 | 0.345390 | 453.477 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | 0.000085 | 0.000096 | 30.916 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | 0.126522 | 0.189239 | 21.095 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | 0.000399 | 0.000775 | 169.838 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | 1.426308 | 1.974494 | 108.665 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | 0.000668 | 0.002356 | 136.289 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | 0.505248 | 1.149276 | 24.802 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | 0.000324 | 0.000577 | 63.193 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | 0.472147 | 1.069285 | 27.355 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/svr/2026-04-25_track1_forward_svr_original_dataset_mega_campaign/005_track1_original_dataset_forward_svr_attempt_05.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-25-12-36-11__track1_original_dataset_forward_svr_attempt_05_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-25-12-36-11__track1_original_dataset_forward_svr_attempt_05_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-25-12-36-11__track1_original_dataset_forward_svr_attempt_05_campaign_validation/validation_summary.yaml`
