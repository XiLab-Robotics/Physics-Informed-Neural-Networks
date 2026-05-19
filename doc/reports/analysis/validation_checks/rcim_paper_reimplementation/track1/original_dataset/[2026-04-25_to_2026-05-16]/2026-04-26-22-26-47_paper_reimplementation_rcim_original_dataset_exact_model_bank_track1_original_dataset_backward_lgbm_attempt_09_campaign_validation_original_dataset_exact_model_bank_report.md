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
- random seed: `19`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `53.165%`
- winning mean component MAE: `0.152366`
- winning mean component RMSE: `0.228571`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 53.165 | 0.152366 | 0.228571 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 10, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `LGBM` | 0.005859 | 0.007141 | 100.869 |
| `fft_y_Bw_filtered_ampl_1` | `LGBM` | 0.000033 | 0.000057 | 0.191 |
| `fft_y_Bw_filtered_phase_1` | `LGBM` | 0.002214 | 0.003064 | 68.945 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000043 | 0.000056 | 4.526 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.076781 | 0.091224 | 5.738 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000040 | 0.000053 | 9.111 |
| `fft_y_Bw_filtered_phase_39` | `LGBM` | 1.097028 | 1.496320 | 39.996 |
| `fft_y_Bw_filtered_ampl_40` | `LGBM` | 0.000027 | 0.000036 | 8.911 |
| `fft_y_Bw_filtered_phase_40` | `LGBM` | 0.162299 | 0.241029 | 48.680 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000246 | 0.000290 | 47.470 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.104908 | 0.154268 | 84.759 |
| `fft_y_Bw_filtered_ampl_81` | `LGBM` | 0.000017 | 0.000022 | 15.607 |
| `fft_y_Bw_filtered_phase_81` | `LGBM` | 0.172376 | 0.207057 | 194.288 |
| `fft_y_Bw_filtered_ampl_156` | `LGBM` | 0.000710 | 0.002027 | 97.679 |
| `fft_y_Bw_filtered_phase_156` | `LGBM` | 0.303163 | 0.638661 | 25.868 |
| `fft_y_Bw_filtered_ampl_162` | `LGBM` | 0.000730 | 0.001884 | 139.642 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.423895 | 0.657419 | 22.102 |
| `fft_y_Bw_filtered_ampl_240` | `LGBM` | 0.000199 | 0.000282 | 49.155 |
| `fft_y_Bw_filtered_phase_240` | `LGBM` | 0.544384 | 0.841968 | 46.597 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/lgbm/2026-04-26_track1_backward_lgbm_original_dataset_mega_campaign/009_track1_original_dataset_backward_lgbm_attempt_09.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-22-04-53__track1_original_dataset_backward_lgbm_attempt_09_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-22-04-53__track1_original_dataset_backward_lgbm_attempt_09_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-22-04-53__track1_original_dataset_backward_lgbm_attempt_09_campaign_validation/validation_summary.yaml`
