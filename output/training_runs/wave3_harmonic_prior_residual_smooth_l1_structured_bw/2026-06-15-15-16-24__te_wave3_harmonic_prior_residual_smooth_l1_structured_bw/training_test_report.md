# Wave3 Harmonic Prior Residual Smooth L1 Structured Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_harmonic_prior_residual_smooth_l1_structured_bw`
- Model Family: `wave3_harmonic_prior_residual_smooth_l1_structured_bw`
- Model Type: `wave3_harmonic_prior_residual`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_harmonic_prior_residual_smooth_l1_structured_bw\2026-06-15-15-16-24__te_wave3_harmonic_prior_residual_smooth_l1_structured_bw\checkpoints\wave3_harmonic_prior_residual-epoch=114-val_mae=0.00364433.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.020954`
- val_mae: `0.003644`
- val_rmse: `0.004208`
- val_pointwise_loss: `0.020954`
- val_centered_curve_shape_loss: `0.028701`
- val_curve_offset_loss: `0.013538`
- val_curve_amplitude_loss: `0.229289`
- val_sparse_harmonic_shape_loss: `0.000696`
- val_structured_mae: `0.005880`
- val_structured_rmse: `0.006554`

## Test Metrics

- test_loss: `0.015246`
- test_mae: `0.003431`
- test_rmse: `0.003953`
- test_pointwise_loss: `0.015246`
- test_centered_curve_shape_loss: `0.013907`
- test_curve_offset_loss: `0.016587`
- test_curve_amplitude_loss: `0.094665`
- test_sparse_harmonic_shape_loss: `0.000316`
- test_structured_mae: `0.005690`
- test_structured_rmse: `0.006348`

## Interpretation

The held-out val error stayed finite with MAE=0.003644 deg and RMSE=0.004208 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003431 deg and RMSE=0.003953 deg, which indicates a numerically stable baseline run.
