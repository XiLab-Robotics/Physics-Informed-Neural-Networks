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
- random seed: `42`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `23.248%`
- winning mean component MAE: `0.056180`
- winning mean component RMSE: `0.105906`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 23.248 | 0.056180 | 0.105906 | `{'estimator__learning_rate': 0.39, 'estimator__max_depth': 11, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `LGBM` | 0.002408 | 0.003087 | 45.172 |
| `fft_y_Bw_filtered_ampl_1` | `LGBM` | 0.000025 | 0.000034 | 0.147 |
| `fft_y_Bw_filtered_phase_1` | `LGBM` | 0.001635 | 0.002070 | 46.654 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000022 | 0.000033 | 2.108 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.019747 | 0.025588 | 1.470 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000018 | 0.000026 | 3.965 |
| `fft_y_Bw_filtered_phase_39` | `LGBM` | 0.338017 | 0.705584 | 12.096 |
| `fft_y_Bw_filtered_ampl_40` | `LGBM` | 0.000030 | 0.000044 | 9.605 |
| `fft_y_Bw_filtered_phase_40` | `LGBM` | 0.098610 | 0.180688 | 37.546 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000028 | 0.000037 | 4.137 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.071210 | 0.142568 | 42.189 |
| `fft_y_Bw_filtered_ampl_81` | `LGBM` | 0.000008 | 0.000014 | 7.399 |
| `fft_y_Bw_filtered_phase_81` | `LGBM` | 0.085404 | 0.111466 | 151.528 |
| `fft_y_Bw_filtered_ampl_156` | `LGBM` | 0.000187 | 0.000459 | 17.167 |
| `fft_y_Bw_filtered_phase_156` | `LGBM` | 0.129653 | 0.257105 | 11.936 |
| `fft_y_Bw_filtered_ampl_162` | `LGBM` | 0.000096 | 0.000216 | 16.124 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.076928 | 0.116203 | 4.515 |
| `fft_y_Bw_filtered_ampl_240` | `LGBM` | 0.000099 | 0.000203 | 16.196 |
| `fft_y_Bw_filtered_phase_240` | `LGBM` | 0.243286 | 0.466785 | 11.757 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/lgbm/2026-04-26_track1_backward_lgbm_original_dataset_mega_campaign/016_track1_original_dataset_backward_lgbm_attempt_16.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-27-00-39-11__track1_original_dataset_backward_lgbm_attempt_16_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-27-00-39-11__track1_original_dataset_backward_lgbm_attempt_16_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-27-00-39-11__track1_original_dataset_backward_lgbm_attempt_16_campaign_validation/validation_summary.yaml`
