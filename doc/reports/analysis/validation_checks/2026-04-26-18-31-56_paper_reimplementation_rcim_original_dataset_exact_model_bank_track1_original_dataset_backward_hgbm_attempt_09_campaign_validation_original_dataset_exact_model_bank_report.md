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
- random seed: `19`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `19.998%`
- winning mean component MAE: `0.063182`
- winning mean component RMSE: `0.128115`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 19.998 | 0.063182 | 0.128115 | `{'estimator__learning_rate': 0.19, 'estimator__max_depth': 10, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `HGBM` | 0.002600 | 0.003605 | 42.162 |
| `fft_y_Bw_filtered_ampl_1` | `HGBM` | 0.000025 | 0.000036 | 0.145 |
| `fft_y_Bw_filtered_phase_1` | `HGBM` | 0.001769 | 0.002481 | 49.083 |
| `fft_y_Bw_filtered_ampl_3` | `HGBM` | 0.000016 | 0.000023 | 1.642 |
| `fft_y_Bw_filtered_phase_3` | `HGBM` | 0.018029 | 0.031620 | 1.361 |
| `fft_y_Bw_filtered_ampl_39` | `HGBM` | 0.000018 | 0.000027 | 3.984 |
| `fft_y_Bw_filtered_phase_39` | `HGBM` | 0.420719 | 0.967047 | 14.246 |
| `fft_y_Bw_filtered_ampl_40` | `HGBM` | 0.000022 | 0.000031 | 7.307 |
| `fft_y_Bw_filtered_phase_40` | `HGBM` | 0.081062 | 0.145841 | 24.531 |
| `fft_y_Bw_filtered_ampl_78` | `HGBM` | 0.000030 | 0.000041 | 4.609 |
| `fft_y_Bw_filtered_phase_78` | `HGBM` | 0.050167 | 0.075864 | 23.790 |
| `fft_y_Bw_filtered_ampl_81` | `HGBM` | 0.000009 | 0.000013 | 7.781 |
| `fft_y_Bw_filtered_phase_81` | `HGBM` | 0.093219 | 0.144101 | 103.032 |
| `fft_y_Bw_filtered_ampl_156` | `HGBM` | 0.000232 | 0.000707 | 17.255 |
| `fft_y_Bw_filtered_phase_156` | `HGBM` | 0.149854 | 0.393597 | 17.162 |
| `fft_y_Bw_filtered_ampl_162` | `HGBM` | 0.000113 | 0.000266 | 11.745 |
| `fft_y_Bw_filtered_phase_162` | `HGBM` | 0.097608 | 0.204949 | 5.525 |
| `fft_y_Bw_filtered_ampl_240` | `HGBM` | 0.000101 | 0.000187 | 27.603 |
| `fft_y_Bw_filtered_phase_240` | `HGBM` | 0.284873 | 0.463757 | 16.998 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/hgbm/2026-04-26_track1_backward_hgbm_original_dataset_mega_campaign/009_track1_original_dataset_backward_hgbm_attempt_09.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-30-31__track1_original_dataset_backward_hgbm_attempt_09_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-30-31__track1_original_dataset_backward_hgbm_attempt_09_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-30-31__track1_original_dataset_backward_hgbm_attempt_09_campaign_validation/validation_summary.yaml`
