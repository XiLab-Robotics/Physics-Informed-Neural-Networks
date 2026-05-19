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

- train rows / files: `679` / `679`
- validation rows / files: `116` / `116`
- test rows / files: `174` / `174`
- validation split: `0.12`
- test split: `0.18`
- random seed: `83`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `LGBM`
- winning estimator: `LGBMRegressor`
- winning mean component MAPE: `199.843%`
- winning mean component MAE: `0.000793`
- winning mean component RMSE: `0.002189`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `LGBM` | `LGBMRegressor` | 199.843 | 0.000793 | 0.002189 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 10, 'estimator__num_leaves': 2, 'estimator__subsample': 0.001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_162` | `LGBM` | 0.000793 | 0.002189 | 199.843 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/forward_last_non_green_cells/lgbm/2026-04-28_track1_forward_lgbm_ampl_h162_last_non_green_cells/019_track1_forward_lgbm_ampl_h162_last_non_green_cells_attempt_19.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_non_green_cells/2026-04-28-13-52-58__track1_forward_lgbm_ampl_h162_last_non_green_cells_attempt_19_campaign_run`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_non_green_cells/2026-04-28-13-52-58__track1_forward_lgbm_ampl_h162_last_non_green_cells_attempt_19_campaign_run/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_non_green_cells/2026-04-28-13-52-58__track1_forward_lgbm_ampl_h162_last_non_green_cells_attempt_19_campaign_run/validation_summary.yaml`
