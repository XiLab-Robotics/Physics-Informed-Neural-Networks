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
- random seed: `0`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `22.382%`
- winning mean component MAE: `0.065934`
- winning mean component RMSE: `0.139199`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 22.382 | 0.065934 | 0.139199 | `{'estimator__learning_rate': 0.18, 'estimator__max_depth': 9, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `HGBM` | 0.002538 | 0.003180 | 109.895 |
| `fft_y_Bw_filtered_ampl_1` | `HGBM` | 0.000025 | 0.000036 | 0.147 |
| `fft_y_Bw_filtered_phase_1` | `HGBM` | 0.001661 | 0.002302 | 24.413 |
| `fft_y_Bw_filtered_ampl_3` | `HGBM` | 0.000020 | 0.000029 | 2.133 |
| `fft_y_Bw_filtered_phase_3` | `HGBM` | 0.018765 | 0.027783 | 1.348 |
| `fft_y_Bw_filtered_ampl_39` | `HGBM` | 0.000015 | 0.000020 | 3.506 |
| `fft_y_Bw_filtered_phase_39` | `HGBM` | 0.355576 | 0.883637 | 12.427 |
| `fft_y_Bw_filtered_ampl_40` | `HGBM` | 0.000024 | 0.000033 | 8.127 |
| `fft_y_Bw_filtered_phase_40` | `HGBM` | 0.099157 | 0.129443 | 38.735 |
| `fft_y_Bw_filtered_ampl_78` | `HGBM` | 0.000024 | 0.000033 | 2.908 |
| `fft_y_Bw_filtered_phase_78` | `HGBM` | 0.051079 | 0.082500 | 72.226 |
| `fft_y_Bw_filtered_ampl_81` | `HGBM` | 0.000010 | 0.000014 | 8.183 |
| `fft_y_Bw_filtered_phase_81` | `HGBM` | 0.087795 | 0.116975 | 33.789 |
| `fft_y_Bw_filtered_ampl_156` | `HGBM` | 0.000287 | 0.000977 | 18.569 |
| `fft_y_Bw_filtered_phase_156` | `HGBM` | 0.164608 | 0.449282 | 24.320 |
| `fft_y_Bw_filtered_ampl_162` | `HGBM` | 0.000138 | 0.000356 | 16.083 |
| `fft_y_Bw_filtered_phase_162` | `HGBM` | 0.089466 | 0.140937 | 5.181 |
| `fft_y_Bw_filtered_ampl_240` | `HGBM` | 0.000140 | 0.000379 | 22.831 |
| `fft_y_Bw_filtered_phase_240` | `HGBM` | 0.381412 | 0.806872 | 20.438 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/hgbm/2026-04-26_track1_backward_hgbm_original_dataset_mega_campaign/001_track1_original_dataset_backward_hgbm_attempt_01.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-18-03__track1_original_dataset_backward_hgbm_attempt_01_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-18-03__track1_original_dataset_backward_hgbm_attempt_01_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-18-03__track1_original_dataset_backward_hgbm_attempt_01_campaign_validation/validation_summary.yaml`
