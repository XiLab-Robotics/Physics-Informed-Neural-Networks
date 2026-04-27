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
- random seed: `0`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `54.317%`
- winning mean component MAE: `0.141435`
- winning mean component RMSE: `0.237704`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 54.317 | 0.141435 | 0.237704 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | 0.002930 | 0.003595 | 5.796 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | 0.000062 | 0.000082 | 0.361 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | 0.002402 | 0.003257 | 92.216 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | 0.000140 | 0.000164 | 19.349 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | 0.027246 | 0.036217 | 1.493 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | 0.000070 | 0.000090 | 6.784 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | 0.027436 | 0.053814 | 2.156 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | 0.000082 | 0.000099 | 10.306 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.054415 | 0.090050 | 64.201 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | 0.000305 | 0.000365 | 45.502 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | 0.155952 | 0.284188 | 131.479 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | 0.000085 | 0.000098 | 31.369 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | 0.102334 | 0.148218 | 13.669 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | 0.000409 | 0.000696 | 283.344 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | 1.314808 | 1.705224 | 86.697 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | 0.000635 | 0.002047 | 112.129 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | 0.555504 | 1.266627 | 26.524 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | 0.000335 | 0.000599 | 75.154 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | 0.442113 | 0.920946 | 23.484 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/svr/2026-04-26_track1_forward_svr_original_dataset_mega_campaign/001_track1_original_dataset_forward_svr_attempt_01.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-00-52-04__track1_original_dataset_forward_svr_attempt_01_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-00-52-04__track1_original_dataset_forward_svr_attempt_01_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-00-52-04__track1_original_dataset_forward_svr_attempt_01_campaign_validation/validation_summary.yaml`
