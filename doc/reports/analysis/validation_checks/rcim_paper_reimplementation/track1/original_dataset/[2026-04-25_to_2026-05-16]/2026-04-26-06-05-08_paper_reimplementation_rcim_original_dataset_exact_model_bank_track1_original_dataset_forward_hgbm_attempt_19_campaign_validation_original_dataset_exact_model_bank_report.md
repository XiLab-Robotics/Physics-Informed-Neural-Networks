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
- random seed: `59`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `35.721%`
- winning mean component MAE: `0.098158`
- winning mean component RMSE: `0.182201`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 35.721 | 0.098158 | 0.182201 | `{'estimator__learning_rate': 0.18, 'estimator__max_depth': 9, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | 0.002543 | 0.003161 | 5.622 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | 0.000025 | 0.000032 | 0.146 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | 0.002278 | 0.003351 | 54.419 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | 0.000018 | 0.000023 | 2.210 |
| `fft_y_Fw_filtered_phase_3` | `HGBM` | 0.018813 | 0.024864 | 1.049 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | 0.000025 | 0.000034 | 2.228 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | 0.024363 | 0.034533 | 2.086 |
| `fft_y_Fw_filtered_ampl_40` | `HGBM` | 0.000025 | 0.000036 | 3.156 |
| `fft_y_Fw_filtered_phase_40` | `HGBM` | 0.037941 | 0.056659 | 89.338 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | 0.000034 | 0.000048 | 5.194 |
| `fft_y_Fw_filtered_phase_78` | `HGBM` | 0.106243 | 0.241464 | 126.994 |
| `fft_y_Fw_filtered_ampl_81` | `HGBM` | 0.000011 | 0.000016 | 3.541 |
| `fft_y_Fw_filtered_phase_81` | `HGBM` | 0.057719 | 0.081950 | 5.721 |
| `fft_y_Fw_filtered_ampl_156` | `HGBM` | 0.000109 | 0.000294 | 23.421 |
| `fft_y_Fw_filtered_phase_156` | `HGBM` | 0.687384 | 1.093438 | 40.479 |
| `fft_y_Fw_filtered_ampl_162` | `HGBM` | 0.000099 | 0.000242 | 26.853 |
| `fft_y_Fw_filtered_phase_162` | `HGBM` | 0.577013 | 1.168022 | 24.656 |
| `fft_y_Fw_filtered_ampl_240` | `HGBM` | 0.000037 | 0.000068 | 11.741 |
| `fft_y_Fw_filtered_phase_240` | `HGBM` | 0.350322 | 0.753586 | 249.848 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/hgbm/2026-04-26_track1_forward_hgbm_original_dataset_mega_campaign/019_track1_original_dataset_forward_hgbm_attempt_19.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-03-38__track1_original_dataset_forward_hgbm_attempt_19_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-03-38__track1_original_dataset_forward_hgbm_attempt_19_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-03-38__track1_original_dataset_forward_hgbm_attempt_19_campaign_validation/validation_summary.yaml`
