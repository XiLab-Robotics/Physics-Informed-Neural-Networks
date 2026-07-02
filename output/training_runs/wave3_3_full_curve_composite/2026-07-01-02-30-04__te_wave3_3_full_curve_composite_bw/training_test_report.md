# Wave3 3 Full Curve Composite Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_full_curve_composite_bw`
- Model Family: `wave3_3_full_curve_composite_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_full_curve_composite\2026-07-01-02-30-04__te_wave3_3_full_curve_composite_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=071-val_mae=0.00191986.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.008592`
- val_mae: `0.001920`
- val_rmse: `0.002371`
- val_pointwise_loss: `0.005108`
- val_centered_curve_shape_loss: `0.004701`
- val_curve_offset_loss: `0.000408`
- val_curve_amplitude_loss: `0.021499`
- val_sparse_harmonic_shape_loss: `0.000104`
- val_structured_mae: `0.007810`
- val_structured_rmse: `0.008349`
- val_residual_offset_mean_abs: `0.007261`

## Test Metrics

- test_loss: `0.010056`
- test_mae: `0.002067`
- test_rmse: `0.002638`
- test_pointwise_loss: `0.005987`
- test_centered_curve_shape_loss: `0.005455`
- test_curve_offset_loss: `0.000532`
- test_curve_amplitude_loss: `0.025020`
- test_sparse_harmonic_shape_loss: `0.000113`
- test_structured_mae: `0.008056`
- test_structured_rmse: `0.008720`
- test_residual_offset_mean_abs: `0.007341`

## Interpretation

The held-out val error stayed finite with MAE=0.001920 deg and RMSE=0.002371 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002067 deg and RMSE=0.002638 deg, which indicates a numerically stable baseline run.
