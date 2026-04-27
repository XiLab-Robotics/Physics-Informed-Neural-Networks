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
- random seed: `17`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `16.977%`
- winning mean component MAE: `0.065520`
- winning mean component RMSE: `0.126052`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 16.977 | 0.065520 | 0.126052 | `{'estimator__learning_rate': 0.22, 'estimator__max_depth': 13, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `HGBM` | 0.002574 | 0.003294 | 37.393 |
| `fft_y_Bw_filtered_ampl_1` | `HGBM` | 0.000024 | 0.000034 | 0.138 |
| `fft_y_Bw_filtered_phase_1` | `HGBM` | 0.001714 | 0.002365 | 51.583 |
| `fft_y_Bw_filtered_ampl_3` | `HGBM` | 0.000021 | 0.000029 | 2.160 |
| `fft_y_Bw_filtered_phase_3` | `HGBM` | 0.017628 | 0.022362 | 1.344 |
| `fft_y_Bw_filtered_ampl_39` | `HGBM` | 0.000017 | 0.000028 | 3.477 |
| `fft_y_Bw_filtered_phase_39` | `HGBM` | 0.349265 | 0.716870 | 12.050 |
| `fft_y_Bw_filtered_ampl_40` | `HGBM` | 0.000028 | 0.000045 | 8.764 |
| `fft_y_Bw_filtered_phase_40` | `HGBM` | 0.099712 | 0.137844 | 39.638 |
| `fft_y_Bw_filtered_ampl_78` | `HGBM` | 0.000034 | 0.000045 | 4.621 |
| `fft_y_Bw_filtered_phase_78` | `HGBM` | 0.064714 | 0.119927 | 15.748 |
| `fft_y_Bw_filtered_ampl_81` | `HGBM` | 0.000009 | 0.000013 | 7.808 |
| `fft_y_Bw_filtered_phase_81` | `HGBM` | 0.093736 | 0.131331 | 46.544 |
| `fft_y_Bw_filtered_ampl_156` | `HGBM` | 0.000287 | 0.000682 | 23.268 |
| `fft_y_Bw_filtered_phase_156` | `HGBM` | 0.129253 | 0.330410 | 11.478 |
| `fft_y_Bw_filtered_ampl_162` | `HGBM` | 0.000147 | 0.000338 | 15.024 |
| `fft_y_Bw_filtered_phase_162` | `HGBM` | 0.108607 | 0.209948 | 5.769 |
| `fft_y_Bw_filtered_ampl_240` | `HGBM` | 0.000125 | 0.000224 | 19.211 |
| `fft_y_Bw_filtered_phase_240` | `HGBM` | 0.376984 | 0.719209 | 16.543 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/hgbm/2026-04-26_track1_backward_hgbm_original_dataset_mega_campaign/008_track1_original_dataset_backward_hgbm_attempt_08.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-28-58__track1_original_dataset_backward_hgbm_attempt_08_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-28-58__track1_original_dataset_backward_hgbm_attempt_08_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-28-58__track1_original_dataset_backward_hgbm_attempt_08_campaign_validation/validation_summary.yaml`
