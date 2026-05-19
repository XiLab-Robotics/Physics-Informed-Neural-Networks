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
- random seed: `23`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `35.894%`
- winning mean component MAE: `0.081166`
- winning mean component RMSE: `0.159472`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 35.894 | 0.081166 | 0.159472 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.3, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `XGBM` | 0.002796 | 0.003147 | 69.627 |
| `fft_y_Bw_filtered_ampl_1` | `XGBM` | 0.000070 | 0.000099 | 0.407 |
| `fft_y_Bw_filtered_phase_1` | `XGBM` | 0.002061 | 0.002958 | 105.734 |
| `fft_y_Bw_filtered_ampl_3` | `XGBM` | 0.000084 | 0.000114 | 8.522 |
| `fft_y_Bw_filtered_phase_3` | `XGBM` | 0.022047 | 0.028690 | 1.647 |
| `fft_y_Bw_filtered_ampl_39` | `XGBM` | 0.000079 | 0.000095 | 18.477 |
| `fft_y_Bw_filtered_phase_39` | `XGBM` | 0.390463 | 0.841559 | 14.960 |
| `fft_y_Bw_filtered_ampl_40` | `XGBM` | 0.000048 | 0.000060 | 16.440 |
| `fft_y_Bw_filtered_phase_40` | `XGBM` | 0.182254 | 0.246323 | 54.570 |
| `fft_y_Bw_filtered_ampl_78` | `XGBM` | 0.000137 | 0.000176 | 23.657 |
| `fft_y_Bw_filtered_phase_78` | `XGBM` | 0.085872 | 0.140936 | 26.404 |
| `fft_y_Bw_filtered_ampl_81` | `XGBM` | 0.000026 | 0.000034 | 23.163 |
| `fft_y_Bw_filtered_phase_81` | `XGBM` | 0.111966 | 0.144616 | 138.974 |
| `fft_y_Bw_filtered_ampl_156` | `XGBM` | 0.000432 | 0.001267 | 46.209 |
| `fft_y_Bw_filtered_phase_156` | `XGBM` | 0.198558 | 0.457577 | 31.876 |
| `fft_y_Bw_filtered_ampl_162` | `XGBM` | 0.000208 | 0.000391 | 38.270 |
| `fft_y_Bw_filtered_phase_162` | `XGBM` | 0.188672 | 0.468765 | 10.735 |
| `fft_y_Bw_filtered_ampl_240` | `XGBM` | 0.000175 | 0.000300 | 31.270 |
| `fft_y_Bw_filtered_phase_240` | `XGBM` | 0.356205 | 0.692858 | 21.050 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/xgbm/2026-04-26_track1_backward_xgbm_original_dataset_mega_campaign/011_track1_original_dataset_backward_xgbm_attempt_11.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-58-51__track1_original_dataset_backward_xgbm_attempt_11_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-58-51__track1_original_dataset_backward_xgbm_attempt_11_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-58-51__track1_original_dataset_backward_xgbm_attempt_11_campaign_validation/validation_summary.yaml`
