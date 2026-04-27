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
- random seed: `9`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `17.682%`
- winning mean component MAE: `0.085759`
- winning mean component RMSE: `0.168179`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 17.682 | 0.085759 | 0.168179 | `{'estimator__learning_rate': 0.2, 'estimator__max_depth': 10, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | 0.002324 | 0.002893 | 4.746 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | 0.000023 | 0.000030 | 0.133 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | 0.001861 | 0.002561 | 22.109 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | 0.000017 | 0.000023 | 2.161 |
| `fft_y_Fw_filtered_phase_3` | `HGBM` | 0.020460 | 0.025584 | 1.133 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | 0.000023 | 0.000031 | 2.144 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | 0.018597 | 0.026418 | 1.643 |
| `fft_y_Fw_filtered_ampl_40` | `HGBM` | 0.000026 | 0.000034 | 3.384 |
| `fft_y_Fw_filtered_phase_40` | `HGBM` | 0.040446 | 0.068560 | 50.292 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | 0.000029 | 0.000039 | 20.518 |
| `fft_y_Fw_filtered_phase_78` | `HGBM` | 0.115285 | 0.344838 | 76.156 |
| `fft_y_Fw_filtered_ampl_81` | `HGBM` | 0.000012 | 0.000016 | 4.016 |
| `fft_y_Fw_filtered_phase_81` | `HGBM` | 0.047953 | 0.065909 | 8.934 |
| `fft_y_Fw_filtered_ampl_156` | `HGBM` | 0.000122 | 0.000323 | 27.136 |
| `fft_y_Fw_filtered_phase_156` | `HGBM` | 0.573591 | 1.023590 | 32.558 |
| `fft_y_Fw_filtered_ampl_162` | `HGBM` | 0.000155 | 0.000470 | 24.219 |
| `fft_y_Fw_filtered_phase_162` | `HGBM` | 0.463627 | 0.902809 | 19.614 |
| `fft_y_Fw_filtered_ampl_240` | `HGBM` | 0.000047 | 0.000084 | 15.764 |
| `fft_y_Fw_filtered_phase_240` | `HGBM` | 0.344817 | 0.731188 | 19.298 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/hgbm/2026-04-26_track1_forward_hgbm_original_dataset_mega_campaign/004_track1_original_dataset_forward_hgbm_attempt_04.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-39-16__track1_original_dataset_forward_hgbm_attempt_04_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-39-16__track1_original_dataset_forward_hgbm_attempt_04_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-39-16__track1_original_dataset_forward_hgbm_attempt_04_campaign_validation/validation_summary.yaml`
