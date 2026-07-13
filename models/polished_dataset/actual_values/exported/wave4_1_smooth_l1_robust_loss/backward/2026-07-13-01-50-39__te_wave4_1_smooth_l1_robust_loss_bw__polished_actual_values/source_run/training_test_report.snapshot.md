# Wave4 1 Smooth L1 Robust Loss Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_smooth_l1_robust_loss_bw__polished_actual_values`
- Model Family: `wave4_1_smooth_l1_robust_loss_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_smooth_l1_robust_loss/2026-07-13-01-50-39__te_wave4_1_smooth_l1_robust_loss_bw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=128-val_mae=0.00189374.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002487`
- val_mae: `0.001894`
- val_rmse: `0.002657`
- val_pointwise_loss: `0.002487`
- val_centered_curve_shape_loss: `0.004503`
- val_curve_offset_loss: `0.000472`
- val_curve_amplitude_loss: `0.035738`
- val_sparse_harmonic_shape_loss: `9.957497e-05`
- val_structured_mae: `0.012492`
- val_structured_rmse: `0.014636`
- val_residual_offset_mean_abs: `0.012148`

## Test Metrics

- test_loss: `0.002910`
- test_mae: `0.002011`
- test_rmse: `0.003057`
- test_pointwise_loss: `0.002910`
- test_centered_curve_shape_loss: `0.005385`
- test_curve_offset_loss: `0.000434`
- test_curve_amplitude_loss: `0.040652`
- test_sparse_harmonic_shape_loss: `0.000108`
- test_structured_mae: `0.011990`
- test_structured_rmse: `0.014565`
- test_residual_offset_mean_abs: `0.011632`

## Interpretation

The held-out val error stayed finite with MAE=0.001894 deg and RMSE=0.002657 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002011 deg and RMSE=0.003057 deg, which indicates a numerically stable baseline run.
