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
- random seed: `29`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `31.602%`
- winning mean component MAE: `0.098630`
- winning mean component RMSE: `0.189171`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 31.602 | 0.098630 | 0.189171 | `{'estimator__learning_rate': 0.21, 'estimator__max_depth': 9, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | 0.002722 | 0.004271 | 16.258 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | 0.000027 | 0.000040 | 0.157 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | 0.002101 | 0.002843 | 23.231 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | 0.000020 | 0.000045 | 2.535 |
| `fft_y_Fw_filtered_phase_3` | `HGBM` | 0.026056 | 0.035545 | 1.463 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | 0.000025 | 0.000039 | 2.425 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | 0.020336 | 0.026282 | 1.667 |
| `fft_y_Fw_filtered_ampl_40` | `HGBM` | 0.000031 | 0.000050 | 3.892 |
| `fft_y_Fw_filtered_phase_40` | `HGBM` | 0.040976 | 0.067573 | 94.496 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | 0.000029 | 0.000040 | 5.003 |
| `fft_y_Fw_filtered_phase_78` | `HGBM` | 0.103343 | 0.178888 | 221.837 |
| `fft_y_Fw_filtered_ampl_81` | `HGBM` | 0.000013 | 0.000020 | 4.194 |
| `fft_y_Fw_filtered_phase_81` | `HGBM` | 0.060436 | 0.093703 | 6.069 |
| `fft_y_Fw_filtered_ampl_156` | `HGBM` | 0.000140 | 0.000316 | 17.447 |
| `fft_y_Fw_filtered_phase_156` | `HGBM` | 0.707752 | 1.185690 | 37.771 |
| `fft_y_Fw_filtered_ampl_162` | `HGBM` | 0.000120 | 0.000238 | 29.202 |
| `fft_y_Fw_filtered_phase_162` | `HGBM` | 0.528774 | 1.109342 | 22.748 |
| `fft_y_Fw_filtered_ampl_240` | `HGBM` | 0.000073 | 0.000291 | 87.676 |
| `fft_y_Fw_filtered_phase_240` | `HGBM` | 0.380994 | 0.889027 | 22.360 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/hgbm/2026-04-26_track1_forward_hgbm_original_dataset_mega_campaign/013_track1_original_dataset_forward_hgbm_attempt_13.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-53-54__track1_original_dataset_forward_hgbm_attempt_13_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-53-54__track1_original_dataset_forward_hgbm_attempt_13_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-53-54__track1_original_dataset_forward_hgbm_attempt_13_campaign_validation/validation_summary.yaml`
