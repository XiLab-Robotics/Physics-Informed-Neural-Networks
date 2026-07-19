# Polished-Dataset RCIM Model-Bank Reproduction Validation Report

## Overview

This report covers the direction-specific `RCIM Model-Bank Reproduction` branch trained from measured `polished_dataset` curves.

- direction label: `global`
- dataset root: `data\polished_dataset`
- dataset config: `config\datasets\transmission_error_dataset.yaml`
- selected harmonics: `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`
- decomposition point stride: `1`
- feature schema: `angular_position_deg, input_speed_rpm, input_torque_nm, oil_temperature_deg, direction_flag`
- target count: `19`

## Split Summary

- train rows / files: `1356` / `1356`
- validation rows / files: `388` / `388`
- test rows / files: `194` / `194`
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
- winning mean component MAPE: `17.038%`
- winning mean component MAE: `0.056544`
- winning mean component RMSE: `0.148628`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 17.038 | 0.056544 | 0.148628 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__max_leaf_nodes': None, 'estimator__min_samples_split': 5, 'estimator__n_estimators': 100}` |
| 2 | `ET` | `ExtraTreeRegressor` | 23.011 | 0.072102 | 0.215187 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 16, 'estimator__max_leaf_nodes': None, 'estimator__min_samples_split': 4}` |
| 3 | `RF` | `RandomForestRegressor` | 24.827 | 0.077727 | 0.179035 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 14, 'estimator__max_features': 'log2', 'estimator__min_samples_split': 2, 'estimator__n_estimators': 52}` |
| 4 | `GBM` | `GradientBoostingRegressor` | 25.519 | 0.071030 | 0.177012 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 15, 'estimator__max_features': 'log2', 'estimator__min_samples_split': 6, 'estimator__n_estimators': 84}` |
| 5 | `HGBM` | `HistGradientBoostingRegressor` | 27.141 | 0.088849 | 0.189226 | `{'estimator__learning_rate': 0.39, 'estimator__max_depth': 16, 'estimator__max_iter': 1000, 'estimator__max_leaf_nodes': 28}` |
| 6 | `LGBM` | `LGBMRegressor` | 29.255 | 0.093162 | 0.194605 | `{'estimator__learning_rate': 0.58, 'estimator__max_depth': 16, 'estimator__num_leaves': 64, 'estimator__subsample': 0.1}` |
| 7 | `XGBM` | `XGBRegressor` | 34.577 | 0.084025 | 0.182804 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.3, 'estimator__max_depth': 17, 'estimator__n_estimators': 20}` |
| 8 | `DT` | `DecisionTreeRegressor` | 39.564 | 0.099808 | 0.245895 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 14, 'estimator__max_leaf_nodes': 23, 'estimator__min_samples_split': 2}` |
| 9 | `SVR` | `SVR` | 58.025 | 0.130682 | 0.251718 | - |
| 10 | `MLP` | `MLPRegressor` | 1429.699 | 0.188586 | 0.294426 | `{'estimator__activation': 'tanh', 'estimator__alpha': 0.0001, 'estimator__early_stopping': True, 'estimator__hidden_layer_sizes': (100, 50), 'estimator__learning_rate': 'adaptive', 'estimator__max_iter': 600, 'estimator__solver': 'adam', 'estimator__tol': 0.0001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Global_filtered_ampl_0` | `ERT` | 0.000857 | 0.002261 | 10.452 |
| `fft_y_Global_filtered_ampl_1` | `RF` | 0.000024 | 0.000035 | 0.142 |
| `fft_y_Global_filtered_phase_1` | `XGBM` | 0.002325 | 0.003451 | 41.575 |
| `fft_y_Global_filtered_ampl_3` | `GBM` | 0.000020 | 0.000028 | 2.360 |
| `fft_y_Global_filtered_phase_3` | `ERT` | 0.022085 | 0.036219 | 1.456 |
| `fft_y_Global_filtered_ampl_39` | `ERT` | 0.000021 | 0.000030 | 3.075 |
| `fft_y_Global_filtered_phase_39` | `ERT` | 0.120094 | 0.535965 | 4.646 |
| `fft_y_Global_filtered_ampl_40` | `ERT` | 0.000025 | 0.000037 | 5.876 |
| `fft_y_Global_filtered_phase_40` | `ERT` | 0.061870 | 0.110887 | 94.988 |
| `fft_y_Global_filtered_ampl_78` | `ERT` | 0.000040 | 0.000058 | 6.085 |
| `fft_y_Global_filtered_phase_78` | `ERT` | 0.047961 | 0.111965 | 24.441 |
| `fft_y_Global_filtered_ampl_81` | `ERT` | 0.000011 | 0.000016 | 5.607 |
| `fft_y_Global_filtered_phase_81` | `GBM` | 0.062974 | 0.093908 | 19.885 |
| `fft_y_Global_filtered_ampl_156` | `ERT` | 0.000128 | 0.000448 | 15.226 |
| `fft_y_Global_filtered_phase_156` | `ERT` | 0.349560 | 0.794264 | 36.961 |
| `fft_y_Global_filtered_ampl_162` | `ERT` | 0.000067 | 0.000229 | 10.394 |
| `fft_y_Global_filtered_phase_162` | `ERT` | 0.084236 | 0.209722 | 3.896 |
| `fft_y_Global_filtered_ampl_240` | `ET` | 0.000130 | 0.000381 | 14.591 |
| `fft_y_Global_filtered_phase_240` | `ERT` | 0.323470 | 0.927856 | 14.103 |

## Artifact Paths

- config path: `config\paper_reimplementation\rcim_ml_compensation\rcim_track1_polished_input_mode_retraining\campaigns\dataset_input_mode_retraining__rcim_track1__polished_actual_values\queue\001_rcim_track1_global.yaml`
- output directory: `output\validation_checks\rcim_track1\2026-07-18-11-55-05__rcim_track1_polished_actual_values_global_rcim_track1_polished_input_mode_campaign_validation`
- model bundle: `output\validation_checks\rcim_track1\2026-07-18-11-55-05__rcim_track1_polished_actual_values_global_rcim_track1_polished_input_mode_campaign_validation\paper_family_model_bank.pkl`
- python export root: `output\validation_checks\rcim_track1\2026-07-18-11-55-05__rcim_track1_polished_actual_values_global_rcim_track1_polished_input_mode_campaign_validation\python_export`
- ONNX export root: `output\validation_checks\rcim_track1\2026-07-18-11-55-05__rcim_track1_polished_actual_values_global_rcim_track1_polished_input_mode_campaign_validation\onnx_export`
- validation summary: `output\validation_checks\rcim_track1\2026-07-18-11-55-05__rcim_track1_polished_actual_values_global_rcim_track1_polished_input_mode_campaign_validation\validation_summary.yaml`
- best-parameter summary: `output\validation_checks\rcim_track1\2026-07-18-11-55-05__rcim_track1_polished_actual_values_global_rcim_track1_polished_input_mode_campaign_validation\best_parameter_summary.yaml`
