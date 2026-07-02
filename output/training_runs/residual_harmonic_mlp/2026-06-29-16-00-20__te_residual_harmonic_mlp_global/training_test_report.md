# Residual Harmonic Mlp Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_mlp_global`
- Model Family: `residual_harmonic_mlp_global`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-06-29-16-00-20__te_residual_harmonic_mlp_global\checkpoints\residual_harmonic_mlp-epoch=100-val_mae=0.00162131.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002736`
- val_mae: `0.001621`
- val_rmse: `0.002096`
- val_pointwise_loss: `0.002736`
- val_centered_curve_shape_loss: `0.003080`
- val_curve_offset_loss: `0.000369`
- val_curve_amplitude_loss: `0.046789`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.040321`
- val_structured_rmse: `0.043857`

## Test Metrics

- test_loss: `0.003959`
- test_mae: `0.001710`
- test_rmse: `0.002307`
- test_pointwise_loss: `0.003959`
- test_centered_curve_shape_loss: `0.004028`
- test_curve_offset_loss: `0.001021`
- test_curve_amplitude_loss: `0.058692`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.039696`
- test_structured_rmse: `0.043702`

## Interpretation

The held-out val error stayed finite with MAE=0.001621 deg and RMSE=0.002096 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001710 deg and RMSE=0.002307 deg, which indicates a numerically stable baseline run.
