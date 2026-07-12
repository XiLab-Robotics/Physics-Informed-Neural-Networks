# Wave4 1 Smooth L1 Robust Loss Global Training And Testing Report

## Overview

- Run Name: `te_wave4_1_smooth_l1_robust_loss_global__simplified_setpoints`
- Model Family: `wave4_1_smooth_l1_robust_loss_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-12-20-13-14__te_wave4_1_smooth_l1_robust_loss_global__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=087-val_mae=0.00364010.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005463`
- val_mae: `0.003640`
- val_rmse: `0.004471`
- val_pointwise_loss: `0.005463`
- val_centered_curve_shape_loss: `0.006376`
- val_curve_offset_loss: `0.004550`
- val_curve_amplitude_loss: `0.046057`
- val_sparse_harmonic_shape_loss: `0.000151`
- val_structured_mae: `0.028802`
- val_structured_rmse: `0.034795`
- val_residual_offset_mean_abs: `0.028443`

## Test Metrics

- test_loss: `0.004096`
- test_mae: `0.003373`
- test_rmse: `0.004139`
- test_pointwise_loss: `0.004096`
- test_centered_curve_shape_loss: `0.003191`
- test_curve_offset_loss: `0.005002`
- test_curve_amplitude_loss: `0.019599`
- test_sparse_harmonic_shape_loss: `6.892905e-05`
- test_structured_mae: `0.029456`
- test_structured_rmse: `0.036709`
- test_residual_offset_mean_abs: `0.029225`

## Interpretation

The held-out val error stayed finite with MAE=0.003640 deg and RMSE=0.004471 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003373 deg and RMSE=0.004139 deg, which indicates a numerically stable baseline run.
