# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_trial`
- Model Family: `feedforward`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-06-22-13-09-57__te_feedforward_trial\checkpoints\feedforward-epoch=002-val_mae=0.00272463.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006749`
- val_mae: `0.002725`
- val_rmse: `0.003481`
- val_pointwise_loss: `0.006749`
- val_centered_curve_shape_loss: `0.004750`
- val_curve_offset_loss: `0.002287`
- val_curve_amplitude_loss: `0.030026`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.008724`
- test_mae: `0.002877`
- test_rmse: `0.003835`
- test_pointwise_loss: `0.008724`
- test_centered_curve_shape_loss: `0.006058`
- test_curve_offset_loss: `0.004363`
- test_curve_amplitude_loss: `0.039162`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002725 deg and RMSE=0.003481 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002877 deg and RMSE=0.003835 deg, which indicates a numerically stable baseline run.
