# Original-Dataset Exact RCIM Model Bank Validation Report

## Overview

This report covers the direction-specific exact-model-bank branch trained from the repository dataset under `data/datasets`.

- direction label: `forward`
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
- winning mean component MAPE: `115.060%`
- winning mean component MAE: `0.095033`
- winning mean component RMSE: `0.180245`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 115.060 | 0.095033 | 0.180245 | `{'estimator__learning_rate': 0.19, 'estimator__max_depth': 11, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | 0.002697 | 0.003708 | 8.450 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | 0.000028 | 0.000044 | 0.161 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | 0.002328 | 0.003149 | 1802.848 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | 0.000021 | 0.000030 | 2.736 |
| `fft_y_Fw_filtered_phase_3` | `HGBM` | 0.028718 | 0.064045 | 1.551 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | 0.000025 | 0.000039 | 2.195 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | 0.027336 | 0.047940 | 2.101 |
| `fft_y_Fw_filtered_ampl_40` | `HGBM` | 0.000034 | 0.000054 | 4.465 |
| `fft_y_Fw_filtered_phase_40` | `HGBM` | 0.042723 | 0.066164 | 61.286 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | 0.000035 | 0.000050 | 10.619 |
| `fft_y_Fw_filtered_phase_78` | `HGBM` | 0.111502 | 0.224464 | 115.604 |
| `fft_y_Fw_filtered_ampl_81` | `HGBM` | 0.000012 | 0.000019 | 3.968 |
| `fft_y_Fw_filtered_phase_81` | `HGBM` | 0.063252 | 0.095926 | 10.037 |
| `fft_y_Fw_filtered_ampl_156` | `HGBM` | 0.000130 | 0.000303 | 21.183 |
| `fft_y_Fw_filtered_phase_156` | `HGBM` | 0.638658 | 1.037709 | 49.618 |
| `fft_y_Fw_filtered_ampl_162` | `HGBM` | 0.000144 | 0.000393 | 30.016 |
| `fft_y_Fw_filtered_phase_162` | `HGBM` | 0.465445 | 0.958743 | 19.954 |
| `fft_y_Fw_filtered_ampl_240` | `HGBM` | 0.000039 | 0.000057 | 15.213 |
| `fft_y_Fw_filtered_phase_240` | `HGBM` | 0.422503 | 0.921812 | 24.127 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/hgbm/2026-04-26_track1_forward_hgbm_original_dataset_mega_campaign/018_track1_original_dataset_forward_hgbm_attempt_18.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-02-01__track1_original_dataset_forward_hgbm_attempt_18_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-02-01__track1_original_dataset_forward_hgbm_attempt_18_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-02-01__track1_original_dataset_forward_hgbm_attempt_18_campaign_validation/validation_summary.yaml`
