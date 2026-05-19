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
- random seed: `5`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `75.250%`
- winning mean component MAE: `0.160417`
- winning mean component RMSE: `0.290000`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 75.250 | 0.160417 | 0.290000 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | 0.002798 | 0.004553 | 17.956 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | 0.000054 | 0.000074 | 0.316 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | 0.002740 | 0.003928 | 62.750 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | 0.000152 | 0.000174 | 19.848 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | 0.037839 | 0.049807 | 2.065 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | 0.000171 | 0.000204 | 17.132 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | 0.035574 | 0.058652 | 3.106 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | 0.000077 | 0.000097 | 9.429 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.071033 | 0.111015 | 110.183 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | 0.000271 | 0.000330 | 31.133 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | 0.227658 | 0.344542 | 182.077 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | 0.000084 | 0.000097 | 29.735 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | 0.154764 | 0.246475 | 26.287 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | 0.000318 | 0.000559 | 154.330 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | 1.169618 | 1.673301 | 75.318 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | 0.000398 | 0.001144 | 119.362 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | 0.690689 | 1.609247 | 30.038 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | 0.000313 | 0.000454 | 85.004 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | 0.653377 | 1.405343 | 453.683 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/svr/2026-04-26_track1_forward_svr_original_dataset_mega_campaign/002_track1_original_dataset_forward_svr_attempt_02.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-00-53-21__track1_original_dataset_forward_svr_attempt_02_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-00-53-21__track1_original_dataset_forward_svr_attempt_02_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-00-53-21__track1_original_dataset_forward_svr_attempt_02_campaign_validation/validation_summary.yaml`
