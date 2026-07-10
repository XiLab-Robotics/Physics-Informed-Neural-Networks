# Wave3 2 Harmonic Residual Offset Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_2_harmonic_residual_offset_bw__simplified_setpoints`
- Model Family: `wave3_2_harmonic_residual_offset_bw`
- Model Type: `harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_harmonic_residual_offset/2026-07-10-23-52-02__te_wave3_2_harmonic_residual_offset_bw__simplified_setpoints/checkpoints/harmonic_residual_offset_probe-epoch=091-val_mae=0.00361216.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010638`
- val_mae: `0.003612`
- val_rmse: `0.004398`
- val_pointwise_loss: `0.010638`
- val_centered_curve_shape_loss: `0.006426`
- val_curve_offset_loss: `0.004212`
- val_curve_amplitude_loss: `0.046711`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.047957`
- val_structured_rmse: `0.055939`
- val_residual_offset_mean_abs: `0.047811`

## Test Metrics

- test_loss: `0.008016`
- test_mae: `0.003398`
- test_rmse: `0.004083`
- test_pointwise_loss: `0.008016`
- test_centered_curve_shape_loss: `0.003202`
- test_curve_offset_loss: `0.004815`
- test_curve_amplitude_loss: `0.019622`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.050942`
- test_structured_rmse: `0.058450`
- test_residual_offset_mean_abs: `0.050837`

## Interpretation

The held-out val error stayed finite with MAE=0.003612 deg and RMSE=0.004398 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003398 deg and RMSE=0.004083 deg, which indicates a numerically stable baseline run.
