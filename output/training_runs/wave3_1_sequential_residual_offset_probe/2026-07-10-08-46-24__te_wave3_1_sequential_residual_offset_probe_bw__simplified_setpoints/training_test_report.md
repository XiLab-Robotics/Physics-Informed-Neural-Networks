# Wave3 1 Sequential Residual Offset Probe Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_1_sequential_residual_offset_probe_bw__simplified_setpoints`
- Model Family: `wave3_1_sequential_residual_offset_probe_bw`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_1_sequential_residual_offset_probe/2026-07-10-08-46-24__te_wave3_1_sequential_residual_offset_probe_bw__simplified_setpoints/checkpoints/sequential_residual_offset_probe-epoch=098-val_mae=0.00372763.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011723`
- val_mae: `0.003728`
- val_rmse: `0.004646`
- val_pointwise_loss: `0.011723`
- val_centered_curve_shape_loss: `0.007375`
- val_curve_offset_loss: `0.004348`
- val_curve_amplitude_loss: `0.069775`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.026342`
- val_base_rmse: `0.030836`
- val_residual_offset_mean_abs: `0.026418`

## Test Metrics

- test_loss: `0.009418`
- test_mae: `0.003601`
- test_rmse: `0.004440`
- test_pointwise_loss: `0.009418`
- test_centered_curve_shape_loss: `0.004071`
- test_curve_offset_loss: `0.005347`
- test_curve_amplitude_loss: `0.037019`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.028330`
- test_base_rmse: `0.032586`
- test_residual_offset_mean_abs: `0.028485`

## Interpretation

The held-out val error stayed finite with MAE=0.003728 deg and RMSE=0.004646 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003601 deg and RMSE=0.004440 deg, which indicates a numerically stable baseline run.
