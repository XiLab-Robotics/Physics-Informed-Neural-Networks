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
- random seed: `27`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `65.499%`
- winning mean component MAE: `0.083975`
- winning mean component RMSE: `0.152038`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 65.499 | 0.083975 | 0.152038 | `{'estimator__learning_rate': 0.19, 'estimator__max_depth': 11, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | 0.002469 | 0.003058 | 5.022 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | 0.000028 | 0.000037 | 0.161 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | 0.002240 | 0.003070 | 28.194 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | 0.000018 | 0.000026 | 2.205 |
| `fft_y_Fw_filtered_phase_3` | `HGBM` | 0.021381 | 0.027005 | 1.165 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | 0.000025 | 0.000033 | 2.137 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | 0.020525 | 0.030023 | 1.775 |
| `fft_y_Fw_filtered_ampl_40` | `HGBM` | 0.000028 | 0.000047 | 3.535 |
| `fft_y_Fw_filtered_phase_40` | `HGBM` | 0.044535 | 0.064596 | 83.363 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | 0.000029 | 0.000044 | 4.593 |
| `fft_y_Fw_filtered_phase_78` | `HGBM` | 0.073545 | 0.133800 | 935.216 |
| `fft_y_Fw_filtered_ampl_81` | `HGBM` | 0.000010 | 0.000014 | 3.389 |
| `fft_y_Fw_filtered_phase_81` | `HGBM` | 0.057797 | 0.080997 | 5.786 |
| `fft_y_Fw_filtered_ampl_156` | `HGBM` | 0.000113 | 0.000272 | 17.666 |
| `fft_y_Fw_filtered_phase_156` | `HGBM` | 0.775629 | 1.184830 | 43.349 |
| `fft_y_Fw_filtered_ampl_162` | `HGBM` | 0.000191 | 0.000404 | 31.804 |
| `fft_y_Fw_filtered_phase_162` | `HGBM` | 0.362748 | 0.861066 | 16.666 |
| `fft_y_Fw_filtered_ampl_240` | `HGBM` | 0.000036 | 0.000057 | 11.456 |
| `fft_y_Fw_filtered_phase_240` | `HGBM` | 0.234177 | 0.499349 | 47.008 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/hgbm/2026-04-26_track1_forward_hgbm_original_dataset_mega_campaign/012_track1_original_dataset_forward_hgbm_attempt_12.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-52-15__track1_original_dataset_forward_hgbm_attempt_12_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-52-15__track1_original_dataset_forward_hgbm_attempt_12_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-52-15__track1_original_dataset_forward_hgbm_attempt_12_campaign_validation/validation_summary.yaml`
