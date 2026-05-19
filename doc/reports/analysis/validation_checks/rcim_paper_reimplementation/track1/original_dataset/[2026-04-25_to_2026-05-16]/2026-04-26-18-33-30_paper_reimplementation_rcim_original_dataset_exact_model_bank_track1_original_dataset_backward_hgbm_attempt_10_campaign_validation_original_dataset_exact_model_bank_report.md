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
- random seed: `21`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `22.238%`
- winning mean component MAE: `0.065304`
- winning mean component RMSE: `0.140381`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 22.238 | 0.065304 | 0.140381 | `{'estimator__learning_rate': 0.18, 'estimator__max_depth': 10, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `HGBM` | 0.002583 | 0.003307 | 68.274 |
| `fft_y_Bw_filtered_ampl_1` | `HGBM` | 0.000023 | 0.000030 | 0.135 |
| `fft_y_Bw_filtered_phase_1` | `HGBM` | 0.001644 | 0.002158 | 78.319 |
| `fft_y_Bw_filtered_ampl_3` | `HGBM` | 0.000023 | 0.000032 | 2.451 |
| `fft_y_Bw_filtered_phase_3` | `HGBM` | 0.018412 | 0.026609 | 1.360 |
| `fft_y_Bw_filtered_ampl_39` | `HGBM` | 0.000019 | 0.000025 | 4.274 |
| `fft_y_Bw_filtered_phase_39` | `HGBM` | 0.322922 | 0.966127 | 11.390 |
| `fft_y_Bw_filtered_ampl_40` | `HGBM` | 0.000030 | 0.000044 | 10.279 |
| `fft_y_Bw_filtered_phase_40` | `HGBM` | 0.098447 | 0.137178 | 46.467 |
| `fft_y_Bw_filtered_ampl_78` | `HGBM` | 0.000032 | 0.000045 | 3.708 |
| `fft_y_Bw_filtered_phase_78` | `HGBM` | 0.063431 | 0.112200 | 25.348 |
| `fft_y_Bw_filtered_ampl_81` | `HGBM` | 0.000011 | 0.000018 | 8.927 |
| `fft_y_Bw_filtered_phase_81` | `HGBM` | 0.086130 | 0.114162 | 27.643 |
| `fft_y_Bw_filtered_ampl_156` | `HGBM` | 0.000411 | 0.001120 | 27.372 |
| `fft_y_Bw_filtered_phase_156` | `HGBM` | 0.233287 | 0.594643 | 34.561 |
| `fft_y_Bw_filtered_ampl_162` | `HGBM` | 0.000196 | 0.000505 | 16.369 |
| `fft_y_Bw_filtered_phase_162` | `HGBM` | 0.115030 | 0.244232 | 5.921 |
| `fft_y_Bw_filtered_ampl_240` | `HGBM` | 0.000138 | 0.000283 | 19.604 |
| `fft_y_Bw_filtered_phase_240` | `HGBM` | 0.298005 | 0.464525 | 30.128 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/hgbm/2026-04-26_track1_backward_hgbm_original_dataset_mega_campaign/010_track1_original_dataset_backward_hgbm_attempt_10.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-32-03__track1_original_dataset_backward_hgbm_attempt_10_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-32-03__track1_original_dataset_backward_hgbm_attempt_10_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-32-03__track1_original_dataset_backward_hgbm_attempt_10_campaign_validation/validation_summary.yaml`
