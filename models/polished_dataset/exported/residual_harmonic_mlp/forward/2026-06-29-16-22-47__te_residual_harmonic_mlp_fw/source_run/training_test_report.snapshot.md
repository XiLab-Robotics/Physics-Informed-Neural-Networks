# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_mlp_fw`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-06-29-16-22-47__te_residual_harmonic_mlp_fw\checkpoints\residual_harmonic_mlp-epoch=098-val_mae=0.00163209.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002747`
- val_mae: `0.001632`
- val_rmse: `0.002102`
- val_pointwise_loss: `0.002747`
- val_centered_curve_shape_loss: `0.003083`
- val_curve_offset_loss: `0.000362`
- val_curve_amplitude_loss: `0.046369`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.040326`
- val_structured_rmse: `0.043861`

## Test Metrics

- test_loss: `0.004000`
- test_mae: `0.001783`
- test_rmse: `0.002349`
- test_pointwise_loss: `0.004000`
- test_centered_curve_shape_loss: `0.004008`
- test_curve_offset_loss: `0.001017`
- test_curve_amplitude_loss: `0.058306`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.039662`
- test_structured_rmse: `0.043653`

## Interpretation

The held-out val error stayed finite with MAE=0.001632 deg and RMSE=0.002102 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001783 deg and RMSE=0.002349 deg, which indicates a numerically stable baseline run.
