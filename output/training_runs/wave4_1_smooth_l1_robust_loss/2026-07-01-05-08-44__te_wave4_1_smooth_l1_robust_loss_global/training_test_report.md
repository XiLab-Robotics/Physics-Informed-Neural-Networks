# Wave4 1 Smooth L1 Robust Loss Global Training And Testing Report

## Overview

- Run Name: `te_wave4_1_smooth_l1_robust_loss_global`
- Model Family: `wave4_1_smooth_l1_robust_loss_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_1_smooth_l1_robust_loss\2026-07-01-05-08-44__te_wave4_1_smooth_l1_robust_loss_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=080-val_mae=0.00186636.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002490`
- val_mae: `0.001866`
- val_rmse: `0.002292`
- val_pointwise_loss: `0.002490`
- val_centered_curve_shape_loss: `0.004612`
- val_curve_offset_loss: `0.000369`
- val_curve_amplitude_loss: `0.034794`
- val_sparse_harmonic_shape_loss: `0.000103`
- val_structured_mae: `0.005349`
- val_structured_rmse: `0.005769`
- val_residual_offset_mean_abs: `0.004270`

## Test Metrics

- test_loss: `0.002937`
- test_mae: `0.002017`
- test_rmse: `0.002559`
- test_pointwise_loss: `0.002937`
- test_centered_curve_shape_loss: `0.005284`
- test_curve_offset_loss: `0.000591`
- test_curve_amplitude_loss: `0.039539`
- test_sparse_harmonic_shape_loss: `0.000111`
- test_structured_mae: `0.005430`
- test_structured_rmse: `0.006047`
- test_residual_offset_mean_abs: `0.004177`

## Interpretation

The held-out val error stayed finite with MAE=0.001866 deg and RMSE=0.002292 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002017 deg and RMSE=0.002559 deg, which indicates a numerically stable baseline run.
