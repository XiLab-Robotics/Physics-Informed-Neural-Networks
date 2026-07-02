# Wave5 1 Harmonic Prior Smooth L1 Structured Global Training And Testing Report

## Overview

- Run Name: `te_wave5_1_harmonic_prior_smooth_l1_structured_global`
- Model Family: `wave5_1_harmonic_prior_smooth_l1_structured_global`
- Model Type: `wave3_harmonic_prior_residual`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave5_1_harmonic_prior_smooth_l1_structured\2026-07-02-00-24-38__te_wave5_1_harmonic_prior_smooth_l1_structured_global\checkpoints\wave3_harmonic_prior_residual-epoch=077-val_mae=0.00187023.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002495`
- val_mae: `0.001870`
- val_rmse: `0.002295`
- val_pointwise_loss: `0.002495`
- val_centered_curve_shape_loss: `0.004598`
- val_curve_offset_loss: `0.000391`
- val_curve_amplitude_loss: `0.037021`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_structured_mae: `0.011419`
- val_structured_rmse: `0.011775`

## Test Metrics

- test_loss: `0.004056`
- test_mae: `0.002119`
- test_rmse: `0.002712`
- test_pointwise_loss: `0.004056`
- test_centered_curve_shape_loss: `0.005486`
- test_curve_offset_loss: `0.002645`
- test_curve_amplitude_loss: `0.048406`
- test_sparse_harmonic_shape_loss: `0.000110`
- test_structured_mae: `0.011138`
- test_structured_rmse: `0.011641`

## Interpretation

The held-out val error stayed finite with MAE=0.001870 deg and RMSE=0.002295 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002119 deg and RMSE=0.002712 deg, which indicates a numerically stable baseline run.
