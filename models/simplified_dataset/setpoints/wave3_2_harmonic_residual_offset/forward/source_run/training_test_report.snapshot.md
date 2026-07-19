# Wave3 2 Harmonic Residual Offset Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_2_harmonic_residual_offset_fw__simplified_setpoints`
- Model Family: `wave3_2_harmonic_residual_offset_fw`
- Model Type: `harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_harmonic_residual_offset/2026-07-10-23-36-51__te_wave3_2_harmonic_residual_offset_fw__simplified_setpoints/checkpoints/harmonic_residual_offset_probe-epoch=121-val_mae=0.00362257.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010844`
- val_mae: `0.003623`
- val_rmse: `0.004440`
- val_pointwise_loss: `0.010844`
- val_centered_curve_shape_loss: `0.006357`
- val_curve_offset_loss: `0.004487`
- val_curve_amplitude_loss: `0.045783`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.040697`
- val_structured_rmse: `0.049977`
- val_residual_offset_mean_abs: `0.040963`

## Test Metrics

- test_loss: `0.008233`
- test_mae: `0.003391`
- test_rmse: `0.004142`
- test_pointwise_loss: `0.008233`
- test_centered_curve_shape_loss: `0.003146`
- test_curve_offset_loss: `0.005087`
- test_curve_amplitude_loss: `0.019602`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.042696`
- test_structured_rmse: `0.051312`
- test_residual_offset_mean_abs: `0.043022`

## Interpretation

The held-out val error stayed finite with MAE=0.003623 deg and RMSE=0.004440 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003391 deg and RMSE=0.004142 deg, which indicates a numerically stable baseline run.
