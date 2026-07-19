# Wave3 3 Full Curve Composite Global Training And Testing Report

## Overview

- Run Name: `te_wave3_3_full_curve_composite_global__polished_setpoints`
- Model Family: `wave3_3_full_curve_composite_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_full_curve_composite/2026-07-12-09-42-30__te_wave3_3_full_curve_composite_global__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=139-val_mae=0.00205804.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.008933`
- val_mae: `0.002058`
- val_rmse: `0.002857`
- val_pointwise_loss: `0.005511`
- val_centered_curve_shape_loss: `0.004934`
- val_curve_offset_loss: `0.000577`
- val_curve_amplitude_loss: `0.019699`
- val_sparse_harmonic_shape_loss: `0.000109`
- val_structured_mae: `0.032739`
- val_structured_rmse: `0.037650`
- val_residual_offset_mean_abs: `0.033012`

## Test Metrics

- test_loss: `0.014087`
- test_mae: `0.002353`
- test_rmse: `0.003704`
- test_pointwise_loss: `0.008887`
- test_centered_curve_shape_loss: `0.005756`
- test_curve_offset_loss: `0.003131`
- test_curve_amplitude_loss: `0.026482`
- test_sparse_harmonic_shape_loss: `0.000116`
- test_structured_mae: `0.030472`
- test_structured_rmse: `0.035629`
- test_residual_offset_mean_abs: `0.030570`

## Interpretation

The held-out val error stayed finite with MAE=0.002058 deg and RMSE=0.002857 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002353 deg and RMSE=0.003704 deg, which indicates a numerically stable baseline run.
