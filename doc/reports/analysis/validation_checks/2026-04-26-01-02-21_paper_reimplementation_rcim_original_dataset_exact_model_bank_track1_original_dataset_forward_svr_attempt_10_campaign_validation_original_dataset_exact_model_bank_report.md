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
- random seed: `21`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `64.827%`
- winning mean component MAE: `0.151833`
- winning mean component RMSE: `0.268097`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 64.827 | 0.151833 | 0.268097 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | 0.002564 | 0.003070 | 5.146 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | 0.000060 | 0.000074 | 0.349 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | 0.002534 | 0.003595 | 38.051 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | 0.000155 | 0.000178 | 20.953 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | 0.029094 | 0.037486 | 1.599 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | 0.000151 | 0.000179 | 15.073 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | 0.029824 | 0.055618 | 2.427 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | 0.000088 | 0.000103 | 10.938 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.055787 | 0.092048 | 106.618 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | 0.000285 | 0.000354 | 33.870 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | 0.176498 | 0.286037 | 132.900 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | 0.000088 | 0.000100 | 31.865 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | 0.133318 | 0.204085 | 19.374 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | 0.000412 | 0.000809 | 172.188 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | 1.161800 | 1.632919 | 102.366 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | 0.000503 | 0.001484 | 104.322 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | 0.664208 | 1.416522 | 29.790 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | 0.000426 | 0.000724 | 90.135 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | 0.627038 | 1.358462 | 313.749 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/svr/2026-04-26_track1_forward_svr_original_dataset_mega_campaign/010_track1_original_dataset_forward_svr_attempt_10.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-01-18__track1_original_dataset_forward_svr_attempt_10_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-01-18__track1_original_dataset_forward_svr_attempt_10_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-01-18__track1_original_dataset_forward_svr_attempt_10_campaign_validation/validation_summary.yaml`
