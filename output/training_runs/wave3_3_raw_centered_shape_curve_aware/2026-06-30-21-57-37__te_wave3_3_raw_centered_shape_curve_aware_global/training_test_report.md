# Wave3 3 Raw Centered Shape Curve Aware Global Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_centered_shape_curve_aware_global`
- Model Family: `wave3_3_raw_centered_shape_curve_aware_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_raw_centered_shape_curve_aware\2026-06-30-21-57-37__te_wave3_3_raw_centered_shape_curve_aware_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=092-val_mae=0.00179701.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006507`
- val_mae: `0.001797`
- val_rmse: `0.002216`
- val_pointwise_loss: `0.004889`
- val_centered_curve_shape_loss: `0.004581`
- val_curve_offset_loss: `0.000308`
- val_curve_amplitude_loss: `0.035880`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_structured_mae: `0.005227`
- val_structured_rmse: `0.005617`
- val_residual_offset_mean_abs: `0.004589`

## Test Metrics

- test_loss: `0.007765`
- test_mae: `0.001954`
- test_rmse: `0.002494`
- test_pointwise_loss: `0.005897`
- test_centered_curve_shape_loss: `0.005288`
- test_curve_offset_loss: `0.000609`
- test_curve_amplitude_loss: `0.041357`
- test_sparse_harmonic_shape_loss: `0.000111`
- test_structured_mae: `0.005489`
- test_structured_rmse: `0.006005`
- test_residual_offset_mean_abs: `0.004687`

## Interpretation

The held-out val error stayed finite with MAE=0.001797 deg and RMSE=0.002216 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001954 deg and RMSE=0.002494 deg, which indicates a numerically stable baseline run.
