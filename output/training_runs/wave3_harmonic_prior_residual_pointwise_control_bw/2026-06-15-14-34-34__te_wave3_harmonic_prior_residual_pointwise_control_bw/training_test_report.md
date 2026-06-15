# Wave3 Harmonic Prior Residual Pointwise Control Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_harmonic_prior_residual_pointwise_control_bw`
- Model Family: `wave3_harmonic_prior_residual_pointwise_control_bw`
- Model Type: `wave3_harmonic_prior_residual`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_harmonic_prior_residual_pointwise_control_bw\2026-06-15-14-34-34__te_wave3_harmonic_prior_residual_pointwise_control_bw\checkpoints\wave3_harmonic_prior_residual-epoch=123-val_mae=0.00363415.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.041809`
- val_mae: `0.003634`
- val_rmse: `0.004206`
- val_pointwise_loss: `0.041809`
- val_centered_curve_shape_loss: `0.028444`
- val_curve_offset_loss: `0.013365`
- val_curve_amplitude_loss: `0.220268`
- val_sparse_harmonic_shape_loss: `0.000689`
- val_structured_mae: `0.007250`
- val_structured_rmse: `0.008095`

## Test Metrics

- test_loss: `0.029806`
- test_mae: `0.003363`
- test_rmse: `0.003902`
- test_pointwise_loss: `0.029806`
- test_centered_curve_shape_loss: `0.013855`
- test_curve_offset_loss: `0.015950`
- test_curve_amplitude_loss: `0.090358`
- test_sparse_harmonic_shape_loss: `0.000314`
- test_structured_mae: `0.007055`
- test_structured_rmse: `0.007869`

## Interpretation

The held-out val error stayed finite with MAE=0.003634 deg and RMSE=0.004206 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003363 deg and RMSE=0.003902 deg, which indicates a numerically stable baseline run.
