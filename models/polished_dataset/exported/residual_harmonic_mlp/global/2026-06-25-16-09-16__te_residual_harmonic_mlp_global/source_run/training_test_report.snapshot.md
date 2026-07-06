# Residual Harmonic Mlp Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_mlp_global`
- Model Family: `residual_harmonic_mlp_global`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-06-25-16-09-16__te_residual_harmonic_mlp_global\checkpoints\residual_harmonic_mlp-epoch=112-val_mae=0.00165991.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002815`
- val_mae: `0.001660`
- val_rmse: `0.002126`
- val_pointwise_loss: `0.002815`
- val_centered_curve_shape_loss: `0.003082`
- val_curve_offset_loss: `0.000449`
- val_curve_amplitude_loss: `0.046776`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.040303`
- val_structured_rmse: `0.043848`

## Test Metrics

- test_loss: `0.004239`
- test_mae: `0.001841`
- test_rmse: `0.002433`
- test_pointwise_loss: `0.004239`
- test_centered_curve_shape_loss: `0.003938`
- test_curve_offset_loss: `0.001325`
- test_curve_amplitude_loss: `0.058730`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.039928`
- test_structured_rmse: `0.043975`

## Interpretation

The held-out val error stayed finite with MAE=0.001660 deg and RMSE=0.002126 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001841 deg and RMSE=0.002433 deg, which indicates a numerically stable baseline run.
