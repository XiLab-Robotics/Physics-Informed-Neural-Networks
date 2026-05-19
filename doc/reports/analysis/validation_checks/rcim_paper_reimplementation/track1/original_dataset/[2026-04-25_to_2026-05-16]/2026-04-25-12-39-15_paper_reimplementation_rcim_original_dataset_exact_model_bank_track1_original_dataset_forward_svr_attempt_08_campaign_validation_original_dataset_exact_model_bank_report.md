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
- random seed: `17`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `48.497%`
- winning mean component MAE: `0.127331`
- winning mean component RMSE: `0.210640`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 48.497 | 0.127331 | 0.210640 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | 0.002656 | 0.003224 | 5.081 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | 0.000057 | 0.000075 | 0.331 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | 0.002339 | 0.002982 | 41.693 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | 0.000140 | 0.000166 | 18.527 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | 0.030429 | 0.036620 | 1.678 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | 0.000163 | 0.000195 | 14.413 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | 0.020639 | 0.031625 | 1.918 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | 0.000082 | 0.000093 | 9.847 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.063637 | 0.095383 | 88.942 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | 0.000243 | 0.000303 | 28.275 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | 0.156872 | 0.257854 | 167.162 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | 0.000088 | 0.000100 | 32.215 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | 0.118925 | 0.194222 | 13.628 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | 0.000442 | 0.000856 | 197.274 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | 1.188650 | 1.690909 | 62.110 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | 0.000628 | 0.002166 | 106.467 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | 0.427419 | 0.815790 | 22.759 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | 0.000350 | 0.000591 | 81.373 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | 0.405526 | 0.869013 | 27.747 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/svr/2026-04-25_track1_forward_svr_original_dataset_mega_campaign/008_track1_original_dataset_forward_svr_attempt_08.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-25-12-38-35__track1_original_dataset_forward_svr_attempt_08_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-25-12-38-35__track1_original_dataset_forward_svr_attempt_08_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-25-12-38-35__track1_original_dataset_forward_svr_attempt_08_campaign_validation/validation_summary.yaml`
