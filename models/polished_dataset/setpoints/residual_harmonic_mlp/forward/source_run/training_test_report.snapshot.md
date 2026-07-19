# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_mlp_fw__polished_setpoints`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_mlp/2026-07-07-12-02-44__te_residual_harmonic_mlp_fw__polished_setpoints/checkpoints/residual_harmonic_mlp-epoch=122-val_mae=0.00159866.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002670`
- val_mae: `0.001599`
- val_rmse: `0.002052`
- val_pointwise_loss: `0.002670`
- val_centered_curve_shape_loss: `0.003036`
- val_curve_offset_loss: `0.000314`
- val_curve_amplitude_loss: `0.054039`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.040322`
- val_structured_rmse: `0.043858`

## Test Metrics

- test_loss: `0.004056`
- test_mae: `0.001759`
- test_rmse: `0.002336`
- test_pointwise_loss: `0.004056`
- test_centered_curve_shape_loss: `0.003782`
- test_curve_offset_loss: `0.001319`
- test_curve_amplitude_loss: `0.067298`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.039689`
- test_structured_rmse: `0.043692`

## Interpretation

The held-out val error stayed finite with MAE=0.001599 deg and RMSE=0.002052 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001759 deg and RMSE=0.002336 deg, which indicates a numerically stable baseline run.
