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
- random seed: `13`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `24.661%`
- winning mean component MAE: `0.078871`
- winning mean component RMSE: `0.141809`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 24.661 | 0.078871 | 0.141809 | `{'estimator__learning_rate': 0.22, 'estimator__max_depth': 13, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | 0.002325 | 0.003058 | 4.890 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | 0.000024 | 0.000032 | 0.140 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | 0.002051 | 0.002760 | 102.346 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | 0.000017 | 0.000023 | 2.095 |
| `fft_y_Fw_filtered_phase_3` | `HGBM` | 0.020985 | 0.029144 | 1.183 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | 0.000025 | 0.000035 | 2.218 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | 0.021083 | 0.028894 | 1.895 |
| `fft_y_Fw_filtered_ampl_40` | `HGBM` | 0.000027 | 0.000038 | 3.389 |
| `fft_y_Fw_filtered_phase_40` | `HGBM` | 0.036383 | 0.049159 | 57.213 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | 0.000031 | 0.000047 | 6.420 |
| `fft_y_Fw_filtered_phase_78` | `HGBM` | 0.069436 | 0.127061 | 44.596 |
| `fft_y_Fw_filtered_ampl_81` | `HGBM` | 0.000011 | 0.000015 | 3.489 |
| `fft_y_Fw_filtered_phase_81` | `HGBM` | 0.046988 | 0.066548 | 5.786 |
| `fft_y_Fw_filtered_ampl_156` | `HGBM` | 0.000080 | 0.000174 | 26.699 |
| `fft_y_Fw_filtered_phase_156` | `HGBM` | 0.751980 | 1.251728 | 35.424 |
| `fft_y_Fw_filtered_ampl_162` | `HGBM` | 0.000169 | 0.000422 | 23.209 |
| `fft_y_Fw_filtered_phase_162` | `HGBM` | 0.271985 | 0.560556 | 15.565 |
| `fft_y_Fw_filtered_ampl_240` | `HGBM` | 0.000038 | 0.000066 | 12.477 |
| `fft_y_Fw_filtered_phase_240` | `HGBM` | 0.274912 | 0.574607 | 119.524 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/hgbm/2026-04-26_track1_forward_hgbm_original_dataset_mega_campaign/006_track1_original_dataset_forward_hgbm_attempt_06.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-42-29__track1_original_dataset_forward_hgbm_attempt_06_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-42-29__track1_original_dataset_forward_hgbm_attempt_06_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-42-29__track1_original_dataset_forward_hgbm_attempt_06_campaign_validation/validation_summary.yaml`
