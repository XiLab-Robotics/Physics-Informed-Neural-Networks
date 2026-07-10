# Wave3 2 Harmonic Residual Offset Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_2_harmonic_residual_offset_fw__polished_setpoints`
- Model Family: `wave3_2_harmonic_residual_offset_fw`
- Model Type: `harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_harmonic_residual_offset/2026-07-11-00-52-59__te_wave3_2_harmonic_residual_offset_fw__polished_setpoints/checkpoints/harmonic_residual_offset_probe-epoch=085-val_mae=0.00188607.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004946`
- val_mae: `0.001886`
- val_rmse: `0.002648`
- val_pointwise_loss: `0.004946`
- val_centered_curve_shape_loss: `0.004555`
- val_curve_offset_loss: `0.000391`
- val_curve_amplitude_loss: `0.033298`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.036687`
- val_structured_rmse: `0.041180`
- val_residual_offset_mean_abs: `0.036445`

## Test Metrics

- test_loss: `0.008462`
- test_mae: `0.002222`
- test_rmse: `0.003593`
- test_pointwise_loss: `0.008462`
- test_centered_curve_shape_loss: `0.005446`
- test_curve_offset_loss: `0.003016`
- test_curve_amplitude_loss: `0.043728`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.035356`
- test_structured_rmse: `0.040209`
- test_residual_offset_mean_abs: `0.035025`

## Interpretation

The held-out val error stayed finite with MAE=0.001886 deg and RMSE=0.002648 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002222 deg and RMSE=0.003593 deg, which indicates a numerically stable baseline run.
