# Wave3 2 Harmonic Residual Offset Global Training And Testing Report

## Overview

- Run Name: `te_wave3_2_harmonic_residual_offset_global`
- Model Family: `wave3_2_harmonic_residual_offset_global`
- Model Type: `harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_2_harmonic_residual_offset\2026-06-30-18-43-05__te_wave3_2_harmonic_residual_offset_global\checkpoints\harmonic_residual_offset_probe-epoch=124-val_mae=0.00178297.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004860`
- val_mae: `0.001783`
- val_rmse: `0.002206`
- val_pointwise_loss: `0.004860`
- val_centered_curve_shape_loss: `0.004565`
- val_curve_offset_loss: `0.000294`
- val_curve_amplitude_loss: `0.036127`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.006354`
- val_structured_rmse: `0.006772`
- val_residual_offset_mean_abs: `0.005863`

## Test Metrics

- test_loss: `0.005681`
- test_mae: `0.001914`
- test_rmse: `0.002470`
- test_pointwise_loss: `0.005681`
- test_centered_curve_shape_loss: `0.005423`
- test_curve_offset_loss: `0.000257`
- test_curve_amplitude_loss: `0.041355`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.006257`
- test_structured_rmse: `0.006869`
- test_residual_offset_mean_abs: `0.005611`

## Interpretation

The held-out val error stayed finite with MAE=0.001783 deg and RMSE=0.002206 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001914 deg and RMSE=0.002470 deg, which indicates a numerically stable baseline run.
