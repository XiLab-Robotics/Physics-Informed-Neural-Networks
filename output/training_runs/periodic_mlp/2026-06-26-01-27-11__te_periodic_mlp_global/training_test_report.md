# Periodic Mlp Global Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_global`
- Model Family: `periodic_mlp_global`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_mlp\2026-06-26-01-27-11__te_periodic_mlp_global\checkpoints\periodic_mlp-epoch=082-val_mae=0.00163440.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002768`
- val_mae: `0.001634`
- val_rmse: `0.002108`
- val_pointwise_loss: `0.002768`
- val_centered_curve_shape_loss: `0.003104`
- val_curve_offset_loss: `0.000386`
- val_curve_amplitude_loss: `0.047072`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.004076`
- test_mae: `0.001774`
- test_rmse: `0.002355`
- test_pointwise_loss: `0.004076`
- test_centered_curve_shape_loss: `0.004096`
- test_curve_offset_loss: `0.001040`
- test_curve_amplitude_loss: `0.061353`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001634 deg and RMSE=0.002108 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001774 deg and RMSE=0.002355 deg, which indicates a numerically stable baseline run.
