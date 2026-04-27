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
- random seed: `61`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `18.197%`
- winning mean component MAE: `0.054322`
- winning mean component RMSE: `0.113091`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 18.197 | 0.054322 | 0.113091 | `{'estimator__learning_rate': 0.39, 'estimator__max_depth': 10, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `LGBM` | 0.002653 | 0.003201 | 34.473 |
| `fft_y_Bw_filtered_ampl_1` | `LGBM` | 0.000028 | 0.000039 | 0.165 |
| `fft_y_Bw_filtered_phase_1` | `LGBM` | 0.001630 | 0.002374 | 33.228 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000020 | 0.000030 | 2.134 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.020372 | 0.027207 | 1.494 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000016 | 0.000022 | 3.524 |
| `fft_y_Bw_filtered_phase_39` | `LGBM` | 0.271732 | 0.804693 | 9.622 |
| `fft_y_Bw_filtered_ampl_40` | `LGBM` | 0.000031 | 0.000048 | 9.226 |
| `fft_y_Bw_filtered_phase_40` | `LGBM` | 0.099240 | 0.149643 | 39.016 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000031 | 0.000040 | 4.033 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.054999 | 0.096455 | 66.326 |
| `fft_y_Bw_filtered_ampl_81` | `LGBM` | 0.000009 | 0.000013 | 7.786 |
| `fft_y_Bw_filtered_phase_81` | `LGBM` | 0.087227 | 0.114083 | 62.862 |
| `fft_y_Bw_filtered_ampl_156` | `LGBM` | 0.000309 | 0.000971 | 18.130 |
| `fft_y_Bw_filtered_phase_156` | `LGBM` | 0.175357 | 0.444817 | 12.650 |
| `fft_y_Bw_filtered_ampl_162` | `LGBM` | 0.000118 | 0.000311 | 11.223 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.062102 | 0.088254 | 3.567 |
| `fft_y_Bw_filtered_ampl_240` | `LGBM` | 0.000078 | 0.000155 | 12.064 |
| `fft_y_Bw_filtered_phase_240` | `LGBM` | 0.256164 | 0.416376 | 14.229 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/lgbm/2026-04-26_track1_backward_lgbm_original_dataset_mega_campaign/020_track1_original_dataset_backward_lgbm_attempt_20.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-27-02-07-35__track1_original_dataset_backward_lgbm_attempt_20_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-27-02-07-35__track1_original_dataset_backward_lgbm_attempt_20_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-27-02-07-35__track1_original_dataset_backward_lgbm_attempt_20_campaign_validation/validation_summary.yaml`
