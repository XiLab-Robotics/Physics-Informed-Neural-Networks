# Polished-Dataset RCIM Model-Bank Reproduction Validation Report

## Overview

This report covers the direction-specific `RCIM Model-Bank Reproduction` branch trained from measured `polished_dataset` curves.

- direction label: `forward`
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

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `13.206%`
- winning mean component MAE: `0.068143`
- winning mean component RMSE: `0.155034`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 13.206 | 0.068143 | 0.155034 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 15, 'estimator__max_leaf_nodes': None, 'estimator__min_samples_split': 6, 'estimator__n_estimators': 20}` |
| 2 | `LGBM` | `LGBMRegressor` | 15.733 | 0.078928 | 0.157836 | `{'estimator__learning_rate': 0.2, 'estimator__max_depth': 16, 'estimator__num_leaves': 28, 'estimator__subsample': 0.1}` |
| 3 | `DT` | `DecisionTreeRegressor` | 16.337 | 0.068630 | 0.199136 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 17, 'estimator__max_leaf_nodes': None, 'estimator__min_samples_split': 4}` |
| 4 | `RF` | `RandomForestRegressor` | 16.800 | 0.083611 | 0.176574 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 18, 'estimator__max_features': 'log2', 'estimator__min_samples_split': 3, 'estimator__n_estimators': 90}` |
| 5 | `GBM` | `GradientBoostingRegressor` | 16.991 | 0.077909 | 0.172611 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 18, 'estimator__max_features': 'log2', 'estimator__min_samples_split': 6, 'estimator__n_estimators': 36}` |
| 6 | `ET` | `ExtraTreeRegressor` | 18.773 | 0.085991 | 0.211069 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__max_leaf_nodes': None, 'estimator__min_samples_split': 6}` |
| 7 | `HGBM` | `HistGradientBoostingRegressor` | 22.198 | 0.101075 | 0.192864 | `{'estimator__learning_rate': 0.2, 'estimator__max_depth': 11, 'estimator__max_iter': 10, 'estimator__max_leaf_nodes': 27}` |
| 8 | `XGBM` | `XGBRegressor` | 26.548 | 0.102771 | 0.201788 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 15, 'estimator__n_estimators': 20}` |
| 9 | `SVR` | `SVR` | 45.199 | 0.141829 | 0.264584 | - |
| 10 | `MLP` | `MLPRegressor` | 3934.275 | 0.209145 | 0.310406 | `{'estimator__activation': 'tanh', 'estimator__alpha': 0.0001, 'estimator__early_stopping': True, 'estimator__hidden_layer_sizes': (200, 50), 'estimator__learning_rate': 'adaptive', 'estimator__max_iter': 600, 'estimator__solver': 'adam', 'estimator__tol': 0.0001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.000808 | 0.001155 | 1.544 |
| `fft_y_Fw_filtered_ampl_1` | `ERT` | 0.000023 | 0.000030 | 0.135 |
| `fft_y_Fw_filtered_phase_1` | `LGBM` | 0.001589 | 0.002108 | 24.223 |
| `fft_y_Fw_filtered_ampl_3` | `ERT` | 0.000020 | 0.000027 | 2.267 |
| `fft_y_Fw_filtered_phase_3` | `LGBM` | 0.022733 | 0.029683 | 1.261 |
| `fft_y_Fw_filtered_ampl_39` | `LGBM` | 0.000027 | 0.000041 | 2.219 |
| `fft_y_Fw_filtered_phase_39` | `LGBM` | 0.017559 | 0.024067 | 1.463 |
| `fft_y_Fw_filtered_ampl_40` | `ERT` | 0.000025 | 0.000036 | 3.245 |
| `fft_y_Fw_filtered_phase_40` | `SVR` | 0.050400 | 0.079955 | 64.146 |
| `fft_y_Fw_filtered_ampl_78` | `LGBM` | 0.000037 | 0.000051 | 6.033 |
| `fft_y_Fw_filtered_phase_78` | `ERT` | 0.093520 | 0.259441 | 31.908 |
| `fft_y_Fw_filtered_ampl_81` | `LGBM` | 0.000010 | 0.000015 | 3.416 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.045290 | 0.062951 | 3.271 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000062 | 0.000234 | 11.399 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.471632 | 0.968150 | 22.979 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000042 | 0.000117 | 9.310 |
| `fft_y_Fw_filtered_phase_162` | `DT` | 0.212884 | 0.874995 | 8.313 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000034 | 0.000054 | 8.626 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.164686 | 0.634265 | 7.417 |

## Artifact Paths

- config path: `config\paper_reimplementation\rcim_ml_compensation\rcim_track1_polished_input_mode_retraining\campaigns\dataset_input_mode_retraining__rcim_track1__polished_actual_values\queue\002_rcim_track1_fw.yaml`
- output directory: `output\validation_checks\rcim_track1\2026-07-18-11-55-05__rcim_track1_polished_actual_values_fw_rcim_track1_polished_input_mode_campaign_validation`
- model bundle: `output\validation_checks\rcim_track1\2026-07-18-11-55-05__rcim_track1_polished_actual_values_fw_rcim_track1_polished_input_mode_campaign_validation\paper_family_model_bank.pkl`
- python export root: `output\validation_checks\rcim_track1\2026-07-18-11-55-05__rcim_track1_polished_actual_values_fw_rcim_track1_polished_input_mode_campaign_validation\python_export`
- ONNX export root: `output\validation_checks\rcim_track1\2026-07-18-11-55-05__rcim_track1_polished_actual_values_fw_rcim_track1_polished_input_mode_campaign_validation\onnx_export`
- validation summary: `output\validation_checks\rcim_track1\2026-07-18-11-55-05__rcim_track1_polished_actual_values_fw_rcim_track1_polished_input_mode_campaign_validation\validation_summary.yaml`
- best-parameter summary: `output\validation_checks\rcim_track1\2026-07-18-11-55-05__rcim_track1_polished_actual_values_fw_rcim_track1_polished_input_mode_campaign_validation\best_parameter_summary.yaml`
