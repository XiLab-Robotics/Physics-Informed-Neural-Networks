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
- random seed: `13`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `67.813%`
- winning mean component MAE: `0.140540`
- winning mean component RMSE: `0.222328`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 67.813 | 0.140540 | 0.222328 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | 0.002514 | 0.003183 | 4.997 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | 0.000048 | 0.000063 | 0.277 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | 0.002710 | 0.003721 | 95.955 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | 0.000149 | 0.000175 | 20.150 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | 0.028980 | 0.039351 | 1.629 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | 0.000179 | 0.000207 | 16.548 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | 0.025669 | 0.038759 | 2.441 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | 0.000081 | 0.000097 | 9.809 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.059103 | 0.089818 | 80.248 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | 0.000268 | 0.000337 | 33.281 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | 0.203110 | 0.306567 | 150.028 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | 0.000097 | 0.000109 | 35.908 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | 0.153140 | 0.240031 | 22.911 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | 0.000473 | 0.000981 | 194.223 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | 1.342705 | 1.876048 | 71.090 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | 0.000865 | 0.002679 | 105.079 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | 0.395748 | 0.724591 | 25.319 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | 0.000297 | 0.000469 | 86.350 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | 0.454119 | 0.897045 | 332.212 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/svr/2026-04-26_track1_forward_svr_original_dataset_mega_campaign/006_track1_original_dataset_forward_svr_attempt_06.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-00-56-36__track1_original_dataset_forward_svr_attempt_06_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-00-56-36__track1_original_dataset_forward_svr_attempt_06_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-00-56-36__track1_original_dataset_forward_svr_attempt_06_campaign_validation/validation_summary.yaml`
