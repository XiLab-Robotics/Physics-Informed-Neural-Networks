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
- winning mean component MAPE: `16.896%`
- winning mean component MAE: `0.052804`
- winning mean component RMSE: `0.144117`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 16.896 | 0.052804 | 0.144117 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 14, 'estimator__max_leaf_nodes': None, 'estimator__min_samples_split': 4, 'estimator__n_estimators': 100}` |
| 2 | `DT` | `DecisionTreeRegressor` | 17.083 | 0.062226 | 0.204709 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 16, 'estimator__max_leaf_nodes': None, 'estimator__min_samples_split': 6}` |
| 3 | `RF` | `RandomForestRegressor` | 18.443 | 0.055463 | 0.157953 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 14, 'estimator__max_features': 1.0, 'estimator__min_samples_split': 2, 'estimator__n_estimators': 20}` |
| 4 | `ET` | `ExtraTreeRegressor` | 21.424 | 0.073405 | 0.189466 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 16, 'estimator__max_leaf_nodes': None, 'estimator__min_samples_split': 6}` |
| 5 | `HGBM` | `HistGradientBoostingRegressor` | 23.086 | 0.078125 | 0.168457 | `{'estimator__learning_rate': 0.39, 'estimator__max_depth': 11, 'estimator__max_iter': 10, 'estimator__max_leaf_nodes': 27}` |
| 6 | `LGBM` | `LGBMRegressor` | 23.172 | 0.079537 | 0.164991 | `{'estimator__learning_rate': 0.39, 'estimator__max_depth': 14, 'estimator__num_leaves': 10, 'estimator__subsample': 0.1}` |
| 7 | `GBM` | `GradientBoostingRegressor` | 26.651 | 0.079747 | 0.176947 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 15, 'estimator__max_features': None, 'estimator__min_samples_split': 5, 'estimator__n_estimators': 20}` |
| 8 | `XGBM` | `XGBRegressor` | 29.159 | 0.071517 | 0.159024 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.5, 'estimator__max_depth': 14, 'estimator__n_estimators': 20}` |
| 9 | `SVR` | `SVR` | 82.106 | 0.323896 | 0.435097 | - |
| 10 | `MLP` | `MLPRegressor` | 1501.437 | 0.374243 | 0.460604 | `{'estimator__activation': 'tanh', 'estimator__alpha': 0.0001, 'estimator__early_stopping': True, 'estimator__hidden_layer_sizes': (100, 50), 'estimator__learning_rate': 'adaptive', 'estimator__max_iter': 600, 'estimator__solver': 'adam', 'estimator__tol': 0.0001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Global_filtered_ampl_0` | `ERT` | 0.000784 | 0.001913 | 6.150 |
| `fft_y_Global_filtered_ampl_1` | `ERT` | 0.000026 | 0.000037 | 0.149 |
| `fft_y_Global_filtered_phase_1` | `GBM` | 0.002563 | 0.004040 | 35.797 |
| `fft_y_Global_filtered_ampl_3` | `LGBM` | 0.000019 | 0.000029 | 2.248 |
| `fft_y_Global_filtered_phase_3` | `LGBM` | 0.019881 | 0.032848 | 1.305 |
| `fft_y_Global_filtered_ampl_39` | `LGBM` | 0.000021 | 0.000030 | 2.944 |
| `fft_y_Global_filtered_phase_39` | `ERT` | 0.103757 | 0.458963 | 4.127 |
| `fft_y_Global_filtered_ampl_40` | `ERT` | 0.000025 | 0.000037 | 5.822 |
| `fft_y_Global_filtered_phase_40` | `DT` | 0.076045 | 0.130749 | 81.439 |
| `fft_y_Global_filtered_ampl_78` | `LGBM` | 0.000030 | 0.000043 | 4.585 |
| `fft_y_Global_filtered_phase_78` | `ERT` | 0.051397 | 0.124472 | 24.975 |
| `fft_y_Global_filtered_ampl_81` | `RF` | 0.000011 | 0.000018 | 5.549 |
| `fft_y_Global_filtered_phase_81` | `ERT` | 0.059671 | 0.090267 | 21.964 |
| `fft_y_Global_filtered_ampl_156` | `RF` | 0.000139 | 0.000559 | 13.515 |
| `fft_y_Global_filtered_phase_156` | `DT` | 0.375240 | 1.196472 | 21.123 |
| `fft_y_Global_filtered_ampl_162` | `ERT` | 0.000045 | 0.000158 | 8.719 |
| `fft_y_Global_filtered_phase_162` | `ERT` | 0.081959 | 0.232623 | 3.762 |
| `fft_y_Global_filtered_ampl_240` | `DT` | 0.000109 | 0.000324 | 14.978 |
| `fft_y_Global_filtered_phase_240` | `RF` | 0.311247 | 0.997373 | 12.865 |

## Artifact Paths

- config path: `config\paper_reimplementation\rcim_ml_compensation\rcim_track1_polished_input_mode_retraining\campaigns\dataset_input_mode_retraining__rcim_track1__polished_setpoints\queue\001_rcim_track1_global.yaml`
- output directory: `output\validation_checks\rcim_track1\2026-07-13-21-11-39__rcim_track1_polished_setpoints_global_rcim_track1_polished_input_mode_campaign_validation`
- model bundle: `output\validation_checks\rcim_track1\2026-07-13-21-11-39__rcim_track1_polished_setpoints_global_rcim_track1_polished_input_mode_campaign_validation\paper_family_model_bank.pkl`
- python export root: `output\validation_checks\rcim_track1\2026-07-13-21-11-39__rcim_track1_polished_setpoints_global_rcim_track1_polished_input_mode_campaign_validation\python_export`
- ONNX export root: `output\validation_checks\rcim_track1\2026-07-13-21-11-39__rcim_track1_polished_setpoints_global_rcim_track1_polished_input_mode_campaign_validation\onnx_export`
- validation summary: `output\validation_checks\rcim_track1\2026-07-13-21-11-39__rcim_track1_polished_setpoints_global_rcim_track1_polished_input_mode_campaign_validation\validation_summary.yaml`
- best-parameter summary: `output\validation_checks\rcim_track1\2026-07-13-21-11-39__rcim_track1_polished_setpoints_global_rcim_track1_polished_input_mode_campaign_validation\best_parameter_summary.yaml`
