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
- random seed: `13`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `61.894%`
- winning mean component MAE: `0.176952`
- winning mean component RMSE: `0.306216`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 61.894 | 0.176952 | 0.306216 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `SVR` | 0.002687 | 0.003315 | 36.758 |
| `fft_y_Bw_filtered_ampl_1` | `SVR` | 0.000154 | 0.000171 | 0.902 |
| `fft_y_Bw_filtered_phase_1` | `SVR` | 0.002580 | 0.004136 | 478.740 |
| `fft_y_Bw_filtered_ampl_3` | `SVR` | 0.000146 | 0.000168 | 15.726 |
| `fft_y_Bw_filtered_phase_3` | `SVR` | 0.029285 | 0.043369 | 2.117 |
| `fft_y_Bw_filtered_ampl_39` | `SVR` | 0.000104 | 0.000119 | 25.322 |
| `fft_y_Bw_filtered_phase_39` | `SVR` | 0.790317 | 1.227000 | 27.971 |
| `fft_y_Bw_filtered_ampl_40` | `SVR` | 0.000045 | 0.000059 | 14.964 |
| `fft_y_Bw_filtered_phase_40` | `SVR` | 0.145435 | 0.265527 | 46.857 |
| `fft_y_Bw_filtered_ampl_78` | `SVR` | 0.000110 | 0.000134 | 19.164 |
| `fft_y_Bw_filtered_phase_78` | `SVR` | 0.163319 | 0.286844 | 43.143 |
| `fft_y_Bw_filtered_ampl_81` | `SVR` | 0.000042 | 0.000046 | 38.550 |
| `fft_y_Bw_filtered_phase_81` | `SVR` | 0.148518 | 0.205740 | 76.056 |
| `fft_y_Bw_filtered_ampl_156` | `SVR` | 0.000708 | 0.002030 | 64.020 |
| `fft_y_Bw_filtered_phase_156` | `SVR` | 0.479015 | 0.886173 | 41.187 |
| `fft_y_Bw_filtered_ampl_162` | `SVR` | 0.000905 | 0.002505 | 111.372 |
| `fft_y_Bw_filtered_phase_162` | `SVR` | 0.552616 | 0.934025 | 29.388 |
| `fft_y_Bw_filtered_ampl_240` | `SVR` | 0.000330 | 0.000994 | 52.398 |
| `fft_y_Bw_filtered_phase_240` | `SVR` | 1.045762 | 1.955747 | 51.345 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/svr/2026-04-26_track1_backward_svr_original_dataset_mega_campaign/006_track1_original_dataset_backward_svr_attempt_06.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-53-50__track1_original_dataset_backward_svr_attempt_06_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-53-50__track1_original_dataset_backward_svr_attempt_06_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-53-50__track1_original_dataset_backward_svr_attempt_06_campaign_validation/validation_summary.yaml`
