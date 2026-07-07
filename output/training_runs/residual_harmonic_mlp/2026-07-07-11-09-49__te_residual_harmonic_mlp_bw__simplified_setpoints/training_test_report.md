# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_mlp_bw__simplified_setpoints`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_mlp/2026-07-07-11-09-49__te_residual_harmonic_mlp_bw__simplified_setpoints/checkpoints/residual_harmonic_mlp-epoch=032-val_mae=0.00306476.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007493`
- val_mae: `0.003065`
- val_rmse: `0.003594`
- val_pointwise_loss: `0.007493`
- val_centered_curve_shape_loss: `0.003054`
- val_curve_offset_loss: `0.004894`
- val_curve_amplitude_loss: `0.049966`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.040594`
- val_structured_rmse: `0.042552`

## Test Metrics

- test_loss: `0.007824`
- test_mae: `0.003380`
- test_rmse: `0.003868`
- test_pointwise_loss: `0.007824`
- test_centered_curve_shape_loss: `0.002140`
- test_curve_offset_loss: `0.005638`
- test_curve_amplitude_loss: `0.039606`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.039436`
- test_structured_rmse: `0.042853`

## Interpretation

The held-out val error stayed finite with MAE=0.003065 deg and RMSE=0.003594 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003380 deg and RMSE=0.003868 deg, which indicates a numerically stable baseline run.
