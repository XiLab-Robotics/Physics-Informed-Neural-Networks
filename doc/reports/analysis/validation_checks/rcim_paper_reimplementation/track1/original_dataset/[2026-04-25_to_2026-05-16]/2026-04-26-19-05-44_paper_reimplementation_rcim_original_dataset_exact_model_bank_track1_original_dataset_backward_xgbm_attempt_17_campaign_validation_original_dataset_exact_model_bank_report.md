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
- random seed: `47`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `XGBM`
- winning estimator: `XGBRegressor`
- winning mean component MAPE: `39.292%`
- winning mean component MAE: `0.085485`
- winning mean component RMSE: `0.154407`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `XGBM` | `XGBRegressor` | 39.292 | 0.085485 | 0.154407 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `XGBM` | 0.003002 | 0.004044 | 94.146 |
| `fft_y_Bw_filtered_ampl_1` | `XGBM` | 0.000066 | 0.000088 | 0.385 |
| `fft_y_Bw_filtered_phase_1` | `XGBM` | 0.002297 | 0.003278 | 145.697 |
| `fft_y_Bw_filtered_ampl_3` | `XGBM` | 0.000095 | 0.000124 | 9.836 |
| `fft_y_Bw_filtered_phase_3` | `XGBM` | 0.022652 | 0.041937 | 1.694 |
| `fft_y_Bw_filtered_ampl_39` | `XGBM` | 0.000101 | 0.000120 | 21.977 |
| `fft_y_Bw_filtered_phase_39` | `XGBM` | 0.385406 | 0.883608 | 14.810 |
| `fft_y_Bw_filtered_ampl_40` | `XGBM` | 0.000054 | 0.000069 | 17.261 |
| `fft_y_Bw_filtered_phase_40` | `XGBM` | 0.182749 | 0.258343 | 125.507 |
| `fft_y_Bw_filtered_ampl_78` | `XGBM` | 0.000138 | 0.000178 | 21.968 |
| `fft_y_Bw_filtered_phase_78` | `XGBM` | 0.080582 | 0.124841 | 48.732 |
| `fft_y_Bw_filtered_ampl_81` | `XGBM` | 0.000031 | 0.000041 | 23.339 |
| `fft_y_Bw_filtered_phase_81` | `XGBM` | 0.097681 | 0.130281 | 43.975 |
| `fft_y_Bw_filtered_ampl_156` | `XGBM` | 0.000437 | 0.001715 | 34.730 |
| `fft_y_Bw_filtered_phase_156` | `XGBM` | 0.213681 | 0.465039 | 33.542 |
| `fft_y_Bw_filtered_ampl_162` | `XGBM` | 0.000229 | 0.000549 | 28.957 |
| `fft_y_Bw_filtered_phase_162` | `XGBM` | 0.185130 | 0.318102 | 11.103 |
| `fft_y_Bw_filtered_ampl_240` | `XGBM` | 0.000246 | 0.000666 | 46.007 |
| `fft_y_Bw_filtered_phase_240` | `XGBM` | 0.449639 | 0.700717 | 22.888 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/xgbm/2026-04-26_track1_backward_xgbm_original_dataset_mega_campaign/017_track1_original_dataset_backward_xgbm_attempt_17.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-04-48__track1_original_dataset_backward_xgbm_attempt_17_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-04-48__track1_original_dataset_backward_xgbm_attempt_17_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-19-04-48__track1_original_dataset_backward_xgbm_attempt_17_campaign_validation/validation_summary.yaml`
