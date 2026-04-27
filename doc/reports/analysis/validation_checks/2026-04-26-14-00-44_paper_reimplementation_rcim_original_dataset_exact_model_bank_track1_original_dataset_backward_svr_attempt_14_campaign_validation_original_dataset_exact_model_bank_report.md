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
- random seed: `31`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `47.929%`
- winning mean component MAE: `0.141499`
- winning mean component RMSE: `0.268456`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 47.929 | 0.141499 | 0.268456 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `SVR` | 0.003288 | 0.004443 | 50.048 |
| `fft_y_Bw_filtered_ampl_1` | `SVR` | 0.000217 | 0.000231 | 1.271 |
| `fft_y_Bw_filtered_phase_1` | `SVR` | 0.002394 | 0.004007 | 152.296 |
| `fft_y_Bw_filtered_ampl_3` | `SVR` | 0.000135 | 0.000162 | 15.338 |
| `fft_y_Bw_filtered_phase_3` | `SVR` | 0.026075 | 0.036711 | 1.850 |
| `fft_y_Bw_filtered_ampl_39` | `SVR` | 0.000122 | 0.000139 | 32.468 |
| `fft_y_Bw_filtered_phase_39` | `SVR` | 0.717750 | 1.179228 | 25.852 |
| `fft_y_Bw_filtered_ampl_40` | `SVR` | 0.000043 | 0.000056 | 15.763 |
| `fft_y_Bw_filtered_phase_40` | `SVR` | 0.136324 | 0.251293 | 52.636 |
| `fft_y_Bw_filtered_ampl_78` | `SVR` | 0.000142 | 0.000191 | 17.442 |
| `fft_y_Bw_filtered_phase_78` | `SVR` | 0.199545 | 0.404365 | 51.890 |
| `fft_y_Bw_filtered_ampl_81` | `SVR` | 0.000042 | 0.000047 | 38.890 |
| `fft_y_Bw_filtered_phase_81` | `SVR` | 0.156849 | 0.219067 | 76.647 |
| `fft_y_Bw_filtered_ampl_156` | `SVR` | 0.000482 | 0.001077 | 62.481 |
| `fft_y_Bw_filtered_phase_156` | `SVR` | 0.390664 | 0.773488 | 40.998 |
| `fft_y_Bw_filtered_ampl_162` | `SVR` | 0.000587 | 0.001837 | 151.278 |
| `fft_y_Bw_filtered_phase_162` | `SVR` | 0.402033 | 0.796146 | 20.231 |
| `fft_y_Bw_filtered_ampl_240` | `SVR` | 0.000220 | 0.000352 | 66.433 |
| `fft_y_Bw_filtered_phase_240` | `SVR` | 0.651571 | 1.427823 | 36.833 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/svr/2026-04-26_track1_backward_svr_original_dataset_mega_campaign/014_track1_original_dataset_backward_svr_attempt_14.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-00-04__track1_original_dataset_backward_svr_attempt_14_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-00-04__track1_original_dataset_backward_svr_attempt_14_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-00-04__track1_original_dataset_backward_svr_attempt_14_campaign_validation/validation_summary.yaml`
