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
- random seed: `7`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `24.343%`
- winning mean component MAE: `0.081420`
- winning mean component RMSE: `0.150344`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 24.343 | 0.081420 | 0.150344 | `{'estimator__learning_rate': 0.21, 'estimator__max_depth': 12, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | 0.002452 | 0.003065 | 4.855 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | 0.000024 | 0.000032 | 0.142 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | 0.001798 | 0.002400 | 20.854 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | 0.000015 | 0.000021 | 1.855 |
| `fft_y_Fw_filtered_phase_3` | `HGBM` | 0.022085 | 0.028982 | 1.237 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | 0.000029 | 0.000039 | 2.525 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | 0.019019 | 0.024966 | 1.706 |
| `fft_y_Fw_filtered_ampl_40` | `HGBM` | 0.000029 | 0.000045 | 3.597 |
| `fft_y_Fw_filtered_phase_40` | `HGBM` | 0.038714 | 0.052521 | 83.275 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | 0.000027 | 0.000038 | 7.726 |
| `fft_y_Fw_filtered_phase_78` | `HGBM` | 0.095194 | 0.267823 | 151.384 |
| `fft_y_Fw_filtered_ampl_81` | `HGBM` | 0.000012 | 0.000017 | 4.286 |
| `fft_y_Fw_filtered_phase_81` | `HGBM` | 0.049743 | 0.067690 | 7.689 |
| `fft_y_Fw_filtered_ampl_156` | `HGBM` | 0.000128 | 0.000414 | 26.394 |
| `fft_y_Fw_filtered_phase_156` | `HGBM` | 0.646856 | 1.034446 | 66.334 |
| `fft_y_Fw_filtered_ampl_162` | `HGBM` | 0.000158 | 0.000454 | 23.248 |
| `fft_y_Fw_filtered_phase_162` | `HGBM` | 0.428987 | 0.876268 | 18.784 |
| `fft_y_Fw_filtered_ampl_240` | `HGBM` | 0.000038 | 0.000068 | 9.307 |
| `fft_y_Fw_filtered_phase_240` | `HGBM` | 0.241671 | 0.497242 | 27.310 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/hgbm/2026-04-26_track1_forward_hgbm_original_dataset_mega_campaign/003_track1_original_dataset_forward_hgbm_attempt_03.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-37-41__track1_original_dataset_forward_hgbm_attempt_03_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-37-41__track1_original_dataset_forward_hgbm_attempt_03_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-37-41__track1_original_dataset_forward_hgbm_attempt_03_campaign_validation/validation_summary.yaml`
