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
- random seed: `47`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `53.654%`
- winning mean component MAE: `0.146494`
- winning mean component RMSE: `0.270620`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 53.654 | 0.146494 | 0.270620 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `SVR` | 0.003259 | 0.004403 | 98.591 |
| `fft_y_Bw_filtered_ampl_1` | `SVR` | 0.000139 | 0.000153 | 0.811 |
| `fft_y_Bw_filtered_phase_1` | `SVR` | 0.002933 | 0.004367 | 230.430 |
| `fft_y_Bw_filtered_ampl_3` | `SVR` | 0.000139 | 0.000164 | 15.389 |
| `fft_y_Bw_filtered_phase_3` | `SVR` | 0.033165 | 0.056504 | 2.401 |
| `fft_y_Bw_filtered_ampl_39` | `SVR` | 0.000121 | 0.000140 | 30.395 |
| `fft_y_Bw_filtered_phase_39` | `SVR` | 0.589644 | 1.077170 | 21.176 |
| `fft_y_Bw_filtered_ampl_40` | `SVR` | 0.000055 | 0.000070 | 17.223 |
| `fft_y_Bw_filtered_phase_40` | `SVR` | 0.157587 | 0.283824 | 69.496 |
| `fft_y_Bw_filtered_ampl_78` | `SVR` | 0.000147 | 0.000169 | 23.480 |
| `fft_y_Bw_filtered_phase_78` | `SVR` | 0.124121 | 0.172885 | 82.043 |
| `fft_y_Bw_filtered_ampl_81` | `SVR` | 0.000039 | 0.000045 | 35.852 |
| `fft_y_Bw_filtered_phase_81` | `SVR` | 0.143475 | 0.193766 | 60.851 |
| `fft_y_Bw_filtered_ampl_156` | `SVR` | 0.000761 | 0.003060 | 63.711 |
| `fft_y_Bw_filtered_phase_156` | `SVR` | 0.406609 | 0.783395 | 46.036 |
| `fft_y_Bw_filtered_ampl_162` | `SVR` | 0.000662 | 0.001828 | 94.422 |
| `fft_y_Bw_filtered_phase_162` | `SVR` | 0.451356 | 0.787320 | 23.293 |
| `fft_y_Bw_filtered_ampl_240` | `SVR` | 0.000351 | 0.000918 | 58.267 |
| `fft_y_Bw_filtered_phase_240` | `SVR` | 0.868819 | 1.771592 | 45.561 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/svr/2026-04-26_track1_backward_svr_original_dataset_mega_campaign/017_track1_original_dataset_backward_svr_attempt_17.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-02-26__track1_original_dataset_backward_svr_attempt_17_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-02-26__track1_original_dataset_backward_svr_attempt_17_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-02-26__track1_original_dataset_backward_svr_attempt_17_campaign_validation/validation_summary.yaml`
