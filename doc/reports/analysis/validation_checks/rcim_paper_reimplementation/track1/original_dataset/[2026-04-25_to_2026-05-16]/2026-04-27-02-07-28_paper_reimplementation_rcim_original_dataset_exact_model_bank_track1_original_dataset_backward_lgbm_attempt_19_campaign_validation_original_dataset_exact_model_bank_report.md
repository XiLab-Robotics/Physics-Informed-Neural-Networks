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
- random seed: `59`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `22.714%`
- winning mean component MAE: `0.065242`
- winning mean component RMSE: `0.126341`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 22.714 | 0.065242 | 0.126341 | `{'estimator__learning_rate': 0.2, 'estimator__max_depth': 10, 'estimator__num_leaves': 10, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `LGBM` | 0.002463 | 0.002953 | 65.811 |
| `fft_y_Bw_filtered_ampl_1` | `LGBM` | 0.000025 | 0.000038 | 0.145 |
| `fft_y_Bw_filtered_phase_1` | `LGBM` | 0.002138 | 0.003291 | 107.450 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000026 | 0.000041 | 2.519 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.021395 | 0.027412 | 1.597 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000015 | 0.000021 | 3.298 |
| `fft_y_Bw_filtered_phase_39` | `LGBM` | 0.362907 | 0.853126 | 12.603 |
| `fft_y_Bw_filtered_ampl_40` | `LGBM` | 0.000027 | 0.000039 | 8.896 |
| `fft_y_Bw_filtered_phase_40` | `LGBM` | 0.092598 | 0.126418 | 34.864 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000034 | 0.000047 | 4.483 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.075459 | 0.130158 | 21.682 |
| `fft_y_Bw_filtered_ampl_81` | `LGBM` | 0.000010 | 0.000014 | 8.659 |
| `fft_y_Bw_filtered_phase_81` | `LGBM` | 0.094312 | 0.123026 | 44.855 |
| `fft_y_Bw_filtered_ampl_156` | `LGBM` | 0.000356 | 0.001038 | 27.451 |
| `fft_y_Bw_filtered_phase_156` | `LGBM` | 0.142287 | 0.252715 | 34.780 |
| `fft_y_Bw_filtered_ampl_162` | `LGBM` | 0.000087 | 0.000194 | 14.668 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.140849 | 0.275405 | 7.676 |
| `fft_y_Bw_filtered_ampl_240` | `LGBM` | 0.000097 | 0.000162 | 15.586 |
| `fft_y_Bw_filtered_phase_240` | `LGBM` | 0.304504 | 0.604370 | 14.534 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/lgbm/2026-04-26_track1_backward_lgbm_original_dataset_mega_campaign/019_track1_original_dataset_backward_lgbm_attempt_19.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-27-01-45-34__track1_original_dataset_backward_lgbm_attempt_19_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-27-01-45-34__track1_original_dataset_backward_lgbm_attempt_19_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-27-01-45-34__track1_original_dataset_backward_lgbm_attempt_19_campaign_validation/validation_summary.yaml`
