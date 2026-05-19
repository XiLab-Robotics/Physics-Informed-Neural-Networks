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
- random seed: `42`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `27.168%`
- winning mean component MAE: `0.058456`
- winning mean component RMSE: `0.109555`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 27.168 | 0.058456 | 0.109555 | `{'estimator__learning_rate': 0.18, 'estimator__max_depth': 12, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `HGBM` | 0.002428 | 0.003046 | 47.067 |
| `fft_y_Bw_filtered_ampl_1` | `HGBM` | 0.000026 | 0.000036 | 0.152 |
| `fft_y_Bw_filtered_phase_1` | `HGBM` | 0.001642 | 0.002197 | 70.565 |
| `fft_y_Bw_filtered_ampl_3` | `HGBM` | 0.000021 | 0.000033 | 2.001 |
| `fft_y_Bw_filtered_phase_3` | `HGBM` | 0.019670 | 0.025479 | 1.476 |
| `fft_y_Bw_filtered_ampl_39` | `HGBM` | 0.000018 | 0.000026 | 3.886 |
| `fft_y_Bw_filtered_phase_39` | `HGBM` | 0.334408 | 0.730854 | 11.712 |
| `fft_y_Bw_filtered_ampl_40` | `HGBM` | 0.000029 | 0.000043 | 9.424 |
| `fft_y_Bw_filtered_phase_40` | `HGBM` | 0.099360 | 0.187082 | 75.151 |
| `fft_y_Bw_filtered_ampl_78` | `HGBM` | 0.000027 | 0.000038 | 3.933 |
| `fft_y_Bw_filtered_phase_78` | `HGBM` | 0.072163 | 0.141642 | 45.544 |
| `fft_y_Bw_filtered_ampl_81` | `HGBM` | 0.000009 | 0.000015 | 7.577 |
| `fft_y_Bw_filtered_phase_81` | `HGBM` | 0.083591 | 0.109548 | 154.628 |
| `fft_y_Bw_filtered_ampl_156` | `HGBM` | 0.000204 | 0.000568 | 19.237 |
| `fft_y_Bw_filtered_phase_156` | `HGBM` | 0.126681 | 0.201806 | 13.329 |
| `fft_y_Bw_filtered_ampl_162` | `HGBM` | 0.000123 | 0.000311 | 15.579 |
| `fft_y_Bw_filtered_phase_162` | `HGBM` | 0.088772 | 0.155045 | 5.003 |
| `fft_y_Bw_filtered_ampl_240` | `HGBM` | 0.000100 | 0.000272 | 15.443 |
| `fft_y_Bw_filtered_phase_240` | `HGBM` | 0.281394 | 0.523507 | 14.485 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/hgbm/2026-04-26_track1_backward_hgbm_original_dataset_mega_campaign/016_track1_original_dataset_backward_hgbm_attempt_16.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-41-27__track1_original_dataset_backward_hgbm_attempt_16_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-41-27__track1_original_dataset_backward_hgbm_attempt_16_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-41-27__track1_original_dataset_backward_hgbm_attempt_16_campaign_validation/validation_summary.yaml`
