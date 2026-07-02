# Wave5 1 Harmonic Prior Pointwise Control Bw Training And Testing Report

## Overview

- Run Name: `te_wave5_1_harmonic_prior_pointwise_control_bw`
- Model Family: `wave5_1_harmonic_prior_pointwise_control_bw`
- Model Type: `wave3_harmonic_prior_residual`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave5_1_harmonic_prior_pointwise_control\2026-07-01-23-48-40__te_wave5_1_harmonic_prior_pointwise_control_bw\checkpoints\wave3_harmonic_prior_residual-epoch=106-val_mae=0.00189325.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005190`
- val_mae: `0.001893`
- val_rmse: `0.002332`
- val_pointwise_loss: `0.005190`
- val_centered_curve_shape_loss: `0.004589`
- val_curve_offset_loss: `0.000600`
- val_curve_amplitude_loss: `0.035071`
- val_sparse_harmonic_shape_loss: `0.000101`
- val_structured_mae: `0.007574`
- val_structured_rmse: `0.007983`

## Test Metrics

- test_loss: `0.007213`
- test_mae: `0.002105`
- test_rmse: `0.002680`
- test_pointwise_loss: `0.007213`
- test_centered_curve_shape_loss: `0.005271`
- test_curve_offset_loss: `0.001942`
- test_curve_amplitude_loss: `0.041316`
- test_sparse_harmonic_shape_loss: `0.000112`
- test_structured_mae: `0.007885`
- test_structured_rmse: `0.008358`

## Interpretation

The held-out val error stayed finite with MAE=0.001893 deg and RMSE=0.002332 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002105 deg and RMSE=0.002680 deg, which indicates a numerically stable baseline run.
