# Wave3 3 Raw Offset Curve Aware Global Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_offset_curve_aware_global__simplified_setpoints`
- Model Family: `wave3_3_raw_offset_curve_aware_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-11-21-48-20__te_wave3_3_raw_offset_curve_aware_global__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=159-val_mae=0.00354446.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.012694`
- val_mae: `0.003544`
- val_rmse: `0.004389`
- val_pointwise_loss: `0.010746`
- val_centered_curve_shape_loss: `0.006418`
- val_curve_offset_loss: `0.004328`
- val_curve_amplitude_loss: `0.049996`
- val_sparse_harmonic_shape_loss: `0.000152`
- val_structured_mae: `0.029142`
- val_structured_rmse: `0.035925`
- val_residual_offset_mean_abs: `0.029073`

## Test Metrics

- test_loss: `0.011179`
- test_mae: `0.003501`
- test_rmse: `0.004263`
- test_pointwise_loss: `0.008694`
- test_centered_curve_shape_loss: `0.003169`
- test_curve_offset_loss: `0.005524`
- test_curve_amplitude_loss: `0.021994`
- test_sparse_harmonic_shape_loss: `6.864437e-05`
- test_structured_mae: `0.032335`
- test_structured_rmse: `0.038239`
- test_residual_offset_mean_abs: `0.032221`

## Interpretation

The held-out val error stayed finite with MAE=0.003544 deg and RMSE=0.004389 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003501 deg and RMSE=0.004263 deg, which indicates a numerically stable baseline run.
