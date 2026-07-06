# Harmonic Regression Fw Training And Testing Report

## Overview

- Run Name: `te_harmonic_regression_fw`
- Model Family: `harmonic_regression_fw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression\2026-06-29-20-32-49__te_harmonic_regression_fw\checkpoints\harmonic_regression-epoch=042-val_mae=0.00390024.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010240`
- val_mae: `0.003900`
- val_rmse: `0.004483`
- val_pointwise_loss: `0.010240`
- val_centered_curve_shape_loss: `0.003081`
- val_curve_offset_loss: `0.007583`
- val_curve_amplitude_loss: `0.047286`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.010822`
- test_mae: `0.003819`
- test_rmse: `0.004525`
- test_pointwise_loss: `0.010822`
- test_centered_curve_shape_loss: `0.003831`
- test_curve_offset_loss: `0.007608`
- test_curve_amplitude_loss: `0.060528`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003900 deg and RMSE=0.004483 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003819 deg and RMSE=0.004525 deg, which indicates a numerically stable baseline run.
