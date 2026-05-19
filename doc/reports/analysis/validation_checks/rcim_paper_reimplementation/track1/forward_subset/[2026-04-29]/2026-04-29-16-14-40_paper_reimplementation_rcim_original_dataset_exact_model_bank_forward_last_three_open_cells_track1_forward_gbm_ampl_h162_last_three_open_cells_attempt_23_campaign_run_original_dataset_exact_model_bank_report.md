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

- train rows / files: `659` / `659`
- validation rows / files: `155` / `155`
- test rows / files: `155` / `155`
- validation split: `0.16`
- test split: `0.16`
- random seed: `103`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `185.129%`
- winning mean component MAE: `0.000419`
- winning mean component RMSE: `0.000875`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 185.129 | 0.000419 | 0.000875 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.01, 'estimator__max_depth': 14, 'estimator__min_samples_split': 18, 'estimator__n_estimators': 68}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000419 | 0.000875 | 185.129 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/forward_last_three_open_cells/gbm/2026-04-29_track1_forward_gbm_ampl_h162_last_three_open_cells/023_track1_forward_gbm_ampl_h162_last_three_open_cells_attempt_23.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_three_open_cells/2026-04-29-16-13-52__track1_forward_gbm_ampl_h162_last_three_open_cells_attempt_23_campaign_run`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_three_open_cells/2026-04-29-16-13-52__track1_forward_gbm_ampl_h162_last_three_open_cells_attempt_23_campaign_run/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_three_open_cells/2026-04-29-16-13-52__track1_forward_gbm_ampl_h162_last_three_open_cells_attempt_23_campaign_run/validation_summary.yaml`
