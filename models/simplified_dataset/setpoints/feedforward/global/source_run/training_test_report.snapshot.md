# Feedforward Global Training And Testing Report

## Overview

- Run Name: `te_feedforward_global__simplified_setpoints`
- Model Family: `feedforward_global`
- Model Type: `feedforward`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/feedforward/2026-07-07-16-02-57__te_feedforward_global__simplified_setpoints/checkpoints/feedforward-epoch=095-val_mae=0.00296788.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007125`
- val_mae: `0.002968`
- val_rmse: `0.003608`
- val_pointwise_loss: `0.007125`
- val_centered_curve_shape_loss: `0.003563`
- val_curve_offset_loss: `0.004203`
- val_curve_amplitude_loss: `0.062014`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.007415`
- test_mae: `0.003243`
- test_rmse: `0.003875`
- test_pointwise_loss: `0.007415`
- test_centered_curve_shape_loss: `0.002877`
- test_curve_offset_loss: `0.005063`
- test_curve_amplitude_loss: `0.050430`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002968 deg and RMSE=0.003608 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003243 deg and RMSE=0.003875 deg, which indicates a numerically stable baseline run.
