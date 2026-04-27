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
- random seed: `19`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `35.279%`
- winning mean component MAE: `0.088923`
- winning mean component RMSE: `0.174996`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 35.279 | 0.088923 | 0.174996 | `{'estimator__learning_rate': 0.2, 'estimator__max_depth': 13, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | 0.002586 | 0.003958 | 15.406 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | 0.000027 | 0.000037 | 0.157 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | 0.001479 | 0.002115 | 109.112 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | 0.000016 | 0.000022 | 1.981 |
| `fft_y_Fw_filtered_phase_3` | `HGBM` | 0.023293 | 0.031794 | 1.288 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | 0.000026 | 0.000038 | 2.241 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | 0.017429 | 0.026290 | 1.433 |
| `fft_y_Fw_filtered_ampl_40` | `HGBM` | 0.000025 | 0.000039 | 3.200 |
| `fft_y_Fw_filtered_phase_40` | `HGBM` | 0.037440 | 0.060625 | 59.697 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | 0.000029 | 0.000037 | 8.780 |
| `fft_y_Fw_filtered_phase_78` | `HGBM` | 0.074033 | 0.120953 | 314.446 |
| `fft_y_Fw_filtered_ampl_81` | `HGBM` | 0.000010 | 0.000013 | 3.433 |
| `fft_y_Fw_filtered_phase_81` | `HGBM` | 0.058499 | 0.089247 | 5.154 |
| `fft_y_Fw_filtered_ampl_156` | `HGBM` | 0.000115 | 0.000317 | 22.278 |
| `fft_y_Fw_filtered_phase_156` | `HGBM` | 0.661622 | 1.185527 | 30.877 |
| `fft_y_Fw_filtered_ampl_162` | `HGBM` | 0.000123 | 0.000294 | 20.825 |
| `fft_y_Fw_filtered_phase_162` | `HGBM` | 0.380041 | 0.791968 | 18.002 |
| `fft_y_Fw_filtered_ampl_240` | `HGBM` | 0.000041 | 0.000143 | 28.129 |
| `fft_y_Fw_filtered_phase_240` | `HGBM` | 0.432709 | 1.011504 | 23.859 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/hgbm/2026-04-26_track1_forward_hgbm_original_dataset_mega_campaign/009_track1_original_dataset_forward_hgbm_attempt_09.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-47-19__track1_original_dataset_forward_hgbm_attempt_09_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-47-19__track1_original_dataset_forward_hgbm_attempt_09_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-47-19__track1_original_dataset_forward_hgbm_attempt_09_campaign_validation/validation_summary.yaml`
