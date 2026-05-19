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
- random seed: `42`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `24.915%`
- winning mean component MAE: `0.076360`
- winning mean component RMSE: `0.143156`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 24.915 | 0.076360 | 0.143156 | `{'estimator__learning_rate': 0.19, 'estimator__max_depth': 11, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | 0.002554 | 0.003050 | 5.038 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | 0.000025 | 0.000032 | 0.148 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | 0.001641 | 0.002231 | 104.578 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | 0.000017 | 0.000022 | 2.019 |
| `fft_y_Fw_filtered_phase_3` | `HGBM` | 0.021967 | 0.027781 | 1.217 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | 0.000027 | 0.000038 | 2.271 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | 0.017630 | 0.022956 | 1.502 |
| `fft_y_Fw_filtered_ampl_40` | `HGBM` | 0.000029 | 0.000042 | 3.708 |
| `fft_y_Fw_filtered_phase_40` | `HGBM` | 0.044090 | 0.063512 | 60.397 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | 0.000029 | 0.000041 | 6.572 |
| `fft_y_Fw_filtered_phase_78` | `HGBM` | 0.078506 | 0.154526 | 90.148 |
| `fft_y_Fw_filtered_ampl_81` | `HGBM` | 0.000009 | 0.000012 | 2.865 |
| `fft_y_Fw_filtered_phase_81` | `HGBM` | 0.050222 | 0.076147 | 5.011 |
| `fft_y_Fw_filtered_ampl_156` | `HGBM` | 0.000082 | 0.000250 | 19.642 |
| `fft_y_Fw_filtered_phase_156` | `HGBM` | 0.476110 | 0.748709 | 23.055 |
| `fft_y_Fw_filtered_ampl_162` | `HGBM` | 0.000103 | 0.000244 | 26.332 |
| `fft_y_Fw_filtered_phase_162` | `HGBM` | 0.408481 | 0.907873 | 16.325 |
| `fft_y_Fw_filtered_ampl_240` | `HGBM` | 0.000028 | 0.000044 | 7.088 |
| `fft_y_Fw_filtered_phase_240` | `HGBM` | 0.349299 | 0.712453 | 95.467 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/forward_remote_micro/hgbm/2026-04-25_track1_forward_hgbm_remote_micro/001_track1_original_dataset_forward_hgbm_remote_micro.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_micro/2026-04-25-23-20-45__track1_original_dataset_forward_hgbm_remote_micro_campaign_run`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_micro/2026-04-25-23-20-45__track1_original_dataset_forward_hgbm_remote_micro_campaign_run/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_remote_micro/2026-04-25-23-20-45__track1_original_dataset_forward_hgbm_remote_micro_campaign_run/validation_summary.yaml`
