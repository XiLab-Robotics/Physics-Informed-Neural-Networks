# Wave3 3 Full Curve Composite Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_full_curve_composite_fw__polished_actual_values`
- Model Family: `wave3_3_full_curve_composite_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_full_curve_composite/2026-07-12-12-13-42__te_wave3_3_full_curve_composite_fw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=211-val_mae=0.00198008.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.008394`
- val_mae: `0.001980`
- val_rmse: `0.002774`
- val_pointwise_loss: `0.005263`
- val_centered_curve_shape_loss: `0.004826`
- val_curve_offset_loss: `0.000437`
- val_curve_amplitude_loss: `0.017555`
- val_sparse_harmonic_shape_loss: `0.000106`
- val_structured_mae: `0.016817`
- val_structured_rmse: `0.020102`
- val_residual_offset_mean_abs: `0.016471`

## Test Metrics

- test_loss: `0.009687`
- test_mae: `0.002113`
- test_rmse: `0.003176`
- test_pointwise_loss: `0.006171`
- test_centered_curve_shape_loss: `0.005705`
- test_curve_offset_loss: `0.000466`
- test_curve_amplitude_loss: `0.019096`
- test_sparse_harmonic_shape_loss: `0.000115`
- test_structured_mae: `0.017178`
- test_structured_rmse: `0.020555`
- test_residual_offset_mean_abs: `0.016712`

## Interpretation

The held-out val error stayed finite with MAE=0.001980 deg and RMSE=0.002774 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002113 deg and RMSE=0.003176 deg, which indicates a numerically stable baseline run.
