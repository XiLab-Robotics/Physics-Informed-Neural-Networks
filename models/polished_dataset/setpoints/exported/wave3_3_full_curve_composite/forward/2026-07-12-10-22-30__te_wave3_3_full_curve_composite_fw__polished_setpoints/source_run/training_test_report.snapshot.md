# Wave3 3 Full Curve Composite Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_full_curve_composite_fw__polished_setpoints`
- Model Family: `wave3_3_full_curve_composite_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_full_curve_composite/2026-07-12-10-22-30__te_wave3_3_full_curve_composite_fw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=107-val_mae=0.00203018.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.008746`
- val_mae: `0.002030`
- val_rmse: `0.002814`
- val_pointwise_loss: `0.005368`
- val_centered_curve_shape_loss: `0.004866`
- val_curve_offset_loss: `0.000502`
- val_curve_amplitude_loss: `0.019702`
- val_sparse_harmonic_shape_loss: `0.000109`
- val_structured_mae: `0.022821`
- val_structured_rmse: `0.027330`
- val_residual_offset_mean_abs: `0.022636`

## Test Metrics

- test_loss: `0.014152`
- test_mae: `0.002353`
- test_rmse: `0.003715`
- test_pointwise_loss: `0.008862`
- test_centered_curve_shape_loss: `0.005663`
- test_curve_offset_loss: `0.003199`
- test_curve_amplitude_loss: `0.027380`
- test_sparse_harmonic_shape_loss: `0.000114`
- test_structured_mae: `0.021965`
- test_structured_rmse: `0.026899`
- test_residual_offset_mean_abs: `0.021497`

## Interpretation

The held-out val error stayed finite with MAE=0.002030 deg and RMSE=0.002814 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002353 deg and RMSE=0.003715 deg, which indicates a numerically stable baseline run.
