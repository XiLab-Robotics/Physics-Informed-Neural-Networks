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
- random seed: `7`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `42.518%`
- winning mean component MAE: `0.149738`
- winning mean component RMSE: `0.274508`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 42.518 | 0.149738 | 0.274508 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `SVR` | 0.002808 | 0.003431 | 27.992 |
| `fft_y_Bw_filtered_ampl_1` | `SVR` | 0.000181 | 0.000194 | 1.056 |
| `fft_y_Bw_filtered_phase_1` | `SVR` | 0.002094 | 0.003142 | 84.645 |
| `fft_y_Bw_filtered_ampl_3` | `SVR` | 0.000132 | 0.000156 | 14.386 |
| `fft_y_Bw_filtered_phase_3` | `SVR` | 0.028260 | 0.039817 | 2.048 |
| `fft_y_Bw_filtered_ampl_39` | `SVR` | 0.000109 | 0.000122 | 26.523 |
| `fft_y_Bw_filtered_phase_39` | `SVR` | 0.712794 | 1.158231 | 25.211 |
| `fft_y_Bw_filtered_ampl_40` | `SVR` | 0.000045 | 0.000059 | 14.076 |
| `fft_y_Bw_filtered_phase_40` | `SVR` | 0.160847 | 0.302039 | 60.899 |
| `fft_y_Bw_filtered_ampl_78` | `SVR` | 0.000175 | 0.000197 | 23.544 |
| `fft_y_Bw_filtered_phase_78` | `SVR` | 0.141986 | 0.317171 | 30.271 |
| `fft_y_Bw_filtered_ampl_81` | `SVR` | 0.000044 | 0.000048 | 41.693 |
| `fft_y_Bw_filtered_phase_81` | `SVR` | 0.123957 | 0.168478 | 77.125 |
| `fft_y_Bw_filtered_ampl_156` | `SVR` | 0.000799 | 0.003178 | 55.305 |
| `fft_y_Bw_filtered_phase_156` | `SVR` | 0.473886 | 0.938192 | 41.363 |
| `fft_y_Bw_filtered_ampl_162` | `SVR` | 0.000628 | 0.002094 | 109.404 |
| `fft_y_Bw_filtered_phase_162` | `SVR` | 0.399324 | 0.705789 | 21.267 |
| `fft_y_Bw_filtered_ampl_240` | `SVR` | 0.000443 | 0.001190 | 66.715 |
| `fft_y_Bw_filtered_phase_240` | `SVR` | 0.796507 | 1.572128 | 84.322 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/svr/2026-04-26_track1_backward_svr_original_dataset_mega_campaign/003_track1_original_dataset_backward_svr_attempt_03.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-51-41__track1_original_dataset_backward_svr_attempt_03_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-51-41__track1_original_dataset_backward_svr_attempt_03_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-13-51-41__track1_original_dataset_backward_svr_attempt_03_campaign_validation/validation_summary.yaml`
