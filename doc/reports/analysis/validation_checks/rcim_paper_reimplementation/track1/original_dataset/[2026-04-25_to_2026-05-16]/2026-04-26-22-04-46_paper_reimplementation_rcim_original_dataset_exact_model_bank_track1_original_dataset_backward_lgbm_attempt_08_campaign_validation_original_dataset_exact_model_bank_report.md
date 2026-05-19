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
- random seed: `17`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `19.283%`
- winning mean component MAE: `0.071152`
- winning mean component RMSE: `0.133535`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 19.283 | 0.071152 | 0.133535 | `{'estimator__learning_rate': 0.2, 'estimator__max_depth': 10, 'estimator__num_leaves': 10, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `LGBM` | 0.002498 | 0.003005 | 38.892 |
| `fft_y_Bw_filtered_ampl_1` | `LGBM` | 0.000024 | 0.000033 | 0.138 |
| `fft_y_Bw_filtered_phase_1` | `LGBM` | 0.001754 | 0.002396 | 52.759 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000023 | 0.000031 | 2.312 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.018005 | 0.022819 | 1.380 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000016 | 0.000028 | 3.349 |
| `fft_y_Bw_filtered_phase_39` | `LGBM` | 0.354209 | 0.722030 | 12.214 |
| `fft_y_Bw_filtered_ampl_40` | `LGBM` | 0.000029 | 0.000044 | 8.926 |
| `fft_y_Bw_filtered_phase_40` | `LGBM` | 0.102915 | 0.136136 | 41.792 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000034 | 0.000048 | 4.970 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.063832 | 0.112502 | 30.350 |
| `fft_y_Bw_filtered_ampl_81` | `LGBM` | 0.000010 | 0.000014 | 8.836 |
| `fft_y_Bw_filtered_phase_81` | `LGBM` | 0.098210 | 0.141601 | 57.873 |
| `fft_y_Bw_filtered_ampl_156` | `LGBM` | 0.000303 | 0.000739 | 26.811 |
| `fft_y_Bw_filtered_phase_156` | `LGBM` | 0.156369 | 0.347117 | 14.125 |
| `fft_y_Bw_filtered_ampl_162` | `LGBM` | 0.000155 | 0.000372 | 16.724 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.133816 | 0.304124 | 6.675 |
| `fft_y_Bw_filtered_ampl_240` | `LGBM` | 0.000127 | 0.000226 | 20.149 |
| `fft_y_Bw_filtered_phase_240` | `LGBM` | 0.419558 | 0.743902 | 18.099 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/lgbm/2026-04-26_track1_backward_lgbm_original_dataset_mega_campaign/008_track1_original_dataset_backward_lgbm_attempt_08.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-21-42-53__track1_original_dataset_backward_lgbm_attempt_08_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-21-42-53__track1_original_dataset_backward_lgbm_attempt_08_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-26-21-42-53__track1_original_dataset_backward_lgbm_attempt_08_campaign_validation/validation_summary.yaml`
