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
- validation rows / files: `58` / `58`
- test rows / files: `233` / `233`
- validation split: `0.06`
- test split: `0.24`
- random seed: `173`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `14.885%`
- winning mean component MAE: `0.000051`
- winning mean component RMSE: `0.000092`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 14.885 | 0.000051 | 0.000092 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 17, 'estimator__min_samples_split': 6, 'estimator__n_estimators': 20}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000051 | 0.000092 | 14.885 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/forward_last_four_open_cells/ert/2026-04-29_track1_forward_ert_ampl_h240_last_four_open_cells/036_track1_forward_ert_ampl_h240_last_four_open_cells_attempt_36.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_four_open_cells/2026-04-29-13-07-03__track1_forward_ert_ampl_h240_last_four_open_cells_attempt_36_campaign_run`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_four_open_cells/2026-04-29-13-07-03__track1_forward_ert_ampl_h240_last_four_open_cells_attempt_36_campaign_run/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_last_four_open_cells/2026-04-29-13-07-03__track1_forward_ert_ampl_h240_last_four_open_cells_attempt_36_campaign_run/validation_summary.yaml`
