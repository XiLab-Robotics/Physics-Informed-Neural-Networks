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
- random seed: `23`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `28.294%`
- winning mean component MAE: `0.057420`
- winning mean component RMSE: `0.122843`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 28.294 | 0.057420 | 0.122843 | `{'estimator__learning_rate': 0.18, 'estimator__max_depth': 10, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `HGBM` | 0.002577 | 0.003079 | 66.405 |
| `fft_y_Bw_filtered_ampl_1` | `HGBM` | 0.000024 | 0.000033 | 0.142 |
| `fft_y_Bw_filtered_phase_1` | `HGBM` | 0.001823 | 0.002622 | 103.545 |
| `fft_y_Bw_filtered_ampl_3` | `HGBM` | 0.000018 | 0.000029 | 1.726 |
| `fft_y_Bw_filtered_phase_3` | `HGBM` | 0.019014 | 0.024225 | 1.436 |
| `fft_y_Bw_filtered_ampl_39` | `HGBM` | 0.000015 | 0.000020 | 3.411 |
| `fft_y_Bw_filtered_phase_39` | `HGBM` | 0.275506 | 0.719084 | 9.952 |
| `fft_y_Bw_filtered_ampl_40` | `HGBM` | 0.000028 | 0.000039 | 9.417 |
| `fft_y_Bw_filtered_phase_40` | `HGBM` | 0.088094 | 0.115684 | 47.240 |
| `fft_y_Bw_filtered_ampl_78` | `HGBM` | 0.000031 | 0.000040 | 4.449 |
| `fft_y_Bw_filtered_phase_78` | `HGBM` | 0.059542 | 0.098010 | 19.888 |
| `fft_y_Bw_filtered_ampl_81` | `HGBM` | 0.000009 | 0.000013 | 8.189 |
| `fft_y_Bw_filtered_phase_81` | `HGBM` | 0.098241 | 0.126298 | 174.517 |
| `fft_y_Bw_filtered_ampl_156` | `HGBM` | 0.000203 | 0.000691 | 20.030 |
| `fft_y_Bw_filtered_phase_156` | `HGBM` | 0.166241 | 0.416129 | 21.179 |
| `fft_y_Bw_filtered_ampl_162` | `HGBM` | 0.000074 | 0.000174 | 8.472 |
| `fft_y_Bw_filtered_phase_162` | `HGBM` | 0.112560 | 0.263453 | 6.550 |
| `fft_y_Bw_filtered_ampl_240` | `HGBM` | 0.000114 | 0.000196 | 16.996 |
| `fft_y_Bw_filtered_phase_240` | `HGBM` | 0.266872 | 0.564205 | 14.050 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/hgbm/2026-04-26_track1_backward_hgbm_original_dataset_mega_campaign/011_track1_original_dataset_backward_hgbm_attempt_11.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-33-37__track1_original_dataset_backward_hgbm_attempt_11_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-33-37__track1_original_dataset_backward_hgbm_attempt_11_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-33-37__track1_original_dataset_backward_hgbm_attempt_11_campaign_validation/validation_summary.yaml`
