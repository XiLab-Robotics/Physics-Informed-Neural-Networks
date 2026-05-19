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
- random seed: `61`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `25.515%`
- winning mean component MAE: `0.095553`
- winning mean component RMSE: `0.174851`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 25.515 | 0.095553 | 0.174851 | `{'estimator__learning_rate': 0.22, 'estimator__max_depth': 9, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | 0.002474 | 0.002994 | 5.285 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | 0.000027 | 0.000036 | 0.156 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | 0.001844 | 0.002242 | 33.132 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | 0.000015 | 0.000021 | 1.854 |
| `fft_y_Fw_filtered_phase_3` | `HGBM` | 0.018613 | 0.024638 | 1.048 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | 0.000022 | 0.000030 | 1.998 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | 0.017971 | 0.026576 | 1.467 |
| `fft_y_Fw_filtered_ampl_40` | `HGBM` | 0.000025 | 0.000037 | 3.180 |
| `fft_y_Fw_filtered_phase_40` | `HGBM` | 0.034676 | 0.052378 | 77.063 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | 0.000036 | 0.000052 | 7.062 |
| `fft_y_Fw_filtered_phase_78` | `HGBM` | 0.091477 | 0.185446 | 169.270 |
| `fft_y_Fw_filtered_ampl_81` | `HGBM` | 0.000011 | 0.000015 | 3.877 |
| `fft_y_Fw_filtered_phase_81` | `HGBM` | 0.053673 | 0.077268 | 6.107 |
| `fft_y_Fw_filtered_ampl_156` | `HGBM` | 0.000143 | 0.000404 | 34.623 |
| `fft_y_Fw_filtered_phase_156` | `HGBM` | 0.836200 | 1.376761 | 75.936 |
| `fft_y_Fw_filtered_ampl_162` | `HGBM` | 0.000108 | 0.000264 | 14.950 |
| `fft_y_Fw_filtered_phase_162` | `HGBM` | 0.419556 | 0.855402 | 18.102 |
| `fft_y_Fw_filtered_ampl_240` | `HGBM` | 0.000045 | 0.000112 | 10.531 |
| `fft_y_Fw_filtered_phase_240` | `HGBM` | 0.338597 | 0.717499 | 19.136 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/hgbm/2026-04-26_track1_forward_hgbm_original_dataset_mega_campaign/020_track1_original_dataset_forward_hgbm_attempt_20.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-05-15__track1_original_dataset_forward_hgbm_attempt_20_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-05-15__track1_original_dataset_forward_hgbm_attempt_20_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-06-05-15__track1_original_dataset_forward_hgbm_attempt_20_campaign_validation/validation_summary.yaml`
