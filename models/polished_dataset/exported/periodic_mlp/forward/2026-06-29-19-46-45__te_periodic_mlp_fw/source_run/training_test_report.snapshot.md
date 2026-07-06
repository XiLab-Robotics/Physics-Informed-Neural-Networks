# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_fw`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-06-29-19-46-45__te_periodic_mlp_fw\checkpoints\periodic_mlp-epoch=064-val_mae=0.00167050.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002893`
- val_mae: `0.001670`
- val_rmse: `0.002171`
- val_pointwise_loss: `0.002893`
- val_centered_curve_shape_loss: `0.003150`
- val_curve_offset_loss: `0.000463`
- val_curve_amplitude_loss: `0.042499`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.004114`
- test_mae: `0.001747`
- test_rmse: `0.002347`
- test_pointwise_loss: `0.004114`
- test_centered_curve_shape_loss: `0.003923`
- test_curve_offset_loss: `0.001262`
- test_curve_amplitude_loss: `0.056705`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001670 deg and RMSE=0.002171 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001747 deg and RMSE=0.002347 deg, which indicates a numerically stable baseline run.
