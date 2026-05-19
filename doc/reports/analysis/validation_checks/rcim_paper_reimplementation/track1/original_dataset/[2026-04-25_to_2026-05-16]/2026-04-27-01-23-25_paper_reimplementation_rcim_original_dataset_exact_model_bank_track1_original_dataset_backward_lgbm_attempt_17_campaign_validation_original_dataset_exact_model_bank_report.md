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

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `65.897%`
- winning mean component MAE: `0.151440`
- winning mean component RMSE: `0.225412`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 65.897 | 0.151440 | 0.225412 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 13, 'estimator__num_leaves': 31, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `LGBM` | 0.006229 | 0.007373 | 229.006 |
| `fft_y_Bw_filtered_ampl_1` | `LGBM` | 0.000035 | 0.000045 | 0.202 |
| `fft_y_Bw_filtered_phase_1` | `LGBM` | 0.002860 | 0.004070 | 252.616 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000052 | 0.000072 | 5.345 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.081441 | 0.094823 | 6.085 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000044 | 0.000054 | 9.882 |
| `fft_y_Bw_filtered_phase_39` | `LGBM` | 0.904660 | 1.141700 | 35.035 |
| `fft_y_Bw_filtered_ampl_40` | `LGBM` | 0.000038 | 0.000051 | 11.968 |
| `fft_y_Bw_filtered_phase_40` | `LGBM` | 0.155731 | 0.239230 | 58.289 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000241 | 0.000283 | 40.887 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.124510 | 0.185774 | 114.322 |
| `fft_y_Bw_filtered_ampl_81` | `LGBM` | 0.000019 | 0.000027 | 14.396 |
| `fft_y_Bw_filtered_phase_81` | `LGBM` | 0.183069 | 0.238451 | 105.652 |
| `fft_y_Bw_filtered_ampl_156` | `LGBM` | 0.000732 | 0.002678 | 94.070 |
| `fft_y_Bw_filtered_phase_156` | `LGBM` | 0.367624 | 0.747242 | 46.059 |
| `fft_y_Bw_filtered_ampl_162` | `LGBM` | 0.000480 | 0.001110 | 132.732 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.423573 | 0.591956 | 22.604 |
| `fft_y_Bw_filtered_ampl_240` | `LGBM` | 0.000244 | 0.000735 | 41.643 |
| `fft_y_Bw_filtered_phase_240` | `LGBM` | 0.625776 | 1.027157 | 31.240 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_original_dataset/backward/lgbm/2026-04-26_track1_backward_lgbm_original_dataset_mega_campaign/017_track1_original_dataset_backward_lgbm_attempt_17.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-27-01-01-28__track1_original_dataset_backward_lgbm_attempt_17_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-27-01-01-28__track1_original_dataset_backward_lgbm_attempt_17_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-04-27-01-01-28__track1_original_dataset_backward_lgbm_attempt_17_campaign_validation/validation_summary.yaml`
