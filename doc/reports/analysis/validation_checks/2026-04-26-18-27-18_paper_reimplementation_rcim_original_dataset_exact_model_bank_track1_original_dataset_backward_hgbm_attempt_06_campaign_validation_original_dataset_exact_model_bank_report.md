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

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `20.491%`
- winning mean component MAE: `0.077449`
- winning mean component RMSE: `0.161834`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 20.491 | 0.077449 | 0.161834 | `{'estimator__learning_rate': 0.18, 'estimator__max_depth': 12, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `HGBM` | 0.002255 | 0.003034 | 37.498 |
| `fft_y_Bw_filtered_ampl_1` | `HGBM` | 0.000026 | 0.000036 | 0.149 |
| `fft_y_Bw_filtered_phase_1` | `HGBM` | 0.001501 | 0.002034 | 85.763 |
| `fft_y_Bw_filtered_ampl_3` | `HGBM` | 0.000017 | 0.000025 | 1.703 |
| `fft_y_Bw_filtered_phase_3` | `HGBM` | 0.018734 | 0.025101 | 1.371 |
| `fft_y_Bw_filtered_ampl_39` | `HGBM` | 0.000015 | 0.000020 | 3.303 |
| `fft_y_Bw_filtered_phase_39` | `HGBM` | 0.308664 | 0.820198 | 10.608 |
| `fft_y_Bw_filtered_ampl_40` | `HGBM` | 0.000031 | 0.000045 | 10.178 |
| `fft_y_Bw_filtered_phase_40` | `HGBM` | 0.102201 | 0.151590 | 39.157 |
| `fft_y_Bw_filtered_ampl_78` | `HGBM` | 0.000033 | 0.000044 | 4.321 |
| `fft_y_Bw_filtered_phase_78` | `HGBM` | 0.071145 | 0.126012 | 25.079 |
| `fft_y_Bw_filtered_ampl_81` | `HGBM` | 0.000009 | 0.000014 | 7.102 |
| `fft_y_Bw_filtered_phase_81` | `HGBM` | 0.099006 | 0.131603 | 57.467 |
| `fft_y_Bw_filtered_ampl_156` | `HGBM` | 0.000232 | 0.000499 | 24.398 |
| `fft_y_Bw_filtered_phase_156` | `HGBM` | 0.210680 | 0.534996 | 18.076 |
| `fft_y_Bw_filtered_ampl_162` | `HGBM` | 0.000170 | 0.000446 | 15.725 |
| `fft_y_Bw_filtered_phase_162` | `HGBM` | 0.115491 | 0.208902 | 6.353 |
| `fft_y_Bw_filtered_ampl_240` | `HGBM` | 0.000135 | 0.000358 | 18.555 |
| `fft_y_Bw_filtered_phase_240` | `HGBM` | 0.541193 | 1.069895 | 22.524 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/hgbm/2026-04-26_track1_backward_hgbm_original_dataset_mega_campaign/006_track1_original_dataset_backward_hgbm_attempt_06.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-25-52__track1_original_dataset_backward_hgbm_attempt_06_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-25-52__track1_original_dataset_backward_hgbm_attempt_06_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-25-52__track1_original_dataset_backward_hgbm_attempt_06_campaign_validation/validation_summary.yaml`
