# Polished-Dataset RCIM Model-Bank Reproduction Validation Report

## Overview

This report covers the direction-specific `RCIM Model-Bank Reproduction` branch trained from measured `polished_dataset` curves.

- direction label: `backward`
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
- winning mean component MAPE: `18.400%`
- winning mean component MAE: `0.043815`
- winning mean component RMSE: `0.110706`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 18.400 | 0.043815 | 0.110706 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__max_leaf_nodes': None, 'estimator__min_samples_split': 2, 'estimator__n_estimators': 40}` |
| 2 | `ET` | `ExtraTreeRegressor` | 27.376 | 0.057998 | 0.154673 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 18, 'estimator__max_leaf_nodes': None, 'estimator__min_samples_split': 6}` |
| 3 | `LGBM` | `LGBMRegressor` | 29.294 | 0.082098 | 0.153147 | `{'estimator__learning_rate': 0.39, 'estimator__max_depth': 16, 'estimator__num_leaves': 28, 'estimator__subsample': 0.1}` |
| 4 | `GBM` | `GradientBoostingRegressor` | 33.201 | 0.070695 | 0.148584 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 18, 'estimator__max_features': 'log2', 'estimator__min_samples_split': 3, 'estimator__n_estimators': 36}` |
| 5 | `RF` | `RandomForestRegressor` | 34.669 | 0.075804 | 0.146386 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__max_features': 'log2', 'estimator__min_samples_split': 3, 'estimator__n_estimators': 36}` |
| 6 | `HGBM` | `HistGradientBoostingRegressor` | 34.670 | 0.086857 | 0.165503 | `{'estimator__learning_rate': 0.21, 'estimator__max_depth': 11, 'estimator__max_iter': 10, 'estimator__max_leaf_nodes': 27}` |
| 7 | `DT` | `DecisionTreeRegressor` | 36.138 | 0.060626 | 0.151510 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 14, 'estimator__max_leaf_nodes': 25, 'estimator__min_samples_split': 2}` |
| 8 | `XGBM` | `XGBRegressor` | 44.755 | 0.105164 | 0.171097 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.3, 'estimator__max_depth': 17, 'estimator__n_estimators': 36}` |
| 9 | `SVR` | `SVR` | 51.588 | 0.126698 | 0.241140 | - |
| 10 | `MLP` | `MLPRegressor` | 4129.776 | 0.248888 | 0.345650 | `{'estimator__activation': 'tanh', 'estimator__alpha': 0.0001, 'estimator__early_stopping': True, 'estimator__hidden_layer_sizes': (100, 50), 'estimator__learning_rate': 'adaptive', 'estimator__max_iter': 600, 'estimator__solver': 'adam', 'estimator__tol': 0.0001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.002274 | 0.002831 | 25.103 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000021 | 0.000029 | 0.123 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001564 | 0.002158 | 33.989 |
| `fft_y_Bw_filtered_ampl_3` | `ERT` | 0.000025 | 0.000041 | 2.352 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.022161 | 0.028847 | 1.656 |
| `fft_y_Bw_filtered_ampl_39` | `ERT` | 0.000020 | 0.000030 | 4.361 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.234614 | 1.073811 | 8.070 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000031 | 0.000045 | 10.346 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.092330 | 0.143420 | 112.319 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000041 | 0.000056 | 4.857 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.067285 | 0.130040 | 38.472 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000009 | 0.000017 | 7.632 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.066989 | 0.091399 | 21.926 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000072 | 0.000260 | 8.182 |
| `fft_y_Bw_filtered_phase_156` | `ERT` | 0.122703 | 0.476499 | 31.244 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000050 | 0.000157 | 6.985 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.041678 | 0.070106 | 2.201 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000091 | 0.000225 | 11.852 |
| `fft_y_Bw_filtered_phase_240` | `ERT` | 0.162039 | 0.371046 | 8.118 |

## Artifact Paths

- config path: `config\paper_reimplementation\rcim_ml_compensation\polished_dataset_rcim_model_bank_reproduction\campaigns\2026-06-22_polished_rcim_model_bank_reproduction\queue\rcim_model_bank_reproduction_polished_dataset_bw.yaml`
- output directory: `output\validation_checks\rcim_model_bank_reproduction\2026-06-25-15-19-40__rcim_model_bank_reproduction_polished_dataset_bw_polished_dataset_campaign_validation`
- model bundle: `output\validation_checks\rcim_model_bank_reproduction\2026-06-25-15-19-40__rcim_model_bank_reproduction_polished_dataset_bw_polished_dataset_campaign_validation\paper_family_model_bank.pkl`
- python export root: `output\validation_checks\rcim_model_bank_reproduction\2026-06-25-15-19-40__rcim_model_bank_reproduction_polished_dataset_bw_polished_dataset_campaign_validation\python_export`
- ONNX export root: `output\validation_checks\rcim_model_bank_reproduction\2026-06-25-15-19-40__rcim_model_bank_reproduction_polished_dataset_bw_polished_dataset_campaign_validation\onnx_export`
- validation summary: `output\validation_checks\rcim_model_bank_reproduction\2026-06-25-15-19-40__rcim_model_bank_reproduction_polished_dataset_bw_polished_dataset_campaign_validation\validation_summary.yaml`
- best-parameter summary: `output\validation_checks\rcim_model_bank_reproduction\2026-06-25-15-19-40__rcim_model_bank_reproduction_polished_dataset_bw_polished_dataset_campaign_validation\best_parameter_summary.yaml`
