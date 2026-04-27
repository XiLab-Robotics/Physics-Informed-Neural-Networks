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
- random seed: `13`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `31.693%`
- winning mean component MAE: `0.110457`
- winning mean component RMSE: `0.204948`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 31.693 | 0.110457 | 0.204948 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.3, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `XGBM` | 0.002751 | 0.003426 | 48.309 |
| `fft_y_Bw_filtered_ampl_1` | `XGBM` | 0.000066 | 0.000116 | 0.385 |
| `fft_y_Bw_filtered_phase_1` | `XGBM` | 0.002064 | 0.003024 | 108.344 |
| `fft_y_Bw_filtered_ampl_3` | `XGBM` | 0.000092 | 0.000130 | 9.117 |
| `fft_y_Bw_filtered_phase_3` | `XGBM` | 0.020690 | 0.029267 | 1.535 |
| `fft_y_Bw_filtered_ampl_39` | `XGBM` | 0.000089 | 0.000109 | 19.578 |
| `fft_y_Bw_filtered_phase_39` | `XGBM` | 0.431795 | 0.900266 | 16.108 |
| `fft_y_Bw_filtered_ampl_40` | `XGBM` | 0.000045 | 0.000059 | 14.989 |
| `fft_y_Bw_filtered_phase_40` | `XGBM` | 0.182572 | 0.241163 | 76.857 |
| `fft_y_Bw_filtered_ampl_78` | `XGBM` | 0.000122 | 0.000162 | 28.234 |
| `fft_y_Bw_filtered_phase_78` | `XGBM` | 0.104526 | 0.165875 | 33.572 |
| `fft_y_Bw_filtered_ampl_81` | `XGBM` | 0.000029 | 0.000038 | 22.768 |
| `fft_y_Bw_filtered_phase_81` | `XGBM` | 0.106460 | 0.143654 | 54.661 |
| `fft_y_Bw_filtered_ampl_156` | `XGBM` | 0.000335 | 0.000773 | 30.869 |
| `fft_y_Bw_filtered_phase_156` | `XGBM` | 0.265685 | 0.617648 | 21.768 |
| `fft_y_Bw_filtered_ampl_162` | `XGBM` | 0.000328 | 0.000705 | 34.378 |
| `fft_y_Bw_filtered_phase_162` | `XGBM` | 0.208441 | 0.455088 | 12.423 |
| `fft_y_Bw_filtered_ampl_240` | `XGBM` | 0.000217 | 0.000708 | 33.597 |
| `fft_y_Bw_filtered_phase_240` | `XGBM` | 0.772378 | 1.331796 | 34.672 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/xgbm/2026-04-26_track1_backward_xgbm_original_dataset_mega_campaign/006_track1_original_dataset_backward_xgbm_attempt_06.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-54-02__track1_original_dataset_backward_xgbm_attempt_06_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-54-02__track1_original_dataset_backward_xgbm_attempt_06_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-18-54-02__track1_original_dataset_backward_xgbm_attempt_06_campaign_validation/validation_summary.yaml`
