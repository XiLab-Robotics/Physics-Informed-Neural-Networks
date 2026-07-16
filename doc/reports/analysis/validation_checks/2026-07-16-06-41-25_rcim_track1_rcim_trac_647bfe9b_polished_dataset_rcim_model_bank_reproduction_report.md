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
- winning mean component MAPE: `11.974%`
- winning mean component MAE: `0.054452`
- winning mean component RMSE: `0.147582`

## Family Ranking

| Rank | Family | Estimator | Mean MAPE % | Mean MAE | Mean RMSE | Best Params |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | `ERT` | `ExtraTreesRegressor` | 11.974 | 0.054452 | 0.147582 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 18, 'estimator__max_leaf_nodes': None, 'estimator__min_samples_split': 2, 'estimator__n_estimators': 20}` |
| 2 | `GBM` | `GradientBoostingRegressor` | 13.331 | 0.071038 | 0.169806 | `{'estimator__criterion': 'squared_error', 'estimator__learning_rate': 0.1, 'estimator__max_depth': 16, 'estimator__max_features': 'log2', 'estimator__min_samples_split': 6, 'estimator__n_estimators': 36}` |
| 3 | `DT` | `DecisionTreeRegressor` | 13.461 | 0.061555 | 0.199731 | `{'estimator__criterion': 'absolute_error', 'estimator__max_depth': 14, 'estimator__max_leaf_nodes': None, 'estimator__min_samples_split': 5}` |
| 4 | `RF` | `RandomForestRegressor` | 13.581 | 0.074108 | 0.167930 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__max_features': 'log2', 'estimator__min_samples_split': 3, 'estimator__n_estimators': 52}` |
| 5 | `ET` | `ExtraTreeRegressor` | 16.627 | 0.064366 | 0.187656 | `{'estimator__criterion': 'squared_error', 'estimator__max_depth': 14, 'estimator__max_leaf_nodes': None, 'estimator__min_samples_split': 4}` |
| 6 | `HGBM` | `HistGradientBoostingRegressor` | 21.422 | 0.098844 | 0.191102 | `{'estimator__learning_rate': 0.21, 'estimator__max_depth': 14, 'estimator__max_iter': 10, 'estimator__max_leaf_nodes': 27}` |
| 7 | `XGBM` | `XGBRegressor` | 26.397 | 0.093559 | 0.181755 | `{'estimator__colsample_bytree': 0.8, 'estimator__learning_rate': 0.2, 'estimator__max_depth': 14, 'estimator__n_estimators': 20}` |
| 8 | `LGBM` | `LGBMRegressor` | 44.037 | 0.141358 | 0.232188 | `{'estimator__learning_rate': 0.01, 'estimator__max_depth': 14, 'estimator__num_leaves': 28, 'estimator__subsample': 0.1}` |
| 9 | `SVR` | `SVR` | 45.871 | 0.141857 | 0.264935 | - |
| 10 | `MLP` | `MLPRegressor` | 5542.992 | 0.194432 | 0.303693 | `{'estimator__activation': 'tanh', 'estimator__alpha': 0.0001, 'estimator__early_stopping': True, 'estimator__hidden_layer_sizes': (100, 50), 'estimator__learning_rate': 'adaptive', 'estimator__max_iter': 600, 'estimator__solver': 'adam', 'estimator__tol': 0.0001}` |

## Per-Target Winners

| Target | Winning Family | MAE | RMSE | MAPE % |
| --- | --- | ---: | ---: | ---: |
| `fft_y_Fw_filtered_ampl_0` | `ERT` | 0.000769 | 0.001055 | 1.416 |
| `fft_y_Fw_filtered_ampl_1` | `GBM` | 0.000023 | 0.000029 | 0.133 |
| `fft_y_Fw_filtered_phase_1` | `GBM` | 0.001817 | 0.002619 | 18.526 |
| `fft_y_Fw_filtered_ampl_3` | `GBM` | 0.000019 | 0.000026 | 2.307 |
| `fft_y_Fw_filtered_phase_3` | `RF` | 0.020418 | 0.028345 | 1.132 |
| `fft_y_Fw_filtered_ampl_39` | `RF` | 0.000031 | 0.000043 | 2.623 |
| `fft_y_Fw_filtered_phase_39` | `GBM` | 0.018213 | 0.026614 | 1.457 |
| `fft_y_Fw_filtered_ampl_40` | `GBM` | 0.000027 | 0.000041 | 3.366 |
| `fft_y_Fw_filtered_phase_40` | `RF` | 0.041747 | 0.067010 | 60.613 |
| `fft_y_Fw_filtered_ampl_78` | `ERT` | 0.000039 | 0.000058 | 7.556 |
| `fft_y_Fw_filtered_phase_78` | `RF` | 0.083179 | 0.237482 | 24.915 |
| `fft_y_Fw_filtered_ampl_81` | `ERT` | 0.000011 | 0.000016 | 3.470 |
| `fft_y_Fw_filtered_phase_81` | `ERT` | 0.045361 | 0.064992 | 3.369 |
| `fft_y_Fw_filtered_ampl_156` | `ERT` | 0.000041 | 0.000133 | 10.014 |
| `fft_y_Fw_filtered_phase_156` | `ERT` | 0.359726 | 0.988177 | 19.795 |
| `fft_y_Fw_filtered_ampl_162` | `ERT` | 0.000027 | 0.000080 | 6.567 |
| `fft_y_Fw_filtered_phase_162` | `ET` | 0.200400 | 0.788483 | 7.728 |
| `fft_y_Fw_filtered_ampl_240` | `ERT` | 0.000033 | 0.000060 | 7.076 |
| `fft_y_Fw_filtered_phase_240` | `DT` | 0.145582 | 0.635436 | 6.637 |

## Artifact Paths

- config path: `config\paper_reimplementation\rcim_ml_compensation\rcim_track1_polished_input_mode_retraining\campaigns\dataset_input_mode_retraining__rcim_track1__polished_setpoints\queue\002_rcim_track1_fw.yaml`
- output directory: `output\validation_checks\rcim_track1\2026-07-13-21-11-39__rcim_track1_polished_setpoints_fw_rcim_track1_polished_input_mode_campaign_validation`
- model bundle: `output\validation_checks\rcim_track1\2026-07-13-21-11-39__rcim_track1_polished_setpoints_fw_rcim_track1_polished_input_mode_campaign_validation\paper_family_model_bank.pkl`
- python export root: `output\validation_checks\rcim_track1\2026-07-13-21-11-39__rcim_track1_polished_setpoints_fw_rcim_track1_polished_input_mode_campaign_validation\python_export`
- ONNX export root: `output\validation_checks\rcim_track1\2026-07-13-21-11-39__rcim_track1_polished_setpoints_fw_rcim_track1_polished_input_mode_campaign_validation\onnx_export`
- validation summary: `output\validation_checks\rcim_track1\2026-07-13-21-11-39__rcim_track1_polished_setpoints_fw_rcim_track1_polished_input_mode_campaign_validation\validation_summary.yaml`
- best-parameter summary: `output\validation_checks\rcim_track1\2026-07-13-21-11-39__rcim_track1_polished_setpoints_fw_rcim_track1_polished_input_mode_campaign_validation\best_parameter_summary.yaml`
