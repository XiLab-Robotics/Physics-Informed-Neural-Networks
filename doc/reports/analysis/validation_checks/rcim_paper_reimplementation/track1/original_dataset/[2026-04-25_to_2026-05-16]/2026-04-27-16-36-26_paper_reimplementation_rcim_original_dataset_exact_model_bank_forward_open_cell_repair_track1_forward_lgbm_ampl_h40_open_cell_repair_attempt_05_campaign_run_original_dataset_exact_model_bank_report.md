# Original-Dataset Exact RCIM Model Bank Validation Report

## Overview

This report covers the direction-specific exact-model-bank branch trained from the repository dataset under `data/datasets`.

- direction label: `forward`
- dataset root: `data/datasets`
- dataset config: `config/datasets/transmission_error_dataset.yaml`
- selected harmonics: `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`
- decomposition point stride: `1`
- feature schema: `rpm, deg, tor`
- target count: `1`

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
- winning mean component MAPE: `3.390%`
- winning mean component MAE: `0.000028`
- winning mean component RMSE: `0.000042`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 3.390 | 0.000028 | 0.000042 | `{'estimator__learning_rate': 0.39, 'estimator__max_depth': 10, 'estimator__num_leaves': 6, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_40` | `LGBM` | 0.000028 | 0.000042 | 3.390 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/forward_open_cell_repair/lgbm/2026-04-27_track1_forward_lgbm_ampl_h40_open_cell_repair/005_track1_forward_lgbm_ampl_h40_open_cell_repair_attempt_05.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_open_cell_repair/2026-04-27-16-34-13__track1_forward_lgbm_ampl_h40_open_cell_repair_attempt_05_campaign_run`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_open_cell_repair/2026-04-27-16-34-13__track1_forward_lgbm_ampl_h40_open_cell_repair_attempt_05_campaign_run/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_open_cell_repair/2026-04-27-16-34-13__track1_forward_lgbm_ampl_h40_open_cell_repair_attempt_05_campaign_run/validation_summary.yaml`
