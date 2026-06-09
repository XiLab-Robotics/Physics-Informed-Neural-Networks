# Track2G Curve Aware Harmonic Residual Offset Pointwise Control Global Training And Testing Report

## Overview

- Run Name: `te_track2g_curve_aware_pointwise_control_global`
- Model Family: `track2g_curve_aware_harmonic_residual_offset_pointwise_control_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2g_curve_aware_harmonic_residual_offset_pointwise_control_global\2026-06-08-18-36-30__te_track2g_curve_aware_pointwise_control_global\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=038-val_mae=0.00360750.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011100`
- val_mae: `0.003607`
- val_rmse: `0.004134`
- val_pointwise_loss: `0.011100`
- val_centered_curve_shape_loss: `0.006436`
- val_curve_offset_loss: `0.004664`
- val_curve_amplitude_loss: `0.041865`
- val_sparse_harmonic_shape_loss: `0.000152`
- val_structured_mae: `0.040284`
- val_structured_rmse: `0.043027`
- val_residual_offset_mean_abs: `0.040871`

## Test Metrics

- test_loss: `0.009168`
- test_mae: `0.003587`
- test_rmse: `0.004001`
- test_pointwise_loss: `0.009168`
- test_centered_curve_shape_loss: `0.003245`
- test_curve_offset_loss: `0.005923`
- test_curve_amplitude_loss: `0.017539`
- test_sparse_harmonic_shape_loss: `7.053500e-05`
- test_structured_mae: `0.043163`
- test_structured_rmse: `0.045931`
- test_residual_offset_mean_abs: `0.043697`

## Interpretation

The held-out val error stayed finite with MAE=0.003607 deg and RMSE=0.004134 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003587 deg and RMSE=0.004001 deg, which indicates a numerically stable baseline run.
