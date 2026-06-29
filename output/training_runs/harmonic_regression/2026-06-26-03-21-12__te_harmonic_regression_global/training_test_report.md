# Harmonic Regression Global Training And Testing Report

## Overview

- Run Name: `te_harmonic_regression_global`
- Model Family: `harmonic_regression_global`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression\2026-06-26-03-21-12__te_harmonic_regression_global\checkpoints\harmonic_regression-epoch=055-val_mae=0.00387866.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010239`
- val_mae: `0.003879`
- val_rmse: `0.004472`
- val_pointwise_loss: `0.010239`
- val_centered_curve_shape_loss: `0.003089`
- val_curve_offset_loss: `0.007672`
- val_curve_amplitude_loss: `0.047777`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.010905`
- test_mae: `0.003795`
- test_rmse: `0.004515`
- test_pointwise_loss: `0.010905`
- test_centered_curve_shape_loss: `0.003839`
- test_curve_offset_loss: `0.007826`
- test_curve_amplitude_loss: `0.060798`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003879 deg and RMSE=0.004472 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003795 deg and RMSE=0.004515 deg, which indicates a numerically stable baseline run.
