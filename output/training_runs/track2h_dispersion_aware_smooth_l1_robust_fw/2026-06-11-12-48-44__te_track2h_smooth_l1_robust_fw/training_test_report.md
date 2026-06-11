# Track2H Dispersion Aware Smooth L1 Robust Fw Training And Testing Report

## Overview

- Run Name: `te_track2h_smooth_l1_robust_fw`
- Model Family: `track2h_dispersion_aware_smooth_l1_robust_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_dispersion_aware_smooth_l1_robust_fw\2026-06-11-12-48-44__te_track2h_smooth_l1_robust_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=014-val_mae=0.00323536.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.015728`
- val_mae: `0.003235`
- val_rmse: `0.003729`
- val_pointwise_loss: `0.015728`
- val_centered_curve_shape_loss: `0.014985`
- val_curve_offset_loss: `0.016473`
- val_curve_amplitude_loss: `0.099628`
- val_sparse_harmonic_shape_loss: `0.000326`
- val_structured_mae: `0.015154`
- val_structured_rmse: `0.016521`
- val_residual_offset_mean_abs: `0.015192`

## Test Metrics

- test_loss: `0.013845`
- test_mae: `0.003314`
- test_rmse: `0.003679`
- test_pointwise_loss: `0.013845`
- test_centered_curve_shape_loss: `0.007564`
- test_curve_offset_loss: `0.020127`
- test_curve_amplitude_loss: `0.044672`
- test_sparse_harmonic_shape_loss: `0.000139`
- test_structured_mae: `0.015695`
- test_structured_rmse: `0.017173`
- test_residual_offset_mean_abs: `0.015681`

## Interpretation

The held-out val error stayed finite with MAE=0.003235 deg and RMSE=0.003729 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003314 deg and RMSE=0.003679 deg, which indicates a numerically stable baseline run.
