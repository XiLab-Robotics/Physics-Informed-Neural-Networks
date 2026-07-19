# Wave3 3 Full Curve Composite Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_full_curve_composite_fw__simplified_setpoints`
- Model Family: `wave3_3_full_curve_composite_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_full_curve_composite/2026-07-12-04-39-03__te_wave3_3_full_curve_composite_fw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=137-val_mae=0.00367911.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.017631`
- val_mae: `0.003679`
- val_rmse: `0.004554`
- val_pointwise_loss: `0.011221`
- val_centered_curve_shape_loss: `0.006523`
- val_curve_offset_loss: `0.004697`
- val_curve_amplitude_loss: `0.031123`
- val_sparse_harmonic_shape_loss: `0.000154`
- val_structured_mae: `0.027714`
- val_structured_rmse: `0.032237`
- val_residual_offset_mean_abs: `0.027716`

## Test Metrics

- test_loss: `0.013098`
- test_mae: `0.003575`
- test_rmse: `0.004322`
- test_pointwise_loss: `0.008970`
- test_centered_curve_shape_loss: `0.003308`
- test_curve_offset_loss: `0.005661`
- test_curve_amplitude_loss: `0.013094`
- test_sparse_harmonic_shape_loss: `7.152269e-05`
- test_structured_mae: `0.027504`
- test_structured_rmse: `0.032875`
- test_residual_offset_mean_abs: `0.027929`

## Interpretation

The held-out val error stayed finite with MAE=0.003679 deg and RMSE=0.004554 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003575 deg and RMSE=0.004322 deg, which indicates a numerically stable baseline run.
