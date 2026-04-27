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
- random seed: `23`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `HGBM`
- winning estimator: `HistGradientBoostingRegressor`
- winning mean component MAPE: `25.477%`
- winning mean component MAE: `0.094387`
- winning mean component RMSE: `0.176777`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `HGBM` | `HistGradientBoostingRegressor` | 25.477 | 0.094387 | 0.176777 | `{'estimator__learning_rate': 0.18, 'estimator__max_depth': 10, 'estimator__max_iter': 100, 'estimator__max_leaf_nodes': 24}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `HGBM` | 0.002596 | 0.003147 | 5.220 |
| `fft_y_Fw_filtered_ampl_1` | `HGBM` | 0.000028 | 0.000037 | 0.166 |
| `fft_y_Fw_filtered_phase_1` | `HGBM` | 0.001703 | 0.002376 | 30.310 |
| `fft_y_Fw_filtered_ampl_3` | `HGBM` | 0.000017 | 0.000023 | 2.151 |
| `fft_y_Fw_filtered_phase_3` | `HGBM` | 0.019851 | 0.026328 | 1.099 |
| `fft_y_Fw_filtered_ampl_39` | `HGBM` | 0.000021 | 0.000029 | 1.881 |
| `fft_y_Fw_filtered_phase_39` | `HGBM` | 0.019048 | 0.029674 | 1.590 |
| `fft_y_Fw_filtered_ampl_40` | `HGBM` | 0.000028 | 0.000041 | 3.826 |
| `fft_y_Fw_filtered_phase_40` | `HGBM` | 0.035602 | 0.048093 | 201.460 |
| `fft_y_Fw_filtered_ampl_78` | `HGBM` | 0.000029 | 0.000041 | 6.570 |
| `fft_y_Fw_filtered_phase_78` | `HGBM` | 0.089214 | 0.150038 | 91.342 |
| `fft_y_Fw_filtered_ampl_81` | `HGBM` | 0.000010 | 0.000013 | 3.301 |
| `fft_y_Fw_filtered_phase_81` | `HGBM` | 0.056409 | 0.081093 | 6.661 |
| `fft_y_Fw_filtered_ampl_156` | `HGBM` | 0.000115 | 0.000360 | 28.488 |
| `fft_y_Fw_filtered_phase_156` | `HGBM` | 0.777236 | 1.337906 | 37.352 |
| `fft_y_Fw_filtered_ampl_162` | `HGBM` | 0.000058 | 0.000158 | 9.476 |
| `fft_y_Fw_filtered_phase_162` | `HGBM` | 0.491244 | 1.007435 | 20.598 |
| `fft_y_Fw_filtered_ampl_240` | `HGBM` | 0.000037 | 0.000066 | 10.691 |
| `fft_y_Fw_filtered_phase_240` | `HGBM` | 0.300100 | 0.671903 | 21.882 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/forward/hgbm/2026-04-26_track1_forward_hgbm_original_dataset_mega_campaign/011_track1_original_dataset_forward_hgbm_attempt_11.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-50-38__track1_original_dataset_forward_hgbm_attempt_11_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-50-38__track1_original_dataset_forward_hgbm_attempt_11_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-05-50-38__track1_original_dataset_forward_hgbm_attempt_11_campaign_validation/validation_summary.yaml`
