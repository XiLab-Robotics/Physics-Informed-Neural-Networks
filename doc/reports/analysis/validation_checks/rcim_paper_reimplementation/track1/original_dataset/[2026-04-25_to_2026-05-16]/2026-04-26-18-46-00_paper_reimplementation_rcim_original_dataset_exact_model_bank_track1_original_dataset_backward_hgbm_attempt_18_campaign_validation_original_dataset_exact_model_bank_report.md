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
- random seed: `53`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `31.883%`
- winning mean component MAE: `0.068708`
- winning mean component RMSE: `0.145765`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 31.883 | 0.068708 | 0.145765 | `{'estimator__learning_rate': 0.21, 'estimator__max_depth': 12, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `HGBM` | 0.002656 | 0.003286 | 37.864 |
| `fft_y_Bw_filtered_ampl_1` | `HGBM` | 0.000030 | 0.000044 | 0.176 |
| `fft_y_Bw_filtered_phase_1` | `HGBM` | 0.001942 | 0.002613 | 34.584 |
| `fft_y_Bw_filtered_ampl_3` | `HGBM` | 0.000023 | 0.000037 | 2.446 |
| `fft_y_Bw_filtered_phase_3` | `HGBM` | 0.019666 | 0.049376 | 1.490 |
| `fft_y_Bw_filtered_ampl_39` | `HGBM` | 0.000016 | 0.000022 | 3.543 |
| `fft_y_Bw_filtered_phase_39` | `HGBM` | 0.264429 | 0.831210 | 9.897 |
| `fft_y_Bw_filtered_ampl_40` | `HGBM` | 0.000027 | 0.000041 | 8.853 |
| `fft_y_Bw_filtered_phase_40` | `HGBM` | 0.114523 | 0.183720 | 220.334 |
| `fft_y_Bw_filtered_ampl_78` | `HGBM` | 0.000034 | 0.000047 | 8.992 |
| `fft_y_Bw_filtered_phase_78` | `HGBM` | 0.086236 | 0.167705 | 33.339 |
| `fft_y_Bw_filtered_ampl_81` | `HGBM` | 0.000009 | 0.000011 | 7.195 |
| `fft_y_Bw_filtered_phase_81` | `HGBM` | 0.114404 | 0.193675 | 126.582 |
| `fft_y_Bw_filtered_ampl_156` | `HGBM` | 0.000386 | 0.001315 | 20.178 |
| `fft_y_Bw_filtered_phase_156` | `HGBM` | 0.144479 | 0.270785 | 21.345 |
| `fft_y_Bw_filtered_ampl_162` | `HGBM` | 0.000140 | 0.000323 | 18.691 |
| `fft_y_Bw_filtered_phase_162` | `HGBM` | 0.122866 | 0.300939 | 6.710 |
| `fft_y_Bw_filtered_ampl_240` | `HGBM` | 0.000082 | 0.000129 | 17.673 |
| `fft_y_Bw_filtered_phase_240` | `HGBM` | 0.433509 | 0.764248 | 25.889 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/hgbm/2026-04-26_track1_backward_hgbm_original_dataset_mega_campaign/018_track1_original_dataset_backward_hgbm_attempt_18.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-44-32__track1_original_dataset_backward_hgbm_attempt_18_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-44-32__track1_original_dataset_backward_hgbm_attempt_18_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-44-32__track1_original_dataset_backward_hgbm_attempt_18_campaign_validation/validation_summary.yaml`
