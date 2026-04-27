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
- random seed: `47`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `22.232%`
- winning mean component MAE: `0.062227`
- winning mean component RMSE: `0.129220`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 22.232 | 0.062227 | 0.129220 | `{'estimator__learning_rate': 0.21, 'estimator__max_depth': 11, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `HGBM` | 0.002795 | 0.003768 | 76.219 |
| `fft_y_Bw_filtered_ampl_1` | `HGBM` | 0.000028 | 0.000037 | 0.162 |
| `fft_y_Bw_filtered_phase_1` | `HGBM` | 0.001989 | 0.002650 | 86.899 |
| `fft_y_Bw_filtered_ampl_3` | `HGBM` | 0.000021 | 0.000031 | 2.101 |
| `fft_y_Bw_filtered_phase_3` | `HGBM` | 0.020651 | 0.036113 | 1.533 |
| `fft_y_Bw_filtered_ampl_39` | `HGBM` | 0.000016 | 0.000022 | 3.563 |
| `fft_y_Bw_filtered_phase_39` | `HGBM` | 0.284782 | 0.828171 | 10.182 |
| `fft_y_Bw_filtered_ampl_40` | `HGBM` | 0.000029 | 0.000046 | 8.997 |
| `fft_y_Bw_filtered_phase_40` | `HGBM` | 0.104123 | 0.188585 | 30.402 |
| `fft_y_Bw_filtered_ampl_78` | `HGBM` | 0.000034 | 0.000054 | 4.736 |
| `fft_y_Bw_filtered_phase_78` | `HGBM` | 0.061470 | 0.109920 | 42.108 |
| `fft_y_Bw_filtered_ampl_81` | `HGBM` | 0.000010 | 0.000017 | 7.395 |
| `fft_y_Bw_filtered_phase_81` | `HGBM` | 0.095833 | 0.130340 | 45.736 |
| `fft_y_Bw_filtered_ampl_156` | `HGBM` | 0.000352 | 0.001103 | 21.695 |
| `fft_y_Bw_filtered_phase_156` | `HGBM` | 0.162123 | 0.416867 | 23.977 |
| `fft_y_Bw_filtered_ampl_162` | `HGBM` | 0.000149 | 0.000451 | 15.326 |
| `fft_y_Bw_filtered_phase_162` | `HGBM` | 0.123084 | 0.199247 | 7.528 |
| `fft_y_Bw_filtered_ampl_240` | `HGBM` | 0.000116 | 0.000259 | 18.663 |
| `fft_y_Bw_filtered_phase_240` | `HGBM` | 0.324710 | 0.537506 | 15.191 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/hgbm/2026-04-26_track1_backward_hgbm_original_dataset_mega_campaign/017_track1_original_dataset_backward_hgbm_attempt_17.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-42-59__track1_original_dataset_backward_hgbm_attempt_17_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-42-59__track1_original_dataset_backward_hgbm_attempt_17_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-42-59__track1_original_dataset_backward_hgbm_attempt_17_campaign_validation/validation_summary.yaml`
