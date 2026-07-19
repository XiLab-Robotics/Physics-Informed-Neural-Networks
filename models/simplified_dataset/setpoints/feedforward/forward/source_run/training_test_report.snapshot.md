# Feedforward Fw Training And Testing Report

## Overview

- Run Name: `te_feedforward_fw__simplified_setpoints`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/feedforward/2026-07-07-16-21-15__te_feedforward_fw__simplified_setpoints/checkpoints/feedforward-epoch=057-val_mae=0.00299942.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007410`
- val_mae: `0.002999`
- val_rmse: `0.003677`
- val_pointwise_loss: `0.007410`
- val_centered_curve_shape_loss: `0.003642`
- val_curve_offset_loss: `0.004551`
- val_curve_amplitude_loss: `0.064483`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.008251`
- test_mae: `0.003423`
- test_rmse: `0.004082`
- test_pointwise_loss: `0.008251`
- test_centered_curve_shape_loss: `0.002963`
- test_curve_offset_loss: `0.005442`
- test_curve_amplitude_loss: `0.053037`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002999 deg and RMSE=0.003677 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003423 deg and RMSE=0.004082 deg, which indicates a numerically stable baseline run.
