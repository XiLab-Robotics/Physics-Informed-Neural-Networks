# Original-Dataset Exact RCIM Model Bank Validation Report

## Overview

This report covers the direction-specific exact-model-bank branch trained from the repository dataset under `data/simplified_dataset`.

- direction label: `forward`
- dataset root: `data/simplified_dataset`
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
- random seed: `0`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.
- workflow stage: `search`
- best-parameter source: `grid_search`
- historical wrapper `cross_validate(...)` replay: `True`

## Winner Summary

- winning family: `DT`
- winning estimator: `DecisionTreeRegressor`
- winning mean component MAPE: `40.559%`
- winning mean component MAE: `0.095493`
- winning mean component RMSE: `0.186076`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `DT` | `DecisionTreeRegressor` | 40.559 | 0.095493 | 0.186076 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__max_leaf_nodes': 23, 'estimator__min_samples_split': 5}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `DT` | 0.003343 | 0.004488 | 6.993 |
| `fft_y_Fw_filtered_ampl_1` | `DT` | 0.000032 | 0.000043 | 0.187 |
| `fft_y_Fw_filtered_phase_1` | `DT` | 0.002496 | 0.003436 | 54.749 |
| `fft_y_Fw_filtered_ampl_3` | `DT` | 0.000025 | 0.000034 | 3.185 |
| `fft_y_Fw_filtered_phase_3` | `DT` | 0.041711 | 0.050719 | 2.282 |
| `fft_y_Fw_filtered_ampl_39` | `DT` | 0.000054 | 0.000069 | 4.840 |
| `fft_y_Fw_filtered_phase_39` | `DT` | 0.038158 | 0.063658 | 3.058 |
| `fft_y_Fw_filtered_ampl_40` | `DT` | 0.000034 | 0.000042 | 4.382 |
| `fft_y_Fw_filtered_phase_40` | `DT` | 0.056848 | 0.073511 | 105.086 |
| `fft_y_Fw_filtered_ampl_78` | `DT` | 0.000097 | 0.000121 | 39.794 |
| `fft_y_Fw_filtered_phase_78` | `DT` | 0.104668 | 0.160754 | 312.894 |
| `fft_y_Fw_filtered_ampl_81` | `DT` | 0.000018 | 0.000022 | 6.155 |
| `fft_y_Fw_filtered_phase_81` | `DT` | 0.098556 | 0.134366 | 8.876 |
| `fft_y_Fw_filtered_ampl_156` | `DT` | 0.000150 | 0.000388 | 61.946 |
| `fft_y_Fw_filtered_phase_156` | `DT` | 0.833520 | 1.560504 | 75.482 |
| `fft_y_Fw_filtered_ampl_162` | `DT` | 0.000143 | 0.000556 | 20.477 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.290414 | 0.769901 | 13.244 |
| `fft_y_Fw_filtered_ampl_240` | `DT` | 0.000085 | 0.000120 | 28.134 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.344008 | 0.712705 | 18.858 |

## Artifact Paths

- config path: `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/bidirectional_paper_faithful_grid_search/forward/dt/2026-05-04_track1_forward_dt_paper_faithful_grid_search_campaign/001_track1_paper_faithful_grid_search_forward_dt.yaml`
- output directory: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-05-08-17-08-23__track1_paper_faithful_grid_search_forward_dt_campaign_validation`
- model bundle: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-05-08-17-08-23__track1_paper_faithful_grid_search_forward_dt_campaign_validation/paper_family_model_bank.pkl`
- validation summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-05-08-17-08-23__track1_paper_faithful_grid_search_forward_dt_campaign_validation/validation_summary.yaml`
- best-parameter summary: `output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank/2026-05-08-17-08-23__track1_paper_faithful_grid_search_forward_dt_campaign_validation/best_parameter_summary.yaml`
