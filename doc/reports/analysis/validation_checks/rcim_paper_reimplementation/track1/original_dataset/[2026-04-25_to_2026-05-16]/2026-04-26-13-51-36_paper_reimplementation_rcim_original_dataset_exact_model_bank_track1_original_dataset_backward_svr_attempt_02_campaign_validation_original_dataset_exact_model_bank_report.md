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
- random seed: `5`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `46.885%`
- winning mean component MAE: `0.161092`
- winning mean component RMSE: `0.291881`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 46.885 | 0.161092 | 0.291881 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `SVR` | 0.002870 | 0.004119 | 45.499 |
| `fft_y_Bw_filtered_ampl_1` | `SVR` | 0.000216 | 0.000229 | 1.260 |
| `fft_y_Bw_filtered_phase_1` | `SVR` | 0.002884 | 0.004412 | 184.480 |
| `fft_y_Bw_filtered_ampl_3` | `SVR` | 0.000135 | 0.000156 | 14.081 |
| `fft_y_Bw_filtered_phase_3` | `SVR` | 0.033764 | 0.056887 | 2.593 |
| `fft_y_Bw_filtered_ampl_39` | `SVR` | 0.000104 | 0.000120 | 24.588 |
| `fft_y_Bw_filtered_phase_39` | `SVR` | 0.632712 | 1.032680 | 22.970 |
| `fft_y_Bw_filtered_ampl_40` | `SVR` | 0.000045 | 0.000057 | 15.179 |
| `fft_y_Bw_filtered_phase_40` | `SVR` | 0.158700 | 0.279081 | 59.750 |
| `fft_y_Bw_filtered_ampl_78` | `SVR` | 0.000166 | 0.000185 | 26.789 |
| `fft_y_Bw_filtered_phase_78` | `SVR` | 0.196315 | 0.372534 | 43.132 |
| `fft_y_Bw_filtered_ampl_81` | `SVR` | 0.000041 | 0.000045 | 38.313 |
| `fft_y_Bw_filtered_phase_81` | `SVR` | 0.153359 | 0.216285 | 49.023 |
| `fft_y_Bw_filtered_ampl_156` | `SVR` | 0.000387 | 0.000849 | 60.648 |
| `fft_y_Bw_filtered_phase_156` | `SVR` | 0.438772 | 0.854428 | 43.345 |
| `fft_y_Bw_filtered_ampl_162` | `SVR` | 0.000474 | 0.001159 | 137.078 |
| `fft_y_Bw_filtered_phase_162` | `SVR` | 0.416949 | 0.793538 | 21.720 |
| `fft_y_Bw_filtered_ampl_240` | `SVR` | 0.000369 | 0.000830 | 50.944 |
| `fft_y_Bw_filtered_phase_240` | `SVR` | 1.022492 | 1.928145 | 49.426 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/svr/2026-04-26_track1_backward_svr_original_dataset_mega_campaign/002_track1_original_dataset_backward_svr_attempt_02.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-50-59__track1_original_dataset_backward_svr_attempt_02_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-50-59__track1_original_dataset_backward_svr_attempt_02_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-50-59__track1_original_dataset_backward_svr_attempt_02_campaign_validation/validation_summary.yaml`
