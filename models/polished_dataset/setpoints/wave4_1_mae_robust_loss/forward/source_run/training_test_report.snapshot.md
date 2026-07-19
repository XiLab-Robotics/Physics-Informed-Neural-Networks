# Wave4 1 Mae Robust Loss Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_1_mae_robust_loss_fw__polished_setpoints`
- Model Family: `wave4_1_mae_robust_loss_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_1_mae_robust_loss/2026-07-12-16-19-34__te_wave4_1_mae_robust_loss_fw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=105-val_mae=0.00179190.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.038495`
- val_mae: `0.001792`
- val_rmse: `0.002558`
- val_pointwise_loss: `0.038495`
- val_centered_curve_shape_loss: `0.004614`
- val_curve_offset_loss: `0.000328`
- val_curve_amplitude_loss: `0.037378`
- val_sparse_harmonic_shape_loss: `0.000103`
- val_structured_mae: `0.021963`
- val_structured_rmse: `0.026554`
- val_residual_offset_mean_abs: `0.021783`

## Test Metrics

- test_loss: `0.045308`
- test_mae: `0.002109`
- test_rmse: `0.003545`
- test_pointwise_loss: `0.045308`
- test_centered_curve_shape_loss: `0.005583`
- test_curve_offset_loss: `0.003029`
- test_curve_amplitude_loss: `0.048912`
- test_sparse_harmonic_shape_loss: `0.000113`
- test_structured_mae: `0.020214`
- test_structured_rmse: `0.025171`
- test_residual_offset_mean_abs: `0.019798`

## Interpretation

The held-out val error stayed finite with MAE=0.001792 deg and RMSE=0.002558 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002109 deg and RMSE=0.003545 deg, which indicates a numerically stable baseline run.
