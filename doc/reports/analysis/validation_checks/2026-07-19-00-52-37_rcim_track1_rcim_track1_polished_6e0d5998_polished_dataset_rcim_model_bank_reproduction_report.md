# Polished-Dataset RCIM Model-Bank Reproduction Validation Report

## Overview

This report covers the direction-specific `RCIM Model-Bank Reproduction` branch trained from measured `polished_dataset` curves.

- direction label: `backward`
- dataset root: `data\polished_dataset`
- dataset config: `config\datasets\transmission_error_dataset.yaml`
- selected harmonics: `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`
- decomposition point stride: `1`
- feature schema: `angular_position_deg, input_speed_rpm, input_torque_nm, oil_temperature_deg, direction_flag`
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

- winning family: `ET`
- winning estimator: `ExtraTreeRegressor`
- winning mean component MAPE: `20.402%`
- winning mean component MAE: `0.059906`
- winning mean component RMSE: `0.164197`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ET` | `ExtraTreeRegressor` | 20.402 | 0.059906 | 0.164197 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__max_leaf_nodes': None, 'estimator__min_samples_split': 4}` |
| 2 | `ERT` | `ExtraTreesRegressor` | 22.220 | 0.054000 | 0.132008 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__max_leaf_nodes': None, 'estimator__min_samples_split': 6, 'estimator__n_estimators': 20}` |
| 3 | `LGBM` | `LGBMRegressor` | 29.294 | 0.082098 | 0.153147 | `{'estimator__learning_rate': 0.39, 'estimator__max_depth': 16, 'estimator__num_leaves': 28, 'estimator__subsample': 0.1}` |
| 4 | `GBM` | `GradientBoostingRegressor` | 29.872 | 0.058564 | 0.137715 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 16, 'estimator__max_features': 'log2', 'estimator__min_samples_split': 2, 'estimator__n_estimators': 36}` |
| 5 | `RF` | `RandomForestRegressor` | 29.915 | 0.063030 | 0.135792 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__max_features': 'log2', 'estimator__min_samples_split': 2, 'estimator__n_estimators': 90}` |
| 6 | `HGBM` | `HistGradientBoostingRegressor` | 34.670 | 0.086857 | 0.165503 | `{'estimator__learning_rate': 0.21, 'estimator__max_depth': 11, 'estimator__max_iter': 10, 'estimator__max_leaf_nodes': 27}` |
| 7 | `DT` | `DecisionTreeRegressor` | 35.855 | 0.063324 | 0.159736 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 14, 'estimator__max_leaf_nodes': 27, 'estimator__min_samples_split': 3}` |
| 8 | `XGBM` | `XGBRegressor` | 40.493 | 0.089319 | 0.168283 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14, 'estimator__n_estimators': 20}` |
| 9 | `SVR` | `SVR` | 53.213 | 0.126707 | 0.241140 | - |
| 10 | `MLP` | `MLPRegressor` | 2345.781 | 0.248637 | 0.349289 | `{'estimator__activation': 'tanh', 'estimator__alpha': 0.0001, 'estimator__early_stopping': True, 'estimator__hidden_layer_sizes': (100, 50), 'estimator__learning_rate': 'adaptive', 'estimator__max_iter': 600, 'estimator__solver': 'adam', 'estimator__tol': 0.0001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `DT` | 0.002286 | 0.002862 | 25.211 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000022 | 0.000029 | 0.126 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001604 | 0.002172 | 32.508 |
| `fft_y_Bw_filtered_ampl_3` | `RF` | 0.000023 | 0.000036 | 2.198 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.022161 | 0.028847 | 1.656 |
| `fft_y_Bw_filtered_ampl_39` | `RF` | 0.000021 | 0.000030 | 4.443 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.294936 | 1.235920 | 10.014 |
| `fft_y_Bw_filtered_ampl_40` | `ERT` | 0.000029 | 0.000042 | 9.646 |
| `fft_y_Bw_filtered_phase_40` | `ET` | 0.113752 | 0.222893 | 105.477 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000041 | 0.000056 | 4.857 |
| `fft_y_Bw_filtered_phase_78` | `LGBM` | 0.067285 | 0.130040 | 38.472 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000010 | 0.000018 | 7.591 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.078225 | 0.102423 | 28.044 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000093 | 0.000285 | 8.476 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.123047 | 0.478520 | 19.164 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000046 | 0.000158 | 6.639 |
| `fft_y_Bw_filtered_phase_162` | `ERT` | 0.050000 | 0.093031 | 2.581 |
| `fft_y_Bw_filtered_ampl_240` | `ET` | 0.000082 | 0.000194 | 11.408 |
| `fft_y_Bw_filtered_phase_240` | `GBM` | 0.241564 | 0.546893 | 12.390 |

## Artifact Paths

- config path: `config\paper_reimplementation\rcim_ml_compensation\rcim_track1_polished_input_mode_retraining\campaigns\dataset_input_mode_retraining__rcim_track1__polished_actual_values\queue\003_rcim_track1_bw.yaml`
- output directory: `output\validation_checks\rcim_track1\2026-07-18-11-56-46__rcim_track1_polished_actual_values_bw_rcim_track1_polished_input_mode_campaign_validation`
- model bundle: `output\validation_checks\rcim_track1\2026-07-18-11-56-46__rcim_track1_polished_actual_values_bw_rcim_track1_polished_input_mode_campaign_validation\paper_family_model_bank.pkl`
- python export root: `output\validation_checks\rcim_track1\2026-07-18-11-56-46__rcim_track1_polished_actual_values_bw_rcim_track1_polished_input_mode_campaign_validation\python_export`
- ONNX export root: `output\validation_checks\rcim_track1\2026-07-18-11-56-46__rcim_track1_polished_actual_values_bw_rcim_track1_polished_input_mode_campaign_validation\onnx_export`
- validation summary: `output\validation_checks\rcim_track1\2026-07-18-11-56-46__rcim_track1_polished_actual_values_bw_rcim_track1_polished_input_mode_campaign_validation\validation_summary.yaml`
- best-parameter summary: `output\validation_checks\rcim_track1\2026-07-18-11-56-46__rcim_track1_polished_actual_values_bw_rcim_track1_polished_input_mode_campaign_validation\best_parameter_summary.yaml`
