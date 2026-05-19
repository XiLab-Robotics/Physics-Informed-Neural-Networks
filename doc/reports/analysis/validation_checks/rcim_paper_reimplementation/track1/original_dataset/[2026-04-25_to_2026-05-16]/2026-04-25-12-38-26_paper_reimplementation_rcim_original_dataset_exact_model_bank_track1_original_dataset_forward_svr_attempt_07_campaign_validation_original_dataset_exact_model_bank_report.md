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
- random seed: `15`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `51.997%`
- winning mean component MAE: `0.131588`
- winning mean component RMSE: `0.238905`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 51.997 | 0.131588 | 0.238905 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | 0.002824 | 0.004594 | 18.558 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | 0.000050 | 0.000069 | 0.292 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | 0.002713 | 0.004058 | 36.617 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | 0.000136 | 0.000164 | 19.331 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | 0.033947 | 0.043213 | 1.903 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | 0.000161 | 0.000205 | 16.700 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | 0.027214 | 0.049831 | 2.179 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | 0.000078 | 0.000092 | 9.751 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.065437 | 0.106105 | 88.687 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | 0.000305 | 0.000357 | 141.407 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | 0.216876 | 0.429207 | 106.253 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | 0.000084 | 0.000095 | 30.424 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | 0.130045 | 0.204806 | 25.292 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | 0.000370 | 0.000897 | 176.236 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | 1.209097 | 1.788302 | 68.257 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | 0.000697 | 0.002308 | 125.564 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | 0.387766 | 0.913507 | 24.595 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | 0.000292 | 0.000530 | 74.053 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | 0.422079 | 0.990853 | 21.854 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/svr/2026-04-25_track1_forward_svr_original_dataset_mega_campaign/007_track1_original_dataset_forward_svr_attempt_07.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-25-12-37-47__track1_original_dataset_forward_svr_attempt_07_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-25-12-37-47__track1_original_dataset_forward_svr_attempt_07_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-25-12-37-47__track1_original_dataset_forward_svr_attempt_07_campaign_validation/validation_summary.yaml`
