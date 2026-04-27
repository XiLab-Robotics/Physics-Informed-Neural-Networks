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
- random seed: `29`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `32.050%`
- winning mean component MAE: `0.069216`
- winning mean component RMSE: `0.148512`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 32.050 | 0.069216 | 0.148512 | `{'estimator__learning_rate': 0.21, 'estimator__max_depth': 10, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `HGBM` | 0.002890 | 0.004006 | 72.088 |
| `fft_y_Bw_filtered_ampl_1` | `HGBM` | 0.000028 | 0.000039 | 0.164 |
| `fft_y_Bw_filtered_phase_1` | `HGBM` | 0.001752 | 0.002244 | 84.620 |
| `fft_y_Bw_filtered_ampl_3` | `HGBM` | 0.000022 | 0.000034 | 2.347 |
| `fft_y_Bw_filtered_phase_3` | `HGBM` | 0.023437 | 0.037932 | 1.716 |
| `fft_y_Bw_filtered_ampl_39` | `HGBM` | 0.000017 | 0.000027 | 4.211 |
| `fft_y_Bw_filtered_phase_39` | `HGBM` | 0.304612 | 0.839842 | 10.883 |
| `fft_y_Bw_filtered_ampl_40` | `HGBM` | 0.000026 | 0.000039 | 8.641 |
| `fft_y_Bw_filtered_phase_40` | `HGBM` | 0.120424 | 0.237495 | 43.384 |
| `fft_y_Bw_filtered_ampl_78` | `HGBM` | 0.000031 | 0.000052 | 4.043 |
| `fft_y_Bw_filtered_phase_78` | `HGBM` | 0.074954 | 0.124696 | 26.001 |
| `fft_y_Bw_filtered_ampl_81` | `HGBM` | 0.000011 | 0.000018 | 7.920 |
| `fft_y_Bw_filtered_phase_81` | `HGBM` | 0.112213 | 0.167127 | 221.251 |
| `fft_y_Bw_filtered_ampl_156` | `HGBM` | 0.000396 | 0.001171 | 16.472 |
| `fft_y_Bw_filtered_phase_156` | `HGBM` | 0.200497 | 0.498353 | 20.948 |
| `fft_y_Bw_filtered_ampl_162` | `HGBM` | 0.000103 | 0.000195 | 17.833 |
| `fft_y_Bw_filtered_phase_162` | `HGBM` | 0.099161 | 0.171374 | 6.120 |
| `fft_y_Bw_filtered_ampl_240` | `HGBM` | 0.000100 | 0.000197 | 26.946 |
| `fft_y_Bw_filtered_phase_240` | `HGBM` | 0.374424 | 0.736884 | 33.355 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/hgbm/2026-04-26_track1_backward_hgbm_original_dataset_mega_campaign/013_track1_original_dataset_backward_hgbm_attempt_13.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-36-45__track1_original_dataset_backward_hgbm_attempt_13_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-36-45__track1_original_dataset_backward_hgbm_attempt_13_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-36-45__track1_original_dataset_backward_hgbm_attempt_13_campaign_validation/validation_summary.yaml`
