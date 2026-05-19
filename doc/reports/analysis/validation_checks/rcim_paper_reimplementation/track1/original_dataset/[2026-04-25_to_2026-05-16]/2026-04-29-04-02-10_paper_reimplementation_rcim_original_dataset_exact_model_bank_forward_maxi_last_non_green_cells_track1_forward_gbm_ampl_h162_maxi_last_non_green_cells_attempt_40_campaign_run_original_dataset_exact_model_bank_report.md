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
- validation rows / files: `48` / `48`
- test rows / files: `242` / `242`
- validation split: `0.05`
- test split: `0.25`
- random seed: `263`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `GBM`
- winning estimator: `GradientBoostingRegressor`
- winning mean component MAPE: `161.350%`
- winning mean component MAE: `0.000422`
- winning mean component RMSE: `0.001022`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `GBM` | `GradientBoostingRegressor` | 161.350 | 0.000422 | 0.001022 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.01, 'estimator__max_depth': 15, 'estimator__min_samples_split': 10, 'estimator__n_estimators': 84}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_162` | `GBM` | 0.000422 | 0.001022 | 161.350 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/forward_maxi_last_non_green_cells/gbm/2026-04-29_track1_forward_gbm_ampl_h162_maxi_last_non_green_cells/040_track1_forward_gbm_ampl_h162_maxi_last_non_green_cells_attempt_40.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_maxi_last_non_green_cells/2026-04-29-04-01-20__track1_forward_gbm_ampl_h162_maxi_last_non_green_cells_attempt_40_campaign_run`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_maxi_last_non_green_cells/2026-04-29-04-01-20__track1_forward_gbm_ampl_h162_maxi_last_non_green_cells_attempt_40_campaign_run/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_maxi_last_non_green_cells/2026-04-29-04-01-20__track1_forward_gbm_ampl_h162_maxi_last_non_green_cells_attempt_40_campaign_run/validation_summary.yaml`
