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
- random seed: `15`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `32.716%`
- winning mean component MAE: `0.068689`
- winning mean component RMSE: `0.137662`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 32.716 | 0.068689 | 0.137662 | `{'estimator__learning_rate': 0.18, 'estimator__max_depth': 11, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `HGBM` | 0.002414 | 0.003294 | 26.102 |
| `fft_y_Bw_filtered_ampl_1` | `HGBM` | 0.000019 | 0.000028 | 0.113 |
| `fft_y_Bw_filtered_phase_1` | `HGBM` | 0.001725 | 0.002351 | 59.315 |
| `fft_y_Bw_filtered_ampl_3` | `HGBM` | 0.000024 | 0.000034 | 2.442 |
| `fft_y_Bw_filtered_phase_3` | `HGBM` | 0.021367 | 0.034748 | 1.567 |
| `fft_y_Bw_filtered_ampl_39` | `HGBM` | 0.000019 | 0.000026 | 4.334 |
| `fft_y_Bw_filtered_phase_39` | `HGBM` | 0.305117 | 0.637651 | 10.905 |
| `fft_y_Bw_filtered_ampl_40` | `HGBM` | 0.000025 | 0.000039 | 8.024 |
| `fft_y_Bw_filtered_phase_40` | `HGBM` | 0.096175 | 0.162737 | 31.066 |
| `fft_y_Bw_filtered_ampl_78` | `HGBM` | 0.000028 | 0.000040 | 3.839 |
| `fft_y_Bw_filtered_phase_78` | `HGBM` | 0.057392 | 0.085996 | 18.102 |
| `fft_y_Bw_filtered_ampl_81` | `HGBM` | 0.000010 | 0.000014 | 8.099 |
| `fft_y_Bw_filtered_phase_81` | `HGBM` | 0.106387 | 0.155496 | 319.445 |
| `fft_y_Bw_filtered_ampl_156` | `HGBM` | 0.000264 | 0.001142 | 14.023 |
| `fft_y_Bw_filtered_phase_156` | `HGBM` | 0.189482 | 0.609461 | 56.246 |
| `fft_y_Bw_filtered_ampl_162` | `HGBM` | 0.000171 | 0.000554 | 17.783 |
| `fft_y_Bw_filtered_phase_162` | `HGBM` | 0.085611 | 0.156436 | 5.018 |
| `fft_y_Bw_filtered_ampl_240` | `HGBM` | 0.000097 | 0.000195 | 14.263 |
| `fft_y_Bw_filtered_phase_240` | `HGBM` | 0.438773 | 0.765326 | 20.924 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/hgbm/2026-04-26_track1_backward_hgbm_original_dataset_mega_campaign/007_track1_original_dataset_backward_hgbm_attempt_07.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-27-25__track1_original_dataset_backward_hgbm_attempt_07_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-27-25__track1_original_dataset_backward_hgbm_attempt_07_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-27-25__track1_original_dataset_backward_hgbm_attempt_07_campaign_validation/validation_summary.yaml`
