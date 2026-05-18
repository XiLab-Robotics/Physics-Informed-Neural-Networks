# Track 2 Directional Model Comparison

## Overview

This report is the canonical `Track 2` offline comparison between
`Track 1`, recovered original, retuned paper-reference model banks, and
exported `Wave 1` repository models. It starts from the current
direction-aware comparison matrix.

## Dataset And Split

- dataset config: `config/datasets/transmission_error_dataset.yaml`;
- dataset root: `data\datasets`;
- comparison mode: `full_directional_candidate_matrix`;
- candidate count: `75`;
- held-out curve count before candidate filtering: `194`;
- percentage-error denominator: `peak_to_peak_truth`;
- `Fw` candidates are evaluated only on forward curves;
- `Bw` candidates are evaluated only on backward curves;
- `global` candidates are evaluated on both directions and reported with
  direction-separated metrics.

## Candidate Inventory

| Candidate | Family | Source | Kind | Surface | Valid Directions | Model Source |
| --- | --- | --- | --- | --- | --- | --- |
| `SVM19_Fw` | `SVM` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\svm_reference_models\reference_inventory.yaml` |
| `SVM19_Bw` | `SVM` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\svm_reference_models\reference_inventory.yaml` |
| `MLP19_Fw` | `MLP` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\mlp_reference_models\reference_inventory.yaml` |
| `MLP19_Bw` | `MLP` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\mlp_reference_models\reference_inventory.yaml` |
| `RF19_Fw` | `RF` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\rf_reference_models\reference_inventory.yaml` |
| `RF19_Bw` | `RF` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\rf_reference_models\reference_inventory.yaml` |
| `DT19_Fw` | `DT` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\dt_reference_models\reference_inventory.yaml` |
| `DT19_Bw` | `DT` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\dt_reference_models\reference_inventory.yaml` |
| `ET19_Fw` | `ET` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\et_reference_models\reference_inventory.yaml` |
| `ET19_Bw` | `ET` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\et_reference_models\reference_inventory.yaml` |
| `ERT19_Fw` | `ERT` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\ert_reference_models\reference_inventory.yaml` |
| `ERT19_Bw` | `ERT` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\ert_reference_models\reference_inventory.yaml` |
| `GBM19_Fw` | `GBM` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\gbm_reference_models\reference_inventory.yaml` |
| `GBM19_Bw` | `GBM` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\gbm_reference_models\reference_inventory.yaml` |
| `HGBM19_Fw` | `HGBM` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\hgbm_reference_models\reference_inventory.yaml` |
| `HGBM19_Bw` | `HGBM` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\hgbm_reference_models\reference_inventory.yaml` |
| `XGBM19_Fw` | `XGBM` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\xgbm_reference_models\reference_inventory.yaml` |
| `XGBM19_Bw` | `XGBM` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\xgbm_reference_models\reference_inventory.yaml` |
| `LGBM19_Fw` | `LGBM` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\lgbm_reference_models\reference_inventory.yaml` |
| `LGBM19_Bw` | `LGBM` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\reference_inventory.yaml` |
| `ELM19_Fw` | `ELM` | `rcim_track1` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\elm_reference_models\reference_inventory.yaml` |
| `ELM19_Bw` | `ELM` | `rcim_track1` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\elm_reference_models\reference_inventory.yaml` |
| `rcim_original_SVM19_Fw` | `SVM` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\svm_reference_models\reference_inventory.yaml` |
| `rcim_original_MLP19_Fw` | `MLP` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\mlp_reference_models\reference_inventory.yaml` |
| `rcim_original_RF19_Fw` | `RF` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\rf_reference_models\reference_inventory.yaml` |
| `rcim_original_DT19_Fw` | `DT` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\dt_reference_models\reference_inventory.yaml` |
| `rcim_original_ET19_Fw` | `ET` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\et_reference_models\reference_inventory.yaml` |
| `rcim_original_ERT19_Fw` | `ERT` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\ert_reference_models\reference_inventory.yaml` |
| `rcim_original_GBM19_Fw` | `GBM` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\gbm_reference_models\reference_inventory.yaml` |
| `rcim_original_HGBM19_Fw` | `HGBM` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\hgbm_reference_models\reference_inventory.yaml` |
| `rcim_original_XGBM19_Fw` | `XGBM` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\xgbm_reference_models\reference_inventory.yaml` |
| `rcim_original_LGBM19_Fw` | `LGBM` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\lgbm_reference_models\reference_inventory.yaml` |
| `rcim_original_ELM19_Fw` | `ELM` | `rcim_original` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward\elm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_SVM19_Fw` | `SVM` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\svm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_MLP19_Fw` | `MLP` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\mlp_reference_models\reference_inventory.yaml` |
| `rcim_retuned_RF19_Fw` | `RF` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\rf_reference_models\reference_inventory.yaml` |
| `rcim_retuned_DT19_Fw` | `DT` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\dt_reference_models\reference_inventory.yaml` |
| `rcim_retuned_ET19_Fw` | `ET` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\et_reference_models\reference_inventory.yaml` |
| `rcim_retuned_ERT19_Fw` | `ERT` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\ert_reference_models\reference_inventory.yaml` |
| `rcim_retuned_GBM19_Fw` | `GBM` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\gbm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_HGBM19_Fw` | `HGBM` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\hgbm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_XGBM19_Fw` | `XGBM` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\xgbm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_LGBM19_Fw` | `LGBM` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\lgbm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_ELM19_Fw` | `ELM` | `rcim_retuned` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward\elm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_SVM19_Bw` | `SVM` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\svm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_MLP19_Bw` | `MLP` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\mlp_reference_models\reference_inventory.yaml` |
| `rcim_retuned_RF19_Bw` | `RF` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\rf_reference_models\reference_inventory.yaml` |
| `rcim_retuned_DT19_Bw` | `DT` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\dt_reference_models\reference_inventory.yaml` |
| `rcim_retuned_ET19_Bw` | `ET` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\et_reference_models\reference_inventory.yaml` |
| `rcim_retuned_ERT19_Bw` | `ERT` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\ert_reference_models\reference_inventory.yaml` |
| `rcim_retuned_GBM19_Bw` | `GBM` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\gbm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_HGBM19_Bw` | `HGBM` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\hgbm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_XGBM19_Bw` | `XGBM` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\xgbm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_LGBM19_Bw` | `LGBM` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\lgbm_reference_models\reference_inventory.yaml` |
| `rcim_retuned_ELM19_Bw` | `ELM` | `rcim_retuned` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward\elm_reference_models\reference_inventory.yaml` |
| `feedforward_global` | `feedforward` | `wave1` | `wave1_exported_model` | `global` | `forward, backward` | `models\exported\feedforward\global\python\feedforward-epoch=198-val_mae=0.00295772.ckpt` |
| `feedforward_Fw` | `feedforward` | `wave1` | `wave1_exported_model` | `Fw` | `forward` | `models\exported\feedforward\forward\python\feedforward-epoch=086-val_mae=0.00274640.ckpt` |
| `feedforward_Bw` | `feedforward` | `wave1` | `wave1_exported_model` | `Bw` | `backward` | `models\exported\feedforward\backward\python\feedforward-epoch=209-val_mae=0.00287506.ckpt` |
| `harmonic_regression_global` | `harmonic_regression` | `wave1` | `wave1_exported_model` | `global` | `forward, backward` | `models\exported\harmonic_regression\global\python\harmonic_regression-epoch=040-val_mae=0.01702522.ckpt` |
| `harmonic_regression_Fw` | `harmonic_regression` | `wave1` | `wave1_exported_model` | `Fw` | `forward` | `models\exported\harmonic_regression\forward\python\harmonic_regression-epoch=043-val_mae=0.00284796.ckpt` |
| `harmonic_regression_Bw` | `harmonic_regression` | `wave1` | `wave1_exported_model` | `Bw` | `backward` | `models\exported\harmonic_regression\backward\python\harmonic_regression-epoch=047-val_mae=0.00363757.ckpt` |
| `periodic_mlp_global` | `periodic_mlp` | `wave1` | `wave1_exported_model` | `global` | `forward, backward` | `models\exported\periodic_mlp\global\python\periodic_mlp-epoch=075-val_mae=0.00296443.ckpt` |
| `periodic_mlp_Fw` | `periodic_mlp` | `wave1` | `wave1_exported_model` | `Fw` | `forward` | `models\exported\periodic_mlp\forward\python\periodic_mlp-epoch=023-val_mae=0.00275063.ckpt` |
| `periodic_mlp_Bw` | `periodic_mlp` | `wave1` | `wave1_exported_model` | `Bw` | `backward` | `models\exported\periodic_mlp\backward\python\periodic_mlp-epoch=112-val_mae=0.00290718.ckpt` |
| `residual_harmonic_mlp_global` | `residual_harmonic_mlp` | `wave1` | `wave1_exported_model` | `global` | `forward, backward` | `models\exported\residual_harmonic_mlp\global\python\residual_harmonic_mlp-epoch=200-val_mae=0.00286835.ckpt` |
| `residual_harmonic_mlp_Fw` | `residual_harmonic_mlp` | `wave1` | `wave1_exported_model` | `Fw` | `forward` | `models\exported\residual_harmonic_mlp\forward\python\residual_harmonic_mlp-epoch=018-val_mae=0.00275861.ckpt` |
| `residual_harmonic_mlp_Bw` | `residual_harmonic_mlp` | `wave1` | `wave1_exported_model` | `Bw` | `backward` | `models\exported\residual_harmonic_mlp\backward\python\residual_harmonic_mlp-epoch=115-val_mae=0.00292969.ckpt` |
| `tree_global` | `tree` | `wave1` | `wave1_exported_model` | `global` | `forward, backward` | `models\exported\tree\global\python\tree_model.pkl` |
| `tree_Fw` | `tree` | `wave1` | `wave1_exported_model` | `Fw` | `forward` | `models\exported\tree\forward\python\tree_model.pkl` |
| `tree_Bw` | `tree` | `wave1` | `wave1_exported_model` | `Bw` | `backward` | `models\exported\tree\backward\python\tree_model.pkl` |
| `paper_original_best_Fw` | `best_composite` | `rcim_original` | `composite_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_original\forward` |
| `paper_retuned_best_Fw` | `best_composite` | `rcim_retuned` | `composite_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_retuned\forward` |
| `track1_best_Fw` | `best_composite` | `rcim_track1` | `composite_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward` |
| `paper_retuned_best_Bw` | `best_composite` | `rcim_retuned` | `composite_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_retuned\backward` |
| `track1_best_Bw` | `best_composite` | `rcim_track1` | `composite_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward` |

## Forward Comparison

### Original Forward Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `rcim_original_ERT19_Fw` | 0.001471 | 0.001677 | 3.253 | 6.145 |
| `rcim_original_RF19_Fw` | 0.001767 | 0.001971 | 3.940 | 6.872 |
| `rcim_original_LGBM19_Fw` | 0.001801 | 0.002004 | 4.017 | 10.054 |
| `rcim_original_DT19_Fw` | 0.001919 | 0.002114 | 4.306 | 9.063 |
| `rcim_original_GBM19_Fw` | 0.001921 | 0.002122 | 4.312 | 8.193 |
| `rcim_original_HGBM19_Fw` | 0.002011 | 0.002217 | 4.493 | 10.617 |
| `rcim_original_ET19_Fw` | 0.002232 | 0.002432 | 4.985 | 11.357 |
| `rcim_original_XGBM19_Fw` | 0.002594 | 0.002814 | 5.805 | 10.574 |
| `paper_original_best_Fw` | 0.002769 | 0.002951 | 6.250 | 13.827 |
| `rcim_original_SVM19_Fw` | 0.003052 | 0.003324 | 6.767 | 13.827 |
| `rcim_original_ELM19_Fw` | 0.005423 | 0.005731 | 12.130 | 28.721 |
| `rcim_original_MLP19_Fw` | 0.018754 | 0.022589 | 42.943 | 107.515 |

### Retuned Forward Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `rcim_retuned_GBM19_Fw` | 0.001089 | 0.001299 | 2.372 | 4.912 |
| `rcim_retuned_RF19_Fw` | 0.001487 | 0.001699 | 3.292 | 5.998 |
| `rcim_retuned_ERT19_Fw` | 0.001807 | 0.002010 | 4.039 | 7.599 |
| `paper_retuned_best_Fw` | 0.001839 | 0.002041 | 4.109 | 9.866 |
| `rcim_retuned_HGBM19_Fw` | 0.001851 | 0.002056 | 4.126 | 9.401 |
| `rcim_retuned_LGBM19_Fw` | 0.001851 | 0.002055 | 4.135 | 9.866 |
| `rcim_retuned_DT19_Fw` | 0.001919 | 0.002114 | 4.306 | 9.063 |
| `rcim_retuned_ET19_Fw` | 0.002001 | 0.002196 | 4.426 | 9.533 |
| `rcim_retuned_XGBM19_Fw` | 0.002054 | 0.002264 | 4.588 | 10.488 |
| `rcim_retuned_SVM19_Fw` | 0.003167 | 0.003428 | 7.035 | 12.971 |
| `rcim_retuned_ELM19_Fw` | 0.007182 | 0.007463 | 16.181 | 40.024 |
| `rcim_retuned_MLP19_Fw` | 0.016647 | 0.020154 | 38.510 | 86.197 |

### Track 1 Forward Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `RF19_Fw` | 0.002164 | 0.002371 | 4.841 | 11.061 |
| `ERT19_Fw` | 0.002295 | 0.002491 | 5.163 | 13.141 |
| `GBM19_Fw` | 0.002779 | 0.002981 | 6.238 | 12.995 |
| `track1_best_Fw` | 0.003014 | 0.003204 | 6.819 | 11.638 |
| `DT19_Fw` | 0.003122 | 0.003313 | 7.011 | 13.928 |
| `SVM19_Fw` | 0.003236 | 0.003487 | 7.185 | 11.841 |
| `HGBM19_Fw` | 0.003251 | 0.003464 | 7.315 | 13.802 |
| `ET19_Fw` | 0.003267 | 0.003467 | 7.339 | 14.670 |
| `XGBM19_Fw` | 0.004190 | 0.004396 | 9.407 | 22.660 |
| `LGBM19_Fw` | 0.006812 | 0.007009 | 15.415 | 30.398 |
| `ELM19_Fw` | 0.007281 | 0.007573 | 16.352 | 36.326 |
| `MLP19_Fw` | 0.038690 | 0.047157 | 89.567 | 201.437 |

### Wave 1 Forward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `tree_global` | 0.002998 | 0.003364 | 6.590 | 11.601 |
| `tree_Fw` | 0.003053 | 0.003395 | 6.731 | 11.995 |
| `periodic_mlp_Fw` | 0.003366 | 0.003794 | 7.467 | 12.904 |
| `periodic_mlp_global` | 0.003380 | 0.003791 | 7.493 | 14.349 |
| `harmonic_regression_Fw` | 0.003394 | 0.003807 | 7.534 | 11.391 |
| `residual_harmonic_mlp_Fw` | 0.003434 | 0.003876 | 7.618 | 13.617 |
| `feedforward_Fw` | 0.003466 | 0.003904 | 7.685 | 13.132 |
| `feedforward_global` | 0.003550 | 0.003979 | 7.916 | 16.195 |
| `residual_harmonic_mlp_global` | 0.003649 | 0.004051 | 8.123 | 14.713 |
| `harmonic_regression_global` | 0.018314 | 0.018547 | 41.749 | 79.404 |

## Backward Comparison

### Retuned Backward Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `rcim_retuned_GBM19_Bw` | 0.002766 | 0.003300 | 5.398 | 12.280 |
| `rcim_retuned_ET19_Bw` | 0.003441 | 0.004028 | 7.021 | 15.287 |
| `rcim_retuned_ERT19_Bw` | 0.003551 | 0.004161 | 7.269 | 13.187 |
| `rcim_retuned_RF19_Bw` | 0.003649 | 0.004256 | 7.543 | 15.083 |
| `paper_retuned_best_Bw` | 0.003675 | 0.004284 | 7.572 | 15.645 |
| `rcim_retuned_SVM19_Bw` | 0.004016 | 0.004599 | 8.813 | 17.215 |
| `rcim_retuned_DT19_Bw` | 0.004578 | 0.005169 | 9.728 | 19.601 |
| `rcim_retuned_HGBM19_Bw` | 0.004683 | 0.005301 | 9.978 | 17.712 |
| `rcim_retuned_LGBM19_Bw` | 0.008105 | 0.008655 | 18.057 | 35.748 |
| `rcim_retuned_ELM19_Bw` | 0.008917 | 0.009518 | 20.169 | 51.896 |
| `rcim_retuned_XGBM19_Bw` | 0.010679 | 0.011209 | 24.184 | 48.082 |
| `rcim_retuned_MLP19_Bw` | 0.019115 | 0.023025 | 44.141 | 88.991 |

### Track 1 Backward Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `SVM19_Bw` | 0.004822 | 0.005116 | 10.864 | 25.533 |
| `track1_best_Bw` | 0.005027 | 0.005212 | 11.860 | 48.106 |
| `LGBM19_Bw` | 0.005037 | 0.005231 | 11.880 | 48.106 |
| `GBM19_Bw` | 0.005180 | 0.005363 | 12.252 | 49.984 |
| `DT19_Bw` | 0.005226 | 0.005409 | 12.359 | 48.860 |
| `ERT19_Bw` | 0.005258 | 0.005442 | 12.434 | 51.665 |
| `RF19_Bw` | 0.005392 | 0.005584 | 12.731 | 55.740 |
| `ET19_Bw` | 0.006273 | 0.006520 | 14.314 | 48.624 |
| `HGBM19_Bw` | 0.006619 | 0.006834 | 15.494 | 53.982 |
| `XGBM19_Bw` | 0.007991 | 0.008195 | 18.722 | 59.067 |
| `ELM19_Bw` | 0.010071 | 0.010486 | 23.034 | 52.159 |
| `MLP19_Bw` | 0.036681 | 0.044921 | 86.544 | 225.831 |

### Wave 1 Backward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `tree_Bw` | 0.003258 | 0.003651 | 7.051 | 14.116 |
| `tree_global` | 0.003290 | 0.003702 | 7.118 | 13.703 |
| `periodic_mlp_Bw` | 0.003574 | 0.004006 | 7.807 | 13.970 |
| `periodic_mlp_global` | 0.003610 | 0.004030 | 7.879 | 13.661 |
| `residual_harmonic_mlp_global` | 0.003639 | 0.004044 | 7.967 | 14.489 |
| `feedforward_Bw` | 0.003644 | 0.004067 | 7.977 | 14.284 |
| `residual_harmonic_mlp_Bw` | 0.003672 | 0.004089 | 8.046 | 14.973 |
| `harmonic_regression_Bw` | 0.003745 | 0.004173 | 8.171 | 15.684 |
| `feedforward_global` | 0.003741 | 0.004188 | 8.186 | 15.259 |
| `harmonic_regression_global` | 0.018006 | 0.018276 | 41.275 | 83.603 |

## Global Model Direction Breakdown

| Candidate | Direction | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `feedforward_global` | `forward` | 0.003550 | 0.003979 | 7.916 | 16.195 |
| `feedforward_global` | `backward` | 0.003741 | 0.004188 | 8.186 | 15.259 |
| `feedforward_global` | `combined` | 0.003646 | 0.004083 | 8.051 | 15.583 |
| `harmonic_regression_global` | `forward` | 0.018314 | 0.018547 | 41.749 | 79.404 |
| `harmonic_regression_global` | `backward` | 0.018006 | 0.018276 | 41.275 | 83.603 |
| `harmonic_regression_global` | `combined` | 0.018160 | 0.018412 | 41.512 | 82.048 |
| `periodic_mlp_global` | `forward` | 0.003380 | 0.003791 | 7.493 | 14.349 |
| `periodic_mlp_global` | `backward` | 0.003610 | 0.004030 | 7.879 | 13.661 |
| `periodic_mlp_global` | `combined` | 0.003495 | 0.003910 | 7.686 | 14.284 |
| `residual_harmonic_mlp_global` | `forward` | 0.003649 | 0.004051 | 8.123 | 14.713 |
| `residual_harmonic_mlp_global` | `backward` | 0.003639 | 0.004044 | 7.967 | 14.489 |
| `residual_harmonic_mlp_global` | `combined` | 0.003644 | 0.004048 | 8.045 | 14.717 |
| `tree_global` | `forward` | 0.002998 | 0.003364 | 6.590 | 11.601 |
| `tree_global` | `backward` | 0.003290 | 0.003702 | 7.118 | 13.703 |
| `tree_global` | `combined` | 0.003144 | 0.003533 | 6.854 | 13.314 |

## Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-05-18-16-35-26__track2_full_directional_family_matrix_composite_best_reference_validation/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-05-18-16-35-26__track2_full_directional_family_matrix_composite_best_reference_validation\per_condition_metrics.csv`;
- grouped report plot root: `doc\reports\campaign_results\track 2`;
- grouped report plot count: `600`;
- preview plot: `output\validation_checks\track2_reference_comparison\2026-05-18-16-35-26__track2_full_directional_family_matrix_composite_best_reference_validation\preview_curves\preview_01.png`;
- preview plot: `output\validation_checks\track2_reference_comparison\2026-05-18-16-35-26__track2_full_directional_family_matrix_composite_best_reference_validation\preview_curves\preview_02.png`;
- preview plot: `output\validation_checks\track2_reference_comparison\2026-05-18-16-35-26__track2_full_directional_family_matrix_composite_best_reference_validation\preview_curves\preview_03.png`;
- preview plot: `output\validation_checks\track2_reference_comparison\2026-05-18-16-35-26__track2_full_directional_family_matrix_composite_best_reference_validation\preview_curves\preview_04.png`;
- preview plot: `output\validation_checks\track2_reference_comparison\2026-05-18-16-35-26__track2_full_directional_family_matrix_composite_best_reference_validation\preview_curves\preview_05.png`;
- preview plot: `output\validation_checks\track2_reference_comparison\2026-05-18-16-35-26__track2_full_directional_family_matrix_composite_best_reference_validation\preview_curves\preview_06.png`;
- preview plot: `output\validation_checks\track2_reference_comparison\2026-05-18-16-35-26__track2_full_directional_family_matrix_composite_best_reference_validation\preview_curves\preview_07.png`;
- preview plot: `output\validation_checks\track2_reference_comparison\2026-05-18-16-35-26__track2_full_directional_family_matrix_composite_best_reference_validation\preview_curves\preview_08.png`;

## Interpretation

Rows are ranked by mean percentage error within each source group
and direction. Directional paper-reference and Wave 1 models are
never evaluated on the opposite direction. Global Wave 1 models
remain valid on both directions and are therefore shown in both
directional Wave 1 sections and again in the global breakdown.
The `rcim_track1` forward reference banks use the opposite stored
`h0` sign convention relative to the Track 2 reconstruction
contract, so the Track 2 comparison applies the documented
source-specific `h0` compatibility multiplier before curve
reconstruction.

## Open Gaps

- This remains an offline TE-curve comparison and does not replace the
  future online `Table 9` compensation benchmark.
- The report uses the saved Python model artifacts from `models/`; ONNX
  parity checks remain a separate deployment-readiness task.
