# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_mlp_bw`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-06-29-16-42-14__te_residual_harmonic_mlp_bw\checkpoints\residual_harmonic_mlp-epoch=065-val_mae=0.00163724.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002777`
- val_mae: `0.001637`
- val_rmse: `0.002108`
- val_pointwise_loss: `0.002777`
- val_centered_curve_shape_loss: `0.003080`
- val_curve_offset_loss: `0.000423`
- val_curve_amplitude_loss: `0.048215`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.040317`
- val_structured_rmse: `0.043853`

## Test Metrics

- test_loss: `0.004170`
- test_mae: `0.001799`
- test_rmse: `0.002380`
- test_pointwise_loss: `0.004170`
- test_centered_curve_shape_loss: `0.003934`
- test_curve_offset_loss: `0.001300`
- test_curve_amplitude_loss: `0.060327`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.039738`
- test_structured_rmse: `0.043759`

## Interpretation

The held-out val error stayed finite with MAE=0.001637 deg and RMSE=0.002108 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001799 deg and RMSE=0.002380 deg, which indicates a numerically stable baseline run.
