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
- random seed: `11`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `42.110%`
- winning mean component MAE: `0.074836`
- winning mean component RMSE: `0.145511`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 42.110 | 0.074836 | 0.145511 | `{'estimator__learning_rate': 0.2, 'estimator__max_depth': 10, 'estimator__num_leaves': 8, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `LGBM` | 0.002746 | 0.003194 | 81.318 |
| `fft_y_Bw_filtered_ampl_1` | `LGBM` | 0.000025 | 0.000032 | 0.145 |
| `fft_y_Bw_filtered_phase_1` | `LGBM` | 0.001847 | 0.002742 | 53.977 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000022 | 0.000034 | 2.223 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.021597 | 0.030008 | 1.609 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000016 | 0.000024 | 3.696 |
| `fft_y_Bw_filtered_phase_39` | `LGBM` | 0.417715 | 0.964184 | 14.707 |
| `fft_y_Bw_filtered_ampl_40` | `LGBM` | 0.000032 | 0.000050 | 10.406 |
| `fft_y_Bw_filtered_phase_40` | `LGBM` | 0.091895 | 0.127858 | 61.174 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000029 | 0.000042 | 4.371 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.063552 | 0.107822 | 26.013 |
| `fft_y_Bw_filtered_ampl_81` | `LGBM` | 0.000010 | 0.000014 | 7.825 |
| `fft_y_Bw_filtered_phase_81` | `LGBM` | 0.093316 | 0.124218 | 400.609 |
| `fft_y_Bw_filtered_ampl_156` | `LGBM` | 0.000488 | 0.001132 | 34.754 |
| `fft_y_Bw_filtered_phase_156` | `LGBM` | 0.227520 | 0.462221 | 16.446 |
| `fft_y_Bw_filtered_ampl_162` | `LGBM` | 0.000203 | 0.000460 | 25.623 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.132165 | 0.244347 | 8.280 |
| `fft_y_Bw_filtered_ampl_240` | `LGBM` | 0.000117 | 0.000195 | 19.321 |
| `fft_y_Bw_filtered_phase_240` | `LGBM` | 0.368598 | 0.696138 | 27.597 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/lgbm/2026-04-26_track1_backward_lgbm_original_dataset_mega_campaign/005_track1_original_dataset_backward_lgbm_attempt_05.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-20-36-49__track1_original_dataset_backward_lgbm_attempt_05_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-20-36-49__track1_original_dataset_backward_lgbm_attempt_05_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-20-36-49__track1_original_dataset_backward_lgbm_attempt_05_campaign_validation/validation_summary.yaml`
