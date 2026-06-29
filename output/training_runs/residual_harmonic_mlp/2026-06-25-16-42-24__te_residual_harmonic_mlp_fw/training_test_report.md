# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_mlp_fw`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-06-25-16-42-24__te_residual_harmonic_mlp_fw\checkpoints\residual_harmonic_mlp-epoch=075-val_mae=0.00164699.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002838`
- val_mae: `0.001647`
- val_rmse: `0.002142`
- val_pointwise_loss: `0.002838`
- val_centered_curve_shape_loss: `0.003081`
- val_curve_offset_loss: `0.000483`
- val_curve_amplitude_loss: `0.047038`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.040343`
- val_structured_rmse: `0.043883`

## Test Metrics

- test_loss: `0.004206`
- test_mae: `0.001808`
- test_rmse: `0.002420`
- test_pointwise_loss: `0.004206`
- test_centered_curve_shape_loss: `0.003995`
- test_curve_offset_loss: `0.001237`
- test_curve_amplitude_loss: `0.058928`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.039554`
- test_structured_rmse: `0.043491`

## Interpretation

The held-out val error stayed finite with MAE=0.001647 deg and RMSE=0.002142 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001808 deg and RMSE=0.002420 deg, which indicates a numerically stable baseline run.
