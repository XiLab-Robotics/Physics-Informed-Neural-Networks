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
- random seed: `15`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `18.548%`
- winning mean component MAE: `0.087628`
- winning mean component RMSE: `0.172207`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 18.548 | 0.087628 | 0.172207 | `{'estimator__learning_rate': 0.18, 'estimator__max_depth': 13, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | 0.002459 | 0.003893 | 15.440 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | 0.000028 | 0.000038 | 0.162 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | 0.001983 | 0.002770 | 29.103 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | 0.000017 | 0.000023 | 2.134 |
| `fft_y_Fw_filtered_phase_3` | `HGBM` | 0.023036 | 0.030511 | 1.290 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | 0.000023 | 0.000030 | 2.054 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | 0.021867 | 0.031950 | 1.797 |
| `fft_y_Fw_filtered_ampl_40` | `HGBM` | 0.000027 | 0.000039 | 3.589 |
| `fft_y_Fw_filtered_phase_40` | `HGBM` | 0.040122 | 0.064109 | 59.315 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | 0.000028 | 0.000040 | 20.949 |
| `fft_y_Fw_filtered_phase_78` | `HGBM` | 0.115881 | 0.351180 | 57.038 |
| `fft_y_Fw_filtered_ampl_81` | `HGBM` | 0.000011 | 0.000016 | 3.544 |
| `fft_y_Fw_filtered_phase_81` | `HGBM` | 0.057180 | 0.089022 | 8.149 |
| `fft_y_Fw_filtered_ampl_156` | `HGBM` | 0.000116 | 0.000353 | 20.797 |
| `fft_y_Fw_filtered_phase_156` | `HGBM` | 0.668617 | 1.089898 | 50.985 |
| `fft_y_Fw_filtered_ampl_162` | `HGBM` | 0.000158 | 0.000568 | 22.767 |
| `fft_y_Fw_filtered_phase_162` | `HGBM` | 0.402190 | 0.817588 | 22.079 |
| `fft_y_Fw_filtered_ampl_240` | `HGBM` | 0.000038 | 0.000064 | 14.311 |
| `fft_y_Fw_filtered_phase_240` | `HGBM` | 0.331156 | 0.789839 | 16.913 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/hgbm/2026-04-26_track1_forward_hgbm_original_dataset_mega_campaign/007_track1_original_dataset_forward_hgbm_attempt_07.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-44-02__track1_original_dataset_forward_hgbm_attempt_07_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-44-02__track1_original_dataset_forward_hgbm_attempt_07_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-44-02__track1_original_dataset_forward_hgbm_attempt_07_campaign_validation/validation_summary.yaml`
