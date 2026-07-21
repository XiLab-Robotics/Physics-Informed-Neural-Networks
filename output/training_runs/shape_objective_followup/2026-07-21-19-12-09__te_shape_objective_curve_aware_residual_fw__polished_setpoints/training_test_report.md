# Shape Objective Curve Aware Residual Fw Training And Testing Report

## Overview

- Run Name: `te_shape_objective_curve_aware_residual_fw__polished_setpoints`
- Model Family: `shape_objective_curve_aware_residual_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\shape_objective_followup\2026-07-21-19-12-09__te_shape_objective_curve_aware_residual_fw__polished_setpoints\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=019-val_mae=0.00197236.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.092987`
- val_mae: `0.001972`
- val_rmse: `0.002445`
- val_pointwise_loss: `0.081736`
- val_centered_curve_shape_loss: `0.015238`
- val_curve_offset_loss: `0.002675`
- val_curve_amplitude_loss: `0.050126`
- val_sparse_harmonic_shape_loss: `0.000370`
- val_structured_mae: `0.015538`
- val_structured_rmse: `0.017536`
- val_residual_offset_mean_abs: `0.015304`

## Test Metrics

- test_loss: `0.065787`
- test_mae: `0.001463`
- test_rmse: `0.001854`
- test_pointwise_loss: `0.060630`
- test_centered_curve_shape_loss: `0.007788`
- test_curve_offset_loss: `0.002088`
- test_curve_amplitude_loss: `0.020338`
- test_sparse_harmonic_shape_loss: `0.000162`
- test_structured_mae: `0.015091`
- test_structured_rmse: `0.017498`
- test_residual_offset_mean_abs: `0.015020`

## Interpretation

The held-out val error stayed finite with MAE=0.001972 deg and RMSE=0.002445 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001463 deg and RMSE=0.001854 deg, which indicates a numerically stable baseline run.
