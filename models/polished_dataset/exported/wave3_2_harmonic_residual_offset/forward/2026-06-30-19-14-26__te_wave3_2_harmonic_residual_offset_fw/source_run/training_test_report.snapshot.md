# Wave3 2 Harmonic Residual Offset Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_2_harmonic_residual_offset_fw`
- Model Family: `wave3_2_harmonic_residual_offset_fw`
- Model Type: `harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_2_harmonic_residual_offset\2026-06-30-19-14-26__te_wave3_2_harmonic_residual_offset_fw\checkpoints\harmonic_residual_offset_probe-epoch=066-val_mae=0.00180926.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004934`
- val_mae: `0.001809`
- val_rmse: `0.002240`
- val_pointwise_loss: `0.004934`
- val_centered_curve_shape_loss: `0.004623`
- val_curve_offset_loss: `0.000312`
- val_curve_amplitude_loss: `0.036814`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.009307`
- val_structured_rmse: `0.009708`
- val_residual_offset_mean_abs: `0.009202`

## Test Metrics

- test_loss: `0.005802`
- test_mae: `0.001948`
- test_rmse: `0.002507`
- test_pointwise_loss: `0.005802`
- test_centered_curve_shape_loss: `0.005462`
- test_curve_offset_loss: `0.000341`
- test_curve_amplitude_loss: `0.042048`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.009190`
- test_structured_rmse: `0.009750`
- test_residual_offset_mean_abs: `0.009036`

## Interpretation

The held-out val error stayed finite with MAE=0.001809 deg and RMSE=0.002240 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001948 deg and RMSE=0.002507 deg, which indicates a numerically stable baseline run.
