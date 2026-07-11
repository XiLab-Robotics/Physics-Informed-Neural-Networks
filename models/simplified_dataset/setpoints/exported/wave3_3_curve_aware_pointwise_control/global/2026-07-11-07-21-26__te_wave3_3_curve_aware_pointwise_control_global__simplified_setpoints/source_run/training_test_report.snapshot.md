# Wave3 3 Curve Aware Pointwise Control Global Training And Testing Report

## Overview

- Run Name: `te_wave3_3_curve_aware_pointwise_control_global__simplified_setpoints`
- Model Family: `wave3_3_curve_aware_pointwise_control_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-07-21-26__te_wave3_3_curve_aware_pointwise_control_global__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=139-val_mae=0.00358483.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010706`
- val_mae: `0.003585`
- val_rmse: `0.004401`
- val_pointwise_loss: `0.010706`
- val_centered_curve_shape_loss: `0.006395`
- val_curve_offset_loss: `0.004311`
- val_curve_amplitude_loss: `0.047394`
- val_sparse_harmonic_shape_loss: `0.000152`
- val_structured_mae: `0.040200`
- val_structured_rmse: `0.044959`
- val_residual_offset_mean_abs: `0.039814`

## Test Metrics

- test_loss: `0.008350`
- test_mae: `0.003445`
- test_rmse: `0.004177`
- test_pointwise_loss: `0.008350`
- test_centered_curve_shape_loss: `0.003201`
- test_curve_offset_loss: `0.005149`
- test_curve_amplitude_loss: `0.021276`
- test_sparse_harmonic_shape_loss: `6.950882e-05`
- test_structured_mae: `0.043038`
- test_structured_rmse: `0.047667`
- test_residual_offset_mean_abs: `0.042818`

## Interpretation

The held-out val error stayed finite with MAE=0.003585 deg and RMSE=0.004401 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003445 deg and RMSE=0.004177 deg, which indicates a numerically stable baseline run.
