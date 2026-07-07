# Feedforward Bw Training And Testing Report

## Overview

- Run Name: `te_feedforward_bw__polished_setpoints`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/feedforward/2026-07-07-17-41-33__te_feedforward_bw__polished_setpoints/checkpoints/feedforward-epoch=057-val_mae=0.00164066.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002807`
- val_mae: `0.001641`
- val_rmse: `0.002208`
- val_pointwise_loss: `0.002807`
- val_centered_curve_shape_loss: `0.003337`
- val_curve_offset_loss: `0.000452`
- val_curve_amplitude_loss: `0.056534`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.004465`
- test_mae: `0.001853`
- test_rmse: `0.002874`
- test_pointwise_loss: `0.004465`
- test_centered_curve_shape_loss: `0.005351`
- test_curve_offset_loss: `0.003779`
- test_curve_amplitude_loss: `0.087980`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001641 deg and RMSE=0.002208 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001853 deg and RMSE=0.002874 deg, which indicates a numerically stable baseline run.
