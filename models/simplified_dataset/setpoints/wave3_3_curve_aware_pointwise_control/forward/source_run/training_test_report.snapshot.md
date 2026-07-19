# Wave3 3 Curve Aware Pointwise Control Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_curve_aware_pointwise_control_fw__simplified_setpoints`
- Model Family: `wave3_3_curve_aware_pointwise_control_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-07-56-33__te_wave3_3_curve_aware_pointwise_control_fw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=099-val_mae=0.00361775.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010710`
- val_mae: `0.003618`
- val_rmse: `0.004432`
- val_pointwise_loss: `0.010710`
- val_centered_curve_shape_loss: `0.006383`
- val_curve_offset_loss: `0.004327`
- val_curve_amplitude_loss: `0.044730`
- val_sparse_harmonic_shape_loss: `0.000151`
- val_structured_mae: `0.029746`
- val_structured_rmse: `0.035709`
- val_residual_offset_mean_abs: `0.029449`

## Test Metrics

- test_loss: `0.008158`
- test_mae: `0.003400`
- test_rmse: `0.004125`
- test_pointwise_loss: `0.008158`
- test_centered_curve_shape_loss: `0.003194`
- test_curve_offset_loss: `0.004964`
- test_curve_amplitude_loss: `0.018603`
- test_sparse_harmonic_shape_loss: `6.909751e-05`
- test_structured_mae: `0.033294`
- test_structured_rmse: `0.038580`
- test_residual_offset_mean_abs: `0.032871`

## Interpretation

The held-out val error stayed finite with MAE=0.003618 deg and RMSE=0.004432 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003400 deg and RMSE=0.004125 deg, which indicates a numerically stable baseline run.
