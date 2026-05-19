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
- random seed: `19`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `6.198%`
- winning mean component MAE: `0.072840`
- winning mean component RMSE: `0.102046`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 6.198 | 0.072840 | 0.102046 | `{'estimator__learning_rate': 0.39, 'estimator__max_depth': 10, 'estimator__num_leaves': 4, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_phase_81` | `LGBM` | 0.072840 | 0.102046 | 6.198 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/forward_final_open_cells/lgbm/2026-04-28_track1_forward_lgbm_phase_h81_final_open_cells/004_track1_forward_lgbm_phase_h81_final_open_cells_attempt_04.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_final_open_cells/2026-04-28-02-09-30__track1_forward_lgbm_phase_h81_final_open_cells_attempt_04_campaign_run`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_final_open_cells/2026-04-28-02-09-30__track1_forward_lgbm_phase_h81_final_open_cells_attempt_04_campaign_run/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_final_open_cells/2026-04-28-02-09-30__track1_forward_lgbm_phase_h81_final_open_cells_attempt_04_campaign_run/validation_summary.yaml`
