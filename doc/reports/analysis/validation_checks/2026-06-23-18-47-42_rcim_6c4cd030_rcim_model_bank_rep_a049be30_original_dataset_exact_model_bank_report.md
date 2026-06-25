# Original-Dataset Exact RCIM Model Bank Validation Report

## Overview

This report covers the direction-specific exact-model-bank branch trained from the repository dataset under `data/simplified_dataset`.

- direction label: `forward`
- dataset root: `data\polished_dataset`
- dataset config: `config\datasets\transmission_error_dataset.yaml`
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
- random seed: `42`
- validation usage note: Validation split is reserved for future campaign-level tuning. The current stabilization branch fits on the train split and reports held-out test metrics.
- workflow stage: `search`
- best-parameter source: `grid_search`
- historical wrapper `cross_validate(...)` replay: `True`

## Winner Summary

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `11.939%`
- winning mean component MAE: `0.062217`
- winning mean component RMSE: `0.149061`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 11.939 | 0.062217 | 0.149061 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__max_leaf_nodes': None, 'estimator__min_samples_split': 4, 'estimator__n_estimators': 80}` |
| 2 | `LGBM` | `LGBMRegressor` | 15.733 | 0.078928 | 0.157836 | `{'estimator__learning_rate': 0.2, 'estimator__max_depth': 16, 'estimator__num_leaves': 28, 'estimator__subsample': 0.1}` |
| 3 | `ET` | `ExtraTreeRegressor` | 16.417 | 0.075635 | 0.224607 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 18, 'estimator__max_leaf_nodes': None, 'estimator__min_samples_split': 2}` |
| 4 | `GBM` | `GradientBoostingRegressor` | 19.419 | 0.082451 | 0.170773 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 14, 'estimator__max_features': 'log2', 'estimator__min_samples_split': 6, 'estimator__n_estimators': 36}` |
| 5 | `RF` | `RandomForestRegressor` | 21.296 | 0.094821 | 0.190475 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 18, 'estimator__max_features': 'log2', 'estimator__min_samples_split': 4, 'estimator__n_estimators': 90}` |
| 6 | `HGBM` | `HistGradientBoostingRegressor` | 22.198 | 0.101075 | 0.192864 | `{'estimator__learning_rate': 0.2, 'estimator__max_depth': 11, 'estimator__max_iter': 10, 'estimator__max_leaf_nodes': 27}` |
| 7 | `DT` | `DecisionTreeRegressor` | 23.434 | 0.082357 | 0.194015 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__max_leaf_nodes': 26, 'estimator__min_samples_split': 5}` |
| 8 | `XGBM` | `XGBRegressor` | 26.547 | 0.102607 | 0.197927 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 16, 'estimator__n_estimators': 36}` |
| 9 | `SVR` | `SVR` | 50.228 | 0.141837 | 0.264592 | - |
| 10 | `MLP` | `MLPRegressor` | 3807.391 | 0.210378 | 0.308531 | `{'estimator__activation': 'tanh', 'estimator__alpha': 0.0001, 'estimator__early_stopping': True, 'estimator__hidden_layer_sizes': (200, 50), 'estimator__learning_rate': 'adaptive', 'estimator__max_iter': 600, 'estimator__solver': 'adam', 'estimator__tol': 0.0001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.000759 | 0.001036 | 1.406 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000024 | 0.000030 | 0.138 |
| `fft_y_Fw_filtered_phase_1` | `XGBM` | 0.001977 | 0.002782 | 18.904 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000020 | 0.000027 | 2.229 |
| `fft_y_Fw_filtered_phase_3` | `LGBM` | 0.022733 | 0.029683 | 1.261 |
| `fft_y_Fw_filtered_ampl_39` | `LGBM` | 0.000027 | 0.000041 | 2.219 |
| `fft_y_Fw_filtered_phase_39` | `LGBM` | 0.017559 | 0.024067 | 1.463 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000023 | 0.000033 | 2.929 |
| `fft_y_Fw_filtered_phase_40` | `ERT` | 0.038479 | 0.054690 | 64.241 |
| `fft_y_Fw_filtered_ampl_78` | `LGBM` | 0.000037 | 0.000051 | 6.033 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.099935 | 0.308704 | 29.913 |
| `fft_y_Fw_filtered_ampl_81` | `LGBM` | 0.000010 | 0.000015 | 3.416 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.045829 | 0.064217 | 3.319 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000058 | 0.000240 | 10.451 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.409690 | 0.875946 | 17.625 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000036 | 0.000093 | 8.048 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.206873 | 0.831122 | 8.681 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000029 | 0.000051 | 7.418 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.275653 | 0.780217 | 12.553 |

## Artifact Paths

- config path: `config\paper_reimplementation\rcim_ml_compensation\polished_dataset_rcim_model_bank_reproduction\campaigns\2026-06-22_polished_rcim_model_bank_reproduction\queue\rcim_model_bank_reproduction_polished_dataset_fw.yaml`
- output directory: `output\validation_checks\rcim_model_bank_reproduction\2026-06-22-23-42-04__rcim_model_bank_reproduction_polished_dataset_fw_polished_dataset_campaign_validation`
- model bundle: `output\validation_checks\rcim_model_bank_reproduction\2026-06-22-23-42-04__rcim_model_bank_reproduction_polished_dataset_fw_polished_dataset_campaign_validation\paper_family_model_bank.pkl`
- python export root: `output\validation_checks\rcim_model_bank_reproduction\2026-06-22-23-42-04__rcim_model_bank_reproduction_polished_dataset_fw_polished_dataset_campaign_validation\python_export`
- ONNX export root: `output\validation_checks\rcim_model_bank_reproduction\2026-06-22-23-42-04__rcim_model_bank_reproduction_polished_dataset_fw_polished_dataset_campaign_validation\onnx_export`
- validation summary: `output\validation_checks\rcim_model_bank_reproduction\2026-06-22-23-42-04__rcim_model_bank_reproduction_polished_dataset_fw_polished_dataset_campaign_validation\validation_summary.yaml`
- best-parameter summary: `output\validation_checks\rcim_model_bank_reproduction\2026-06-22-23-42-04__rcim_model_bank_reproduction_polished_dataset_fw_polished_dataset_campaign_validation\best_parameter_summary.yaml`
