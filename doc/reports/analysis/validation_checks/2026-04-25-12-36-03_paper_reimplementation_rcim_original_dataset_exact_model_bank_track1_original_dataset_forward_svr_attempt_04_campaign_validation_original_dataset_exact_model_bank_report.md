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
- random seed: `9`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `54.001%`
- winning mean component MAE: `0.145856`
- winning mean component RMSE: `0.266528`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 54.001 | 0.145856 | 0.266528 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | 0.002634 | 0.003231 | 5.426 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | 0.000051 | 0.000064 | 0.296 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | 0.002266 | 0.003168 | 32.903 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | 0.000149 | 0.000171 | 20.598 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | 0.033057 | 0.044261 | 1.835 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | 0.000143 | 0.000176 | 14.415 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | 0.020385 | 0.028337 | 1.774 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | 0.000087 | 0.000105 | 11.226 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.064771 | 0.106401 | 74.190 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | 0.000218 | 0.000275 | 47.930 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | 0.213862 | 0.399741 | 206.157 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | 0.000070 | 0.000082 | 24.663 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | 0.115829 | 0.191560 | 33.645 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | 0.000503 | 0.001161 | 172.650 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | 1.120084 | 1.711609 | 79.283 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | 0.000763 | 0.002392 | 133.393 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | 0.617426 | 1.337794 | 28.621 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | 0.000334 | 0.000548 | 104.462 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | 0.578626 | 1.232965 | 32.549 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/svr/2026-04-25_track1_forward_svr_original_dataset_mega_campaign/004_track1_original_dataset_forward_svr_attempt_04.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-25-12-35-22__track1_original_dataset_forward_svr_attempt_04_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-25-12-35-22__track1_original_dataset_forward_svr_attempt_04_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-25-12-35-22__track1_original_dataset_forward_svr_attempt_04_campaign_validation/validation_summary.yaml`
