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
- random seed: `11`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `34.003%`
- winning mean component MAE: `0.070313`
- winning mean component RMSE: `0.144622`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 34.003 | 0.070313 | 0.144622 | `{'estimator__learning_rate': 0.19, 'estimator__max_depth': 9, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `HGBM` | 0.002625 | 0.003210 | 75.180 |
| `fft_y_Bw_filtered_ampl_1` | `HGBM` | 0.000027 | 0.000035 | 0.158 |
| `fft_y_Bw_filtered_phase_1` | `HGBM` | 0.001694 | 0.002621 | 48.564 |
| `fft_y_Bw_filtered_ampl_3` | `HGBM` | 0.000022 | 0.000034 | 2.243 |
| `fft_y_Bw_filtered_phase_3` | `HGBM` | 0.022805 | 0.033196 | 1.680 |
| `fft_y_Bw_filtered_ampl_39` | `HGBM` | 0.000016 | 0.000024 | 3.680 |
| `fft_y_Bw_filtered_phase_39` | `HGBM` | 0.385251 | 0.978658 | 13.359 |
| `fft_y_Bw_filtered_ampl_40` | `HGBM` | 0.000034 | 0.000053 | 10.785 |
| `fft_y_Bw_filtered_phase_40` | `HGBM` | 0.081643 | 0.109993 | 42.970 |
| `fft_y_Bw_filtered_ampl_78` | `HGBM` | 0.000029 | 0.000043 | 4.568 |
| `fft_y_Bw_filtered_phase_78` | `HGBM` | 0.059135 | 0.107684 | 23.785 |
| `fft_y_Bw_filtered_ampl_81` | `HGBM` | 0.000009 | 0.000014 | 7.170 |
| `fft_y_Bw_filtered_phase_81` | `HGBM` | 0.096633 | 0.127255 | 294.158 |
| `fft_y_Bw_filtered_ampl_156` | `HGBM` | 0.000477 | 0.001155 | 32.824 |
| `fft_y_Bw_filtered_phase_156` | `HGBM` | 0.225479 | 0.508407 | 15.648 |
| `fft_y_Bw_filtered_ampl_162` | `HGBM` | 0.000182 | 0.000481 | 18.588 |
| `fft_y_Bw_filtered_phase_162` | `HGBM` | 0.110395 | 0.209552 | 6.990 |
| `fft_y_Bw_filtered_ampl_240` | `HGBM` | 0.000104 | 0.000179 | 17.219 |
| `fft_y_Bw_filtered_phase_240` | `HGBM` | 0.349381 | 0.665228 | 26.490 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/hgbm/2026-04-26_track1_backward_hgbm_original_dataset_mega_campaign/005_track1_original_dataset_backward_hgbm_attempt_05.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-24-18__track1_original_dataset_backward_hgbm_attempt_05_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-24-18__track1_original_dataset_backward_hgbm_attempt_05_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-24-18__track1_original_dataset_backward_hgbm_attempt_05_campaign_validation/validation_summary.yaml`
