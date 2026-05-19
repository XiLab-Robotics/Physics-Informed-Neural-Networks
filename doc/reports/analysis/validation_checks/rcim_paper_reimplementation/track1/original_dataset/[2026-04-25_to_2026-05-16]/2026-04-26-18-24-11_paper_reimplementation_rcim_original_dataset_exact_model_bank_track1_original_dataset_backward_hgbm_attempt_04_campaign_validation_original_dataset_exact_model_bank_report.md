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
- random seed: `9`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `45.202%`
- winning mean component MAE: `0.064551`
- winning mean component RMSE: `0.121582`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 45.202 | 0.064551 | 0.121582 | `{'estimator__learning_rate': 0.21, 'estimator__max_depth': 13, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `HGBM` | 0.002589 | 0.003093 | 61.473 |
| `fft_y_Bw_filtered_ampl_1` | `HGBM` | 0.000026 | 0.000037 | 0.150 |
| `fft_y_Bw_filtered_phase_1` | `HGBM` | 0.001813 | 0.002410 | 47.121 |
| `fft_y_Bw_filtered_ampl_3` | `HGBM` | 0.000018 | 0.000026 | 1.906 |
| `fft_y_Bw_filtered_phase_3` | `HGBM` | 0.018697 | 0.025737 | 1.402 |
| `fft_y_Bw_filtered_ampl_39` | `HGBM` | 0.000016 | 0.000023 | 3.489 |
| `fft_y_Bw_filtered_phase_39` | `HGBM` | 0.330255 | 0.793307 | 11.445 |
| `fft_y_Bw_filtered_ampl_40` | `HGBM` | 0.000024 | 0.000035 | 7.760 |
| `fft_y_Bw_filtered_phase_40` | `HGBM` | 0.108647 | 0.170287 | 24.949 |
| `fft_y_Bw_filtered_ampl_78` | `HGBM` | 0.000031 | 0.000044 | 21.816 |
| `fft_y_Bw_filtered_phase_78` | `HGBM` | 0.084514 | 0.249349 | 25.092 |
| `fft_y_Bw_filtered_ampl_81` | `HGBM` | 0.000009 | 0.000013 | 7.191 |
| `fft_y_Bw_filtered_phase_81` | `HGBM` | 0.108524 | 0.145777 | 558.396 |
| `fft_y_Bw_filtered_ampl_156` | `HGBM` | 0.000389 | 0.001271 | 17.726 |
| `fft_y_Bw_filtered_phase_156` | `HGBM` | 0.143620 | 0.247514 | 17.608 |
| `fft_y_Bw_filtered_ampl_162` | `HGBM` | 0.000141 | 0.000402 | 15.880 |
| `fft_y_Bw_filtered_phase_162` | `HGBM` | 0.101584 | 0.168426 | 6.792 |
| `fft_y_Bw_filtered_ampl_240` | `HGBM` | 0.000107 | 0.000330 | 12.939 |
| `fft_y_Bw_filtered_phase_240` | `HGBM` | 0.325460 | 0.501976 | 15.697 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/hgbm/2026-04-26_track1_backward_hgbm_original_dataset_mega_campaign/004_track1_original_dataset_backward_hgbm_attempt_04.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-22-45__track1_original_dataset_backward_hgbm_attempt_04_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-22-45__track1_original_dataset_backward_hgbm_attempt_04_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-22-45__track1_original_dataset_backward_hgbm_attempt_04_campaign_validation/validation_summary.yaml`
