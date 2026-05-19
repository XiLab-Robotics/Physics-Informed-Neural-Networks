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
- random seed: `53`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `133.898%`
- winning mean component MAE: `0.156933`
- winning mean component RMSE: `0.270650`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 133.898 | 0.156933 | 0.270650 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | 0.003165 | 0.004500 | 10.244 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | 0.000067 | 0.000083 | 0.389 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | 0.002861 | 0.004223 | 1587.206 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | 0.000159 | 0.000180 | 21.885 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | 0.037085 | 0.069368 | 2.011 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | 0.000143 | 0.000181 | 15.024 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | 0.035403 | 0.065369 | 2.722 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | 0.000099 | 0.000118 | 12.479 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.065408 | 0.100338 | 61.196 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | 0.000279 | 0.000342 | 46.736 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | 0.186254 | 0.288535 | 159.533 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | 0.000088 | 0.000103 | 32.515 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | 0.141456 | 0.213671 | 33.837 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | 0.000425 | 0.000890 | 163.077 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | 1.362620 | 1.917546 | 90.036 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | 0.000583 | 0.001664 | 125.828 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | 0.561637 | 1.211710 | 26.724 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | 0.000314 | 0.000520 | 102.747 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | 0.583688 | 1.263018 | 49.880 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/svr/2026-04-26_track1_forward_svr_original_dataset_mega_campaign/018_track1_original_dataset_forward_svr_attempt_18.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-11-06__track1_original_dataset_forward_svr_attempt_18_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-11-06__track1_original_dataset_forward_svr_attempt_18_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-11-06__track1_original_dataset_forward_svr_attempt_18_campaign_validation/validation_summary.yaml`
