# Wave3 3 Full Curve Composite Global Training And Testing Report

## Overview

- Run Name: `te_wave3_3_full_curve_composite_global__simplified_setpoints`
- Model Family: `wave3_3_full_curve_composite_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_full_curve_composite/2026-07-12-04-02-10__te_wave3_3_full_curve_composite_global__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=172-val_mae=0.00363873.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.017282`
- val_mae: `0.003639`
- val_rmse: `0.004478`
- val_pointwise_loss: `0.011033`
- val_centered_curve_shape_loss: `0.006618`
- val_curve_offset_loss: `0.004415`
- val_curve_amplitude_loss: `0.030266`
- val_sparse_harmonic_shape_loss: `0.000157`
- val_structured_mae: `0.032694`
- val_structured_rmse: `0.038091`
- val_residual_offset_mean_abs: `0.032439`

## Test Metrics

- test_loss: `0.012313`
- test_mae: `0.003419`
- test_rmse: `0.004198`
- test_pointwise_loss: `0.008425`
- test_centered_curve_shape_loss: `0.003363`
- test_curve_offset_loss: `0.005062`
- test_curve_amplitude_loss: `0.012647`
- test_sparse_harmonic_shape_loss: `7.341267e-05`
- test_structured_mae: `0.035945`
- test_structured_rmse: `0.041080`
- test_residual_offset_mean_abs: `0.035701`

## Interpretation

The held-out val error stayed finite with MAE=0.003639 deg and RMSE=0.004478 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003419 deg and RMSE=0.004198 deg, which indicates a numerically stable baseline run.
