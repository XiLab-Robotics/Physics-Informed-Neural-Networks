# Wave3 3 Curve Aware Pointwise Control Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_curve_aware_pointwise_control_fw__polished_setpoints`
- Model Family: `wave3_3_curve_aware_pointwise_control_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-11-40-50__te_wave3_3_curve_aware_pointwise_control_fw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=094-val_mae=0.00191479.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005041`
- val_mae: `0.001915`
- val_rmse: `0.002682`
- val_pointwise_loss: `0.005041`
- val_centered_curve_shape_loss: `0.004587`
- val_curve_offset_loss: `0.000454`
- val_curve_amplitude_loss: `0.031172`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_structured_mae: `0.049215`
- val_structured_rmse: `0.054163`
- val_residual_offset_mean_abs: `0.049132`

## Test Metrics

- test_loss: `0.008465`
- test_mae: `0.002239`
- test_rmse: `0.003598`
- test_pointwise_loss: `0.008465`
- test_centered_curve_shape_loss: `0.005443`
- test_curve_offset_loss: `0.003021`
- test_curve_amplitude_loss: `0.041697`
- test_sparse_harmonic_shape_loss: `0.000109`
- test_structured_mae: `0.046765`
- test_structured_rmse: `0.052413`
- test_residual_offset_mean_abs: `0.046474`

## Interpretation

The held-out val error stayed finite with MAE=0.001915 deg and RMSE=0.002682 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002239 deg and RMSE=0.003598 deg, which indicates a numerically stable baseline run.
