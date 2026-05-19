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
- random seed: `7`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `16.436%`
- winning mean component MAE: `0.065691`
- winning mean component RMSE: `0.147696`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 16.436 | 0.065691 | 0.147696 | `{'estimator__learning_rate': 0.22, 'estimator__max_depth': 9, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `HGBM` | 0.002490 | 0.003051 | 31.414 |
| `fft_y_Bw_filtered_ampl_1` | `HGBM` | 0.000028 | 0.000038 | 0.162 |
| `fft_y_Bw_filtered_phase_1` | `HGBM` | 0.001582 | 0.002119 | 39.549 |
| `fft_y_Bw_filtered_ampl_3` | `HGBM` | 0.000020 | 0.000031 | 2.045 |
| `fft_y_Bw_filtered_phase_3` | `HGBM` | 0.017626 | 0.025534 | 1.285 |
| `fft_y_Bw_filtered_ampl_39` | `HGBM` | 0.000015 | 0.000020 | 3.292 |
| `fft_y_Bw_filtered_phase_39` | `HGBM` | 0.347912 | 1.057002 | 11.886 |
| `fft_y_Bw_filtered_ampl_40` | `HGBM` | 0.000026 | 0.000037 | 8.402 |
| `fft_y_Bw_filtered_phase_40` | `HGBM` | 0.099663 | 0.149664 | 37.952 |
| `fft_y_Bw_filtered_ampl_78` | `HGBM` | 0.000031 | 0.000044 | 6.013 |
| `fft_y_Bw_filtered_phase_78` | `HGBM` | 0.055211 | 0.094621 | 18.022 |
| `fft_y_Bw_filtered_ampl_81` | `HGBM` | 0.000008 | 0.000011 | 6.531 |
| `fft_y_Bw_filtered_phase_81` | `HGBM` | 0.086730 | 0.115575 | 41.545 |
| `fft_y_Bw_filtered_ampl_156` | `HGBM` | 0.000346 | 0.001454 | 15.594 |
| `fft_y_Bw_filtered_phase_156` | `HGBM` | 0.170681 | 0.478551 | 13.379 |
| `fft_y_Bw_filtered_ampl_162` | `HGBM` | 0.000137 | 0.000385 | 13.955 |
| `fft_y_Bw_filtered_phase_162` | `HGBM` | 0.095297 | 0.153621 | 5.570 |
| `fft_y_Bw_filtered_ampl_240` | `HGBM` | 0.000135 | 0.000288 | 29.691 |
| `fft_y_Bw_filtered_phase_240` | `HGBM` | 0.370183 | 0.724183 | 26.003 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/hgbm/2026-04-26_track1_backward_hgbm_original_dataset_mega_campaign/003_track1_original_dataset_backward_hgbm_attempt_03.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-21-10__track1_original_dataset_backward_hgbm_attempt_03_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-21-10__track1_original_dataset_backward_hgbm_attempt_03_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-21-10__track1_original_dataset_backward_hgbm_attempt_03_campaign_validation/validation_summary.yaml`
