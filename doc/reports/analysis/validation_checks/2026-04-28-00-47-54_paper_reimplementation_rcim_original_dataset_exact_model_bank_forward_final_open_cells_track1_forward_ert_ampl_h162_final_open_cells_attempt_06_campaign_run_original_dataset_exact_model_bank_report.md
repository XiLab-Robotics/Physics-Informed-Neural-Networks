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
- validation rows / files: `145` / `145`
- test rows / files: `145` / `145`
- validation split: `0.15`
- test split: `0.15`
- random seed: `29`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `7.214%`
- winning mean component MAE: `0.000058`
- winning mean component RMSE: `0.000203`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 7.214 | 0.000058 | 0.000203 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__min_samples_split': 5, 'estimator__n_estimators': 40}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000058 | 0.000203 | 7.214 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/forward_final_open_cells/ert/2026-04-28_track1_forward_ert_ampl_h162_final_open_cells/006_track1_forward_ert_ampl_h162_final_open_cells_attempt_06.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_final_open_cells/2026-04-28-00-47-01__track1_forward_ert_ampl_h162_final_open_cells_attempt_06_campaign_run`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_final_open_cells/2026-04-28-00-47-01__track1_forward_ert_ampl_h162_final_open_cells_attempt_06_campaign_run/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_final_open_cells/2026-04-28-00-47-01__track1_forward_ert_ampl_h162_final_open_cells_attempt_06_campaign_run/validation_summary.yaml`
