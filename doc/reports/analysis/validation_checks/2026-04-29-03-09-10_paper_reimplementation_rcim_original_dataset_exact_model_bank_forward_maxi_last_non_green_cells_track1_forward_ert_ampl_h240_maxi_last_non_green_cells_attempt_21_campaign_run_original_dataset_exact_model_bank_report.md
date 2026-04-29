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

- train rows / files: `640` / `640`
- validation rows / files: `271` / `271`
- test rows / files: `58` / `58`
- validation split: `0.28`
- test split: `0.06`
- random seed: `157`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `37.405%`
- winning mean component MAE: `0.000051`
- winning mean component RMSE: `0.000103`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 37.405 | 0.000051 | 0.000103 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 17, 'estimator__min_samples_split': 4, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000051 | 0.000103 | 37.405 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/forward_maxi_last_non_green_cells/ert/2026-04-29_track1_forward_ert_ampl_h240_maxi_last_non_green_cells/021_track1_forward_ert_ampl_h240_maxi_last_non_green_cells_attempt_21.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_maxi_last_non_green_cells/2026-04-29-03-08-16__track1_forward_ert_ampl_h240_maxi_last_non_green_cells_attempt_21_campaign_run`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_maxi_last_non_green_cells/2026-04-29-03-08-16__track1_forward_ert_ampl_h240_maxi_last_non_green_cells_attempt_21_campaign_run/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_maxi_last_non_green_cells/2026-04-29-03-08-16__track1_forward_ert_ampl_h240_maxi_last_non_green_cells_attempt_21_campaign_run/validation_summary.yaml`
