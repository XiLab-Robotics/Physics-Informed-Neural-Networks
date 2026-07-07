# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_mlp_fw__simplified_setpoints`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_mlp/2026-07-07-10-54-26__te_residual_harmonic_mlp_fw__simplified_setpoints/checkpoints/residual_harmonic_mlp-epoch=079-val_mae=0.00306417.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007540`
- val_mae: `0.003064`
- val_rmse: `0.003599`
- val_pointwise_loss: `0.007540`
- val_centered_curve_shape_loss: `0.003051`
- val_curve_offset_loss: `0.004796`
- val_curve_amplitude_loss: `0.050972`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.040536`
- val_structured_rmse: `0.042561`

## Test Metrics

- test_loss: `0.007309`
- test_mae: `0.003218`
- test_rmse: `0.003723`
- test_pointwise_loss: `0.007309`
- test_centered_curve_shape_loss: `0.002136`
- test_curve_offset_loss: `0.005264`
- test_curve_amplitude_loss: `0.040521`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.039409`
- test_structured_rmse: `0.042799`

## Interpretation

The held-out val error stayed finite with MAE=0.003064 deg and RMSE=0.003599 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003218 deg and RMSE=0.003723 deg, which indicates a numerically stable baseline run.
