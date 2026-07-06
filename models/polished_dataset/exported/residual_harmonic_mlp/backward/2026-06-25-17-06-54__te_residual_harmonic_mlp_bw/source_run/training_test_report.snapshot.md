# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_mlp_bw`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-06-25-17-06-54__te_residual_harmonic_mlp_bw\checkpoints\residual_harmonic_mlp-epoch=131-val_mae=0.00160855.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002727`
- val_mae: `0.001609`
- val_rmse: `0.002089`
- val_pointwise_loss: `0.002727`
- val_centered_curve_shape_loss: `0.003088`
- val_curve_offset_loss: `0.000331`
- val_curve_amplitude_loss: `0.047727`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.040339`
- val_structured_rmse: `0.043878`

## Test Metrics

- test_loss: `0.003935`
- test_mae: `0.001712`
- test_rmse: `0.002294`
- test_pointwise_loss: `0.003935`
- test_centered_curve_shape_loss: `0.003986`
- test_curve_offset_loss: `0.001016`
- test_curve_amplitude_loss: `0.059983`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.039575`
- test_structured_rmse: `0.043521`

## Interpretation

The held-out val error stayed finite with MAE=0.001609 deg and RMSE=0.002089 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001712 deg and RMSE=0.002294 deg, which indicates a numerically stable baseline run.
