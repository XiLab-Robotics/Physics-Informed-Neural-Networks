# Wave3 3 Raw Centered Shape Curve Aware Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_centered_shape_curve_aware_bw`
- Model Family: `wave3_3_raw_centered_shape_curve_aware_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_raw_centered_shape_curve_aware\2026-06-30-23-05-54__te_wave3_3_raw_centered_shape_curve_aware_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=117-val_mae=0.00180437.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006547`
- val_mae: `0.001804`
- val_rmse: `0.002222`
- val_pointwise_loss: `0.004912`
- val_centered_curve_shape_loss: `0.004627`
- val_curve_offset_loss: `0.000284`
- val_curve_amplitude_loss: `0.036404`
- val_sparse_harmonic_shape_loss: `0.000103`
- val_structured_mae: `0.006148`
- val_structured_rmse: `0.006575`
- val_residual_offset_mean_abs: `0.005604`

## Test Metrics

- test_loss: `0.007514`
- test_mae: `0.001916`
- test_rmse: `0.002460`
- test_pointwise_loss: `0.005636`
- test_centered_curve_shape_loss: `0.005318`
- test_curve_offset_loss: `0.000318`
- test_curve_amplitude_loss: `0.041714`
- test_sparse_harmonic_shape_loss: `0.000111`
- test_structured_mae: `0.006497`
- test_structured_rmse: `0.007024`
- test_residual_offset_mean_abs: `0.005864`

## Interpretation

The held-out val error stayed finite with MAE=0.001804 deg and RMSE=0.002222 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001916 deg and RMSE=0.002460 deg, which indicates a numerically stable baseline run.
