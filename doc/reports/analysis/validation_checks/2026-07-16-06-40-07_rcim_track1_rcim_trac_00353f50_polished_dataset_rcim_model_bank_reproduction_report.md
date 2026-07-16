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

- winning family: `ERT`
- winning estimator: `ExtraTreesRegressor`
- winning mean component MAPE: `18.246%`
- winning mean component MAE: `0.045708`
- winning mean component RMSE: `0.122004`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 18.246 | 0.045708 | 0.122004 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 18, 'estimator__max_leaf_nodes': None, 'estimator__min_samples_split': 5, 'estimator__n_estimators': 60}` |
| 2 | `ET` | `ExtraTreeRegressor` | 20.890 | 0.050174 | 0.149909 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 18, 'estimator__max_leaf_nodes': None, 'estimator__min_samples_split': 3}` |
| 3 | `LGBM` | `LGBMRegressor` | 24.084 | 0.061847 | 0.118226 | `{'estimator__learning_rate': 0.2, 'estimator__max_depth': 15, 'estimator__num_leaves': 28, 'estimator__subsample': 0.1}` |
| 4 | `RF` | `RandomForestRegressor` | 26.648 | 0.061383 | 0.129740 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__max_features': 'log2', 'estimator__min_samples_split': 6, 'estimator__n_estimators': 68}` |
| 5 | `GBM` | `GradientBoostingRegressor` | 30.468 | 0.065739 | 0.112880 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 17, 'estimator__max_features': 'log2', 'estimator__min_samples_split': 3, 'estimator__n_estimators': 20}` |
| 6 | `HGBM` | `HistGradientBoostingRegressor` | 34.101 | 0.086951 | 0.160629 | `{'estimator__learning_rate': 0.21, 'estimator__max_depth': 14, 'estimator__max_iter': 10, 'estimator__max_leaf_nodes': 27}` |
| 7 | `DT` | `DecisionTreeRegressor` | 36.120 | 0.056082 | 0.148074 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 14, 'estimator__max_leaf_nodes': 25, 'estimator__min_samples_split': 3}` |
| 8 | `XGBM` | `XGBRegressor` | 38.561 | 0.082693 | 0.155222 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14, 'estimator__n_estimators': 20}` |
| 9 | `SVR` | `SVR` | 53.149 | 0.126566 | 0.241018 | - |
| 10 | `MLP` | `MLPRegressor` | 3331.713 | 0.203671 | 0.314888 | `{'estimator__activation': 'tanh', 'estimator__alpha': 0.0001, 'estimator__early_stopping': True, 'estimator__hidden_layer_sizes': (100, 50), 'estimator__learning_rate': 'adaptive', 'estimator__max_iter': 600, 'estimator__solver': 'adam', 'estimator__tol': 0.0001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Bw_filtered_ampl_0` | `ET` | 0.000723 | 0.000984 | 15.593 |
| `fft_y_Bw_filtered_ampl_1` | `ERT` | 0.000023 | 0.000030 | 0.131 |
| `fft_y_Bw_filtered_phase_1` | `ERT` | 0.001470 | 0.001996 | 28.255 |
| `fft_y_Bw_filtered_ampl_3` | `LGBM` | 0.000020 | 0.000031 | 1.947 |
| `fft_y_Bw_filtered_phase_3` | `LGBM` | 0.018116 | 0.024326 | 1.361 |
| `fft_y_Bw_filtered_ampl_39` | `LGBM` | 0.000019 | 0.000029 | 4.198 |
| `fft_y_Bw_filtered_phase_39` | `DT` | 0.231609 | 1.073952 | 7.957 |
| `fft_y_Bw_filtered_ampl_40` | `RF` | 0.000029 | 0.000042 | 9.483 |
| `fft_y_Bw_filtered_phase_40` | `ERT` | 0.087080 | 0.142841 | 105.465 |
| `fft_y_Bw_filtered_ampl_78` | `LGBM` | 0.000028 | 0.000038 | 4.110 |
| `fft_y_Bw_filtered_phase_78` | `GBM` | 0.067565 | 0.156399 | 38.831 |
| `fft_y_Bw_filtered_ampl_81` | `ERT` | 0.000009 | 0.000017 | 7.539 |
| `fft_y_Bw_filtered_phase_81` | `ERT` | 0.070751 | 0.092324 | 24.730 |
| `fft_y_Bw_filtered_ampl_156` | `ERT` | 0.000092 | 0.000342 | 6.569 |
| `fft_y_Bw_filtered_phase_156` | `ET` | 0.191639 | 0.659514 | 17.612 |
| `fft_y_Bw_filtered_ampl_162` | `ERT` | 0.000031 | 0.000089 | 5.765 |
| `fft_y_Bw_filtered_phase_162` | `LGBM` | 0.043125 | 0.073989 | 2.282 |
| `fft_y_Bw_filtered_ampl_240` | `ERT` | 0.000085 | 0.000216 | 11.292 |
| `fft_y_Bw_filtered_phase_240` | `ET` | 0.138411 | 0.450707 | 6.943 |

## Artifact Paths

- config path: `config\paper_reimplementation\rcim_ml_compensation\rcim_track1_polished_input_mode_retraining\campaigns\dataset_input_mode_retraining__rcim_track1__polished_setpoints\queue\003_rcim_track1_bw.yaml`
- output directory: `output\validation_checks\rcim_track1\2026-07-13-21-11-39__rcim_track1_polished_setpoints_bw_rcim_track1_polished_input_mode_campaign_validation`
- model bundle: `output\validation_checks\rcim_track1\2026-07-13-21-11-39__rcim_track1_polished_setpoints_bw_rcim_track1_polished_input_mode_campaign_validation\paper_family_model_bank.pkl`
- python export root: `output\validation_checks\rcim_track1\2026-07-13-21-11-39__rcim_track1_polished_setpoints_bw_rcim_track1_polished_input_mode_campaign_validation\python_export`
- ONNX export root: `output\validation_checks\rcim_track1\2026-07-13-21-11-39__rcim_track1_polished_setpoints_bw_rcim_track1_polished_input_mode_campaign_validation\onnx_export`
- validation summary: `output\validation_checks\rcim_track1\2026-07-13-21-11-39__rcim_track1_polished_setpoints_bw_rcim_track1_polished_input_mode_campaign_validation\validation_summary.yaml`
- best-parameter summary: `output\validation_checks\rcim_track1\2026-07-13-21-11-39__rcim_track1_polished_setpoints_bw_rcim_track1_polished_input_mode_campaign_validation\best_parameter_summary.yaml`
