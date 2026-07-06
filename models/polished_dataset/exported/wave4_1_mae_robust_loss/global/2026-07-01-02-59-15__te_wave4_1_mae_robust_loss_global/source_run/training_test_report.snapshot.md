# Wave4 1 Mae Robust Loss Global Training And Testing Report

## Overview

- Run Name: `te_wave4_1_mae_robust_loss_global`
- Model Family: `wave4_1_mae_robust_loss_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_1_mae_robust_loss\2026-07-01-02-59-15__te_wave4_1_mae_robust_loss_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=196-val_mae=0.00175450.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.037692`
- val_mae: `0.001754`
- val_rmse: `0.002170`
- val_pointwise_loss: `0.037692`
- val_centered_curve_shape_loss: `0.004606`
- val_curve_offset_loss: `0.000261`
- val_curve_amplitude_loss: `0.035204`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_structured_mae: `0.007685`
- val_structured_rmse: `0.008084`
- val_residual_offset_mean_abs: `0.007304`

## Test Metrics

- test_loss: `0.040606`
- test_mae: `0.001890`
- test_rmse: `0.002443`
- test_pointwise_loss: `0.040606`
- test_centered_curve_shape_loss: `0.005444`
- test_curve_offset_loss: `0.000241`
- test_curve_amplitude_loss: `0.040656`
- test_sparse_harmonic_shape_loss: `0.000112`
- test_structured_mae: `0.008040`
- test_structured_rmse: `0.008635`
- test_residual_offset_mean_abs: `0.007578`

## Interpretation

The held-out val error stayed finite with MAE=0.001754 deg and RMSE=0.002170 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001890 deg and RMSE=0.002443 deg, which indicates a numerically stable baseline run.
