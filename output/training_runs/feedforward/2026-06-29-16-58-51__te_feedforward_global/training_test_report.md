# Feedforward Global Training And Testing Report

## Overview

- Run Name: `te_feedforward_global`
- Model Family: `feedforward_global`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-06-29-16-58-51__te_feedforward_global\checkpoints\feedforward-epoch=090-val_mae=0.00167189.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002856`
- val_mae: `0.001672`
- val_rmse: `0.002074`
- val_pointwise_loss: `0.002856`
- val_centered_curve_shape_loss: `0.002461`
- val_curve_offset_loss: `0.000423`
- val_curve_amplitude_loss: `0.036403`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.004097`
- test_mae: `0.001790`
- test_rmse: `0.002281`
- test_pointwise_loss: `0.004097`
- test_centered_curve_shape_loss: `0.003635`
- test_curve_offset_loss: `0.000995`
- test_curve_amplitude_loss: `0.052268`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001672 deg and RMSE=0.002074 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001790 deg and RMSE=0.002281 deg, which indicates a numerically stable baseline run.
