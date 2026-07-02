# Periodic Mlp Global Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_global`
- Model Family: `periodic_mlp_global`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-06-29-19-27-09__te_periodic_mlp_global\checkpoints\periodic_mlp-epoch=113-val_mae=0.00165497.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002825`
- val_mae: `0.001655`
- val_rmse: `0.002142`
- val_pointwise_loss: `0.002825`
- val_centered_curve_shape_loss: `0.003102`
- val_curve_offset_loss: `0.000416`
- val_curve_amplitude_loss: `0.046100`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.004020`
- test_mae: `0.001741`
- test_rmse: `0.002333`
- test_pointwise_loss: `0.004020`
- test_centered_curve_shape_loss: `0.004004`
- test_curve_offset_loss: `0.001094`
- test_curve_amplitude_loss: `0.059879`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001655 deg and RMSE=0.002142 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001741 deg and RMSE=0.002333 deg, which indicates a numerically stable baseline run.
