# Wave3 2 Harmonic Residual Offset Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_2_harmonic_residual_offset_fw__polished_actual_values`
- Model Family: `wave3_2_harmonic_residual_offset_fw`
- Model Type: `harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-05-29-51__te_wave3_2_harmonic_residual_offset_fw__polished_actual_values/checkpoints/harmonic_residual_offset_probe-epoch=205-val_mae=0.00184965.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004851`
- val_mae: `0.001850`
- val_rmse: `0.002606`
- val_pointwise_loss: `0.004851`
- val_centered_curve_shape_loss: `0.004496`
- val_curve_offset_loss: `0.000355`
- val_curve_amplitude_loss: `0.034166`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.011177`
- val_structured_rmse: `0.013175`
- val_residual_offset_mean_abs: `0.010914`

## Test Metrics

- test_loss: `0.005648`
- test_mae: `0.001961`
- test_rmse: `0.003003`
- test_pointwise_loss: `0.005648`
- test_centered_curve_shape_loss: `0.005283`
- test_curve_offset_loss: `0.000365`
- test_curve_amplitude_loss: `0.038984`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.011039`
- test_structured_rmse: `0.013454`
- test_residual_offset_mean_abs: `0.010650`

## Interpretation

The held-out val error stayed finite with MAE=0.001850 deg and RMSE=0.002606 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001961 deg and RMSE=0.003003 deg, which indicates a numerically stable baseline run.
