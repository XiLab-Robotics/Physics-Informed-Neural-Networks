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
- random seed: `37`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `SVR`
- winning estimator: `SVR`
- winning mean component MAPE: `56.591%`
- winning mean component MAE: `0.130961`
- winning mean component RMSE: `0.248375`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `SVR` | `SVR` | 56.591 | 0.130961 | 0.248375 | - |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `SVR` | 0.002771 | 0.003349 | 37.252 |
| `fft_y_Bw_filtered_ampl_1` | `SVR` | 0.000195 | 0.000211 | 1.140 |
| `fft_y_Bw_filtered_phase_1` | `SVR` | 0.002288 | 0.003209 | 158.958 |
| `fft_y_Bw_filtered_ampl_3` | `SVR` | 0.000136 | 0.000158 | 15.886 |
| `fft_y_Bw_filtered_phase_3` | `SVR` | 0.028578 | 0.039100 | 1.975 |
| `fft_y_Bw_filtered_ampl_39` | `SVR` | 0.000110 | 0.000123 | 26.653 |
| `fft_y_Bw_filtered_phase_39` | `SVR` | 0.600008 | 1.068794 | 21.748 |
| `fft_y_Bw_filtered_ampl_40` | `SVR` | 0.000048 | 0.000061 | 15.848 |
| `fft_y_Bw_filtered_phase_40` | `SVR` | 0.141794 | 0.257017 | 61.462 |
| `fft_y_Bw_filtered_ampl_78` | `SVR` | 0.000187 | 0.000231 | 26.713 |
| `fft_y_Bw_filtered_phase_78` | `SVR` | 0.161237 | 0.344156 | 53.055 |
| `fft_y_Bw_filtered_ampl_81` | `SVR` | 0.000047 | 0.000052 | 46.631 |
| `fft_y_Bw_filtered_phase_81` | `SVR` | 0.117430 | 0.158214 | 280.320 |
| `fft_y_Bw_filtered_ampl_156` | `SVR` | 0.001011 | 0.003487 | 61.073 |
| `fft_y_Bw_filtered_phase_156` | `SVR` | 0.410703 | 0.807106 | 42.580 |
| `fft_y_Bw_filtered_ampl_162` | `SVR` | 0.000424 | 0.001488 | 115.550 |
| `fft_y_Bw_filtered_phase_162` | `SVR` | 0.373475 | 0.667091 | 20.177 |
| `fft_y_Bw_filtered_ampl_240` | `SVR` | 0.000323 | 0.000757 | 52.230 |
| `fft_y_Bw_filtered_phase_240` | `SVR` | 0.647487 | 1.364518 | 35.983 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/svr/2026-04-26_track1_backward_svr_original_dataset_mega_campaign/015_track1_original_dataset_backward_svr_attempt_15.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-00-49__track1_original_dataset_backward_svr_attempt_15_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-00-49__track1_original_dataset_backward_svr_attempt_15_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-14-00-49__track1_original_dataset_backward_svr_attempt_15_campaign_validation/validation_summary.yaml`
