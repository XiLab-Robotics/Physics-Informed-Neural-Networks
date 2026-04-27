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
- random seed: `31`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `70.913%`
- winning mean component MAE: `0.151259`
- winning mean component RMSE: `0.276060`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 70.913 | 0.151259 | 0.276060 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `SVR` | 0.003004 | 0.004237 | 7.104 |
| `fft_y_Fw_filtered_ampl_1` | `SVR` | 0.000062 | 0.000078 | 0.362 |
| `fft_y_Fw_filtered_phase_1` | `SVR` | 0.002530 | 0.003744 | 42.042 |
| `fft_y_Fw_filtered_ampl_3` | `SVR` | 0.000146 | 0.000171 | 20.555 |
| `fft_y_Fw_filtered_phase_3` | `SVR` | 0.034904 | 0.045684 | 1.898 |
| `fft_y_Fw_filtered_ampl_39` | `SVR` | 0.000159 | 0.000208 | 17.076 |
| `fft_y_Fw_filtered_phase_39` | `SVR` | 0.028415 | 0.050750 | 2.374 |
| `fft_y_Fw_filtered_ampl_40` | `SVR` | 0.000088 | 0.000104 | 10.831 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.051582 | 0.074228 | 66.632 |
| `fft_y_Fw_filtered_ampl_78` | `SVR` | 0.000225 | 0.000289 | 28.560 |
| `fft_y_Fw_filtered_phase_78` | `SVR` | 0.231601 | 0.424587 | 447.891 |
| `fft_y_Fw_filtered_ampl_81` | `SVR` | 0.000085 | 0.000094 | 29.204 |
| `fft_y_Fw_filtered_phase_81` | `SVR` | 0.114251 | 0.178791 | 17.128 |
| `fft_y_Fw_filtered_ampl_156` | `SVR` | 0.000317 | 0.000578 | 221.534 |
| `fft_y_Fw_filtered_phase_156` | `SVR` | 1.135839 | 1.695692 | 70.551 |
| `fft_y_Fw_filtered_ampl_162` | `SVR` | 0.000588 | 0.001983 | 175.900 |
| `fft_y_Fw_filtered_phase_162` | `SVR` | 0.580817 | 1.327775 | 26.505 |
| `fft_y_Fw_filtered_ampl_240` | `SVR` | 0.000278 | 0.000410 | 108.837 |
| `fft_y_Fw_filtered_phase_240` | `SVR` | 0.689042 | 1.435742 | 52.359 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/svr/2026-04-26_track1_forward_svr_original_dataset_mega_campaign/014_track1_original_dataset_forward_svr_attempt_14.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-06-10__track1_original_dataset_forward_svr_attempt_14_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-06-10__track1_original_dataset_forward_svr_attempt_14_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-01-06-10__track1_original_dataset_forward_svr_attempt_14_campaign_validation/validation_summary.yaml`
