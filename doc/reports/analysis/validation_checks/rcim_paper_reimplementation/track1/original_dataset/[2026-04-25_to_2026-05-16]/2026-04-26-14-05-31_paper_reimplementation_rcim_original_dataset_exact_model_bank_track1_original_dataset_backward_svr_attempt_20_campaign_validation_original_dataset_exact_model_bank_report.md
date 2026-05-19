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
- random seed: `61`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `36.991%`
- winning mean component MAE: `0.125445`
- winning mean component RMSE: `0.239319`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 36.991 | 0.125445 | 0.239319 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `SVR` | 0.002619 | 0.003183 | 32.841 |
| `fft_y_Bw_filtered_ampl_1` | `SVR` | 0.000198 | 0.000215 | 1.159 |
| `fft_y_Bw_filtered_phase_1` | `SVR` | 0.002333 | 0.003661 | 51.921 |
| `fft_y_Bw_filtered_ampl_3` | `SVR` | 0.000192 | 0.000210 | 22.099 |
| `fft_y_Bw_filtered_phase_3` | `SVR` | 0.027960 | 0.039192 | 2.034 |
| `fft_y_Bw_filtered_ampl_39` | `SVR` | 0.000117 | 0.000132 | 29.243 |
| `fft_y_Bw_filtered_phase_39` | `SVR` | 0.584225 | 1.040109 | 21.038 |
| `fft_y_Bw_filtered_ampl_40` | `SVR` | 0.000044 | 0.000058 | 13.214 |
| `fft_y_Bw_filtered_phase_40` | `SVR` | 0.162229 | 0.313814 | 48.799 |
| `fft_y_Bw_filtered_ampl_78` | `SVR` | 0.000286 | 0.000349 | 28.698 |
| `fft_y_Bw_filtered_phase_78` | `SVR` | 0.131372 | 0.183879 | 46.423 |
| `fft_y_Bw_filtered_ampl_81` | `SVR` | 0.000037 | 0.000041 | 34.893 |
| `fft_y_Bw_filtered_phase_81` | `SVR` | 0.123544 | 0.162037 | 82.002 |
| `fft_y_Bw_filtered_ampl_156` | `SVR` | 0.000742 | 0.003043 | 54.610 |
| `fft_y_Bw_filtered_phase_156` | `SVR` | 0.437366 | 0.895018 | 30.604 |
| `fft_y_Bw_filtered_ampl_162` | `SVR` | 0.000506 | 0.001530 | 89.583 |
| `fft_y_Bw_filtered_phase_162` | `SVR` | 0.362640 | 0.711994 | 18.913 |
| `fft_y_Bw_filtered_ampl_240` | `SVR` | 0.000249 | 0.000358 | 44.679 |
| `fft_y_Bw_filtered_phase_240` | `SVR` | 0.546792 | 1.188234 | 50.070 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/svr/2026-04-26_track1_backward_svr_original_dataset_mega_campaign/020_track1_original_dataset_backward_svr_attempt_20.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-04-46__track1_original_dataset_backward_svr_attempt_20_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-04-46__track1_original_dataset_backward_svr_attempt_20_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-04-46__track1_original_dataset_backward_svr_attempt_20_campaign_validation/validation_summary.yaml`
