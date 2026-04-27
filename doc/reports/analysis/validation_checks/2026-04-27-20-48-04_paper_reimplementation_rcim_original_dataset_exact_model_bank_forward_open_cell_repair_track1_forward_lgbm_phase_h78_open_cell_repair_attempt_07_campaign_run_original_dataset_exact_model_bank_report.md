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
- random seed: `15`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `64.870%`
- winning mean component MAE: `0.116572`
- winning mean component RMSE: `0.347550`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 64.870 | 0.116572 | 0.347550 | `{'estimator__learning_rate': 0.39, 'estimator__max_depth': 10, 'estimator__num_leaves': 8, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_phase_78` | `LGBM` | 0.116572 | 0.347550 | 64.870 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/forward_open_cell_repair/lgbm/2026-04-27_track1_forward_lgbm_phase_h78_open_cell_repair/007_track1_forward_lgbm_phase_h78_open_cell_repair_attempt_07.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_open_cell_repair/2026-04-27-20-46-02__track1_forward_lgbm_phase_h78_open_cell_repair_attempt_07_campaign_run`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_open_cell_repair/2026-04-27-20-46-02__track1_forward_lgbm_phase_h78_open_cell_repair_attempt_07_campaign_run/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_open_cell_repair/2026-04-27-20-46-02__track1_forward_lgbm_phase_h78_open_cell_repair_attempt_07_campaign_run/validation_summary.yaml`
